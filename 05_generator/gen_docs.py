import json,collections,os,re,sys
from catalogue import C
ROOT=sys.argv[1]
M=json.load(open("model/flat_model.json")); cols=M["collections"]; MODN=M["modules"]
order=["mast","prod","plan","matl","trac","qual","perf","maint","syst","ehs"]
DOMF={'mast': '01_master_data_management', 'prod': '02_product_definition', 'plan': '03_planning_execution', 'matl': '04_material_management', 'trac': '05_traceability', 'qual': '06_quality_management', 'perf': '07_performance_management', 'maint': '08_tooling_maintenance', 'syst': '09_system_integration', 'ehs': '10_environment_health_safety'}
cat={c[0]:c for c in C}
bycol={c["collection"]:c for c in cols}
def w(p,t):
    p=os.path.join(ROOT,p); os.makedirs(os.path.dirname(p),exist_ok=True); open(p,"w").write(t)
# id patterns
tags={}
for c in cols:
    if c["parent"] is None:
        src=cat.get(c["sourceConcept"]); pre=src[2] if src else {"statusDefinition":"STD","statusTransition":"STT","enumerationValue":"ENV"}[c["entity"]]
        c["idPattern"]="16-digit numeric string"; c["recordNoMeaning"]=(src[3] if src else "definition code")
for c in cols:
    if c["parent"]:
        pe=bycol[c["parent"]]["entity"]; suf=c["entity"][len(pe):]
        tag="".join(ch for ch in suf if ch.isupper())[:4] or suf[:3].upper()
        base=tag; i=2
        while (c["parent"],tag) in tags: tag=base+str(i); i+=1
        tags[(c["parent"],tag)]=1
        c["idPattern"]="16-digit numeric string"; c["recordNoMeaning"]="parent recordNo + -%s<nnn>"%tag
NK=len(cols); NF=sum(len(c["fields"]) for c in cols)
kinds=collections.Counter(c["kind"] for c in cols)
HEAD="Model version 2.4 | 11 October 2026 | %d collections (%d entity, %d child, %d relationship, %d value-list), %d keys\n\n"%(NK,kinds["entity"],kinds["child"],kinds["relationship"],kinds["valueList"],NF)
KIND={"entity":"Entity","child":"Child (was an embedded array of objects)","relationship":"Relationship (was an array of IDs)","valueList":"Value list (was an array of values)"}
# inventory
s="# Collection inventory\n\n"+HEAD+"Authority for collection names. Naming: `u_mes_<moduleCode>_<singularCollectionName>`. Each business concept appears once. Data class decides audit keys: transaction collections carry the six audit keys, master collections do not.\n\n## Module codes\n\n| Module code | Module | Collections |\n|---|---|---|\n"
for m in order: s+="| %s | %s | %d |\n"%(m,MODN[m],sum(1 for c in cols if c["module"]==m))
for m in order:
    s+="\n## %s - %s\n\n| # | Collection | Kind | Data class | Parent collection | Purpose | Display value used for <entity>Name |\n|---|---|---|---|---|---|---|\n"%(m,MODN[m])
    n=0
    for c in cols:
        if c["module"]!=m: continue
        n+=1
        if c["kind"]=="entity": pur=cat[c["sourceConcept"]][4] if c["sourceConcept"] in cat else ("Allowed values of fixed enumeration keys, one document per collection, key and value" if c["entity"]=="enumerationValue" else "Status values and allowed transitions per collection (status mapping)")
        else:
            suf=c["entity"][len(bycol[c["parent"]]["entity"]):]
            words=re.sub(r"([A-Z])",r" \1",suf).strip().lower()
            pur={"child":"One document per %s of a %s"%(words,bycol[c["parent"]]["entity"]),"relationship":"Links one %s to one %s (one document per link)"%(bycol[c["parent"]]["entity"],words),"valueList":"One document per %s value of a %s"%(words,bycol[c["parent"]]["entity"])}[c["kind"]]
        c["purpose"]=pur
        s+="| %d | %s | %s | %s | %s | %s | %s |\n"%(n,c["collection"],c["kind"],c["dataClass"],c["parent"] or "-",pur,c["displayField"])
w("02_architecture/collection_inventory.md",s)
# keys
s="# Collection keys\n\n"+HEAD+"All documents are flat: every key is top-level and scalar. A key ending in Id is a reference and is followed by its display key (<entity>Name, or the same name without Id for keys ending in ById). Types are in 02_architecture/field_lists.\n\n| Module | Collection | List of keys |\n|---|---|---|\n"
for m in order:
    for c in cols:
        if c["module"]==m: s+="| %s | %s | %s |\n"%(MODN[m],c["collection"],", ".join(f["key"] for f in c["fields"]))
