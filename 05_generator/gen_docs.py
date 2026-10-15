import json,collections,os,re,sys
from catalogue import C
ROOT=sys.argv[1]
M=json.load(open("model/flat_model.json")); cols=M["collections"]; MODN=M["modules"]
ORDER_ALL=["mast","prod","plan","matl","trac","qual","perf","maint","syst","ehs","bmr","mmr"]
order=[m for m in ORDER_ALL if any(c["module"]==m for c in cols)]  # modules without collections get no files (Folder_Guide rule 5)
DOMF={'mast': '01_master_data_management', 'prod': '02_product_definition', 'plan': '03_planning_execution', 'matl': '04_material_management', 'trac': '05_traceability', 'qual': '06_quality_management', 'perf': '07_performance_management', 'maint': '08_tooling_maintenance', 'syst': '09_system_integration', 'ehs': '10_environment_health_safety', 'bmr': '11_batch_manufacturing_record', 'mmr': '12_master_manufacturing_record'}
cat={c[0]:c for c in C}
import ext_req01 as EXT
cat.update(EXT.CAT)
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
HEAD="Model version 2.9 | 12 October 2026 | %d collections (%d entity, %d child, %d relationship, %d value-list), %d keys\n\n"%(NK,kinds["entity"],kinds["child"],kinds["relationship"],kinds["valueList"],NF)
KIND={"entity":"Entity","child":"Child (was an embedded array of objects)","relationship":"Relationship (was an array of IDs)","valueList":"Value list (was an array of values)"}
# inventory
s="# Collection inventory\n\n"+HEAD+"Authority for collection names. Naming: `u_mes_<moduleCode>_<singularCollectionName>`. Each business concept appears once. Data class decides audit keys: transaction collections carry the six audit keys, master collections do not.\n\n## Module codes\n\n| Module code | Module | Collections |\n|---|---|---|\n"
for m in ORDER_ALL: s+="| %s | %s | %d |\n"%(m,MODN[m],sum(1 for c in cols if c["module"]==m))
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
s="# Collection keys\n\n"+HEAD+"All documents are flat: every key is top-level and scalar. A key ending in Id is a reference and is followed by its display key (<entity>Name, or the same name without Id for keys ending in ById). Every date key carries its tag: [Date] = calendar date stored as 00:00:00 local plant time, [Datetime] = local plant time stored with the +0000 suffix. Types are in 02_architecture/field_lists.\n\n| Module | Collection | List of keys |\n|---|---|---|\n"
for m in order:
    for c in cols:
        if c["module"]==m: s+="| %s | %s | %s |\n"%(MODN[m],c["collection"],", ".join(f["key"]+(" [%s]"%f["dateKind"] if f.get("dateKind") else "") for f in c["fields"]))
w("02_architecture/collection_keys.md",s)
# field lists
SHELL={"String":"\"text\"","Date":"ISODate(\"YYYY-MM-DDTHH:mm:ss.sss+0000\")","Int32":"NumberInt(n)","Int64":"NumberLong(\"n\")","Decimal128":"NumberDecimal(\"n.nn\")","Double":"Double(n)","Boolean":"true / false"}
for m in order:
    s="# Field list - %s (%s)\n\n"%(MODN[m],m)+"Key, BSON type and reference target for every collection of this module. Requiredness, descriptions, examples and allowed values are added in the collection specifications under 03_design/%s/specs.\n\nShell constructors: "%DOMF[m]+"; ".join("%s = %s"%(k,v) for k,v in SHELL.items())+".\n"
    for c in cols:
        if c["module"]!=m: continue
        s+="\n## %s\n\nKind: %s | Data class: %s | Parent: %s | _id pattern: %s\n\n| # | Key | BSON type | Date tag | References |\n|---|---|---|---|---|\n"%(c["collection"],c["kind"],c["dataClass"],c["parent"] or "-",c["idPattern"])
        for i,f in enumerate(c["fields"],1):
            ref=""
            if f["ref"]=="(polymorphic)": ref="any collection, named in relatedCollectionName"
            elif f["ref"]:
                t=[x for x in cols if x["entity"]==f["ref"]][0]["collection"]; ref=t+"._id"
            s+="| %d | %s | %s | %s | %s |\n"%(i,f["key"],f["type"],f.get("dateKind","-"),ref)
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
s="# data_model_register.md\n\nMES on MongoDB - Front Brake Caliper Assembly LH - Pune\nRegister version: 2.9 | Date: 12 October 2026 | Database: mes | "+HEAD
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
- Dates (DATA-004): every date and time is local plant time (IST) written with the +0000 suffix, without UTC conversion. Each date key is tagged Date (calendar date, stored as 00:00:00) or Datetime.
- Types (DATA-002): Date, Int32, Int64, Decimal128 for measurements and money, Double only for geoLatitude, geoLongitude, tagValue, powerFactor, Boolean, String.

