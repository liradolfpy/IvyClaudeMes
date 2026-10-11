"""Generates collection specifications, validators, index scripts and shell-style samples for every collection.
Usage: python gen_specs.py <project root>   (run from 05_generator)"""
import json,re,os,sys,collections,datetime
from catalogue import C
from keydict_text import TEXT
from keydict_num import NUM
from master_refs import OPTIONAL_MASTER_REFS,NEWC,NEWENT
import gen_samples as _GS
SEED=_GS.build()
from entity_samples import ES_TEXT,ALT_TEXT,USERS,CHILD_TEXT,ENUM_OVERRIDE,REF_OVERRIDE,DOC_OVERRIDE,VALUE_OVERRIDE
ROOT=sys.argv[1]
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
     "status":"Primary lifecycle state of the document","schemaVersion":"Version of this collection's document structure, starting at 1","createdAt":"Date and time the document was created","createdById":"Reference to u_mes_mast_user._id: user or process that created the document","createdBy":"Display name of the creator, copied from u_mes_mast_user.fullName",
     "updatedAt":"Date and time of the most recent update","updatedById":"Reference to u_mes_mast_user._id: user or process that last updated the document","updatedBy":"Display name of the last updater, copied from u_mes_mast_user.fullName","sequenceNo":"Position of this document in its list (within the same parent for child collections), starting at 1",
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
    if t=="Date":
        if k.endswith("At"):
            st=k[:-2]; w=words(st)
            if re.fullmatch(r"[a-z]+ed",st) or st in("sent","read","built"): return "Date and time when the record was %s"%w
            return "%s date and time"%w.capitalize()
        return "%s (calendar date, stored as the start of that day in IST converted to UTC)"%words(k).capitalize()
    w=words(k)
    for suf,txt in UNIT:
        if k.endswith(suf) and len(k)>len(suf):
            w=words(k[:-len(suf)])+txt; break
    if " " not in w and "(" not in w: return "%s of the %s"%(w[0].upper()+w[1:],words(c["entity"]))
    return w[0].upper()+w[1:]
