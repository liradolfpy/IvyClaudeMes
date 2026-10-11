"""Builds the flat (DATA-001) model from the concept model (catalogue.py + keys.py).
Output: model/flat_model.json. Rules are documented in 00_governance/data_modeling_standard.md."""
import re, json, collections, os
from catalogue import C
from keys import K

APP="u_mes"
MOD={"1":"mdm","2":"prd","3":"exe","4":"mat","5":"trc","6":"qlt","7":"eqp","8":"mnt","9":"sys","10":"ehs"}
MODNAME={"mdm":"Master data","prd":"Product definition","exe":"Planning and execution","mat":"Materials","trc":"Traceability","qlt":"Quality","eqp":"Equipment and performance","mnt":"Maintenance and tooling","sys":"Integration and system","ehs":"Energy, safety and andon"}
ENT={"enterprises":"enterprise","work_centres":"workCenter","equipment":"equipment","calendars":"workCalendar","units_of_measure":"unitOfMeasure","certifications":"skillCertification","variants":"productVariant","boms":"billOfMaterial","bills_of_process":"billOfProcess","process_data":"processReading","event_logs":"businessEvent","documents":"controlledDocument","pfmeas":"pfmea","capas":"capa","alarms":"alarm","audits":"audit","labels":"label","kits":"kit","lots":"lot","audit_trails":"auditTrail","inventory_balances":"inventoryBalance","as_built_records":"asBuiltRecord","spc_charts":"spcChart","spc_samples":"spcSample","msa_studies":"msaStudy","erp_messages":"erpMessage","iot_devices":"iotDevice","oee_records":"oeeRecord","wip_units":"wipUnit"}
def camel(n):
    p=n.split("_"); return p[0]+"".join(x.title() for x in p[1:])
def sing(w):
    if w.endswith("ies"): return w[:-3]+"y"
    if w.endswith("sses"): return w[:-2]
    if w.endswith("s") and not w.endswith("ss") and not w.endswith("us"): return w[:-1]
    return w