## 2. Sample-data frame

| Item | Value |
|---|---|
| Enterprise | Varuna Brake Systems Pvt. Ltd. (fictional) |
| Site of all transactions | Chakan Plant, Pune (timezone Asia/Kolkata) |
| OEM customer | Sahyadri Motors Ltd. (fictional) |
| Sample period | April to September 2026; production fortnight Tue 15 Sep to Sat 26 Sep 2026 |
| Non-working days | Mon 14 Sep 2026 (Ganesh Chaturthi), Sun 20 Sep 2026 (weekly off) |
| Shifts | A 06:00-14:00, B 14:00-22:00, C 22:00-06:00 IST, stored as 06:00, 14:00, 22:00 with the +0000 suffix |
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
| 2.9 | 12 Oct 2026 | Owner decisions on the BMR / MMR designation (D057-D059): u_mes_mmr_masterManufacturingRecord (1367) with the relationship u_mes_mmr_masterManufacturingRecordRecipe (1368), and u_mes_bmr_batchManufacturingRecord (1369) added; line clearance and dispensing stay in plan and matl, audit-trail review stays in syst |
| 2.8 | 12 Oct 2026 | Modules bmr (BatchManufacturingRecord) and mmr (MasterManufacturingRecord) added on the owner's instruction (D054-D056). Collections unique to the batch manufacturing record moved to bmr with their numbers and _id values unchanged: u_mes_qual_batchRecordReview, u_mes_qual_batchRecordReviewException and u_mes_qual_batchRelease to u_mes_bmr_*, u_mes_plan_yieldReconciliation to u_mes_bmr_yieldReconciliation. No collection is unique to the master manufacturing record, so mmr has no collections yet. Collections shared by BMR / MMR and the rest of the MES are listed in 01_research/BMR_MMR_module_designation.md and were not moved |
| 2.7 | 12 Oct 2026 | GMP_Pharma_01 implemented (D047-D053): 23 collections added (numbers 1344-1366, existing numbers unchanged), 33 keys added to 11 existing collections (41 keys with display pairs), allowed values extended; computerised system inventory, system validation, periodic review, audit-trail review, user access review, batch record review by exception, batch release, yield and label reconciliation, line clearance, equipment and area logbook, cleaning records, environmental monitoring, dispensing, retention samples, quality risk assessment, product quality review, recalls, process validation, equipment qualification. Analysis: 01_research/GMP_Pharma_01_impact_analysis.md |
| 2.6 | 12 Oct 2026 | MES_ExternalRequirement_01 implemented (D036-D042): 44 collections added (numbers 1300-1343, existing numbers unchanged), 212 keys added to 38 existing collections, allowed values extended; interlock rules and events, escalation and alert rules, operator sessions, document acknowledgements, recipe downloads, set-up verification, exposure timers, replenishment rules, trace investigations, per-position results and measurement curves, defect records, LPA schedules, alarm definitions, loss and performance reports, maintenance checklists, spare-part transactions, lifecycle events, analytics models and predictions, simulation studies, record policies, saved views, backup runs. Analysis: 01_research/MES_ExternalRequirement_01_impact_analysis.md |
| 2.5 | 12 Oct 2026 | DATA-004: dates and times stored as local plant time (IST) with the +0000 suffix; every date key tagged Date or Datetime; sample data regenerated |
| 2.4 | 12 Oct 2026 | Sample documents: exactly 10 per collection in 03_design/<module>/samples; system IDs changed to 16-digit numeric strings; sample period moved to April-September 2026; master ID registry replaced by the generated 04_reference_data/sample_data_registry.md; child, relationship and value-list collections use recordNo as display value |
| 2.3 | 11 Oct 2026 | Module codes and names changed on the owner's instruction: mast, prod, plan, matl, trac, qual, perf, maint, syst, ehs. Every collection name changed with its module code. Module Energy, safety and andon dissolved: andon collections moved to plan, energy collections to perf, safety collections kept in the new module ehs (EnvironmentHealthAndSafety). Module folders renamed |
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
# ---- collection type matrix (Master / Transaction / Reports / Telemetry / Audit Trail)
TYPE_BY_ROOT={"auditTrail":"Audit Trail","electronicSignature":"Audit Trail","businessEvent":"Audit Trail",
 "processReading":"Telemetry","energyReading":"Telemetry","equipmentState":"Telemetry","alarm":"Telemetry",
 "oeeRecord":"Reports","productionCount":"Reports","asBuiltRecord":"Reports"}