BASE=datetime.datetime(2026,9,29,0,30,0)
def D(dt): return ("date",dt)
PAST=re.compile(r"(validFrom|effectiveFrom|commissioned|purchased|dateOfJoining|installed|originalDate|revisionDate|awarded|passwordChanged|customerApprovalDate|lastCalibrated|lastMaintained|lastDone|lastCleaned|lastReset|manufactured|firstReceived|approvedAt|pswSigned|submittedAt|customerDecisionAt|studyDate|calibratedAt|supplierInvoiceDate|lastReceived|masterLeakVerified)")
FUT=re.compile(r"(validTo|effectiveTo|expir|next[A-Z].*Due|nextReview|nextDueAt|nextMaintenance|interimApproval|expiresAt|targetDate)")
FALSEB=re.compile(r"(Hold|Locked|overrid|MicroStop|causedStop|lineStopped|Secret|isPlanned|adjustmentMade|excluded|blocked|SafetyRelated|requiresHold|Insurance|reportable|firstAid|followUp|actionRequired|impactAssessment|frozen|crossesMidnight|isOptional|isSystemRole|isQuarantine|isMasterGauge|isSecondSignature|skipLot|isDirectedSource|vciRequired|requiresShutdown|requiresReason|isFinal|isBaseUnit|isInspection|isSpecialProcess|ppapRequired|closed$|configValueFlag|enteredFlag|backflush|mixedLots|requiresPhoto|isReturnable$|isInitial)")
PREF=["Closed","Completed","Released","Active","Recorded","Posted","Valid","Approved","Delivered","Shipped","Accepted","Dispatched","Resolved","Cleared","Acknowledged","Calculated","Verified","Printed","Available","Full","Mounted","Marked","Handed Over","Published","Classified","Dispositioned","Disposed","Implemented","Sent","Compiling","Complete","In Progress"]
SHORT={"operationExecution","stepCompletion","torqueResult","leakTestResult","inspectionResult","materialMovement","materialConsumption","label","genealogyLink","componentLotLink","processReading","alarm","businessEvent","auditTrail","electronicSignature","erpMessage","notification","andonEvent","equipmentState","toolLifeRecord","spcSample","checkSheetResult","materialRequest","serialNumber","energyReading","productionCount"}
def sample(c):
    doc=collections.OrderedDict(); meta={}
    _id,rec=ident(c); seq=[BASE+(datetime.timedelta(seconds=34) if c["rootEntity"] in SHORT else datetime.timedelta(minutes=5))]
    master=c["dataClass"]=="master"
    alldates=[]
    for f in c["fields"]:
        k=f["key"]; t=f["type"]; nul=nullable(c,f); v=None
        if k=="_id": v=_id
        elif k=="recordNo": v=rec
        elif k=="siteId": v="SITE-PN1"
        elif k=="siteName": v="Chakan Plant, Pune"
        elif k=="schemaVersion": v=1
        elif k=="sequenceNo": v=1
        elif k=="status": v=next((p for p in PREF if p in c["statusValues"]),c["statusValues"][0])
        elif k=="createdAt": v=D(BASE)
        elif k=="updatedAt": v=None  # filled later
        elif k=="relatedCollectionName": v="u_mes_plan_wipUnit"
        elif k=="relatedEntityName": v=display(byent["wipUnit"])
        elif f["ref"]:
            tgt=f["ref"]
            if tgt=="(polymorphic)": v=ident(byent["wipUnit"])[0]; nm=None
            elif tgt=="user":
                r=userrole(k,c)
                if k in("createdById","updatedById") or not re.search(r"^(replaced|injured|witness|reportsTo)",k) : pass
                if nul and re.search(r"^(replaced|injured|voided|revoked|override)",k): v=None; nm=None
                else: v="USR-"+USERS[r][0]; nm=USERS[r][1]
            else:
                tc=byent[tgt]; isparent=c["parent"] and bycol[c["parent"]]["entity"]==tgt and k==tgt+"Id"
                usealt=(not isparent) and (tgt==c["entity"] or re.match(r"(from|component|child|alternate|parent|base|previous|supersedes|reversal|variantItem|rework|toProductionOrder)",k))
                if k.startswith("toProductionOrder"): usealt=False
                if k.startswith("fromProductionOrder"): usealt=True
                if usealt:
                    a=altident(tgt)
                    if a: v,nm=a
                    elif nul: v=None; nm=None
                    else: v=ident(tc)[0]; nm=display(tc)
                else:
                    v=ident(tc)[0]; nm=display(tc)
                    for (re_,suf),val in REF_OVERRIDE.items():
                        if re_==c["rootEntity"] and k[:-2].endswith(suf) and (tgt.lower()==suf.lower() or suf[0].isupper()): v,nm=val
                    if tgt=="controlledDocument":
                        for pre,val in DOC_OVERRIDE.items():
                            if k.startswith(pre): v,nm=val
                if nul and (re.search(r"(contractorSupplier|ownedByCustomer|^parentCustomer|^bodyPart|^injuryType|^indirectActivity)",k) or (c["entity"] in("lot","nonconformance") and re.match(r"(supplier|goodsReceipt)",k))): v=None; nm=None
                if nul and re.search(r"(reversalOf|supersedes|qualityHold|deviationPermit|^replaced|^alternate|^parent(Area|Equipment|Enterprise|Location|StorageLocation|Container|Routing|ReasonCode)?Id$)",k) and not usealt: v=None; nm=None
                if nul and re.search(r"(reversalOf|qualityHold|deviationPermit)",k): v=None; nm=None
            meta[k]=nm
        elif k.endswith("Name") and k[:-4]+"Id" in meta: v=meta[k[:-4]+"Id"]
        elif k+"Id" in meta: v=meta[k+"Id"]
        elif (c["entity"],k) in VALUE_OVERRIDE: v=VALUE_OVERRIDE[(c["entity"],k)]
        elif (c["entity"],k) in CHILD_TEXT: v=CHILD_TEXT[(c["entity"],k)]
        elif k in TD:
            ex=TD[k][1][0]
            if ex=="(entity)":
                e=ES.get(c["entity"],["","",""]); v=(e[2] if (k=="description" and e[2]) else (e[1] or e[2])) if c["parent"] is None else None
                if k=="description" and c["parent"] is None and c["displayField"]!="description" and not e[2]: v=e[1]
                if v is None or v=="": v=words(c["entity"]).capitalize()+" "+rec
            else: v=ex if ex!="" else None
        elif k in ND:
            ex=ND[k][1][0]
            if ex=="": v=None
            elif t in("Int32","Int64"): v=int(float(ex))
            elif t=="Double": v=float(ex)
            else: v=ex if "." in ex or t!="Decimal128" else ex
        elif t=="Boolean": v=not bool(FALSEB.search(k))
        elif t=="Date":
            if nul and re.search(r"(void|revok|removed|scrapp|cancel|nextRetry|lastFailure|interimApproval)",k): v=None
            elif FUT.search(k): v=D(datetime.datetime(2027,3,31,18,29,59) if re.search(r"validTo|effectiveTo|expir",k) else datetime.datetime(2026,10,27,18,30,0))
            elif PAST.search(k) or (master and not re.search(r"^last(Login|Seen|Success|Issued|Downloaded)",k)): v=D(datetime.datetime(2026,3,31,18,30,0))
            elif re.search(r"Date$",k) or k in("horizonFrom",): v=D(datetime.datetime(2026,9,28,18,30,0))
            elif k=="horizonTo": v=D(datetime.datetime(2026,10,12,18,30,0))
            elif re.match(r"(plannedStart|hourStart|periodStart|intervalStart|clockOn|startedAt|raisedAt|occurredAt|timestamp|queueSince)",k): v=D(BASE)
            elif k=="plannedEndAt" or re.match(r"(periodEnd|clockOff)",k): v=D(BASE+datetime.timedelta(hours=8))
            elif k=="hourEndAt": v=D(BASE+datetime.timedelta(hours=1))
            elif k=="intervalEndAt": v=D(BASE+datetime.timedelta(minutes=15))
            elif re.match(r"(due|required|expectedRelease|containmentDue|plannedDispatch)",k): v=D(BASE+datetime.timedelta(days=2))
            else:
                v=D(seq[0]); seq[0]=seq[0]+(datetime.timedelta(seconds=20) if c["rootEntity"] in SHORT else datetime.timedelta(minutes=95))
            if v and v[1]>=BASE and v[1]<datetime.datetime(2026,10,11): alldates.append(v[1])
        if t=="Decimal128" and v is not None: v=("dec",str(v))
        elif t=="Int64" and v is not None: v=("long",int(v))
        elif t=="Int32" and v is not None: v=("int",int(v))
        elif t=="Double" and v is not None: v=("dbl",float(v))
        doc[k]=v
    if "updatedAt" in doc: doc["updatedAt"]=D(max(alldates+[BASE]))
    return doc
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
LINEKEYS=["lineNo","stepNo","itemNo","taskNo","actionNo","findingNo","elementNo","levelNo","stageNo","releaseNo","revisionNo","rank","level","lotSizeFrom","subgroupNo"]
def indexes(c):
    ks=[f["key"] for f in c["fields"]]; out=[]; e=c["entity"]
    def add(keys,unique,why): out.append((collections.OrderedDict(keys),unique,why))
    if c["kind"]=="entity":
        add(([("siteId",1)] if "siteId" in ks else [])+[("recordNo",1)],True,"Business identifier is unique within the site")
        if "status" in ks: add([("siteId",1),("status",1)] if "siteId" in ks else [("status",1)],False,"Work lists filtered by lifecycle state")
        refs=[f["key"] for f in c["fields"] if f["ref"] and f["ref"]!="(polymorphic)" and f["key"]!="siteId" and not f["key"].endswith("ById")][:5]
        for r in refs: add([(r,1)],False,"Look-up of documents by %s"%words(r[:-2]))
        if "relatedEntityId" in ks: add([("relatedCollectionName",1),("relatedEntityId",1)],False,"Look-up by the related document")
        if c["dataClass"]=="transaction":
            d=next((f["key"] for f in c["fields"] if f["type"]=="Date" and f["key"] not in("createdAt","updatedAt")),"createdAt")
            add([("siteId",1),(d,-1)],False,"Time-ordered lists and reports by %s"%words(d))
        sp={"erpMessage":[([("idempotencyKey",1)],True,"A repeated delivery of the same message is rejected")],"statusDefinition":[([("collectionName",1),("statusCode",1)],True,"One definition per collection and status code")],
            "processReading":[([("processTagId",1),("timestamp",-1)],False,"Trend of one tag over time")],"serialNumber":[([("dataMatrixPayload",1)],True,"A marked code is never issued twice")],
            "inventoryBalance":[([("itemId",1),("lotId",1),("storageLocationId",1),("stockStatus",1)],True,"One balance row per item, lot, location and stock status")],"user":[([("userName",1)],True,"Login name is unique"),([("badgeNo",1)],True,"Badge number is unique")],
            "skillCertification":[([("userId",1),("skillId",1),("validTo",-1)],False,"Operator lock-out check at station login")],"genealogyLink":[([("childLotId",1)],False,"Forward trace from a component lot to the units that contain it"),([("parentWipUnitId",1)],False,"Backward trace from a unit to its components")],
            "componentLotLink":[([("childLotId",1)],False,"Backward lot trace"),([("parentLotId",1)],False,"Forward lot trace")],"equipmentState":[([("equipmentId",1),("startedAt",-1)],False,"State history of one equipment")],
            "torqueResult":[([("wipUnitId",1),("tightenedAt",-1)],False,"Tightening history of one unit")],"leakTestResult":[([("wipUnitId",1),("testedAt",-1)],False,"Test history of one unit")],
            "operationExecution":[([("wipUnitId",1),("stepNo",1),("attemptNo",1)],False,"History of one unit through the routing"),([("workCenterId",1),("startedAt",-1)],False,"Activity of one work center over time")],
            "energyReading":[([("meterIotDeviceId",1),("intervalStartAt",-1)],False,"Consumption of one meter over time")],"systemConfiguration":[],"auditTrail":[([("relatedCollectionName",1),("relatedEntityId",1),("changedAt",-1)],False,"Change history of one document")]}
        for a,b,cc in sp.get(e,[]): add(a,b,cc)
    else:
        pe=bycol[c["parent"]]["entity"]; pk=pe+"Id" if pe!="site" else "siteId"
        if c["kind"]=="relationship":
            tk=[f["key"] for f in c["fields"] if f["ref"] and f["key"] not in("siteId",pk,"createdById","updatedById")][0]
            add([(pk,1),(tk,1)],True,"One link per pair"); add([(tk,1),(pk,1)],False,"Look-up from the other side of the relationship")
        else:
            lk=next((x for x in LINEKEYS if x in ks),None) or ("sequenceNo" if "sequenceNo" in ks else None)
            if e=="msaStudyTrial": add([(pk,1),("appraiserUserId",1),("partNo",1),("trialNo",1)],True,"One reading per appraiser, part and trial")
            elif lk: add([(pk,1),(lk,1)],True,"Lines of one parent in order; one line per number")
            else: add([(pk,1)],False,"Lines of one parent")
            for r in [f["key"] for f in c["fields"] if f["ref"] and f["ref"]!="(polymorphic)" and f["key"] not in("siteId",pk) and not f["key"].endswith("ById")][:3]: add([(r,1)],False,"Look-up of lines by %s"%words(r[:-2]))
    # de-duplicate
    seen=set(); res=[]
    for k,u,w in out:
        sig=json.dumps(k)
        if sig in seen: continue
        seen.add(sig); res.append((k,u,w))
    return res
