"""Shared rules for the specification and sample generators: model, dictionaries, requiredness, descriptions, shell formatting."""
import json,re,os,sys,collections,datetime
from catalogue import C
from keydict_text import TEXT
from keydict_num import NUM
from master_refs import OPTIONAL_MASTER_REFS,NEWC,NEWENT
from entity_samples import ES_TEXT,ALT_TEXT,USERS,CHILD_TEXT,ENUM_OVERRIDE,REF_OVERRIDE,DOC_OVERRIDE,VALUE_OVERRIDE
ROOT=sys.argv[1] if len(sys.argv)>1 else "."
M=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"model","flat_model.json")))
cols=M["collections"]; MODN=M["modules"]
order=["mast","prod","plan","matl","trac","qual","perf","maint","syst","ehs"]
DOMF={'mast': '01_master_data_management', 'prod': '02_product_definition', 'plan': '03_planning_execution', 'matl': '04_material_management', 'trac': '05_traceability', 'qual': '06_quality_management', 'perf': '07_performance_management', 'maint': '08_tooling_maintenance', 'syst': '09_system_integration', 'ehs': '10_environment_health_safety'}
cat={c[0]:c for c in C}
bycol={c["collection"]:c for c in cols}; byent={c["entity"]:c for c in cols}
def parse(t,n):
    d={}
    for l in t.strip().split("\n"):
        p=l.split("|"); p+=[""]*(n-len(p)); k=p[0]; nul=k.endswith("?"); d[k.rstrip("?")]=(nul,p[1:])
    return d
TD=parse(TEXT,4); ND=parse(NUM,3)
ES={l.split("|")[0]:(l.split("|")+["",""])[1:4] for l in ES_TEXT.strip().split("\n")}
ALT={l.split("|")[0]:(l.split("|")+[""])[1:3] for l in ALT_TEXT.strip().split("\n")}
# ---------- identifiers
tags={}
for c in cols:
    if c["parent"] is None:
        src=cat.get(c["sourceConcept"]); c["prefix"]=src[2] if src else {"statusDefinition":"STD","statusTransition":"STT","enumerationValue":"ENV"}[c["entity"]]
        c["idPattern"]="16-digit numeric string, unique across the database"
for c in cols:
    if c["parent"]:
        pe=bycol[c["parent"]]["entity"]; suf=c["entity"][len(pe):]
        tag="".join(ch for ch in suf if ch.isupper())[:4] or suf[:3].upper(); base=tag; i=2
        while (c["parent"],tag) in tags: tag=base+str(i); i+=1
        tags[(c["parent"],tag)]=1; c["tag"]=tag; c["idPattern"]="16-digit numeric string, unique across the database"
def ident(c):
    if c["parent"] is None:
        rec=ES[c["entity"]][0]; return c["prefix"]+"-"+rec,rec
    pid,prec=ident(bycol[c["parent"]]); return pid+"-"+c["tag"]+"001",prec+"-"+c["tag"]+"001"
def display(c):
    if c["parent"] is None and ES[c["entity"]][1]: return ES[c["entity"]][1]
    return ident(c)[1]
def altident(ent):
    c=byent[ent]
    if ent in ALT: return c["prefix"]+"-"+ALT[ent][0], (ALT[ent][1] or ALT[ent][0])
    return None