def ent(n): return ENT.get(n) or sing(camel(n))
MASTER=set("""enterprises sites areas lines work_centres equipment shifts calendars roles users skills customers suppliers units_of_measure
items variants boms operations routings bills_of_process work_instructions recipes storage_locations packaging_specifications label_templates
characteristics control_plans inspection_plans sampling_plans check_sheets spc_charts defect_codes pfmeas gauges reason_codes process_tags
maintenance_plans spare_parts tools integration_connectors iot_devices operator_apps number_ranges system_configurations""".split())
NOSTATUS={"process_data","energy_readings","event_logs","audit_trails","electronic_signatures"}
A=["Active","Inactive"]; V=["In Preparation","Released","Obsolete"]
STATUS={"equipment":["Active","Under Maintenance","Decommissioned"],"users":["Active","Suspended","Left"],"suppliers":["Approved","Conditional","Blocked","Inactive"],"items":["Active","Phase Out","Obsolete"],
"variants":V,"boms":V,"routings":V,"bills_of_process":V,"work_instructions":V,"recipes":V,"control_plans":V,"inspection_plans":V,"check_sheets":V,"pfmeas":V,"packaging_specifications":V,"label_templates":V,"operator_apps":V,"documents":V,
"engineering_changes":["Raised","Under Evaluation","Approved","Implemented","Closed","Rejected"],"customer_schedules":["Received","Confirmed","Partially Shipped","Completed","Replaced"],
"production_orders":["Created","Released","In Progress","On Hold","Completed","Closed","Cancelled"],"production_schedules":["Planned","Published","In Progress","Completed"],"dispatch_lists":["Generated","Acknowledged","Closed"],
"operation_executions":["Started","Completed","Aborted"],"step_completions":["Completed","Skipped","Overridden"],"wip_units":["Created","In Process","On Hold","In Rework","Completed","Packed","Shipped","Scrapped"],
"lots":["Created","Available","In Process","On Hold","Consumed","Closed","Rejected"],"containers":["Empty","Filling","Full","Sealed","Shipped","Returned","Under Repair"],"labour_bookings":["Open","Closed","Approved"],
"changeovers":["Planned","In Progress","Awaiting First Off Approval","Completed"],"shift_handovers":["Open","Handed Over","Acknowledged"],"shift_rosters":["Planned","Published","Closed"],
"certifications":["Valid","Expiring Soon","Expired","Revoked"],"inventory_balances":["Active","Closed"],"material_movements":["Posted","Reversed"],"goods_receipts":["Received","Under Inspection","Accepted","Partially Accepted","Rejected"],
"kits":["Requested","Picking","Picked","Delivered","Short"],"material_requests":["Raised","Acknowledged","Delivered","Cancelled"],"material_consumptions":["Posted","Reversed"],"labels":["Printed","Verified","Reprinted","Voided"],
"shipments":["Planned","Loading","Dispatched","Delivered","Cancelled"],"serial_numbers":["Reserved","Issued","Marked","Shipped","Voided","Scrapped"],"genealogy_links":["Active","Removed"],"component_lot_links":["Active","Removed"],
"as_built_records":["Compiling","Released"],"check_sheet_results":["In Progress","Completed","Verified"],"inspection_results":["Recorded","Voided"],"spc_charts":["Active","Suspended","Inactive"],"spc_samples":["Recorded","Under Investigation","Closed"],
"nonconformances":["Open","Contained","Dispositioned","Closed","Cancelled"],"rework_orders":["Issued","In Progress","Awaiting Reinspection","Completed","Scrapped"],"scrap_records":["Declared","Approved","Disposed"],
"quality_holds":["Active","Partially Released","Released"],"deviation_permits":["Requested","Approved","Expired","Closed","Rejected"],"capas":["Open","Containment Done","Root Cause Identified","Actions Implemented","Verified","Closed"],
"ppap_submissions":["In Preparation","Submitted","Approved","Interim Approved","Rejected"],"gauges":["Active","Due For Calibration","Overdue","Under Calibration","Blocked","Retired"],"gauge_calibrations":["Planned","Completed","Failed"],
"msa_studies":["Planned","Completed","Accepted","Not Accepted"],"audits":["Planned","In Progress","Completed","Closed"],"customer_complaints":["Received","Containment Sent","Under Analysis","Closed","Rejected"],
"equipment_states":["Open","Closed"],"downtime_events":["Open","Classified","Closed"],"production_counts":["Open","Closed"],"oee_records":["Calculated","Recalculated"],"alarms":["Raised","Acknowledged","Cleared"],
"torque_results":["Recorded","Voided"],"leak_test_results":["Recorded","Voided"],"maintenance_plans":["Active","Suspended","Inactive"],"maintenance_work_orders":["Reported","Planned","In Progress","Completed","Closed","Cancelled"],
"spare_parts":["Active","Obsolete"],"tools":["Available","Mounted","In Maintenance","Life Expired","Scrapped"],"tool_life_records":["Recorded","Voided"],"erp_messages":["Queued","Sent","Acknowledged","Failed","Dead Letter"],
"integration_connectors":["Active","Disabled"],"iot_devices":["Active","Inactive","Retired"],"notifications":["Raised","Sent","Acknowledged","Expired"],"andon_events":["Raised","Acknowledged","Resolved","Cancelled"],
"safety_incidents":["Reported","Under Investigation","Actions Open","Closed"]}
CHILDSTATUS={"elementStatus":["Not Started","In Progress","Complete","Not Applicable"],"entryStatus":["Queued","Started","Completed","Skipped"]}
# ---- source-key renames (terminology, vague names, redundant state fields)
GLOBAL=[("variantId","productVariantId"),("variantIds","productVariantIds"),("bomId","billOfMaterialId"),("alendarId","alendarId"),("defaultCalendarId","defaultWorkCalendarId"),(" calendarId"," workCalendarId"),("ocumentId","ocumentId"),("Centre","Center"),("centreLine","centerLine"),("UomId","UnitOfMeasureId"),("uomId","unitOfMeasureId"),("holdId","qualityHoldId"),("badgeId","badgeNo"),("controllerResultId","controllerResultNo"),
("nodeId","opcNodeAddress"),("lastCalibrationId","lastGaugeCalibrationId"),("previousVersionAppId","previousVersionOperatorAppId"),("reversalOfMovementId","reversalOfMaterialMovementId"),
("supersedesScheduleId","supersedesCustomerScheduleId"),("triggeredBy","triggerSource"),("byUserId","authorUserId"),("correlationKey","correlationNo")]
LOCAL={"process_data":[("value, valueText","tagValue, tagValueText")],"event_logs":[(" data,"," eventPayloadText,")],
"system_configurations":[("valueString","configValueText"),("valueNumber","configValueNumber"),("valueBoolean","configValueFlag"),("valueObject","configValueJson")],
"step_completions":[("valueText","enteredText"),("valueNumber","enteredNumber"),("valueBoolean","enteredFlag")],"msa_studies":[("trials[].value","trials[].measuredValue")],
"capas":[("d1Team[]","teamMembers[]"),("d3Containment[]","containmentActions[]"),("d5CorrectiveActions[]","correctiveActions[]"),("d6Implementation[]","implementationActions[]")],
"sampling_plans":[("table[]","sizeRows[]")],"maintenance_work_orders":[("sparesUsed[]","usedSpareParts[]")],"work_instructions":[("ppeRequired[]","ppeItems[]"),("steps[].text","steps[].instructionText")],
"reason_codes":[(" path[],","")],"downtime_events":[("reasonPath[]","reasonPathText"),("comments[].at","comments[].commentedAt"),("comments[].text","comments[].commentText")],
"customer_complaints":[("communications[].at","communications[].communicatedAt")],"spc_samples":[(" mean, range,"," subgroupMean, subgroupRange,")],"calendars":[("exceptions[].date","exceptions[].exceptionDate")],
"label_templates":[("fields[].x, fields[].y","fields[].positionXMm, fields[].positionYMm")],"wip_units":[(" unitStatus,","")],"containers":[(" containerStatus,","")],"tools":[(" toolStatus,","")],
"serial_numbers":[(" serialStatus,","")],"erp_messages":[(" messageStatus,","")],"gauges":[(" calibrationStatus,","")],"suppliers":[(" approvalStatus,","")],
"ppap_submissions":[("elements[].elementStatus","elements[].status")],"dispatch_lists":[("entries[].entryStatus","entries[].status")]}
LOCAL2={"notifications":[(" body,"," bodyText,")],"audit_trails":[("changes[].field","changes[].changedFieldName"),(" action,"," changeAction,"),(" hash"," entryHash")],
"operator_apps":[("triggers[].event","triggers[].triggerEvent"),("triggers[].action","triggers[].triggerAction"),("triggers[].target","triggers[].triggerTarget")],
"engineering_changes":[("approvals[].function","approvals[].businessFunction"),("affectedObjects[].action","affectedObjects[].changeAction")],"deviation_permits":[("approvals[].function","approvals[].businessFunction")],
"customers":[("contacts[].function","contacts[].businessFunction")],"suppliers":[("contacts[].function","contacts[].businessFunction")],
"equipment_states":[(" state, subState,"," stateCode, subStateCode,")],"process_data":[(" quality,"," signalQuality,")],"energy_readings":[(" quality"," signalQuality")],
"integration_connectors":[("functions[].path","functions[].endpointPath"),("functions[].schedule","functions[].scheduleExpression")],"event_logs":[(" message,"," messageText,")],
"maintenance_work_orders":[("labour[].minutes","labour[].labourMinutes")],"oee_records":[("losses[].minutes","losses[].lossMinutes"),("losses[].units","losses[].lossUnits")],
"number_ranges":[(" mask,"," formatMask,"),(" example"," exampleValue")],"msa_studies":[(" method,"," studyMethod,")],"customer_complaints":[("communications[].summary","communications[].communicationSummary")],
"routings":[("nextSteps[].condition","nextSteps[].nextStepCondition")],"label_templates":[("fields[].format","fields[].fieldFormat")],"inspection_plans":[(" trigger,"," collectionTrigger,")],
"check_sheets":[("items[].uom","items[].unitText")]}
for k,v in LOCAL2.items(): LOCAL.setdefault(k,[]).extend(v)
names=[c[0] for c in C]
E={n:ent(n) for n in names}
assert len(set(E.values()))==len(E)
STEM={v.lower():v for v in E.values()}
ALIAS={"user":"user","document":"controlledDocument","location":"storageLocation","variant":"productVariant","calendar":"workCalendar","bom":"billOfMaterial","bop":"billOfProcess","schedule":"customerSchedule"}
def target(stem):
    s=stem.lower(); best=None
    for t,v in list(STEM.items())+[(a,b) for a,b in ALIAS.items()]:
        if s.endswith(t) and (best is None or len(t)>len(best[0])): best=(t,v)
    return best[1] if best else None