def w(p,t):
    p=os.path.join(ROOT,p); os.makedirs(os.path.dirname(p),exist_ok=True); open(p,"w",encoding="utf-8").write(t)
def cell(s): return str(s).replace("|","&#124;").replace("\n"," ")
# root entity for CORE lookup and system detection
for c in cols:
    r=c
    while r["parent"]: r=bycol[r["parent"]]
    c["rootEntity"]=r["entity"]; c["sourceEntity"]=r["entity"]
refby=collections.defaultdict(list)
for c in cols:
    for f in c["fields"]:
        if f["ref"] and f["ref"]!="(polymorphic)" and f["key"] not in("createdById","updatedById","siteId"):
            if c["collection"] not in refby[f["ref"]]: refby[f["ref"]].append(c["collection"])
children=collections.defaultdict(list)
for c in cols:
    if c["parent"]: children[c["parent"]].append(c)
KINDTXT={"entity":"Entity","child":"Child","relationship":"Relationship","valueList":"Value list"}
report=[]; tot=collections.Counter()
for m in order:
    summ="# %s (%s) - module summary\n\n| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |\n|---|---|---|---|---|---|---|---|\n"%(MODN[m],m); n=0
    for c in cols:
        if c["module"]!=m: continue
        n+=1; name=c["collection"]; doc=SEED[name][0]; idx=indexes(c)
        rows=[]; props=collections.OrderedDict(); nreq=0; nen=0
        for i,f in enumerate(c["fields"],1):
            nul=nullable(c,f); en=enum(c,f); desc=describe(c,f,nul)
            if not nul: nreq+=1
            if en: nen+=1
            ref=""
            if f["ref"]=="(polymorphic)": ref="Any collection (see relatedCollectionName)"
            elif f["ref"]: ref=byent[f["ref"]]["collection"]+"._id"
            allowed="; ".join(en) if en else ("Reference: "+ref if ref else "")
            rows.append("| %d | %s | %s | %s | %s | `%s` | %s |"%(i,f["key"],f["type"],"Yes" if not nul else "No (null allowed)",cell(desc),cell(sh(doc[f["key"]])),cell(allowed)))
            p=collections.OrderedDict(); p["bsonType"]=BT[f["type"]] if not nul else [BT[f["type"]],"null"]; p["description"]=desc
            if en: p["enum"]=en+([None] if nul else [])
            props[f["key"]]=p
            # self-check of the sample against the rule
            v=doc[f["key"]]
            if v is None and not nul: report.append((name,f["key"],"null in sample but key is required"))
            if en and v is not None and v not in en: report.append((name,f["key"],"sample value not in allowed values: %s"%v))
            exp={"String":str,"Boolean":bool}.get(f["type"])
            if v is not None:
                ok=(isinstance(v,str) if f["type"]=="String" else isinstance(v,bool) if f["type"]=="Boolean" else isinstance(v,tuple) and v[0]=={"Date":"date","Int32":"int","Int64":"long","Decimal128":"dec","Double":"dbl"}[f["type"]])
                if not ok: report.append((name,f["key"],"sample type mismatch"))
        tot["collections"]+=1; tot["keys"]+=len(c["fields"]); tot["required"]+=nreq; tot["enums"]+=nen; tot["indexes"]+=len(idx)
        # ---- spec
        s="# %s\n\n"%name
        src=cat.get(c["sourceConcept"])
        if c["kind"]=="entity": purpose=src[4] if src else {"enumerationValue":"Allowed values of fixed enumeration keys, one document per collection, key and value"}.get(c["entity"],"Status values and allowed transitions per collection (status mapping)")
        else:
            pe=bycol[c["parent"]]["entity"]; wds=words(c["entity"][len(pe):])
            purpose={"child":"One document per %s of a %s"%(wds,words(pe)),"relationship":"Links one %s to one %s; one document per link"%(words(pe),wds),"valueList":"One document per %s value of a %s"%(wds,words(pe))}[c["kind"]]
        s+="| Property | Value |\n|---|---|\n| Module | %s (%s) |\n| Purpose | %s |\n| Kind | %s |\n| Data class | %s |\n| Parent collection | %s |\n| _id pattern | %s |\n| Display value used by references | %s |\n| Keys | %d (%d required, %d may be null) |\n"%(MODN[m],m,cell(purpose),KINDTXT[c["kind"]],c["dataClass"].capitalize(),c["parent"] or "none",c["idPattern"],c["displayField"],len(c["fields"]),nreq,len(c["fields"])-nreq)
        if c["kind"]=="entity" and src: s+="| Estimated volume per year | %s |\n| Storage | %s |\n"%(src[7],src[8])
        s+="\n## Structure\n\n"
        if c["kind"]=="entity":
            s+="Flat entity collection: one document per %s, all keys top-level and scalar.\n"%words(c["entity"])
            if children[name]:
                s+="\nRepeating data of this entity is held in separate collections, one document per occurrence, each pointing back with %sId:\n\n| Collection | Kind | Holds |\n|---|---|---|\n"%c["entity"]
                def walk(pn,depth):
                    out=""
                    for ch in children[pn]:
                        pe=bycol[ch["parent"]]["entity"]
                        out+="| %s | %s | %s%s |\n"%(ch["collection"],KINDTXT[ch["kind"]],"" if depth==0 else "(below %s) "%ch["parent"],words(ch["entity"][len(pe):]))
                        out+=walk(ch["collection"],depth+1)
                    return out
                s+=walk(name,0)
            if src and "time-series" in src[8]: s+="\nStorage note: this collection is a candidate for a MongoDB time-series collection (time key and meta key to be fixed at deployment). A time-series collection cannot carry a JSON Schema validator, so the validator file then serves as the rule the application enforces.\n"
        else:
            pe=bycol[c["parent"]]["entity"]
            s+={"child":"Child collection. The parent %s can have several lines of this kind, and DATA-001 does not allow an array inside the parent, so each line is its own document. %sId and %sName point to the parent.\n",
                "relationship":"Relationship collection. A %s can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. %sId and %sName point to the parent.\n",
                "valueList":"Value-list collection. A %s can have several values of this kind, and DATA-001 does not allow an array, so each value is its own document. %sId and %sName point to the parent.\n"}[c["kind"]]%(words(pe),pe,pe)
            s+="Data class (%s) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.\n"%c["dataClass"]
        s+="\n## Field dictionary\n\nEvery key is present in every document. \"Required\" means the value may not be null.\n\n| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |\n|---|---|---|---|---|---|---|\n"+"\n".join(rows)+"\n"
        if c["statusValues"]: s+="\n## Status values\n\n%s. Initial state: %s. The values are maintained in u_mes_syst_statusDefinition.\n"%(", ".join(c["statusValues"]),c["statusValues"][0])
        s+="\n## Indexes\n\n| # | Keys | Unique | Purpose |\n|---|---|---|---|\n"
        js='// Indexes for %s\n'%name
        for i,(k,u,why) in enumerate(idx,1):
            ks="{ "+", ".join("%s: %d"%(a,b) for a,b in k.items())+" }"; iname=("ux_" if u else "ix_")+"_".join(k.keys())
            s+="| %d | `%s` | %s | %s |\n"%(i,ks,"Yes" if u else "No",why)
            js+='db.getCollection("%s").createIndex(%s, { name: "%s"%s });\n'%(name,ks,iname[:120],", unique: true" if u else "")
        rb=refby.get(c["entity"],[])
        s+="\n## Referenced by\n\n"+((", ".join(rb)+".\n") if rb else "No other collection refers to this one.\n")
        if c["entity"] in("site","user"): s+="\nIn addition, every collection carries siteId, and every transaction collection carries createdById and updatedById.\n"
        s+="\n## Files\n\n- Validator: 03_design/%s/validators/%s.json\n- Indexes: 03_design/%s/indexes/%s.js\n- Sample documents (10): 03_design/%s/samples/%s.js\n"%(DOMF[m],name,DOMF[m],name,DOMF[m],name)
        w("03_design/%s/specs/%s.md"%(DOMF[m],name),s)
        val={"collMod":name,"validator":{"$jsonSchema":{"bsonType":"object","title":name,"required":[f["key"] for f in c["fields"]],"additionalProperties":False,"properties":props}},"validationLevel":"strict","validationAction":"error"}
        w("03_design/%s/validators/%s.json"%(DOMF[m],name),json.dumps(val,indent=2,ensure_ascii=False)+"\n")
        w("03_design/%s/indexes/%s.js"%(DOMF[m],name),js)
        summ+="| %d | %s | %s | %s | %d | %d | %d | %d |\n"%(n,name,KINDTXT[c["kind"]],c["dataClass"],len(c["fields"]),nreq,nen,len(idx))
    w("03_design/%s/module_summary.md"%DOMF[m],summ)