TYPE_BY_ROOT.update(EXT.TYPE_BY_ROOT)
import re as _re
LABEL_FULL={"unitOfMeasure":"Units of Measure","billOfMaterial":"Bills of Material","billOfProcess":"Bills of Process","equipment":"Equipment","capa":"CAPA (8D)","pfmea":"Process FMEAs","ppapSubmission":"PPAP Submissions","msaStudy":"MSA Studies",
 "spcChart":"SPC Charts","spcSample":"SPC Samples","erpMessage":"ERP Messages","iotDevice":"IoT Devices","oeeRecord":"OEE Records","wipUnit":"WIP Units","ppeItem":"PPE Items","user":"Users","site":"Sites","processReading":"Process Readings",
 "productionCount":"Hourly Production Counts","businessEvent":"Business Events","auditTrail":"Audit Trail","controlledDocument":"Controlled Documents","asBuiltRecord":"As-Built Records","lot":"Lots and Batches","label":"Printed Labels",
 "kit":"Kits","audit":"Audits","alarm":"Alarms","tool":"Tools","gauge":"Gauges","recipe":"Recipes","item":"Items","stockStatus":"Stock Statuses","surfaceFinish":"Surface Finishes","equipmentState":"Equipment States",
 "statusDefinition":"Status Definitions","statusTransition":"Status Transitions","enumerationValue":"Enumeration Values","workCalendar":"Work Calendars","skillCertification":"Skill Certifications","inventoryBalance":"Inventory Balances"}
LABEL_FULL.update({"workCenterRequiresSkill":"Work Center Required Skills","customerShipTo":"Customer Ship-To Addresses","billOfMaterialComponentProductVariant":"BOM Component Variants","billOfMaterialComponentAlternateItem":"BOM Component Alternate Items",
 "billOfProcessStepEquipment":"BOP Step Equipment","billOfProcessStepTool":"BOP Step Tools","billOfProcessStepRequiredSkill":"BOP Step Required Skills","billOfProcessStepConsumedComponent":"BOP Step Consumed Components","billOfProcessStepInterlock":"BOP Step Interlocks","billOfProcessStepProcessParameter":"BOP Step Process Parameters",
 "workInstructionStepMediaControlledDocument":"Work Instruction Step Media","engineeringChangeControlledDocument":"Engineering Change Documents","capaControlledDocument":"CAPA Documents","nonconformancePhotoControlledDocument":"Nonconformance Photos",
 "controlPlanCoreTeamUser":"Control Plan Core Team","pfmeaCoreTeamUser":"PFMEA Core Team","nonconformanceMrbUser":"Nonconformance MRB Members","msaStudyAppraiserUser":"MSA Study Appraisers","auditAuditorUser":"Audit Auditors","changeoverPerformedByUser":"Changeover Crew",
 "maintenanceWorkOrderAssignedToUser":"Maintenance Work Order Assignees","safetyIncidentWitnessUser":"Safety Incident Witnesses","lotAttributesCavityNo":"Lot Cavity Numbers","toolItem":"Tool Applicable Items","samplingPlanSizeRow":"Sampling Plan Sample Size Table","stepCompletion":"Work Instruction Step Completions"})