INTNO=set("stepNo lineNo sequenceNo attemptNo subgroupNo sampleNo tighteningNo taskNo actionNo itemNo findingNo elementNo levelNo stageNo trialNo regrindNo revisionNo releaseNo planLineNo bomLineNo currentStepNo entryStepNo nextStepNo returnStepNo reworkReturnStepNo reworkAttemptNo completedStep partNo".split())
INT=set("actualOutput plannedOutput outputActual outputPlanned outputRework outputScrap cumulativeGood cumulativeShipped cumulativeTarget cumulativeRequired retryPolicyMaxAttempts sequenceHint yearOfManufacture labourMinutes lossMinutes lossUnits version bomVersion bopVersion routingVersion scheduleVersion workInstructionVersion checkSheetVersion calculationVersion documentVersionBefore documentVersionAfter maxQueueTimeMin setupTimeMin standardSetupTimeMin escalationLevel level layer rank year minimumLevelRequired cavities copies attempts maxAttempts capacity headcount plannedHeadcount actualHeadcount manning manningStandard standardManning partsCount trialsCount subgroupSize decimalPlaces fiscalYearStartMonth severity occurrence detection rpn revisedSeverity revisedOccurrence revisedDetection maxRegrinds layersPerContainer unitsPerLayer containersPerPallet totalContainers basedOnSubgroups incrementBy port vlan acceptNumber rejectNumber sampleSize lotSizeFrom lotSizeTo unitsLost unitsProduced units modelYear submissionLevel ppapLevelDefault ppmTarget ppmLast12Months ppmImpact capacityPerShift targetPerHour frequencyEveryNUnits skipLotConsecutiveAcceptedToSkip utcOffsetMinutes transitDays cavityNo bodyCavityNo questionsCount".split())
LONG=set("lifetimeCycles currentValue minValue maxValue lastIssuedValue sizeBytes lifeLimit lifeUsed lifeRemaining lifeUsedBefore lifeUsedAfter cyclesThisEvent".split())
DBL=set("geoLatitude geoLongitude tagValue powerFactor".split())
DEC=set("resultsGrrPctStudyVariation resultsGrrPctTolerance temperatureC nominal lowerSpecLimit upperSpecLimit lowerLimit upperLimit measuredValue deviation subgroupMean subgroupRange stdDev ucl lcl centerLine uclRange centerLineRange lclRange setPoint capabilityCp capabilityCpk capabilityPp capabilityPpk targetCpk aql factorToBase offsetToBase resolution accuracy uncertainty consumption triggerValue limitValue deadband lowLimit highLimit lowLowLimit highHighLimit engineeringMin engineeringMax rangeMin rangeMax asFound asLeft tolerance resultsEquipmentVariation resultsAppraiserVariation resultsGrr resultsPartVariation resultsTotalVariation resultsNdc resultsBiasValue resultsKappa requestedValue specifiedValue expectedValue ratedCapacity oeeTarget assessmentScore trainingHours meterReadingStart meterReadingEnd specificConsumption skipLotSkipFraction enteredNumber answerNumber configValueNumber lifetimeRunHours intervalValue reading leakTestLeakRate frequencyValue shiftAllowancePerDay".split())
BOOL=set("blockedForUse reportableToAuthority withinTolerance safetyCharacteristic onHold frozen verified overridden inControl withinLimits inLimits crossesMidnight paid enforced passed effective closed required backflush historise causedStop lineStopped overridden isComplete approvedByCustomer skipLotEnabled".split())
DATEK=set("currentStateSince queueSince dateOfJoining timestamp validFrom validTo effectiveFrom effectiveTo horizonFrom horizonTo interimApprovalValidTo".split())
MATQ={"inventory_balances","material_movements","material_consumptions","boms","kits","goods_receipts","lots","spare_parts","genealogy_links","component_lot_links","material_requests","bills_of_process","maintenance_plans","maintenance_work_orders"}
def btype(k,src):
    if k=="_id" or k.endswith("Id"): return "String"
    if k.endswith("At") or k.endswith("Date") or k in DATEK: return "Date"
    if k in DBL: return "Double"
    if k in LONG: return "Int64"
    if k in INTNO or k in INT or k=="schemaVersion": return "Int32"
    if k in BOOL or re.match(r"(is|has|can|requires|block|checks)[A-Z]",k) or re.search(r"(Required|Allowed|Enabled|Verified|Available|Posted|Flag|Notified|Accepted|Received|Made|Given|OnFail|ByScan|ToController|Signature|FromLimits|WithinTolerance)$",k): return "Boolean"
    if re.search(r"(Pct|Inr|Kg|Mm|Um|Nm|Deg|Bar|Pa|Sccm|Kw|Sqm|Hbw|Km|TemperatureC|CycleTimeSec|taktTimeSec|TimeSec)$",k) or k in DEC: return "Decimal128"
    if re.search(r"(Count|Minutes|Sec|Ms|Days|Months|Years)$",k): return "Int32"
    if re.search(r"Quantity$",k) or k.startswith("quantity"): return "Decimal128" if src in MATQ else "Int32"
    return "String"