NEWMASTER={c["entity"] for c in cols if c["sourceConcept"] in {x[0] for x in NEWC}}
# ---------- rules
STD=("_id","recordNo","siteId","siteName","status","schemaVersion","createdAt","createdById","createdBy","updatedAt","updatedById","updatedBy","sequenceNo")
LATE=re.compile(r"^(closed|completed|approved|acknowledged|released|verified|delivered|ended|cleared|resolved|revoked|voided|removed|scrapped|shipped|actualStart|actualEnd|reinspected|classified|dispatched|pod|last[A-Z]|nextRetry|decided|implemented|handedOver|firstOffApproved|published|inspectionCompleted|pickCompleted|pickStarted|markVerified|marked|finalRelease|d8Closure|pswSigned|submitted|customerDecision|interimApproval|containmentSent|customerClosed|equipmentReleased|processed|sent|read|expires|expiry|investigationCompleted|clockOff|effectiveTo|validTo|capabilityCalculated|masterLeakVerified|disposition|targetDate|packed|customerApprovalDate|asnSent|expectedRelease|attributesCure|nextReview|override|received[A-Z]|receivedBy|witness|equipmentReleased|verifiedBy|closedBy)")
NULLREF=re.compile(r"(^parent|[pP]roductVariant|^lot|Lot(Id|Name)$|^wipUnit|^container|[qQ]ualityHold|ControlledDocument|controlledDocument|engineeringChange|^nonconformance|^capa|downtimeEvent|maintenanceWorkOrder|^alarm|andonEvent|erpMessage|^recipe|^shipment|^label(Id|Name)$|goodsReceipt|^kit|customerSchedule|^productionOrder|^supplier|^customer(Id|Name)$|deviationPermit|^serialNumber|alternate|replaced|injured|reversalOf|supersedes|previousVersion|bottleneck|reportsTo|contractorSupplier|defaultSupplier|ownedByCustomer|^tool|^gauge(Id|Name)$|defectCode|reasonCode|customerComplaint|^audit(Id|Name)$|pfmea|controlPlan|electronicSignature|calibrationSupplier|maintenancePlan|fixtureTool|bodyLot|castingLot|heatTreatmentLot|^base|^from|^equipment|inspectionPlan|workInstruction|samplingPlan|checkSheet|^item|^operation|^workCenter|^line(Id|Name)$|^area|^shift|^role|^user|^iotDevice|^processTag|printerIotDevice|markedAtEquipment|materialConsumption|operationExecution|genealogyLink|torqueResult|leakTestResult|^characteristic|^routing|billOfMaterial|^unitOfMeasure|relatedEntity|^default|^home|inputLocation|outputLocation|dockLocation|quarantineLocation|scrapLocation|toStorage|toLocation|authorUser|ownerUser|supervisorUser|numberRange|serialNumberRange|lotNumberRange|workCalendar|trainingControlled|lastGaugeCalibration|lastOperationExecution|current|createdAtOperation|detectedAt|origin|variantItem|integrationConnector|spcChart|d7Prevention|witnessUser)")
CORE={  # references that are always required in the named collection
 "productionOrder":["itemId","billOfMaterialId","routingId","lineId","unitOfMeasureId"],"wipUnit":["productionOrderId","itemId","routingId","currentOperationId","currentWorkCenterId"],
 "operationExecution":["productionOrderId","itemId","routingId","operationId","workCenterId","shiftId","operatorUserId"],"stepCompletion":["operationExecutionId","workInstructionId","workCenterId","userId"],
 "lot":["itemId","unitOfMeasureId"],"billOfMaterial":["itemId","baseUnitOfMeasureId"],"routing":["itemId"],"billOfProcess":["itemId","routingId"],"workInstruction":["itemId","operationId","authorUserId"],
 "recipe":["equipmentId","operationId"],"line":["areaId"],"workCenter":["areaId","lineId"],"equipment":["lineId","workCenterId"],"area":[],"user":["defaultShiftId"],"skillCertification":["userId","skillId","assessorUserId"],
 "item":["baseUnitOfMeasureId"],"productVariant":["baseItemId"],"operation":["defaultWorkCenterId"],"customerSchedule":["customerId"],"productionSchedule":["lineId","shiftId","workCalendarId"],
 "dispatchList":["workCenterId","shiftId"],"labourBooking":["userId","shiftId"],"changeover":["lineId","workCenterId","toItemId"],"shiftHandover":["shiftId","lineId","outgoingSupervisorUserId"],
 "shiftRoster":["shiftId","lineId","supervisorUserId"],"inventoryBalance":["itemId","storageLocationId","unitOfMeasureId"],"materialMovement":["itemId","unitOfMeasureId"],"goodsReceipt":["supplierId"],
 "kit":["productionOrderId","workCenterId","toLocationId"],"materialRequest":["workCenterId","itemId","unitOfMeasureId","toLocationId"],"materialConsumption":["operationExecutionId","productionOrderId","componentItemId","unitOfMeasureId","workCenterId"],
 "packagingSpecification":["itemId","customerId"],"label":["labelTemplateId","relatedEntityId"],"shipment":["customerId"],"serialNumber":["itemId","numberRangeId"],"genealogyLink":["parentItemId","childItemId","operationId","unitOfMeasureId"],
 "componentLotLink":["parentLotId","childLotId","parentItemId","childItemId","unitOfMeasureId"],"asBuiltRecord":["wipUnitId","serialNumberId","itemId","productionOrderId","customerId"],
 "characteristic":["itemId","unitOfMeasureId"],"controlPlan":["itemId","routingId"],"inspectionPlan":["itemId","operationId"],"checkSheet":["workCenterId"],"checkSheetResult":["checkSheetId","workCenterId","shiftId"],
 "inspectionResult":["characteristicId","itemId","operationId","workCenterId","unitOfMeasureId"],"spcChart":["characteristicId","itemId","workCenterId","ownerUserId"],"spcSample":["spcChartId","characteristicId","workCenterId","shiftId"],
 "nonconformance":["itemId","defectCodeId","detectedAtOperationId","detectedAtWorkCenterId"],"reworkOrder":["nonconformanceId","itemId","reworkRoutingId","workCenterId"],"scrapRecord":["defectCodeId","itemId","unitOfMeasureId","originOperationId","workCenterId","shiftId"],
 "qualityHold":["itemId"],"deviationPermit":["itemId","customerId"],"pfmea":["itemId"],"ppapSubmission":["itemId","customerId"],"gaugeCalibration":["gaugeId"],"msaStudy":["gaugeId","characteristicId","itemId"],
 "audit":["leadAuditorUserId"],"customerComplaint":["customerId","itemId"],"equipmentState":["equipmentId","workCenterId","shiftId"],"downtimeEvent":["equipmentId","lineId","workCenterId","shiftId"],
 "productionCount":["workCenterId","lineId","shiftId"],"oeeRecord":["equipmentId","lineId","shiftId"],"processTag":["equipmentId","iotDeviceId","unitOfMeasureId"],"processReading":["processTagId","equipmentId"],"alarm":["equipmentId"],
 "torqueResult":["wipUnitId","operationExecutionId","equipmentId","recipeId","controllerIotDeviceId","operatorUserId"],"leakTestResult":["wipUnitId","operationExecutionId","equipmentId","recipeId","testerIotDeviceId","operatorUserId"],
 "maintenanceWorkOrder":["equipmentId"],"sparePart":["unitOfMeasureId","storageLocationId"],"toolLifeRecord":["toolId"],"erpMessage":["integrationConnectorId"],"iotDevice":["integrationConnectorId"],
 "electronicSignature":["relatedEntityId","userId","roleId"],"auditTrail":["relatedEntityId"],"energyReading":["meterIotDeviceId","unitOfMeasureId"],"andonEvent":["workCenterId","lineId","shiftId"],"safetyIncident":["areaId"],
 "statusTransition":["fromStatusDefinitionId","toStatusDefinitionId"],"site":["enterpriseId"],"shift":[],"customer":[],"gauge":["rangeUnitOfMeasureId"],"maintenancePlan":[],"tool":[],"businessEvent":[],"notification":[],"controlledDocument":["authorUserId"],
 "container":["packagingSpecificationId","storageLocationId"],"capa":[],"qualityHold2":[]}