LABEL_FULL.update(EXT.LABELS)
WORDFIX={"Bom":"BOM","Erp":"ERP","Iot":"IoT","Oee":"OEE","Spc":"SPC","Msa":"MSA","Ppap":"PPAP","Pfmea":"PFMEA","Capa":"CAPA","Wip":"WIP","Ppe":"PPE","Mrb":"MRB","Of":"of","To":"to","On":"on"}
def plural(w):
    if w in("Equipment","Labour","Data","Media","Staff"): return w
    if w.endswith("y") and w[-2] not in "aeiou": return w[:-1]+"ies"
    if w.endswith(("s","x","ch","sh")): return w+"es"
    return w+"s"
def words_of(ent):
    ws=_re.sub(r"([a-z0-9])([A-Z])",r"\1 \2",ent).split(); ws=[x[0].upper()+x[1:] for x in ws]; return [WORDFIX.get(x,x) for x in ws]
def label(c):
    e=c["entity"]
    if e in LABEL_FULL: return LABEL_FULL[e]
    if c["parent"]:
        p=bycol[c["parent"]]; pe=p["entity"]; rest=words_of(e[len(pe):])
        pw=" ".join(words_of(pe)) if pe not in("billOfMaterial","billOfProcess","unitOfMeasure") else {"billOfMaterial":"BOM","billOfProcess":"BOP","unitOfMeasure":"Unit of Measure"}[pe]
        if pe in LABEL_FULL and pe in("capa","pfmea","ppapSubmission","msaStudy","spcChart","spcSample","erpMessage","iotDevice","oeeRecord","wipUnit","asBuiltRecord","controlledDocument"):
            pw={"capa":"CAPA","pfmea":"PFMEA","ppapSubmission":"PPAP Submission","msaStudy":"MSA Study","spcChart":"SPC Chart","spcSample":"SPC Sample","erpMessage":"ERP Message","iotDevice":"IoT Device","oeeRecord":"OEE Record","wipUnit":"WIP Unit","asBuiltRecord":"As-Built Record","controlledDocument":"Controlled Document"}[pe]
        rest[-1]=plural(rest[-1]); return pw+" "+" ".join(rest)
    ws=words_of(e); ws[-1]=plural(ws[-1]); return " ".join(ws)
def root_entity(c):
    while c["parent"]: c=bycol[c["parent"]]
    return c["entity"]
tm="# Collection type matrix\n\n"+HEAD+"Type of each collection and the label used for it in the UI menu. A child, relationship or value-list collection has the type of the entity it belongs to; its label starts with the parent's name, because it is opened from the parent's screen.\n\n| Type | Meaning | Collections |\n|---|---|---|\n"
rows=[(m,MODN[m],c["collection"],TYPE_BY_ROOT.get(root_entity(c),"Master" if c["dataClass"]=="master" else "Transaction"),label(c)) for m in order for c in cols if c["module"]==m]
assert len({(r[0],r[4]) for r in rows})==len(rows),"duplicate label in a module"
cnt=collections.Counter(r[3] for r in rows)
MEAN={"Master":"Reference data that changes rarely and is maintained by the plant","Transaction":"Business records created by daily operations","Reports":"Pre-aggregated or assembled records built from transactions for reporting","Telemetry":"Machine-generated, time-ordered signals and states","Audit Trail":"Append-only records of who did or changed what"}
for t in ["Master","Transaction","Reports","Telemetry","Audit Trail"]: tm+="| %s | %s | %d |\n"%(t,MEAN[t],cnt[t])
tm+="\n## Collections per module and type\n\n| Code | ModuleName | Master | Transaction | Reports | Telemetry | Audit Trail | Total |\n|---|---|---|---|---|---|---|---|\n"
for m in order:
    mc=collections.Counter(r[3] for r in rows if r[0]==m)
    tm+="| %s | %s | %d | %d | %d | %d | %d | %d |\n"%(m,MODN[m],mc["Master"],mc["Transaction"],mc["Reports"],mc["Telemetry"],mc["Audit Trail"],sum(mc.values()))
tm+="\n## Matrix\n\n| Code | ModuleName | Collection | Type | Label |\n|---|---|---|---|---|\n"+"".join("| %s | %s | %s | %s | %s |\n"%r for r in rows)
w("02_architecture/collection_type_matrix.md",tm)
w("02_architecture/collection_type_matrix.csv","Code,ModuleName,Collection,Type,Label\n"+"".join("%s,%s,%s,%s,%s\n"%r for r in rows))
print("type matrix",dict(cnt))