COLS=collections.OrderedDict(); PROBLEMS=[]
def cap(s): return s[0].upper()+s[1:]
def expand(k,src):
    """one scalar source key -> list of (key,type,refEntity)"""
    if k=="refCollection": return [("relatedCollectionName","String",None)]
    if k=="refId": return [("relatedEntityId","String","(polymorphic)"),("relatedEntityName","String",None)]
    if k.endswith("By") and len(k)>2: return [(k+"Id","String","user"),(k,"String",None)]
    if k.endswith("Id"):
        t=target(k[:-2])
        if not t: PROBLEMS.append((src,k)); return [(k,"String",None)]
        return [(k,"String",t),(k[:-2]+"Name","String",None)]
    return [(k,btype(k,src),None)]
def norm(keys):
    out=[]
    for k in keys:
        parts=k.split(".")
        while len(parts)>1 and not parts[0].endswith("[]"):
            parts=[parts[0]+cap(parts[1])]+parts[2:]
        # embedded doc below an array level
        i=1
        while i<len(parts)-1:
            if not parts[i].endswith("[]"): parts=parts[:i]+[parts[i]+cap(parts[i+1])]+parts[i+2:]
            else: i+=1
        out.append(parts)
    return out
def build(src,entity,keys,parents,top):
    mod=MOD[[c for c in C if c[0]==src][0][1].split(" ")[0]]
    cname="%s_%s_%s"%(APP,mod,entity)
    master=src in MASTER
    f=[("_id","String",None),("recordNo","String",None)]
    if entity!="site": f+=[("siteId","String","site"),("siteName","String",None)]
    for p in parents:
        if p!="site": f+=[(p+"Id","String",p),(p+"Name","String",None)]
    groups=collections.OrderedDict(); scal=[]
    for parts in norm(keys):
        if len(parts)==1 and not parts[0].endswith("[]"): scal.append(parts[0])
        else: groups.setdefault(parts[0][:-2],[]).append(".".join(parts[1:]))
    body=[]
    for k in scal: body+=expand(k,src)
    if not top and not any(k in INTNO for k,_,_ in body): f.append(("sequenceNo","Int32",None))
    f+=body
    st=None
    if top and src not in NOSTATUS: st=STATUS.get(src,A); f.append(("status","String",None))
    elif not top:
        for k,v in CHILDSTATUS.items():
            pass
    f.append(("schemaVersion","Int32",None))
    if not master: f+=[("createdAt","Date",None),("createdById","String","user"),("createdBy","String",None),("updatedAt","Date",None),("updatedById","String","user"),("updatedBy","String",None)]
    ks=[x[0] for x in f]
    dup=[k for k in ks if ks.count(k)>1]
    if dup: PROBLEMS.append((cname,"DUP",sorted(set(dup))))
    disp=next((d for d in ("name","title","description","fullName") if d in ks),"recordNo")
    COLS[cname]=dict(collection=cname,module=mod,moduleName=MODNAME[mod],entity=entity,sourceConcept=src,kind="entity" if top else "child",dataClass="master" if master else "transaction",parent=("%s_%s_%s"%(APP,mod,parents[-1]) if parents else None),displayField=disp,statusValues=st,fields=[dict(key=a,type=b,ref=c) for a,b,c in f])
    for g,sub in groups.items():
        if sub==[""]:
            if g.endswith("Ids"):
                stem=g[:-3]; child=entity+cap(stem)
                if child==entity+cap(entity): child=entity+"Link"
                build_rel(src,child,stem,[*parents[-1:],entity] if False else [entity],mod,master,cname)
            else:
                child=entity+cap(sing(g)); build_val(src,child,sing(g),[entity],mod,master,cname)
        else:
            child=entity+cap(sing(g)); build(src,child,sub,[entity],False)