r="# Specification check\n\nRun: 11 October 2026 | Tool: 05_generator/gen_specs.py\n\n| Item | Count |\n|---|---|\n| Collections specified | %d |\n| Keys specified | %d |\n| Required (non-null) keys | %d |\n| Keys that may be null | %d |\n| Keys with allowed values | %d |\n| Indexes defined | %d |\n| Files written (spec, validator, index script per collection, plus 10 module summaries) | %d |\n\n## Example document (first sample document) checked against its own specification\n\nThe full check of all ten documents per collection is in sample_data_validation.md. Checks: every key present; value type equals the BSON type; a null only where null is allowed; a value from the allowed list where one is defined.\n\n"%(tot["collections"],tot["keys"],tot["required"],tot["keys"]-tot["required"],tot["enums"],tot["indexes"],tot["collections"]*3+10)
r+=("Result: all %d sample documents pass.\n"%tot["collections"]) if not report else ("Result: %d findings.\n\n| Collection | Key | Finding |\n|---|---|---|\n"%len(report)+"".join("| %s | %s | %s |\n"%x for x in report))
r+="\n## Not covered by this check\n\n- Requiredness, allowed values and descriptions were produced from rules and dictionaries in 05_generator (keydict_text.py, keydict_num.py, gen_specs.py); they have not been reviewed collection by collection by a person.\n- Validators have not been loaded into a MongoDB server in this run.\n"
w("08_validation/reports/specification_check.md",r)