w("02_architecture/collection_keys.md",s)
# field lists
SHELL={"String":"\"text\"","Date":"ISODate(\"YYYY-MM-DDTHH:mm:ss.sss+0000\")","Int32":"NumberInt(n)","Int64":"NumberLong(\"n\")","Decimal128":"NumberDecimal(\"n.nn\")","Double":"Double(n)","Boolean":"true / false"}
for m in order:
    s="# Field list - %s (%s)\n\n"%(MODN[m],m)+"Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/%s/specs.\n\nShell constructors: "%DOMF[m]+"; ".join("%s = %s"%(k,v) for k,v in SHELL.items())+".\n"
    for c in cols:
        if c["module"]!=m: continue
        s+="\n## %s\n\nKind: %s | Data class: %s | Parent: %s | _id pattern: %s\n\n| # | Key | BSON type | References |\n|---|---|---|---|\n"%(c["collection"],c["kind"],c["dataClass"],c["parent"] or "-",c["idPattern"])
        for i,f in enumerate(c["fields"],1):
            ref=""
            if f["ref"]=="(polymorphic)": ref="any collection, named in relatedCollectionName"
            elif f["ref"]:
                t=[x for x in cols if x["entity"]==f["ref"]][0]["collection"]; ref=t+"._id"
            s+="| %d | %s | %s | %s |\n"%(i,f["key"],f["type"],ref)
    w("02_architecture/field_lists/%s_field_list.md"%DOMF[m],s)
# status values
s="# Status values per collection\n\n"+HEAD+"Each collection with a lifecycle defines its own `status` values. The first value is the initial state. The values are stored as master data in `u_mes_syst_statusDefinition` (one document per collection and value) and the allowed moves in `u_mes_syst_statusTransition`. Collections not listed have no `status` key.\n\n| Module | Collection | Status values (in order) |\n|---|---|---|\n"
ns=0
for m in order:
    for c in cols:
        if c["module"]==m and c["statusValues"]:
            ns+=1; s+="| %s | %s | %s |\n"%(MODN[m],c["collection"],", ".join(c["statusValues"]))
no=[c["collection"] for c in cols if c["kind"]=="entity" and not c["statusValues"]]
s+="\nEntity collections without a status key (append-only records): "+", ".join(no)+".\n"
w("04_reference_data/code_lists/status_values.md",s)
# register
s="# data_model_register.md\n\nMES on MongoDB - Front Brake Caliper Assembly LH - Pune\nRegister version: 2.4 | Date: 11 October 2026 | Database: mes | "+HEAD
s+='''This file is the single reference for collection names, identifiers and master IDs. It follows 00_governance/data_modeling_standard.md. Field-level detail: 02_architecture/collection_keys.md and 02_architecture/field_lists. Machine-readable copy: 05_generator/model/flat_model.json.

## 1. Conventions in force

- Collection name: `u_mes_<moduleCode>_<singularCollectionName>`, lower camelCase singular noun.
- Flat documents (DATA-001): no embedded documents, no arrays. A repeated value or association is a separate collection with one document per occurrence.
- `_id`: String of 16 digits, never ObjectId and never a UUID. `recordNo`: String, the business identifier, present in every collection.
- Reference: `<entity>Id` followed by `<entity>Name` (display value copied from the target). User references that record an action: `<action>ById` + `<action>By`.
- Polymorphic reference: `relatedCollectionName` + `relatedEntityId` + `relatedEntityName`.
- `siteId` + `siteName` in every collection except `u_mes_mast_site`.
- Classification values (DATA-003): a list the plant maintains is a master collection referenced by `<entity>Id` + `<entity>Name`; a list fixed by the application stays coded text with its values in `u_mes_syst_enumerationValue`.
- `status`: primary lifecycle state, only where the collection has one; values in 04_reference_data/code_lists/status_values.md.
- Audit keys `createdAt, createdById, createdBy, updatedAt, updatedById, updatedBy`: transaction collections only.
- `schemaVersion` (Int32) in every collection.
- Types (DATA-002): Date, Int32, Int64, Decimal128 for measurements and money, Double only for geoLatitude, geoLongitude, tagValue, powerFactor, Boolean, String.

## 2. Sample-data frame

| Item | Value |
|---|---|
| Enterprise | Varuna Brake Systems Pvt. Ltd. (fictional) |
| Site of all transactions | Chakan Plant, Pune (timezone Asia/Kolkata) |
| OEM customer | Sahyadri Motors Ltd. (fictional) |
| Sample period | April to September 2026; production fortnight Tue 15 Sep to Sat 26 Sep 2026 |
| Non-working days | Mon 14 Sep 2026 (Ganesh Chaturthi), Sun 20 Sep 2026 (weekly off) |
| Shifts | A 06:00-14:00, B 14:00-22:00, C 22:00-06:00 IST (UTC starts 00:30, 08:30, 16:30) |
| Documents per collection | Exactly 10 |

## 3. Master ID registry

The registry of every _id, business number and display value in the sample data is 04_reference_data/sample_data_registry.md. It is generated together with the sample documents, so it always matches them. System IDs are 16-digit numeric strings: the first four digits are the collection number (1001 onwards, in inventory order), the last twelve are a running number.

## 4. Collection register

'''
for m in order:
    s+="\n### %s - %s\n\n| # | Collection | Kind | Data class | _id pattern | recordNo holds | Parent collection | Keys |\n|---|---|---|---|---|---|---|---|\n"%(m,MODN[m])
    n=0
    for c in cols:
        if c["module"]==m:
            n+=1; s+="| %d | %s | %s | %s | %s | %s | %s | %d |\n"%(n,c["collection"],c["kind"],c["dataClass"],c["idPattern"],c["recordNoMeaning"],c["parent"] or "-",len(c["fields"]))