def std(child,parents,mod,master,parentc,extra,kind,src):
    cname="%s_%s_%s"%(APP,mod,child)
    f=[("_id","String",None),("recordNo","String",None),("siteId","String","site"),("siteName","String",None)]
    for p in parents:
        if p!="site": f+=[(p+"Id","String",p),(p+"Name","String",None)]
    f.append(("sequenceNo","Int32",None)); f+=extra; f.append(("schemaVersion","Int32",None))
    if not master: f+=[("createdAt","Date",None),("createdById","String","user"),("createdBy","String",None),("updatedAt","Date",None),("updatedById","String","user"),("updatedBy","String",None)]
    ks=[x[0] for x in f]
    if len(ks)!=len(set(ks)): PROBLEMS.append((cname,"DUP",[k for k in ks if ks.count(k)>1]))
    if cname in COLS: PROBLEMS.append((cname,"NAMECLASH"))
    COLS[cname]=dict(collection=cname,module=mod,moduleName=MODNAME[mod],entity=child,sourceConcept=src,kind=kind,dataClass="master" if master else "transaction",parent=parentc,displayField="recordNo",statusValues=None,fields=[dict(key=a,type=b,ref=c) for a,b,c in f])
def build_rel(src,child,stem,parents,mod,master,parentc):
    t=target(stem)
    if not t: PROBLEMS.append((src,stem+"Ids"))
    std(child,parents,mod,master,parentc,[(stem+"Id","String",t),(stem+"Name","String",None)],"relationship",src)