SYSTEMCOLS={"processReading","equipmentState","productionCount","oeeRecord","alarm","erpMessage","businessEvent","energyReading","torqueResult","leakTestResult","auditTrail","notification"}
def userrole(key,c):
    k=key.lower()
    if key in("createdById","updatedById") and c["sourceEntity"] in SYSTEMCOLS: return "system"
    for pat,r in (("approved|released|closed|psw|finalrelease|manager|verifiedby|decid|mrb|witness|headuser","manager"),("supervisor|acknowledg|classif|publish|issuedby|incoming|handed|reportsto","supervisor"),
                  ("measur|inspect|sampl|calibrat|detect|placed|reinspect|assessor|auditor|appraiser|quality|declared|performedby|conducted|investig|coreteam|owneruser|author","quality"),
                  ("assigned|equipmentreleased|maintain|resolved","maintenance"),("moved|picked|received|loaded|packed|printed|counted|consumed|requestedby","stores")):
        if re.search(pat,k): return r
    if c["module"]=="maint": return "maintenance"
    if c["module"]=="matl": return "stores"
    if c["module"]=="qual": return "quality"
    return "operator"
def nullable(c,f):
    k=f["key"]
    if k in STD: return False
    if c["parent"]:
        pe=bycol[c["parent"]]["entity"]
        if k in(pe+"Id",pe+"Name"): return False
    base=k[:-4] if (k.endswith("Name") and any(x["key"]==k[:-4]+"Id" for x in c["fields"])) else (k[:-2] if k.endswith("Id") else k)
    isref = f["ref"] or (k.endswith("Name") and any(x["key"]==k[:-4]+"Id" and x["ref"] for x in c["fields"])) or any(x["key"]==k+"Id" for x in c["fields"])
    if isref:
        idkey = k if k.endswith("Id") else (k+"Id" if any(x["key"]==k+"Id" for x in c["fields"]) else k[:-4]+"Id")
        rf=[x for x in c["fields"] if x["key"]==idkey][0]["ref"]
        if rf in NEWMASTER and c["kind"]!="relationship": return idkey in OPTIONAL_MASTER_REFS
        if idkey in CORE.get(c["rootEntity"],[]) and c["parent"] is None: return False
        if idkey.endswith("ById"): return bool(LATE.match(idkey))
        if c["kind"]=="relationship": return False
        if c["kind"]=="child":
            # in a child line the first reference after the parent is the subject of the line
            refs=[x["key"] for x in c["fields"] if x["ref"] and x["key"] not in("siteId","createdById","updatedById") and x["key"]!=bycol[c["parent"]]["entity"]+"Id"]
            if refs and idkey==refs[0] and not re.search(r"^(parent|alternate|replaced)",idkey): return False
        return bool(NULLREF.search(idkey))
    if k=="relatedCollectionName": return False
    if f["type"]=="Boolean": return False
    if f["type"]=="Date": return bool(LATE.match(k))
    if k in TD: return TD[k][0]
    if k in ND: return ND[k][0]
    return False