# ---- fixed enumerations (kept as coded text, values held in u_mes_syst_enumerationValue)
en_rows=[]; 
for m in order:
    for c in cols:
        if c["module"]!=m: continue
        for f in c["fields"]:
            if f["key"]=="status": continue
            en=enum(c,f)
            if en: en_rows.append((MODN[m],c["collection"],f["key"],en))
s="# Fixed enumeration values\n\nKeys whose values are fixed by the application logic stay coded text (data_modeling_standard.md section 11, rule B). Their allowed values are listed here, enforced by the validators, and stored as data in `u_mes_syst_enumerationValue` (one document per collection, key and value). Status values are in status_values.md.\n\nKeys: %d | Values: %d\n\n| Module | Collection | Key | Allowed values |\n|---|---|---|---|\n"%(len(en_rows),sum(len(r[3]) for r in en_rows))
for r in en_rows: s+="| %s | %s | %s | %s |\n"%(r[0],r[1],r[2],"; ".join(r[3]))
w("04_reference_data/code_lists/enumeration_values.md",s)
conv=M.get("conversions",[])
newm=[c for c in cols if c["entity"] in NEWMASTER]
s="# Master data review\n\nRun: 11 October 2026 | Trigger: owner review of the user document (department, designation, employmentType held as text without a master collection).\n\nScope: every text key of every collection was reviewed against data_modeling_standard.md section 11.\n\n| Result | Count |\n|---|---|\n| New master collections | %d |\n| Keys converted from text to a master reference | %d |\n| Keys kept as fixed enumerations (values in u_mes_syst_enumerationValue) | %d |\n\n## New master collections\n\n| # | Collection | Purpose | Keys |\n|---|---|---|---|\n"%(len(newm),sum(1 for x in conv if x["master"]),len(en_rows))
for i,c in enumerate(newm,1): s+="| %d | %s | %s | %s |\n"%(i,c["collection"],cat[c["sourceConcept"]][4],", ".join(f["key"] for f in c["fields"]))
s+="\n## Keys converted\n\nArray notation refers to the concept model; in the flat model an array of references is a relationship collection.\n\n| # | Concept collection | Key before | Key after | Master collection |\n|---|---|---|---|---|\n"
for i,x in enumerate(conv,1): s+="| %d | %s | %s | %s | %s |\n"%(i,byent[[c for c in cols if c["sourceConcept"]==x["concept"] and c["kind"]=="entity"][0]["entity"]]["collection"],x["oldKey"],x["newKey"],byent[x["master"]]["collection"] if x["master"] else "none (renamed only, to avoid confusion with designationId)")
s+="\n## Keys reviewed and kept as fixed enumerations\n\nListed with their values in 04_reference_data/code_lists/enumeration_values.md.\n"
w("08_validation/reports/master_data_review.md",s)
print("enum keys",len(en_rows),"converted",len(conv),"new masters",len(newm))
print(dict(tot),"findings",len(report)); [print(x) for x in report[:40]]