def build_val(src,child,key,parents,mod,master,parentc):
    std(child,parents,mod,master,parentc,[(key,btype(key,src),None)],"valueList",src)
for c in C:
    s=K[c[0]]
    for a,b in LOCAL.get(c[0],[]):
        assert a in s,(c[0],a); s=s.replace(a,b)
    for a,b in GLOBAL: s=s.replace(a,b)
    s=re.sub(r"\b([a-zA-Z]*?)[dD]ocumentId",lambda m:(m.group(1)+"ControlledDocumentId") if m.group(1) else "controlledDocumentId",s)
    build(c[0],E[c[0]],[k.strip() for k in s.split(",") if k.strip()],[],True)
# child status fields
for col in COLS.values():
    if col["kind"]=="child" and any(f["key"]=="status" for f in col["fields"]):
        col["statusValues"]=CHILDSTATUS["elementStatus"] if "ppap" in col["entity"] else CHILDSTATUS["entryStatus"]
# status mapping collections (flat)
def sysc(entity,fields,src):
    cname="%s_sys_%s"%(APP,entity)
    f=[("_id","String",None),("recordNo","String",None),("siteId","String","site"),("siteName","String",None)]+fields+[("status","String",None),("schemaVersion","Int32",None)]
    COLS[cname]=dict(collection=cname,module="sys",moduleName=MODNAME["sys"],entity=entity,sourceConcept=src,kind="entity",dataClass="master",parent=None,displayField="statusName" if entity=="statusDefinition" else "transitionName",statusValues=A,fields=[dict(key=a,type=b,ref=c) for a,b,c in f])