UNIT=[("Nm"," (N.m)"),("Pct"," (percent)"),("Inr"," (Indian rupees)"),("Kg"," (kg)"),("Mm"," (mm)"),("Um"," (micrometres)"),("Deg"," (degrees)"),("Bar"," (bar)"),("Pa"," (pascal)"),("Sccm"," (standard cubic centimetres per minute)"),("Kw"," (kW)"),("Sqm"," (square metres)"),("Hbw"," (Brinell HBW)"),("Km"," (km)"),("TemperatureC"," temperature (degrees Celsius)"),("Minutes"," (minutes)"),("Sec"," (seconds)"),("Min"," (minutes)"),("Ms"," (milliseconds)"),("Days"," (days)"),("Months"," (months)"),("Years"," (years)")]
def words(k):
    w=re.sub(r"([a-z0-9])([A-Z])",r"\1 \2",k).lower()
    for a,b in (("erp ","ERP "),("ppap","PPAP"),("pfmea","PFMEA"),("oee","OEE"),("spc ","SPC "),("msa","MSA"),("capa","CAPA"),("iot","IoT"),("asn","ASN"),("gstin","GSTIN"),("ucl","UCL"),("lcl","LCL"),(" id"," ID"),("psw","PSW"),("hsn","HSN"),("teep","TEEP"),("aql","AQL"),("bom","BOM"),("bop","BOP"),("d2 ","D2 "),("d4 ","D4 "),("d7 ","D7 "),("d8 ","D8 "),("plc","PLC"),("opc","OPC")): w=w.replace(a,b)
    w=re.sub(r" no$"," number",w); w=re.sub(r"^min ","minimum ",w); w=re.sub(r"^max ","maximum ",w); w=w.replace(" min "," minimum ").replace(" max "," maximum ")
    return w