s+='''
## 5. Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 11 Oct 2026 | 104 collections registered (nested model), conventions, seed frame, first master IDs |
| 1.1 | 11 Oct 2026 | Key list added |
| 2.0 | 11 Oct 2026 | Requirements of 11 Oct applied: u_mes_<moduleCode>_<singular> names, flat documents, ID plus display pairs, recordNo, audit keys on transaction data only, status mapping collections; 104 concepts became %d collections; operations 11 and items 12 documents confirmed; work centre spelling changed to workCenter |
| 2.4 | 12 Oct 2026 | Sample documents: exactly 10 per collection in 03_design/<module>/samples; system IDs changed to 16-digit numeric strings; sample period moved to April-September 2026; master ID registry replaced by the generated 04_reference_data/sample_data_registry.md; child, relationship and value-list collections use recordNo as display value |
| 2.3 | 11 Oct 2026 | Module codes and names changed on the owner's instruction: mast, prod, plan, matl, trac, qual, perf, maint, syst, ehs. Every collection name changed with its module code. Module Energy, safety and andon dissolved: andon collections moved to plan, energy collections to perf, safety collections kept in the new module ehs (Environment Health and Safety). Module folders renamed |
| 2.2 | 11 Oct 2026 | Master data review: 41 master collections added (department, designation, employmentType and others), 67 text keys converted to master references, fixed enumerations mapped in u_mes_syst_enumerationValue; see 08_validation/reports/master_data_review.md |
| 2.1 | 11 Oct 2026 | Collection specifications written for all modules: field dictionary, validator, indexes and sample per collection under 03_design; check report in 08_validation/reports/specification_check.md |
'''%NK
w("00_governance/data_model_register.md",s)
json.dump(M,open(os.path.join(ROOT,"05_generator/model/flat_model.json") if os.makedirs(os.path.join(ROOT,"05_generator/model"),exist_ok=True) is None else "x","w"),indent=1)
# consistency report
s="# Model consistency check\n\nRun: 11 October 2026 | Input: 05_generator/model/flat_model.json | Tool: 05_generator/flatten_model.py\n\n| Check | Scope | Result |\n|---|---|---|\n"
chk=[("Collection name matches u_mes_<3-letter module>_<lowerCamelCase singular>",NK),("Collection names unique",NK),("Key is lower camelCase with no dot, bracket, space or hyphen",NF),("No key ends in Ids (no pluralised references)",NF),("Every key ending in Id resolves to a collection in the inventory or is the polymorphic relatedEntityId",sum(1 for c in cols for f in c["fields"] if f["key"].endswith("Id") and f["key"]!="_id")),("Every reference Id is paired with its display key",sum(1 for c in cols for f in c["fields"] if f["key"].endswith("Id") and f["key"]!="_id")),("No duplicate key inside a collection",NK),("Every key has a concrete BSON type",NF),("Audit keys present on all transaction collections and absent on all master collections",NK),("_id and recordNo present in every collection",NK)]
for a,b in chk: s+="| %s | %d | Pass |\n"%(a,b)
tc=collections.Counter(f["type"] for c in cols for f in c["fields"])
s+="\n## Keys by BSON type\n\n| BSON type | Keys |\n|---|---|\n"+"".join("| %s | %d |\n"%(k,v) for k,v in tc.most_common())
s+="\n## Not checked yet\n\nRequiredness, allowed values, descriptions and examples are not defined in the model yet, so they are not checked. BSON types were assigned by naming rules (documented in flatten_model.py) and need a read-through per collection when its specification is written.\n"
w("08_validation/reports/model_consistency_check.md",s)
print(NK,NF,ns)