sysc("statusDefinition",[("collectionName","String",None),("fieldName","String",None),("statusCode","String",None),("statusName","String",None),("description","String",None),("sequenceNo","Int32",None),("isInitial","Boolean",None),("isFinal","Boolean",None),("colourCode","String",None)],"(new) status mapping")
sysc("statusTransition",[("collectionName","String",None),("fromStatusDefinitionId","String","statusDefinition"),("fromStatusDefinitionName","String",None),("toStatusDefinitionId","String","statusDefinition"),("toStatusDefinitionName","String",None),("transitionName","String",None),("requiresSignature","Boolean",None),("requiresReason","Boolean",None),("sequenceNo","Int32",None)],"(new) status mapping")
# ---- checks
ents={c["entity"] for c in COLS.values()}
for c in COLS.values():
    for f in c["fields"]:
        k=f["key"]
        if not re.fullmatch(r"_id|[a-z][A-Za-z0-9]*",k): PROBLEMS.append((c["collection"],"CASE",k))
        if f["ref"] and f["ref"]!="(polymorphic)" and f["ref"] not in ents: PROBLEMS.append((c["collection"],"REFTARGET",k,f["ref"]))
        if k.endswith("Id") and k!="_id" and f["ref"] is None: PROBLEMS.append((c["collection"],"NOREF",k))
        if k.endswith("Id") and k!="_id":
            pair=k[:-2]+"Name" if not k.endswith("ById") else k[:-2]
            if pair not in [x["key"] for x in c["fields"]]: PROBLEMS.append((c["collection"],"NOPAIR",k))
        if k.endswith("Ids") or "[" in k or "." in k: PROBLEMS.append((c["collection"],"NESTED",k))
    if not re.fullmatch(r"u_mes_[a-z]{3}_[a-z][A-Za-z0-9]*",c["collection"]): PROBLEMS.append((c["collection"],"COLLNAME"))
os.makedirs("model",exist_ok=True)
json.dump(dict(application=APP,modules=MODNAME,collections=list(COLS.values())),open("model/flat_model.json","w"),indent=1)
kinds=collections.Counter(c["kind"] for c in COLS.values())
print("collections",len(COLS),dict(kinds),"fields",sum(len(c["fields"]) for c in COLS.values()))
print("problems",len(PROBLEMS)); [print(p) for p in PROBLEMS[:60]]