def describe(c,f,nul):
    k=f["key"]; t=f["type"]
    fixed={"_id":"Unique identifier of the document. Pattern: %s"%c["idPattern"],"recordNo":"Business identifier of the document, readable by people and unique within the site","siteId":"Reference to u_mes_mast_site._id: the site the document belongs to","siteName":"Display value of the site, copied from u_mes_mast_site.name",
     "status":"Primary lifecycle state of the document","schemaVersion":"Version of this collection's document structure, starting at 1","createdAt":"Date and time the document was created. Datetime field: local plant time (IST) stored with the +0000 suffix","createdById":"Reference to u_mes_mast_user._id: user or process that created the document","createdBy":"Display name of the creator, copied from u_mes_mast_user.fullName",
     "updatedAt":"Date and time of the most recent update. Datetime field: local plant time (IST) stored with the +0000 suffix","updatedById":"Reference to u_mes_mast_user._id: user or process that last updated the document","updatedBy":"Display name of the last updater, copied from u_mes_mast_user.fullName","sequenceNo":"Position of this document in its list (within the same parent for child collections), starting at 1",
     "relatedCollectionName":"Name of the collection the related document is in","relatedEntityId":"_id of the related document in the collection named by relatedCollectionName","relatedEntityName":"Display value of the related document"}
    if k in fixed: return fixed[k]
    ks=[x["key"] for x in c["fields"]]
    if f["ref"]:
        tc=byent[f["ref"]]; stem=k[:-2]
        if k.endswith("ById"): return "Reference to u_mes_mast_user._id: user recorded for '%s'"%words(k[:-4])
        role=words(stem); ent=words(f["ref"])
        if c["parent"] and bycol[c["parent"]]["entity"]==f["ref"] and k==f["ref"]+"Id": return "Reference to %s._id: the parent document this one belongs to"%tc["collection"]
        return "Reference to %s._id"%tc["collection"]+("" if role==ent else ": %s"%role)
    if k+"Id" in ks: return "Display name of the user in %sId, copied from u_mes_mast_user.fullName"%k
    if k.endswith("Name") and k[:-4]+"Id" in ks:
        r=[x for x in c["fields"] if x["key"]==k[:-4]+"Id"][0]["ref"]
        if r: return "Display value of %sId, copied from %s.%s"%(k[:-4],byent[r]["collection"],byent[r]["displayField"])
    for d in (TD,ND):
        if k in d and d[k][1][-1]: return d[k][1][-1]
    if k==c["displayField"] and k in("name","title"): return "%s of the %s; used as its display value in other collections"%(k.capitalize(),words(c["entity"]))
    if t=="Boolean":
        m=re.match(r"(is|has|can|requires)([A-Z].*)",k)
        if m: return {"is":"True when the record is %s","has":"True when the record has %s","can":"True when the holder can %s","requires":"True when %s is required"}[m.group(1)]%words(m.group(2))
        return "True when: %s"%words(k)
    if t=="Date" and f.get("dateKind")=="Date":
        return "%s. Date field: calendar date only, stored as 00:00:00 of that day in local plant time (IST) with the +0000 suffix"%words(k).capitalize()
    if t=="Date":
        if k.endswith("At"):
            st=k[:-2]; w=words(st)
            if re.fullmatch(r"[a-z]+ed",st) or st in("sent","read","built"): return "Date and time when the record was %s. Datetime field: local plant time (IST) stored with the +0000 suffix"%w
            return "%s date and time. Datetime field: local plant time (IST) stored with the +0000 suffix"%w.capitalize()
        return "%s. Datetime field: local plant time (IST) stored with the +0000 suffix"%words(k).capitalize()
    w=words(k)
    for suf,txt in UNIT:
        if k.endswith(suf) and len(k)>len(suf):
            w=words(k[:-len(suf)])+txt; break
    if " " not in w and "(" not in w: return "%s of the %s"%(w[0].upper()+w[1:],words(c["entity"]))
    return w[0].upper()+w[1:]
def D(dt): return ("date",dt)
def sh(v):
    if v is None: return "null"
    if isinstance(v,bool): return "true" if v else "false"
    if isinstance(v,tuple):
        a,b=v
        if a=="date": return 'ISODate("%s.000+0000")'%b.strftime("%Y-%m-%dT%H:%M:%S")
        if a=="int": return "NumberInt(%d)"%b
        if a=="long": return 'NumberLong("%d")'%b
        if a=="dec": return 'NumberDecimal("%s")'%b
        if a=="dbl": return "Double(%s)"%(repr(b) if b!=int(b) else str(int(b)))
    return json.dumps(v,ensure_ascii=False)
BT={"String":"string","Date":"date","Int32":"int","Int64":"long","Decimal128":"decimal","Double":"double","Boolean":"bool"}
def enum(c,f):
    k=f["key"]
    if k=="status": return c["statusValues"]
    if (c["entity"],k) in ENUM_OVERRIDE: return ENUM_OVERRIDE[(c["entity"],k)]
    if k in TD and TD[k][1][1]: return TD[k][1][1].split(";")
    return None
# root entity for CORE lookup and system detection
for c in cols:
    r=c
    while r["parent"]: r=bycol[r["parent"]]
    c["rootEntity"]=r["entity"]; c["sourceEntity"]=r["entity"]
