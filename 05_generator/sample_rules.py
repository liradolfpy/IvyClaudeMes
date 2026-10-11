"""Rules and overrides for the sample generator (which parent, which context, which reference, which value)."""
import re,datetime
from sample_universe import PROC,MASTER
UNSET=object(); N=10
PREF=["Closed","Completed","Released","Active","Recorded","Posted","Valid","Approved","Delivered","Shipped","Accepted","Dispatched","Resolved","Cleared","Acknowledged","Calculated","Verified","Printed","Available","Full","Mounted","Marked","Handed Over","Published","Classified","Dispositioned","Disposed","Implemented","Sent","Compiling","Complete","In Progress"]
FALSEB=re.compile(r"(Hold|Locked|overrid|MicroStop|causedStop|lineStopped|Secret|isPlanned|adjustmentMade|excluded|blocked|SafetyRelated|requiresHold|Insurance|reportable|firstAid|followUp|actionRequired|impactAssessment|frozen|crossesMidnight|isOptional|isSystemRole|isQuarantine|isMasterGauge|isSecondSignature|skipLot|isDirectedSource|vciRequired|requiresShutdown|requiresReason|isFinal|isBaseUnit|isInspection|isSpecialProcess|ppapRequired|closed$|configValueFlag|enteredFlag|backflush|mixedLots|requiresPhoto|isReturnable$|isInitial|isContract|isSupervisory|isInjury|requiresScrap|requiresRework|requiresCustomerApproval|isDefault)")
PAST=re.compile(r"(validFrom|effectiveFrom|originalDate|revisionDate|awarded|passwordChanged|customerApprovalDate|lastCalibrated|lastMaintained|lastDone|lastCleaned|lastReset|manufactured|firstReceived|approvedAt|pswSigned|submittedAt|customerDecisionAt|studyDate|calibratedAt|supplierInvoiceDate|lastReceived|masterLeakVerified|lastIssuedAt|plannedDate)")
EARLY=re.compile(r"(commissioned|purchased|dateOfJoining|installed)")
FUT=re.compile(r"(validTo|effectiveTo|expir|next[A-Z].*Due|nextReview|nextDueAt|nextMaintenance|interimApproval|expiresAt|nextAuditDue|nextStudyDue)")
OPENISH={"Created","Released","In Progress","Open","Planned","Raised","Requested","Queued","Reported","Received","Issued","Started","In Preparation","Under Evaluation","Under Inspection","Under Investigation","Under Analysis","On Hold","Active","In Process","Generated","Picking","Loading","Reserved","Compiling","Declared","Contained","Containment Sent","Containment Done","Root Cause Identified","Submitted","Filling","Empty","Recorded","Awaiting First Off Approval","Awaiting Reinspection","Available","Posted","Printed","Calculated","Valid","Expiring Soon","Sent","Failed","Dead Letter","Actions Open","Not Started","Conditional","Approved?"}
OPENISH-= {"Recorded","Posted","Printed","Calculated","Valid","Available","Approved?"}
R_SHORT={"operationExecution","stepCompletion","torqueResult","leakTestResult","inspectionResult","materialMovement","materialConsumption","label","genealogyLink","componentLotLink","processReading","alarm","businessEvent","auditTrail","electronicSignature","erpMessage","notification","andonEvent","equipmentState","toolLifeRecord","spcSample","checkSheetResult","materialRequest","serialNumber","energyReading","productionCount"}
OWNTIME=set()
QUALROOT={"characteristic","controlPlan","inspectionPlan","inspectionResult","spcChart","spcSample","msaStudy","gauge","gaugeCalibration","deviationPermit"}
TAGROOT={"processTag","processReading","recipe","billOfProcess","alarm","equipment"}
SINGLE={"routingStep","billOfProcessStep","controlPlanLine","pfmeaLine","ppapSubmissionElement","samplingPlanSizeRow","msaStudyTrial","asBuiltRecordOperation","engineeringChangeApproval"}
NOCTXSTEP={"ppapSubmissionElement","samplingPlanSizeRow","msaStudyTrial","engineeringChangeApproval"}
PARENTIDX={"billOfMaterialComponent":[0,0,0,0,0,0,2,3,1,1]}
CTXOF={"torqueResult":[6]*10,"leakTestResult":[7]*10,"wipUnit":[5,6,6,6,7,7,7,7,9,9],"serialNumber":[5,6,6,6,7,7,7,7,9,9],"asBuiltRecord":[5,6,6,6,7,7,7,7,9,9],
 "container":[0,2,4,9,9,9,9,9,9,9],"shipment":[9]*10,"label":[9]*10,"productionOrder":[5,5,2,0,5,2,0,5,4,5],"productionSchedule":[5,5,2,0,5,2,0,5,4,5],"customerSchedule":[9]*10,
 "operationExecution":[0,5,6,6,6,7,7,7,7,9],"lot":[0,1,2,4,5,5,5,6,0,5],"genealogyLink":[5,5,5,5,5,6,5,5,5,5],"materialConsumption":[5,5,5,5,6,6,6,0,0,5],"kit":[5,5,5,6,5,5,6,5,5,5],
 "goodsReceipt":[5,5,5,6,0,5,5,5,6,0],"packagingSpecification":[9]*10,"stepCompletion":[5,5,6,6,6,7,7,7,9,9],"customerComplaint":list(range(10)),"reworkOrder":[7,7,6,7,9,7,6,8,7,6],
 "item":[9,9,4,0,5,5,5,6,5,0],"billOfMaterial":[9,9,4,0,9,9,4,0,9,9],"routing":[9,9,2,0,5,6,4,5,8,9],"billOfProcess":[9,9,2,0,5,6,4,5,8,9],"controlPlan":[9,9,2,0,9,9,2,0,9,9],"pfmea":[9,9,2,0,5,6,4,5,8,9],
 "productVariant":[9]*10,"ppapSubmission":[9,9,2,0,9,9,2,0,9,9]}
# explicit reference picks: (entity, key) -> list of 10 target indexes (None = null)
REFIDX={("wipUnit","productionOrderId"):[0,0,1,1,4,4,7,7,9,9],("wipUnit","serialNumberId"):list(range(10)),("serialNumber","wipUnitId"):list(range(10)),("asBuiltRecord","wipUnitId"):list(range(10)),("asBuiltRecord","serialNumberId"):list(range(10)),
 ("operationExecution","wipUnitId"):[None,0,1,2,3,4,5,6,7,8],("operationExecution","lotId"):[0]+[None]*9,("torqueResult","operationExecutionId"):[2,2,2,2,3,3,3,4,4,4],("leakTestResult","operationExecutionId"):[5,5,5,6,6,7,7,8,8,8],
 ("stepCompletion","operationExecutionId"):[1,1,2,2,3,5,5,6,9,9],("lot","itemId"):[3,3,2,2,4,5,6,7,9,5],("lot","supplierId"):[None,None,None,None,0,1,1,2,3,1],("lot","goodsReceiptId"):[None,None,None,None,0,1,2,3,4,5],
 ("lot","productionOrderId"):[3,3,2,8,None,None,None,None,None,None],("lot","qualityHoldId"):[None]*5+[0]+[None]*4,("goodsReceipt","supplierId"):[0,1,1,2,3,1,0,4,2,3],
 ("genealogyLink","parentWipUnitId"):[0,0,0,1,1,1,2,2,3,3],("genealogyLink","childItemId"):[4,5,6,4,5,7,4,5,4,5],("genealogyLink","childLotId"):[4,5,6,4,5,7,4,9,4,9],("genealogyLink","operationExecutionId"):[1,1,1,None,None,2,None,None,None,None],
 ("materialConsumption","operationExecutionId"):[1,1,1,1,2,3,4,0,0,1],("materialConsumption","componentItemId"):[4,5,6,8,7,7,7,9,9,2],("materialConsumption","componentLotId"):[4,5,6,None,7,7,7,8,8,3],
 ("componentLotLink","parentLotId"):[8,8,0,0,1,1,2,2,1,2],("componentLotLink","childLotId"):[0,0,1,1,2,2,3,3,2,3],("componentLotLink","parentItemId"):[9,9,3,3,3,3,2,2,3,2],("componentLotLink","childItemId"):[3,3,3,3,2,2,2,2,2,2],
 ("billOfMaterial","itemId"):[0,1,2,3,0,1,2,3,0,0],("billOfMaterialComponent","componentItemId"):[2,4,5,6,7,8,3,9,2,4],("routing","itemId"):[0,1,2,3,0,0,2,0,0,0],("billOfProcess","itemId"):[0,1,2,3,0,0,2,0,0,0],("billOfProcess","routingId"):list(range(10)),
 ("controlPlan","itemId"):[0,1,2,3,0,1,2,3,0,0],("controlPlan","routingId"):[0,1,2,3,0,1,2,3,9,7],("pfmea","itemId"):[0,1,2,3,0,0,2,0,0,0],("productVariant","baseItemId"):[0,1,0,1,0,1,0,1,0,1],("productVariant","variantItemId"):[0,1,0,1,0,1,0,1,0,1],
 ("user","reportsToUserId"):[4,4,4,6,6,4,None,4,6,None],("user","departmentId"):[0,0,0,1,0,2,1,3,4,8],("user","designationId"):list(range(10)),("user","employmentTypeId"):[0,0,1,0,0,0,0,1,0,9],("user","homeWorkCenterId"):[6,0,2,7,5,7,None,None,2,None],
 ("user","defaultShiftId"):[0,1,2,3,0,3,3,0,3,3],("user","contractorSupplierId"):[None,None,9,None,None,None,None,9,None,None],("user","languageId"):[1,1,2,0,0,2,0,1,0,0],
 ("site","enterpriseId"):[0,0,0,0,0,0,8,7,6,1],("site","defaultWorkCalendarId"):[0]*10,("area","supervisorUserId"):[4]*10,("area","costCenterId"):list(range(10)),("area","parentAreaId"):[None]*10,
 ("line","areaId"):[0,1,2,3,3,4,5,0,2,4],("line","costCenterId"):[0,1,2,3,3,4,5,0,2,4],("line","workCalendarId"):[1,2,3,4,4,5,6,1,3,5],("line","bottleneckWorkCenterId"):[0,1,2,3,4,7,9,0,2,5],("line","itemFamilyId"):[3,3,2,2,2,0,0,3,2,1],
 ("department","parentDepartmentId"):[None]*10,("department","headUserId"):[4,6,5,7,8,4,5,6,8,6],("department","costCenterId"):[4,7,8,6,2,4,8,9,9,9],("designation","departmentId"):[0,0,0,1,0,2,1,3,4,8],
 ("item","itemGroupId"):[0,0,1,2,3,4,5,6,7,8],("item","defaultSupplierId"):[None,None,None,None,0,1,1,2,4,3],("item","baseUnitOfMeasureId"):[0]*9+[1],("item","defaultStorageLocationId"):[7,7,4,3,1,2,2,1,2,0],
 ("item","serialNumberRangeId"):[0,1]+[None]*8,("item","lotNumberRangeId"):[None,None,2,2,7,7,7,7,7,7],
 ("unitOfMeasure","baseUnitOfMeasureId"):[None]*10,("skillCertification","userId"):[0,0,1,2,0,2,1,3,5,8],("skillCertification","skillId"):[5,6,0,2,7,8,1,9,7,2],("skillCertification","assessorUserId"):[4,4,4,4,3,4,4,6,4,6],
 ("qualityHold","nonconformanceId"):[5,7,1,4,0,2,3,6,8,9],("nonconformance","qualityHoldId"):[4,2,5,6,3,0,7,1,8,9],("nonconformance","capaId"):list(range(10)),("capa","customerComplaintId"):[None]*9+[9],
 ("inventoryBalance","itemId"):[4,5,6,7,8,9,3,2,0,5],("inventoryBalance","lotId"):[4,5,6,7,None,8,1,3,None,9],("inventoryBalance","storageLocationId"):[1,6,2,1,2,0,3,4,7,2],("inventoryBalance","stockStatusId"):[0,2,0,0,0,0,0,0,0,0],
 ("shiftRoster","lineId"):[5,5,5,2,2,0,0,6,4,1],("energyReading","meterIotDeviceId"):[3]*10,("label","printerIotDeviceId"):[9]*10,("serialNumber","numberRangeId"):[0]*10,("serialNumber","itemId"):[0]*10,
}
NULLWHEN={("wipUnit","qualityHoldId"):lambda i,j,s: s!="On Hold",("wipUnit","containerId"):lambda i,j,s: s not in("Packed","Shipped"),("serialNumber","shipmentId"):lambda i,j,s: s!="Shipped",("serialNumber","containerId"):lambda i,j,s: s!="Shipped",
 ("serialNumber","labelId"):lambda i,j,s: s not in("Marked","Shipped"),("asBuiltRecord","shipmentId"):lambda i,j,s: i<8,("asBuiltRecord","containerId"):lambda i,j,s: i<8,("asBuiltRecord","deviationPermitId"):lambda i,j,s: True,
 ("operationExecution","recipeId"):lambda i,j,s: j in(5,9),("inspectionResult","goodsReceiptId"):lambda i,j,s: True,("inspectionResult","nonconformanceId"):lambda i,j,s: i not in(3,8),("inspectionResult","defectCodeId"):lambda i,j,s: i not in(3,8),
 ("spcSample","nonconformanceId"):lambda i,j,s: i!=3,("checkSheetResult","nonconformanceId"):lambda i,j,s: i!=3,("productionOrder","customerScheduleId"):lambda i,j,s: j!=5,("lot","productionOrderId"):lambda i,j,s: False,
 ("nonconformance","supplierId"):lambda i,j,s: j!=5,("nonconformance","customerId"):lambda i,j,s: i!=9,("scrapRecord","wipUnitId"):lambda i,j,s: j<5,("scrapRecord","lotId"):lambda i,j,s: j>=5,("downtimeEvent","alarmId"):lambda i,j,s: i%2==1,
 ("downtimeEvent","maintenanceWorkOrderId"):lambda i,j,s: False,("alarm","downtimeEventId"):lambda i,j,s: i%2==1,("alarm","productionOrderId"):lambda i,j,s: False,("materialMovement","reversalOfMaterialMovementId"):lambda i,j,s: s!="Reversed",
 ("materialMovement","goodsReceiptId"):lambda i,j,s: i not in(0,1),("materialMovement","shipmentId"):lambda i,j,s: i!=7,("materialMovement","kitId"):lambda i,j,s: i!=2,("materialMovement","productionOrderId"):lambda i,j,s: i not in(2,3,6),
 ("maintenanceWorkOrder","maintenancePlanId"):lambda i,j,s: i%3!=0,("maintenanceWorkOrder","toolId"):lambda i,j,s: i not in(0,2,6,7),("labourBooking","productionOrderId"):lambda i,j,s: i in(3,7),("labourBooking","operationId"):lambda i,j,s: i in(3,7),
 ("labourBooking","indirectActivityId"):lambda i,j,s: i not in(3,7),("labourBooking","workCenterId"):lambda i,j,s: False,("torqueResult","toolId"):lambda i,j,s: False,("torqueResult","curveControlledDocumentId"):lambda i,j,s: i!=3,
 ("safetyIncident","injuredUserId"):lambda i,j,s: i not in(1,5),("safetyIncident","bodyPartId"):lambda i,j,s: i not in(1,5),("safetyIncident","injuryTypeId"):lambda i,j,s: i not in(1,5),("safetyIncident","capaId"):lambda i,j,s: True,
 ("customerSchedule","supersedesCustomerScheduleId"):lambda i,j,s: True,("engineeringChange","customerId"):lambda i,j,s: i in(3,5,7,9),("gauge","workCenterId"):lambda i,j,s: False,("gauge","calibrationSupplierId"):lambda i,j,s: False,
 ("container","shipmentId"):lambda i,j,s: s!="Shipped",("container","ownerCustomerId"):lambda i,j,s: j!=9,("container","parentContainerId"):lambda i,j,s: True,("container","labelId"):lambda i,j,s: j!=9,
 ("deviationPermit","nonconformanceId"):lambda i,j,s: i%2==1,("deviationPermit","engineeringChangeId"):lambda i,j,s: True,("capa","auditId"):lambda i,j,s: True,("audit","customerId"):lambda i,j,s: i!=8,("audit","checkSheetId"):lambda i,j,s: i not in(0,3,5,7),
 ("erpMessage","goodsReceiptId"):lambda i,j,s: i%3!=1,("erpMessage","shipmentId"):lambda i,j,s: i%3!=2,("erpMessage","productionOrderId"):lambda i,j,s: i%3!=0,("notification","andonEventId"):lambda i,j,s: i!=6,("notification","alarmId"):lambda i,j,s: i!=0,("notification","nonconformanceId"):lambda i,j,s: i not in(1,5),
 ("andonEvent","downtimeEventId"):lambda i,j,s: i not in(0,6,7),("materialRequest","andonEventId"):lambda i,j,s: i not in(3,5),("materialRequest","lotId"):lambda i,j,s: False,("changeover","equipmentId"):lambda i,j,s: False,
 ("equipmentState","downtimeEventId"):lambda i,j,s: i%3!=1,("equipmentState","productionOrderId"):lambda i,j,s: False,("toolLifeRecord","maintenanceWorkOrderId"):lambda i,j,s: i not in(4,8),("toolLifeRecord","productionOrderId"):lambda i,j,s: False,
 ("processReading","productionOrderId"):lambda i,j,s: False,("processReading","lotId"):lambda i,j,s: j>4,("reworkOrder","lotId"):lambda i,j,s: True,("kit","productionOrderId"):lambda i,j,s: False,
}
STATUSOF={"productionOrder":["Completed","In Progress","Completed","Closed","In Progress","Released","Completed","On Hold","Created","Cancelled"],
 "wipUnit":["On Hold","In Process","In Process","In Rework","In Process","In Process","In Process","Scrapped","Packed","Shipped"],
 "serialNumber":["Issued","Issued","Issued","Issued","Issued","Issued","Issued","Scrapped","Marked","Shipped"],
 "asBuiltRecord":["Compiling"]*8+["Released","Released"],"lot":["Consumed","Consumed","In Process","Available","Available","On Hold","Available","Available","Consumed","Available"],
 "operationExecution":["Completed"]*6+["Completed","Completed","Started","Completed"],"gauge":["Active","Active","Active","Active","Overdue","Active","Active","Due For Calibration","Active","Under Calibration"],
 "equipment":["Active","Under Maintenance"]+["Active"]*8,"tool":["Mounted","Available","Life Expired","Available","Mounted","Mounted","Mounted","In Maintenance","Mounted","Mounted"],
 "user":["Active"]*7+["Active","Active","Active"],"qualityHold":["Active","Released","Released","Partially Released","Released","Released","Active","Released","Released","Released"],
 "container":["Full","Full","Full","Filling","Full","Sealed","Sealed","Shipped","Shipped","Shipped"],"shipment":["Planned","Loading","Dispatched","Dispatched","Delivered","Delivered","Delivered","Delivered","Dispatched","Cancelled"],
 "skillCertification":["Valid","Valid","Valid","Valid","Valid","Expiring Soon","Valid","Valid","Expired","Revoked"],"supplier":["Approved","Approved","Approved","Approved","Conditional","Approved","Approved","Approved","Approved","Approved"],
 "item":["Active"]*10,"recipe":["Released"]*10,"routing":["Released"]*8+["In Preparation","Released"],"workInstruction":["Released"]*10,"inventoryBalance":["Active"]*10,
 "leakTestResult":["Recorded"]*10,"torqueResult":["Recorded"]*10,"inspectionResult":["Recorded"]*9+["Voided"],"materialMovement":["Posted"]*9+["Reversed"],"materialConsumption":["Posted"]*10,
 "genealogyLink":["Active"]*9+["Removed"],"componentLotLink":["Active"]*10,"iotDevice":["Active"]*10,"integrationConnector":["Active"]*9+["Disabled"],"maintenancePlan":["Active"]*10,"spcChart":["Active"]*10,
 "controlledDocument":["Released"]*10,"label":["Printed","Verified","Verified","Printed","Reprinted","Verified","Verified","Voided","Verified","Printed"]}
RELATED={"label":"container","auditTrail":"characteristic","electronicSignature":"recipe","erpMessage":"productionOrder","businessEvent":"operationExecution","notification":"andonEvent","controlledDocument":"item","engineeringChange":"routing","nonconformance":"wipUnit","qualityHold":"lot"}
LINEKEYS_STEP={"stepNo":10,"lineNo":10,"itemNo":1,"taskNo":10,"actionNo":1,"findingNo":1,"elementNo":1,"levelNo":1,"stageNo":1,"releaseNo":1,"revisionNo":1,"rank":1,"trialNo":1,"subgroupNo":1,"sampleNo":1,"tighteningNo":1,"bomLineNo":10,"planLineNo":10,"level":1}
SCALE=[1,0.5,1,2,0.25,1,0.5,1.5,1,0.75]; PCTJ=[0,-1.2,0.8,-3.5,1.1,-0.4,2.0,-2.1,0.5,-0.9]
NOSCALE={"failedLoginCount","absentCount","reprintCount","reworkCount","regrindCount","usageCount","cycleCount","workingDaysCount","partsCount","trialsCount","questionsCount","conformingCount","capabilitySampleCount","quantityPerContainer","maxReworkCount"}
FIRSTONLY={"dataType","toleranceType","scope","direction","source","payloadFormat","environment","printerLanguage","symbology","studyMethod","methodology","samplingType","chartType","phase","bomType","strategy","testMedium","signalQuality","connectionStatus","healthStatus","valueType","authMethod","authenticationMethod","calibrationSource","employmentType","userType","customerType","supplierType","procurementType","itemType","effectivityType","originator","limitType","answerType","recordType","inputType","consumptionType","scanSource","executionType","bookingType","orderType","routingType","planType","inspectionType","frequencyType","collectionTrigger","storageProvider","rangeType","resetPolicy","checkDigitMethod","aggregation","tagClass","alarmClass","intervalType","intervalUom","lifeUom","deviceSource","currentDiscipline","d4RootCauseMethod","stockEffect","triggerSource","requestType","kitType","childType","linkType","roleInTeam","inspectionLevel","frequency","checkSheetType","optionsHand","downtimeType","holdType","deviationType","capaType","ncType","scrapType","disposalMethod","reworkType","calibrationType","studyType","traceLevel","firmness","scheduleType","rule","workOrderType","widgetType","triggerEvent","triggerAction","purpose","appType","connectorType","protocol","controllerProtocol","messageType","eventCategory","channel","meaning","module","dimension","oeeImpact","reasonType","criticality","equipmentClass","siteType","safetyCategory","markGrade","verificationGrade","overallRating","submissionReason","locationType","labelType","internalExternal","changeoverType","exceptionType","roleInCrew","attendance","assessmentMethod","businessFunction","nextStepCondition","interlockType","changeType","decision","changeAction","priority","lineType","areaType","workCenterType","stageName","grade","actionPriority","auditType"}
VARYENUM={"priority":["Normal","Normal","High","Normal","Urgent","Normal","Low","High","Normal","Normal"],"attendance":["Present"]*7+["Absent","Overtime","Leave"],"markGrade":["A","A","B","A","B","A","A","C","A","B"],"verificationGrade":["A","B","A","A","B","A","C","A","B","A"],
 "lineType":["Casting","Heat Treatment","Machining","Surface Treatment","Surface Treatment","Assembly","Inspection","Casting","Machining","Assembly"],"areaType":["Production"]*6+["Storage","Quality","Maintenance","Utility"],
 "siteType":["Manufacturing Plant"]*7+["Warehouse","Technical Center","Head Office"],"criticality":["A","A","A","B","A","B","A","A","B","B"],"direction":["Outbound","Inbound","Outbound","Outbound","Inbound","Outbound","Outbound","Inbound","Outbound","Inbound"],
 "bookingType":["Direct"]*3+["Indirect"]+["Direct"]*3+["Indirect"]+["Direct"]*2,"itemType":["Finished Good","Finished Good","Semi Finished","Semi Finished"]+["Purchased Component"]*5+["Raw Material"],"procurementType":["In House"]*4+["Purchased"]*6,
 "userType":["Employee"]*9+["System"],"customerType":["OEM","OEM","OEM","OEM","OEM","Tier 1","Aftermarket","OEM","OEM","OEM"],"supplierType":["Direct Material"]*5+["Tooling","Calibration Laboratory","Indirect Material","Indirect Material","Service"],
 "orderType":["Production","Production","Production","Production","Production","Production","Production","Rework","Trial","PPAP Run"],"routingType":["Standard","Standard","Standard","Standard","Rework","Rework","Rework","Alternate","Rework","Alternate"],
 "executionType":["Production"]*7+["Retest","Production","Production"],"exceptionType":["Public Holiday"]*6+["Plant Shutdown","Extra Working Day","Reduced Shift","Public Holiday"],"roleInCrew":["Operator","Operator","Setter","Operator","Line Leader","Operator","Quality Inspector","Operator","Material Handler","Operator"],
 "changeType":["Process Change","Material Change","Design Change","Supplier Change","Design Change","Tooling Change","Process Change","Supplier Change","Process Change","Document Change"],"originator":["Customer","Internal","Customer","Internal","Customer","Internal","Customer","Supplier","Customer","Internal"],
 "decision":["Approved"]*7+["Approved With Conditions","Approved","Rejected"],"actionPriority":["Medium","High","High","Medium","Low","High","Medium","High","Low","Low"],"grade":["Minor","Minor","Observation","Major","Minor","Opportunity For Improvement","Minor","Observation","Major","Minor"],
 "auditType":["Layered Process Audit","Process Audit","Process Audit","Layered Process Audit","Process Audit","Layered Process Audit","Product Audit","Layered Process Audit","Customer Audit","System Audit"],"workOrderType":["Breakdown","Breakdown","Breakdown","Preventive","Breakdown","Breakdown","Breakdown","Preventive","Preventive","Breakdown"],
 "downtimeType":["Unplanned"]*8+["Planned","Unplanned"],"ncType":["Internal"]*5+["Supplier"]+["Internal"]*3+["Customer"],"labelType":["Container Label","Shipping Label","Unit Mark","Container Label","Hold Tag","Container Label","Location Label","Container Label","Container Label","Container Label"],
 "locationType":["Receiving Bay","Warehouse Rack","Warehouse Rack","Line Side","Line Side","Line Side","Quarantine","Warehouse Rack","Dispatch Bay","Scrap Yard"],"scheduleType":["Delivery Schedule"]*6+["Forecast","Just In Time Call Off","Delivery Schedule","Forecast"],
 "checkSheetType":["Start Of Shift"]*10,"calibrationType":["Periodic"]*8+["After Repair","Initial"],"studyType":["Gauge R and R"]*7+["Bias","Linearity","Attribute Agreement"],"holdType":["Supplier","Quality","Quality","Quality","Quality","Quality","Customer","Quality","Engineering","Quality"],
 "reworkType":["Replace Component","Replace Component","Retighten","Replace Component","Clean","Replace Component","Retighten","Re-mark","Replace Component","Retighten"],"scrapType":["Process Scrap","Process Scrap","Setup Scrap","Process Scrap","Process Scrap","Material Defect","Process Scrap","Destructive Test","Process Scrap","Process Scrap"],
 "messageType":["Production Order Download","Operation Confirmation","Goods Movement","Goods Receipt","Shipment Advice","Material Master","Quality Notification","Operation Confirmation","Goods Movement","Production Order Download"],
 "connectorType":["ERP","PLM","OPC UA Server","OPC UA Server","Tool Controller","Leak Tester","Label Printer","OPC UA Server","Email Gateway","ERP"],"protocol":["HTTPS REST","HTTPS REST","OPC UA","OPC UA","Open Protocol","Modbus TCP","ZPL Over TCP","MQTT","SMTP","HTTPS REST"],
 "controllerProtocol":["OPC UA","Modbus TCP","OPC UA","Profinet","Modbus TCP","Ethernet/IP","Open Protocol","Modbus TCP","Ethernet/IP","OPC UA"],"channel":["Screen","Mobile Push","Email","Screen","SMS","Mobile Push","Screen","Email","Mobile Push","Screen"],
 "optionsHand":["LH","RH"]*5,"reasonType":["Downtime"]*10,"oeeImpact":["Availability"]*10,"workCenterType":["Machine Station","Batch Process","Machine Station","Machine Station","Batch Process","Manual Station","Machine Station","Test Station","Machine Station","Inspection Station"],
 "stageName":["Low Pressure","High Pressure"]*5,"eventCategory":["Execution","Execution","Quality","Execution","Material","Maintenance","Quality","Integration","Execution","Security"],"interlockType":["Skill","Recipe","Tool Life","Gauge Calibration","Previous Step","Component Scan","Maintenance Due","Skill","Recipe","Previous Step"],
 "frequencyType":["Per Lot","Per Lot","Every N Units","Per Shift","Per Lot","Every N Units","Every Unit","Every Unit","Every Unit","Every N Units"],"inspectionType":["In Process"]*9+["Final"],"planType":["In Process"]*9+["Final"],
 "submissionReason":["Initial Submission","Initial Submission","Engineering Change","Tooling Transfer","Engineering Change","Initial Submission","Engineering Change","Correction Of Discrepancy","Sub Supplier Change","Engineering Change"],
 "currentDiscipline":["D8","D6","D5","D4","D7","D3","D5","D4","D8","D2"],"equipmentClass":["Production Equipment"]*7+["Test Equipment","Production Equipment","Test Equipment"],"safetyCategory":["PL d","PL c","PL d","PL c","PL d","PL d","PL c","PL d","PL e","PL c"]}
NULLENUM={"indirectActivity","fromStockStatus","toStockStatus","reinspectionResult","releaseDecision","customerDecision","overallRating","d4RootCauseMethod","attributeResult","checkDigitMethod"}
FAIL={3}
def _res(env,en): return en[1] if env["i"] in FAIL else en[0]
ENUMRULE={"result":_res,"verdict":_res,"overallResult":_res,"stageResult":lambda env,en: en[1] if env["i"]==7 else en[0],"leakTestVerdict":lambda env,en: "Fail" if env["i"]==7 else "Pass","asFoundResult":lambda env,en: en[1] if env["i"]==4 else en[0],"asLeftResult":lambda env,en: en[0],
 "conclusion":lambda env,en: ["Acceptable","Acceptable","Acceptable","Conditionally Acceptable","Acceptable","Acceptable","Acceptable","Not Acceptable","Acceptable","Acceptable"][env["i"]],
 "qualityStatus":lambda env,en: "On Hold" if env["status"]=="On Hold" else ("Rejected" if env["status"] in("Scrapped","Rejected") else "Released"),
 "currentState":lambda env,en: "Down" if env["status"]=="Under Maintenance" else ["Running","Running","Running","Idle","Running","Running","Setup","Running","Running","Running"][env["i"]],
 "inspectionStatus":lambda env,en: ["Accepted","Accepted","Rejected","Accepted","Pending","Accepted","Accepted","Accepted Under Deviation","Accepted","Accepted"][env["i"]],
 "trackingGrain":lambda env,en: env["p"]["grain"],"operationType":lambda env,en: env["p"]["optype"],"characteristicType":lambda env,en: env["p"]["ctype"],"classification":lambda env,en: env["p"]["cclass"],"recipeType":lambda env,en: env["p"]["rcptype"] if env["p"]["rcptype"] in en else en[5],
 "stateCode":lambda env,en: ["Running","Down","Running","Idle","Setup","Running","Down","Starved","Running","Blocked"][env["i"]],"lotType":lambda env,en: ["Casting Lot","Heat Treatment Charge","Machining Lot","Anodising Load","Supplier Lot","Supplier Lot","Supplier Lot","Supplier Lot","Supplier Lot","Supplier Lot"][env["i"]],
 "connectionStatus":lambda env,en: "Offline" if env["i"]==1 else "Online","healthStatus":lambda env,en: ["Healthy"]*8+["Degraded","Down"][env["i"]-8:env["i"]-7] and (["Healthy"]*8+["Degraded","Down"])[env["i"]],"signalQuality":lambda env,en: "Uncertain" if env["i"]==6 else "Good"}
for _k,_v in VARYENUM.items(): ENUMRULE.setdefault(_k,(lambda v: (lambda env,en: v[env["i"]] if v[env["i"]] in en else en[0]))(_v))
# keys taken from the process row: key -> (PROC field, set of root entities or None for all)
PKEY={"instructionText":("instr",None),"keyPoint":("key",None),"question":("q",None),"faultText":("fault",None),"alarmText":("alarm",None),"problemDescription":("problem",None),"rootCause":("root",None),"rootCauseSummary":("root",None),
 "actionTaken":("action",None),"actionText":("action",None),"processFunction":("pfn",None),"failureMode":("pfm",None),"failureEffect":("pfe",None),"failureCause":("pfc",None),"preventionControl":("pfp",None),"detectionControl":("pfd",None),
 "measurementMethod":("method",None),"measurementTechnique":("method",None),"programNo":("prog",None),"model":("model",{"equipment"}),"defectDescription":("ddesc",None),"pfmeaFailureMode":("pfm",None),"d2ProblemDescription":("ddesc",None),
 "d4RootCauseOccurrence":("pfc",None),"correctiveAction":("action",None),"resolutionText":("action",None),"immediateAction":("action",{"x"}),"processName":("wi",None),"specialProcessStandard":("special",None),"lossReason":("problem",{"x"})}
PERSONS=["Arvind Kelkar","Priya Nair","Mahesh Gawde","Sanjay Deshmukh","Rohini Phadke","Nitin Kshirsagar","Pooja Sawant","Amol Thorat","Swati Bapat","Kiran Jagtap"]
HOLIDAYS=[("Maharashtra Day",datetime.datetime(2026,4,30,18,30)),("Independence Day",datetime.datetime(2026,8,14,18,30)),("Ganesh Chaturthi",datetime.datetime(2026,9,13,18,30)),("Gandhi Jayanti",datetime.datetime(2026,10,1,18,30)),("Dussehra",datetime.datetime(2026,10,19,18,30)),("Diwali Laxmi Pujan",datetime.datetime(2026,11,7,18,30)),
 ("Annual maintenance shutdown",datetime.datetime(2026,5,24,18,30)),("Extra working Sunday for customer pull-in",datetime.datetime(2026,9,26,18,30)),("Half day for plant safety drill",datetime.datetime(2026,6,11,18,30)),("Republic Day",datetime.datetime(2027,1,25,18,30))]
PPAPEL=["Design Records","Engineering Change Documents","Customer Engineering Approval","Design FMEA","Process Flow Diagram","Process FMEA","Control Plan","Measurement System Analysis Studies","Dimensional Results","Material and Performance Test Results"]
BREAKS=["Tea break","Lunch break","Tea break","Dinner break","Tea break","Meal break","Tea break","Lunch break","Tea break","Dinner break"]
def CHILDNAME(env,k):
    e=env["e"]; i=env["i"]; p=env["p"]
    if e in("enterpriseContact","customerContact","supplierContact"): return PERSONS[i]
    if e=="shiftBreak": return BREAKS[i]
    if e=="workCalendarException": return HOLIDAYS[i][0]
    if e=="ppapSubmissionElement": return PPAPEL[i]
    if e=="customerShipTo": return "%s, Dock %d"%(env["pdoc"]["name"] if env["pdoc"] else "Customer plant",env["line"]+2)
    if e in("workInstructionStep","operatorAppStep","reworkOrderStep","changeoverStep","maintenancePlanTask"): return [p["instr"],p["key"]][(env["line"]-1)%2] if k!="name" else ["Prepare and load","Run and confirm result"][(env["line"]-1)%2]
    if e in("recipeParameter","billOfProcessStepProcessParameter"): return p["tag"].split("|")[1]
    if e=="recipeStage": return ["Approach","Process","Hold","Release"][(env["line"]-1)%4]
    if e=="skillLevelScale": return ["Under training, works only under supervision","Works independently to standard and reacts to abnormalities"][(env["line"]-1)%2]
    if e=="itemRevision": return ["Initial release for production","Revised after engineering change"][(env["line"]-1)%2]
    if e=="billOfProcessStepInterlock": return "Operator must hold a valid certification for %s"%p["skill"].split("|")[1].lower()
    if e in("nonconformanceContainmentAction","capaContainmentAction"): return ["Segregate and hold all suspect material at %s"%p["wc"].split("|")[1],"Sort stock back to the last good check and record results"][(env["line"]-1)%2]
    if e=="capaCorrectiveAction": return p["action"]
    if e=="capaImplementationAction": return "%s; effectiveness verified over the next 2,000 pieces"%p["action"]
    if e=="auditFinding": return ["Record for '%s' not signed on one shift"%p["q"].rstrip("?"),"Reaction plan not displayed at %s"%p["wc"].split("|")[1]][(env["line"]-1)%2]
    if e=="spcSampleViolation": return ["One point beyond the upper control limit","Seven consecutive points above the centre line"][(env["line"]-1)%2]
    if e=="shiftHandoverOpenItem": return ["Follow up: %s"%p["problem"].lower(),"Confirm check: %s"%p["q"].lower()][(env["line"]-1)%2]
    if e=="safetyIncidentAction": return ["Brief all shifts on the incident at the start-of-shift meeting","Engineering fix and verification by the safety officer"][(env["line"]-1)%2]
    return "%s %d"%(env["c"]["entity"],env["line"])
VARY={}
def FALLBACK(t,k,env):
    if t=="String": return env["rec"]
    if t=="Boolean": return False
    if t=="Int32": return ("int",1)
    if t=="Int64": return ("long",1)
    if t=="Decimal128": return ("dec","0.0")
    if t=="Double": return ("dbl",0.0)
    return ("date",env["base"])
RECFMT={}; SPECIALIDENT={}; VAL={}; GEN={}; BOOLRULE={}; POST={}
# ------------------------------------------------------------------ part 2: identities, numeric families, master values
import spec_rules as _R
from sample_universe import TITLES
if "engineeringChange" in MASTER: TITLES["engineeringChange"]=MASTER.pop("engineeringChange")
PROC[5]["rcp"]="TRQ-PSET-08|Guide pin bolt M8 torque program"; PROC[5]["rcptype"]="Tightening Program"
PROC[9]["rcp"]="LSR-DM-5110-RH|Serial and 2D code layout, front caliper RH"; PROC[9]["rcptype"]="Laser Marking Program"
CTXOF["recipe"]=[0,1,2,3,4,6,6,7,8,8]
def code(s): return s.split("|")[0]
def nm(s): return s.split("|")[1]
ITEMS=MASTER["item"]; ROUTES=MASTER["routing"]; REV=["D","D","C","B","B","A","A","A","B","-"]
_BI=REFIDX[("billOfMaterial","itemId")]
SPECIALIDENT["billOfMaterial"]=lambda i:("BOM-%s-%02d"%(code(ITEMS[_BI[i]]),1+sum(1 for k in range(i) if _BI[k]==_BI[i])),)*2
SPECIALIDENT["billOfProcess"]=lambda i:("BOP-%s"%code(ROUTES[i]),)*2
SPECIALIDENT["controlPlan"]=lambda i:("CP-%s-%s"%(code(ITEMS[REFIDX[("controlPlan","itemId")][i]]),["PROD","PROD","PROD","PROD","PRELAUNCH","PRELAUNCH","PRELAUNCH","PRELAUNCH","PROTO","SAFE-LAUNCH"][i]),)*2
SPECIALIDENT["pfmea"]=lambda i:("PF-%s"%code(ROUTES[i]),"Process FMEA, %s"%nm(ROUTES[i]))
SPECIALIDENT["packagingSpecification"]=lambda i:("PKS-%s-%s-%02d"%(code(ITEMS[i%2]),code(MASTER["customer"][[0,0,0,1,0,0,2,0,7,0][i]]),i//2+1),)*2
_po=_R.byent["productionOrder"]["statusValues"]; _wu=_R.byent["wipUnit"]["statusValues"]
STDEF=[("productionOrder",s) for s in _po]+[("wipUnit",s) for s in _wu[:3]]
def scode(s): return s.upper().replace(" ","_")
SPECIALIDENT["statusDefinition"]=lambda i:("%s.%s"%(STDEF[i][0],scode(STDEF[i][1])),STDEF[i][1])
_po_ix={s:k for k,s in enumerate(_po)}
STTR=[("Created","Released","Release order"),("Released","In Progress","Start production"),("In Progress","On Hold","Place order on hold"),("On Hold","In Progress","Resume production"),("In Progress","Completed","Complete order"),("Completed","Closed","Close order"),("Created","Cancelled","Cancel before release"),("Released","Cancelled","Cancel released order")]
STTRIDX=[(_po_ix[a],_po_ix[b],n) for a,b,n in STTR]+[(7,8,"Start unit"),(8,9,"Place unit on hold")]
SPECIALIDENT["statusTransition"]=lambda i:("%s-%s"%(code_(STDEF[STTRIDX[i][0]]),scode(STDEF[STTRIDX[i][1]][1])),STTRIDX[i][2])
def code_(x): return "%s.%s"%(x[0],scode(x[1]))
REFIDX[("statusTransition","fromStatusDefinitionId")]=[x[0] for x in STTRIDX]; REFIDX[("statusTransition","toStatusDefinitionId")]=[x[1] for x in STTRIDX]
ENUMV=[("operationExecution","result","OK"),("operationExecution","result","Not OK"),("leakTestResult","verdict","Pass"),("leakTestResult","verdict","Fail"),("lot","lotType","Supplier Lot"),("lot","lotType","Melt Lot"),("lot","lotType","Casting Lot"),("lot","lotType","Heat Treatment Charge"),("lot","lotType","Machining Lot"),("lot","lotType","Anodising Load")]
SPECIALIDENT["enumerationValue"]=lambda i:("%s.%s.%s"%(ENUMV[i][0],ENUMV[i][1],scode(ENUMV[i][2])),ENUMV[i][2])
VAL.update({("statusDefinition","collectionName"):[_R.byent[x[0]]["collection"] for x in STDEF],("statusDefinition","fieldName"):["status"]*10,("statusDefinition","statusCode"):[scode(x[1]) for x in STDEF],("statusDefinition","statusName"):[x[1] for x in STDEF],
 ("statusDefinition","description"):["Order received from ERP and not yet released","Order released to the shop floor","At least one unit or lot has been started","Production stopped by a hold decision","All released quantity has been completed","Order confirmed to ERP and closed","Order cancelled before completion","Unit identifier created at assembly start","Unit is being processed on the routing","Unit is blocked by a quality hold"],
 ("statusDefinition","sequenceNo"):[1,2,3,4,5,6,7,1,2,3],("statusDefinition","isInitial"):[True,False,False,False,False,False,False,True,False,False],("statusDefinition","isFinal"):[False,False,False,False,False,True,True,False,False,False],
 ("statusDefinition","colourCode"):["#9E9E9E","#2196F3","#4CAF50","#F44336","#009688","#607D8B","#795548","#9E9E9E","#4CAF50","#F44336"],
 ("statusTransition","collectionName"):[_R.byent["productionOrder"]["collection"]]*8+[_R.byent["wipUnit"]["collection"]]*2,("statusTransition","transitionName"):[x[2] for x in STTRIDX],("statusTransition","requiresSignature"):[True,False,True,True,False,True,True,True,False,True],("statusTransition","requiresReason"):[False,False,True,False,False,False,True,True,False,True],
 ("enumerationValue","collectionName"):[_R.byent[x[0]]["collection"] for x in ENUMV],("enumerationValue","fieldName"):[x[1] for x in ENUMV],("enumerationValue","valueCode"):[scode(x[2]) for x in ENUMV],("enumerationValue","valueName"):[x[2] for x in ENUMV],
 ("enumerationValue","description"):["Operation finished within all limits","Operation finished with at least one result outside limits","Both test stages within limits","At least one test stage outside limits","Lot received from a supplier","Alloy melt prepared in the foundry","Castings poured from one die in one shift","Castings heat treated in one furnace charge","Bodies machined from one heat treatment charge","Bodies anodised in one tank load"],
 ("enumerationValue","sequenceNo"):[1,2,1,2,1,2,3,4,5,6],("enumerationValue","isDefault"):[True,False,True,False,True,False,False,False,False,False]})
def fmt(x,dp): return "%.*f"%(dp,x)
OFF=[0.05,-0.10,0.15,0.62,-0.20,0.0,0.25,-0.30,0.10,-0.05]
def spec(env):
    p=env["p"]
    if env["root"] in QUALROOT or env["e"].startswith("checkSheet") or env["root"] in("nonconformance","controlPlan"): return float(p["nom"]),float(p["lsl"]),float(p["usl"]),p["dp"]
    return float(p["sp"]),float(p["lo"]),float(p["hi"]),1
def meas(env):
    n,l,u,dp=spec(env); return n+OFF[env["i"]]*(u-l)
GEN.update({
 "nominal":lambda e: fmt(spec(e)[0],spec(e)[3]),"lowerSpecLimit":lambda e: fmt(spec(e)[1],spec(e)[3]),"upperSpecLimit":lambda e: fmt(spec(e)[2],spec(e)[3]),"lowerLimit":lambda e: fmt(spec(e)[1],spec(e)[3]),"upperLimit":lambda e: fmt(spec(e)[2],spec(e)[3]),
 "setPoint":lambda e: fmt(spec(e)[0],spec(e)[3]),"expectedValue":lambda e: fmt(spec(e)[0],spec(e)[3]),"measuredValue":lambda e: fmt(meas(e),spec(e)[3]),"deviation":lambda e: fmt(meas(e)-spec(e)[0],spec(e)[3]),"reading":lambda e: fmt(meas(e)+0.02*(spec(e)[2]-spec(e)[1])*((e["line"] or 1)-1),spec(e)[3]),
 "enteredNumber":lambda e: fmt(meas(e),spec(e)[3]) if e["i"]%2==0 else None,"answerNumber":lambda e: None,
 "centerLine":lambda e: fmt(spec(e)[0]+0.02*(spec(e)[2]-spec(e)[1]),spec(e)[3]),"ucl":lambda e: fmt(spec(e)[0]+0.20*(spec(e)[2]-spec(e)[1]),spec(e)[3]),"lcl":lambda e: fmt(spec(e)[0]-0.16*(spec(e)[2]-spec(e)[1]),spec(e)[3]),
 "uclRange":lambda e: fmt(0.36*(spec(e)[2]-spec(e)[1]),spec(e)[3]),"centerLineRange":lambda e: fmt(0.17*(spec(e)[2]-spec(e)[1]),spec(e)[3]),"lclRange":lambda e: fmt(0,spec(e)[3]),
 "subgroupMean":lambda e: fmt(spec(e)[0]+[0.03,-0.05,0.08,0.24,-0.10,0.01,0.12,-0.14,0.05,-0.02][e["i"]]*(spec(e)[2]-spec(e)[1]),spec(e)[3]),"subgroupRange":lambda e: fmt([0.14,0.11,0.19,0.30,0.16,0.09,0.21,0.13,0.17,0.12][e["i"]]*(spec(e)[2]-spec(e)[1]),spec(e)[3]),
 "stdDev":lambda e: fmt([0.060,0.047,0.082,0.129,0.069,0.039,0.090,0.056,0.073,0.052][e["i"]]*(spec(e)[2]-spec(e)[1]),4),
 "capabilityCp":lambda e: ["1.92","1.71","1.48","1.36","2.05","1.67","2.31","1.84","1.55","1.78"][e["j"]],"capabilityCpk":lambda e: ["1.71","1.52","1.38","1.12","1.86","1.49","2.10","1.69","1.41","1.60"][e["j"]],"capabilityPp":lambda e: ["1.84","1.63","1.41","1.30","1.96","1.60","2.20","1.75","1.47","1.70"][e["j"]],"capabilityPpk":lambda e: ["1.66","1.45","1.33","1.07","1.78","1.42","2.01","1.61","1.35","1.52"][e["j"]],
 "targetCpk":lambda e: "1.67" if e["p"]["cclass"]=="Critical" else "1.33",
 "cycleTimeSec":lambda e: e["p"]["cyc"],"standardCycleTimeSec":lambda e: e["p"]["cyc"],"idealCycleTimeSec":lambda e: e["p"]["cyc"],"taktTimeSec":lambda e: "36.0","setupTimeMin":lambda e: e["p"]["setup"],"standardSetupTimeMin":lambda e: e["p"]["setup"],
 "severity":lambda e: e["p"]["sev"],"occurrence":lambda e: e["p"]["occ"],"detection":lambda e: e["p"]["det"],"rpn":lambda e: e["p"]["sev"]*e["p"]["occ"]*e["p"]["det"],"revisedSeverity":lambda e: e["p"]["sev"],"revisedOccurrence":lambda e: max(1,e["p"]["occ"]-1),"revisedDetection":lambda e: max(1,e["p"]["det"]-1),
 "stepNo":lambda e: (e["j"]+1)*10,"currentStepNo":lambda e: (e["j"]+1)*10,"nextStepNo":lambda e: (e["j"]+2)*10 if e["j"]<9 else None,"entryStepNo":lambda e: 10,"returnStepNo":lambda e: (e["j"]+1)*10,"reworkReturnStepNo":lambda e: 80 if e["j"] in(5,6) else None,"sequenceHint":lambda e: (e["i"]+1)*10,
 "lifeLimit":lambda e: e["p"]["lifelimit"],"lifeUsed":lambda e: int(e["p"]["lifelimit"]*[0.77,0.41,1.0,0.22,0.63,0.35,0.58,0.93,0.12,0.49][e["i"]]),"lifeRemaining":lambda e: e["p"]["lifelimit"]-int(e["p"]["lifelimit"]*[0.77,0.41,1.0,0.22,0.63,0.35,0.58,0.93,0.12,0.49][e["i"]]),
 "lowLimit":lambda e: e["p"]["lo"],"highLimit":lambda e: e["p"]["hi"],"lowLowLimit":lambda e: fmt(float(e["p"]["lo"])-(float(e["p"]["hi"])-float(e["p"]["lo"]))*0.5,1),"highHighLimit":lambda e: fmt(float(e["p"]["hi"])+(float(e["p"]["hi"])-float(e["p"]["lo"]))*0.5,1),
 "engineeringMin":lambda e: "0.0","engineeringMax":lambda e: fmt(float(e["p"]["hi"])*1.5,1),"tagValue":lambda e: float(e["p"]["sp"])+[0.4,-1.2,0.9,2.6,-0.7,0.1,1.5,-2.0,0.6,-0.3][e["i"]]*(float(e["p"]["hi"])-float(e["p"]["lo"]))/10.0,
 "triggerValue":lambda e: fmt(float(e["p"]["hi"])+0.1*(e["i"]+1)*(float(e["p"]["hi"])-float(e["p"]["lo"]))/4,1),"limitValue":lambda e: e["p"]["hi"],"year":lambda e: 2026,"version":lambda e: [1,2,3,1,2,1,4,2,1,3][e["i"]],
 "bomVersion":lambda e: 1+sum(1 for k in range(e["i"]) if _BI[k]==_BI[e["i"]]),"routingVersion":lambda e: 1,"bopVersion":lambda e: 1,"modelYear":lambda e: [2026,2026,2027,2025,2026,2026,2027,2026,2025,2026][e["i"]],
 "attemptNo":lambda e: 1,"itemRevision":lambda e: REV[e["p"]["item"]],"drawingRevision":lambda e: REV[e["i"]],"revision":lambda e: ["A","B","C","D"][(e["line"] or 1)-1] if e["c"]["parent"] else REV[e["i"]],
})
# torque: three joints per unit on executions 2,3,4 plus one repeat on execution 2
TQ=[("Bleed screw M10x1.0","PSET-07",14.0,12.0,16.0,1,1,11.4,31.0),("Bleed screw M10x1.0","PSET-07",14.0,12.0,16.0,1,2,14.2,38.5),("Guide pin bolt M8, upper","PSET-08",28.0,25.0,31.0,2,1,28.6,44.0),("Guide pin bolt M8, lower","PSET-08",28.0,25.0,31.0,3,1,27.9,41.5),
 ("Bleed screw M10x1.0","PSET-07",14.0,12.0,16.0,1,1,13.8,36.0),("Guide pin bolt M8, upper","PSET-08",28.0,25.0,31.0,2,1,28.2,43.0),("Guide pin bolt M8, lower","PSET-08",28.0,25.0,31.0,3,1,29.1,46.5),
 ("Bleed screw M10x1.0","PSET-07",14.0,12.0,16.0,1,1,14.6,40.0),("Guide pin bolt M8, upper","PSET-08",28.0,25.0,31.0,2,1,27.6,39.5),("Guide pin bolt M8, lower","PSET-08",28.0,25.0,31.0,3,1,28.4,42.0)]
T=lambda k: (lambda e: TQ[e["i"]][k])
VAL.update({("torqueResult","jointName"):T(0),("torqueResult","programNo"):T(1),("torqueResult","targetTorqueNm"):lambda e: fmt(TQ[e["i"]][2],1),("torqueResult","minTorqueNm"):lambda e: fmt(TQ[e["i"]][3],1),("torqueResult","maxTorqueNm"):lambda e: fmt(TQ[e["i"]][4],1),
 ("torqueResult","tighteningNo"):T(5),("torqueResult","attemptNo"):T(6),("torqueResult","finalTorqueNm"):lambda e: fmt(TQ[e["i"]][7],1),("torqueResult","finalAngleDeg"):lambda e: fmt(TQ[e["i"]][8],1),
 ("torqueResult","result"):lambda e: "Not OK" if TQ[e["i"]][7]<TQ[e["i"]][3] else "OK",("torqueResult","failureReason"):lambda e: "Final torque below minimum, socket slipped on the hexagon" if e["i"]==0 else None,("torqueResult","rundownTimeMs"):[2140,1840,2310,2260,1795,2290,2345,1860,2275,2300],
 ("torqueResult","recipeId"):lambda e: e["identity"](e["byent"]["recipe"],5 if TQ[e["i"]][1]=="PSET-08" else 6)[0],("torqueResult","recipeName"):lambda e: e["identity"](e["byent"]["recipe"],5 if TQ[e["i"]][1]=="PSET-08" else 6)[2],
 ("recipe","programNo"):["GDC-P12","T6-02","O5110","W03","A12","PSET-08","PSET-07","LT-03","DM-5110","DM-5110R"]})
# leak: executions 5..8; documents 0..4 have two stage documents each
LKV=["Fail","Fail","Pass","Pass","Pass","Fail","Pass","Pass","Pass","Pass"]; LKA=[1,2,3,1,2,1,2,1,2,3]
LKR=["Fill pressure not reached at the high-pressure stage, inlet test seal leaking","Fill pressure not reached at the high-pressure stage, inlet test seal leaking",None,None,None,"Pressure drop above limit at the high-pressure stage, leak at piston seal",None,None,None,None]
VAL.update({("leakTestResult","verdict"):LKV,("leakTestResult","attemptNo"):LKA,("leakTestResult","failureReason"):LKR,("leakTestResult","programNo"):["LT-03"]*10,
 ("leakTestResult","ambientTemperatureC"):["27.4","27.5","27.5","27.8","27.9","28.3","28.4","26.9","27.0","27.1"],("leakTestResult","partTemperatureC"):["28.1","28.2","28.2","28.6","28.6","29.0","29.1","27.5","27.6","27.6"],
 ("leakTestResultStage","stageNo"):[1,2]*5,("leakTestResultStage","stageName"):["Low Pressure","High Pressure"]*5,("leakTestResultStage","testPressureBar"):["5.0","140.0"]*5,("leakTestResultStage","fillTimeSec"):["2.0","3.0"]*5,("leakTestResultStage","stabiliseTimeSec"):["3.0","4.0"]*5,("leakTestResultStage","testTimeSec"):["4.0","5.0"]*5,
 ("leakTestResultStage","limitPressureDropPa"):["30.0","50.0"]*5,("leakTestResultStage","limitLeakRateSccm"):["0.30","0.50"]*5,("leakTestResultStage","pressureDropPa"):["8.0","412.0","9.0","388.0","7.0","18.0","6.0","22.0","8.0","16.0"],
 ("leakTestResultStage","leakRateSccm"):["0.09","4.60","0.10","4.30","0.08","0.21","0.07","0.25","0.09","0.19"],("leakTestResultStage","stageResult"):["Pass","Fail","Pass","Fail","Pass","Pass","Pass","Pass","Pass","Pass"]})
# production order quantities by status
POQ=[(480,480,480,474,2,4),(480,480,312,305,1,6),(240,240,240,238,2,0),(240,240,240,231,9,0),(480,480,96,95,0,1),(240,240,0,0,0,0),(240,240,240,236,4,0),(480,240,180,172,3,5),(480,0,0,0,0,0),(120,0,0,0,0,0)]
for _n,_k in enumerate(["plannedQuantity","releasedQuantity","startedQuantity","goodQuantity","scrapQuantity","reworkQuantity"]): VAL[("productionOrder",_k)]=[x[_n] for x in POQ]
VAL.update({("productionOrder","erpOrderNo"):["0001000%05d"%(41200+7*k) for k in range(10)],("productionOrder","itemRevision"):lambda e: REV[e["p"]["item"]],
 ("wipUnit","reworkCount"):[0,0,0,1,0,0,0,2,0,0],("wipUnit","onHold"):lambda e: e["status"]=="On Hold",("lot","onHold"):lambda e: e["status"]=="On Hold",("container","onHold"):lambda e: False,
 ("wipUnit","bodyCavityNo"):[1,2,1,2,1,2,1,2,1,2],("wipUnit","itemRevision"):["D"]*10,("serialNumber","itemRevision"):["D"]*10,("asBuiltRecord","itemRevision"):["D"]*10,
 ("lot","supplierLotNo"):[None,None,None,None,"KPP-260905-07","ES-260905-11","ES-260828-04","BF-260901-22","WAA-H26-3418","ES-260912-02"],("lot","heatNo"):["H26-3418","H26-3418",None,None,None,None,None,None,"H26-3418",None],
 ("lot","attributesDieNo"):["DIE-5110-LH-02","DIE-5110-LH-02",None,None,None,None,None,None,None,None],("lot","attributesFurnaceChargeNo"):[None,"HT-260915-02","HT-260915-02","HT-260915-02",None,None,None,None,None,None],
 ("lot","attributesHardnessHbw"):[None,"94.0","94.0","94.0",None,None,None,None,None,None],("lot","attributesAnodisingLoadNo"):[None,None,None,"AN-260917-01",None,None,None,None,None,None],("lot","attributesCoatingThicknessUm"):[None,None,None,"12.4",None,None,None,None,None,None],
 ("lot","initialQuantity"):["240","240","236","232","5000","10000","10000","8000","1500.000","10000"],("lot","currentQuantity"):["0","0","118","232","4304","9520","9304","7280","0.000","10000"],
 ("user","userName"):["sunil.jadhav","kavita.bhosale","deepak.gaikwad","anita.kulkarni","rajesh.patil","imran.shaikh","meera.deshpande","vikram.pawar","sneha.joshi","mes.system"],
 ("user","email"):["sunil.jadhav@varunabrakes.example","kavita.bhosale@varunabrakes.example","deepak.gaikwad@varunabrakes.example","anita.kulkarni@varunabrakes.example","rajesh.patil@varunabrakes.example","imran.shaikh@varunabrakes.example","meera.deshpande@varunabrakes.example","vikram.pawar@varunabrakes.example","sneha.joshi@varunabrakes.example",None],
 ("user","mobile"):["+91-98220-55142","+91-98220-55377","+91-98220-55419",None,"+91-98220-55061","+91-98220-55208","+91-98220-55013","+91-98220-55290",None,None],("user","isLocked"):[False]*8+[True,False],("user","failedLoginCount"):[0,0,1,0,0,0,0,0,5,0],
 ("shift","startTimeLocal"):["06:00","14:00","22:00","09:00","06:00","14:00","08:00","20:00","14:00","22:00"],("shift","endTimeLocal"):["14:00","22:00","06:00","17:30","14:00","22:00","16:30","04:30","18:00","02:00"],("shift","crossesMidnight"):[False,False,True,False,False,False,False,True,False,True],
 ("shift","durationMinutes"):[480,480,480,510,480,480,510,510,240,240],("shift","plannedProductionMinutes"):[430,430,430,450,430,430,450,450,225,225],
 ("workCalendarException","exceptionDate"):[h[1] for h in HOLIDAYS],("workCalendarException","isWorking"):[False]*7+[True,True,False],
 ("item","drawingNo"):[code(x) for x in ITEMS],("item","erpMaterialNo"):["0000000000511%05d"%k for k in (10100,10200,20110,20105,30010,30020,30030,30040,30050,90356)],("item","netWeightKg"):["3.420","3.420","1.860","2.240","0.412","0.006","0.011","0.028","0.094","1.000"],
 ("item","grossWeightKg"):["3.480","3.480","1.880","2.260","0.418","0.006","0.011","0.029","0.096","1.000"],("item","standardCostInr"):["2184.50","2184.50","986.00","612.40","248.00","9.60","14.20","18.75","62.00","238.00"],("item","isSerialised"):[True,True]+[False]*8,("item","isLotControlled"):[False,False]+[True]*8,
 ("item","materialSpecification"):[None,None,"EN 1706 AC-42100","EN 1706 AC-42100","EN 10083-2 C45E","SAE J1401 EPDM","SAE J1401 EPDM","ISO 898-1 class 8.8","EN 10083-2 C45E","EN 1676 AB-42100"],("item","materialGrade"):[None,None,"AlSi7Mg0.3 T6","AlSi7Mg0.3 T6","C45E, hard chrome 20 um","EPDM 70 Shore A","EPDM 60 Shore A","Steel 8.8, zinc-nickel","C45E, zinc flake","AlSi7Mg0.3"],
 ("item","shelfLifeDays"):[None,None,None,None,None,730,730,None,None,None],("item","safetyCharacteristic"):[True,True,True,True,True,True,False,True,False,False],
 ("unitOfMeasure","symbol"):["ea","kg","mm","um","N.m","bar","Pa","degC","HBW","kWh"],("unitOfMeasure","isoCode"):["C62","KGM","MMT","4H","NU","BAR","PAL","CEL",None,"KWH"],("unitOfMeasure","dimension"):["Count","Mass","Length","Length","Torque","Pressure","Pressure","Temperature","Hardness","Energy"],
 ("unitOfMeasure","decimalPlaces"):[0,3,3,1,1,1,1,1,1,1],("currency","symbol"):["Rs","$","EUR","JPY","GBP","CNY","KRW","THB","AED","S$"],("currency","isoNumericCode"):["356","840","978","392","826","156","410","764","784","702"],("currency","decimalPlaces"):[2,2,2,0,2,2,0,2,2,2],
 ("country","isoAlpha3Code"):["IND","DEU","JPN","USA","CHN","KOR","THA","ITA","SWE","GBR"],("country","dialCode"):["+91","+49","+81","+1","+86","+82","+66","+39","+46","+44"],("language","nativeName"):["English","Marathi","Hindi","Tamil","Gujarati","Kannada","Deutsch","Nihongo","Telugu","Bangla"],
 ("site","addressCity"):["Pune","Pune","Chennai","Ahmedabad","Gurugram","Rudrapur","Kolar","Pune","Pune","Pune"],("site","addressDistrict"):["Pune","Pune","Kancheepuram","Ahmedabad","Gurugram","Udham Singh Nagar","Kolar","Pune","Pune","Pune"],
 ("site","addressState"):["Maharashtra","Maharashtra","Tamil Nadu","Gujarat","Haryana","Uttarakhand","Karnataka","Maharashtra","Maharashtra","Maharashtra"],("site","addressPostalCode"):["410501","412220","602105","382170","122051","263153","563133","410507","411057","411001"],
 ("site","erpPlantCode"):["PN01","PN02","TN01","GJ01","HR01","UK01","KA01","WH01","TC01","HO01"],("site","headcount"):[412,286,350,240,198,164,120,38,95,140],("tool","cavities"):[2,0,0,0,0,0,0,0,0,0],("tool","regrindCount"):[0,0,2,0,0,0,0,0,0,0],("tool","maxRegrinds"):[0,0,3,0,0,0,0,0,0,0],
 ("gauge","blockedForUse"):lambda e: e["status"]=="Overdue",("gauge","nextCalibrationDueAt"):lambda e: datetime.datetime(2026,8,31,18,30) if e["status"]=="Overdue" else datetime.datetime(2026,9,29,18,30) if e["status"]=="Due For Calibration" else datetime.datetime(2026,11+(e["i"]%2),5+e["i"],18,30),
 ("gauge","lastCalibratedAt"):lambda e: datetime.datetime(2026,3,2,18,30) if e["status"]=="Overdue" else datetime.datetime(2026,5+(e["i"]%3),5+e["i"],18,30),
 ("equipment","currentState"):lambda e: "Down" if e["status"]=="Under Maintenance" else ["Running","Running","Running","Idle","Running","Running","Setup","Running","Running","Running"][e["i"]],
 ("operation","isInspection"):[False]*7+[True,False,True],("operation","isSpecialProcess"):[True,True,False,False,True,False,False,False,False,False],("operation","requiresFirstOffApproval"):[True,True,True,False,True,True,True,True,True,False],
 ("operation","description"):lambda e: e["p"]["pfn"],("role","description"):["Runs operations at an assigned station and records results","Sets up machines, changes tools and approves first-off parts with quality","Leads a line crew and answers andon calls","Plans the shift, releases orders and approves handovers","Inspects parts and records results","Owns control plans, dispositions nonconformances and releases holds","Carries out breakdown and preventive maintenance","Receives, moves and issues material","Maintains routings, recipes and work instructions","Administers users, roles and system settings"],
 ("skill","description"):lambda e: "Can perform '%s' to the work instruction and react to abnormalities"%nm(e["p"]["op"]).lower(),("defectCode","description"):lambda e: e["p"]["ddesc"],("nonconformance","description"):lambda e: "%s. %s"%(e["p"]["ddesc"],e["p"]["problem"]),
 ("engineeringChange","description"):lambda e: "Change request: %s. Affected process step: %s"%(e["disp"].lower(),nm(e["p"]["op"]).lower()),("deviationPermit","description"):lambda e: "Temporary deviation on '%s' at %s; all affected containers carry a deviation tag"%(e["p"]["char"].lower(),nm(e["p"]["op"]).lower()),
 ("safetyIncident","description"):lambda e: "%s; area made safe and the incident reported to the shift supervisor"%e["disp"],("statusDefinition","status"):["Active"]*10})
for _e in ("department","designation","employmentType","equipmentType","skillCategory","permission","signatureMeaning","commodity","itemGroup","itemFamily","ppeItem","market","padCompound","surfaceFinish","vehicleModel","indirectActivity","containerType","movementType","stockStatus","packType","defectGroup","gaugeType","dispositionType","complaintType","lossCategory","reasonCategory","toolType","documentType","deviceType","notificationType","andonType","incidentType","energyType","bodyPart","injuryType","costCenter","manufacturer","systemConfiguration"):
    VAL.setdefault((_e,"description"),lambda e: "%s (%s)"%(e["disp"],e["rec"]))
RECFMT.update({"productionOrder":lambda i,j:"PO-10004%02d"%(12+7*i),"wipUnit":lambda i,j:"U2609%02d%s%04d"%(DAYS_[i],"ABC"[i%3],184+13*i),"serialNumber":lambda i,j:"VB26%03d%s%05d"%(243+DAYS_[i],"ABC"[i%3],184+13*i),"asBuiltRecord":lambda i,j:"ABR-VB26%03d%s%05d"%(243+DAYS_[i],"ABC"[i%3],184+13*i),
 "lot":lambda i,j:["L260915-GDC-014","L260915-HT-002","L260916-CNC-007","L260917-ANO-001","L260905-PST-007","L260905-SEL-011","L260828-BOT-004","L260901-BLS-022","L260910-ING-003","L260912-SEL-002"][i],
 "container":lambda i,j:["TRL-00%03d","TRL-00%03d","RCK-00%03d","BIN-000%03d","BIN-000%03d","BIN-000%03d","BIN-000%03d","BIN-000%03d","BIN-000%03d","BIN-000%03d"][i]%(31+17*i),
 "customerSchedule":lambda i,j:"CSR-%s-DS-2026-%02d"%(code(MASTER["customer"][[0,0,0,1,0,0,2,0,7,0][i]]),36+i),"shipment":lambda i,j:"SHP-2026-%06d"%(377+4*i),"goodsReceipt":lambda i,j:"GRN-2026-%06d"%(918+11*i),
 "nonconformance":lambda i,j:"NCR-2026-%06d"%(118+3*i),"capa":lambda i,j:"CAPA-2026-%04d"%(14+i),"qualityHold":lambda i,j:"HLD-2026-%06d"%(21+2*i),"reworkOrder":lambda i,j:"RWK-2026-%06d"%(52+3*i),"scrapRecord":lambda i,j:"SCR-2026-%06d"%(203+5*i),
 "deviationPermit":lambda i,j:"DEV-2026-%04d"%(6+i),"customerComplaint":lambda i,j:"CMP-2026-%04d"%(4+i),"maintenanceWorkOrder":lambda i,j:"MWO-2026-%06d"%(341+6*i),"engineeringChange":lambda i,j:"ECN-2026-%04d"%(27+i),"audit":lambda i,j:"AUD-2026-%04d"%(931+i),
 "msaStudy":lambda i,j:"MSA-2026-%04d"%(9+i),"ppapSubmission":lambda i,j:"PPAP-%s-L3-%02d"%(code(ITEMS[[0,1,2,3,0,1,2,3,0,0][i]]),i//4+1),"safetyIncident":lambda i,j:"SAF-2026-%04d"%(3+i),"skillCertification":lambda i,j:"CERT-%s-%s"%(code(MASTER["user"][REFIDX[("skillCertification","userId")][i]]),code(PROC[REFIDX[("skillCertification","skillId")][i]]["skill"])),
 "gaugeCalibration":lambda i,j:"GCAL-%s-2026-%02d"%(code(PROC[i]["gauge"]),1+i%2),"controlledDocument":lambda i,j:["DRW-5110-20-0105-B","SPC-VBS-HT-002-3","DRW-5110-20-0110-C","INS-VBS-CL-001-2","SPC-VBS-AN-004-5","CRT-KPP-260905-07","CRV-U260916-0184","REC-LKT-260916","CSP-SM-ES-3501-04","DRW-5110-10-0100-D"][i]})
DAYS_=[15,15,16,17,18,19,21,22,23,24]
BOOLRULE.update({"onHold":lambda e: e["status"]=="On Hold","withinLimits":lambda e: e["i"] not in FAIL,"inLimits":lambda e: e["i"]!=3,"inControl":lambda e: e["i"]!=3,"passed":lambda e: e["i"]!=3,"withinTolerance":lambda e: e["i"]!=4,"overridden":lambda e: False,"isPlanned":lambda e: e["i"]==8,
 "blockedForUse":lambda e: False,"causedStop":lambda e: e["i"]%2==0,"lineStopped":lambda e: e["i"] in(0,6,7),"isMicroStop":lambda e: e["i"]==5,"verified":lambda e: e["status"] in("Verified",),"closed":lambda e: e["i"]%3==0,"isLocked":lambda e: False})
AUTOVARY=re.compile(r"(No|Ref|Key|Address|barcode|Hash|checksum|payload|Payload|humanReadable|fileName|storageKey|scannedCode|castDateCode|phone|Phone|gstin|cin|pan|licenceNo|sha256|Sha256|website|endpoint|portalUrl|credentialRef|workstation|clientIp)$")
NOVARY={"programNo","revisionNo","planLineNo","bomLineNo","partNo","trialNo","balloonNo","erpMovementType","customerPartNo","customerRevision","supplierCodeAtCustomer"}
def bump(v,i):
    if i==0: return v
    m=list(re.finditer(r"\d+",v))
    if m:
        g=m[-1]; n=g.group(0); x=(int(n)+i*37)%(10**len(n)); return v[:g.start()]+("%0*d"%(len(n),x))+v[g.end():]
    return v

_AQL=[(2,8,2,0,1),(9,15,3,0,1),(16,25,5,0,1),(26,50,8,0,1),(51,90,13,0,1),(91,150,20,0,1),(151,280,32,1,2),(281,500,50,1,2),(501,1200,80,2,3),(1201,3200,125,3,4)]
for _n,_k in enumerate(["lotSizeFrom","lotSizeTo","sampleSize","acceptNumber","rejectNumber"]): VAL[("samplingPlanSizeRow",_k)]=[x[_n] for x in _AQL]
_PI=[0,1,2,3,0,1,2,3,0,0]
RECFMT["ppapSubmission"]=lambda i,j:"PPAP-%s-%s-%02d"%(code(ITEMS[_PI[i]]),REV[_PI[i]],1+sum(1 for k in range(i) if _PI[k]==_PI[i]))
REFIDX[("ppapSubmission","itemId")]=_PI

STATUSDATE={"shipped":{"Shipped"},"scrapped":{"Scrapped"},"voided":{"Voided"},"revoked":{"Revoked"},"removed":{"Removed"},"closed":{"Closed"},"dispatched":{"Dispatched","Delivered"},"delivered":{"Delivered"},"podReceived":{"Delivered"},
 "resolved":{"Resolved"},"cleared":{"Cleared"},"packed":{"Packed","Shipped","Full","Sealed"},"actualEnd":{"Completed","Closed"},"completed":{"Completed","Closed","Packed","Shipped","Verified","Accepted","Not Accepted","Delivered","Handed Over","Acknowledged"}}
STATUSDATE_NOT={"actualStart":{"Created","Released","Planned","Cancelled"}}
_PI2=[0,1,2,3,0,2,3,0,2,0]
REFIDX.update({("productionOrder","itemId"):_PI2,("productionOrder","routingId"):_PI2,("productionOrder","billOfMaterialId"):_PI2,("productionOrder","productVariantId"):[0,1,None,None,0,None,None,2,None,0],("productionOrder","lineId"):[5,5,2,0,5,2,0,5,2,5],
 ("wipUnit","bodyLotId"):[3]*10,("asBuiltRecord","bodyLotId"):[3]*10,("asBuiltRecord","castingLotId"):[0]*10,("asBuiltRecord","heatTreatmentLotId"):[1]*10,("nonconformance","supplierId"):[None]*5+[1]+[None]*4,
 ("torqueResult","operationExecutionId"):[2,2,2,3,3,3,4,4,4,4],("leakTestResult","operationExecutionId"):[5,5,6,6,6,7,7,8,8,8]})
CTXOF["productionOrder"]=[5,5,2,0,5,2,0,5,2,5]; CTXOF["productionSchedule"]=[5,5,2,0,5,2,0,5,2,5]
REFIDX[("lot","productionOrderId")]=[3,3,2,2,None,None,None,None,None,None]
NULLWHEN[("inspectionResult","nonconformanceId")]=lambda i,j,s: i!=3; NULLWHEN[("inspectionResult","defectCodeId")]=lambda i,j,s: i!=3
STATUSOF["wipUnit"]=["On Hold","In Process","In Process","In Rework","In Process","In Process","In Process","Scrapped","Packed","Shipped"]
TQ[:]=[("Bleed screw M10x1.0","PSET-07",14.0,12.0,16.0,1,1,14.2,38.5),("Guide pin bolt M8, upper","PSET-08",28.0,25.0,31.0,2,1,28.6,44.0),("Guide pin bolt M8, lower","PSET-08",28.0,25.0,31.0,3,1,27.9,41.5),
 ("Bleed screw M10x1.0","PSET-07",14.0,12.0,16.0,1,1,13.8,36.0),("Guide pin bolt M8, upper","PSET-08",28.0,25.0,31.0,2,1,28.2,43.0),("Guide pin bolt M8, lower","PSET-08",28.0,25.0,31.0,3,1,29.1,46.5),
 ("Bleed screw M10x1.0","PSET-07",14.0,12.0,16.0,1,1,11.4,31.0),("Bleed screw M10x1.0","PSET-07",14.0,12.0,16.0,1,2,11.8,33.5),("Guide pin bolt M8, upper","PSET-08",28.0,25.0,31.0,2,1,27.6,39.5),("Guide pin bolt M8, lower","PSET-08",28.0,25.0,31.0,3,1,28.4,42.0)]
VAL[("torqueResult","failureReason")]=lambda e: "Final torque below minimum, socket slipped on the hexagon" if TQ[e["i"]][7]<TQ[e["i"]][3] else None
VAL[("torqueResult","rundownTimeMs")]=[1840,2310,2260,1795,2290,2345,2140,2190,2275,2300]
LKV[:]=["Fail","Pass","Fail","Fail","Pass","Fail","Pass","Fail","Fail","Fail"]; LKA[:]=[1,2,1,2,3,1,2,1,2,3]
_T="Fill pressure not reached at the high-pressure stage, inlet test seal of the tester leaking"; _S="Pressure drop above limit at the high-pressure stage, leak at piston seal"
LKR[:]=[_T,None,_T,_T,None,_T,None,_S,_S,_S]
VAL[("leakTestResultStage","pressureDropPa")]=["8.0","412.0","9.0","18.0","7.0","388.0","6.0","402.0","8.0","16.0"]; VAL[("leakTestResultStage","leakRateSccm")]=["0.09","4.60","0.10","0.21","0.08","4.30","0.07","4.50","0.09","0.19"]
VAL[("leakTestResultStage","stageResult")]=["Pass","Fail","Pass","Pass","Pass","Fail","Pass","Fail","Pass","Pass"]
_OR=["OK","OK","OK","OK","Not OK","OK","OK","OK","Not OK","OK"]
VAL.update({("operationExecution","result"):_OR,("operationExecution","quantityIn"):[240,1,1,1,1,1,1,1,1,1],("operationExecution","quantityGood"):[231]+[1 if r=="OK" else 0 for r in _OR[1:]],("operationExecution","quantityReject"):[9]+[0 if r=="OK" else 1 for r in _OR[1:]],("operationExecution","quantityRework"):[0]*10,
 ("operationExecution","attemptNo"):[1]*10,("operationExecution","remarks"):["Die 2, both cavities running",None,"Bleed screw and both guide pin bolts tightened",None,"Bleed screw torque low on two attempts, unit sent to rework",None,"Second test after tester fault, passed",None,"Leak at piston seal confirmed on three tests, unit scrapped",None]})
STATUSOF["operationExecution"]=["Completed"]*10
TITLES["nonconformance"][1]="Hardness below 85 HBW on furnace charge HT-260915-02"; TITLES["nonconformance"][4]="Anodic coating below 8 micrometres on load AN-260917-01"

_WP=[0,0,1,1,4,4,7,7,9,9]
RECFMT["wipUnit"]=lambda i,j:"U2609%02d%s%04d"%(DAYS_[_WP[i]],"ABC"[_WP[i]%3],184+13*i)
RECFMT["serialNumber"]=lambda i,j:"VB26%03d%s%05d"%(243+DAYS_[_WP[i]],"ABC"[_WP[i]%3],184+13*i)
RECFMT["asBuiltRecord"]=lambda i,j:"ABR-VB26%03d%s%05d"%(243+DAYS_[_WP[i]],"ABC"[_WP[i]%3],184+13*i)
REFIDX.update({("lot","unitOfMeasureId"):[0]*8+[1,0],("gauge","manufacturerId"):[None]*6+[6,7,None,9],("gauge","rangeUnitOfMeasureId"):[2,8,2,3,3,2,4,5,2,2]})
CTXOF["sparePart"]=[6,1,2,3,4,7,8,9,0,5]
_GR=[("1.000","25.000","0.010","0.050"),("8.0","650.0","0.1","2.0"),("50.000","75.000","0.001","0.002"),("1.0","5000.0","1.0","5.0"),("0.0","2000.0","0.1","1.0"),("0.00","300.00","0.01","0.03"),("2.0","25.0","0.1","0.2"),("0.0","200.0","0.1","0.2"),("0.000","25.000","0.001","0.003"),("0.000","700.000","0.001","0.002")]
for _n,_k in enumerate(["rangeMin","rangeMax","resolution","accuracy"]): VAL[("gauge",_k)]=[x[_n] for x in _GR]
VAL[("gauge","model")]=["38DL Plus","HB-3000B","511-713","VHX-970F","Dualscope FMP40","LH-600F","STa 6000","DPI 611","129-153","Contura G2"]
VAL[("gauge","serialNo")]=["UT-21-0457","HB-19-1132","BG-22-07713","PM-20-0098","CT-21-4410","HG-23-0261","TA-22-1904","PC-21-3327","DM-23-0882","CMM-18-0044"]
DUR=[95,150,42,25,60,18,35,48,30,22]
def GENERIC_POST(env):
    d=env["doc"]; i=env["i"]; e=env["e"]
    def dt(k): return d[k][1] if d.get(k) else None
    if "durationMinutes" in d and dt("startedAt") and e not in("shift",):
        d["durationMinutes"]=("int",DUR[i])
        if dt("endedAt"): d["endedAt"]=("date",dt("startedAt")+datetime.timedelta(minutes=DUR[i]))
        if "repairMinutes" in d: d["repairMinutes"]=("int",int(DUR[i]*0.7)); d["responseMinutes"]=("int",3+i%6)
    if "durationSec" in d and dt("startedAt") and "endedAt" in d:
        secs=[5400,5700,2520,900,1800,1080,2100,2880,1800,1320][i]
        d["durationSec"]=("int",secs)
        if dt("endedAt"): d["endedAt"]=("date",dt("startedAt")+datetime.timedelta(seconds=secs))
    if e=="operationExecution" and dt("startedAt") and dt("completedAt"):
        cyc=float(env["p"]["cyc"]); act=cyc*[1.0,1.06,1.11,0.97,2.4,1.02,1.9,1.05,2.8,1.0][i]
        d["completedAt"]=("date",dt("startedAt")+datetime.timedelta(seconds=int(act))); d["cycleTimeSec"]=("dec","%.1f"%act)
    if dt("clockOnAt") and dt("clockOffAt") and "durationMinutes" in d: d["durationMinutes"]=("int",int((dt("clockOffAt")-dt("clockOnAt")).total_seconds()//60))
    if "updatedAt" in d and d["updatedAt"]:
        ev=[v[1] for k,v in d.items() if isinstance(v,tuple) and v[0]=="date" and k not in("createdAt","updatedAt") and datetime.datetime(2026,9,14)<=v[1]<datetime.datetime(2026,10,1)]
        if ev: d["updatedAt"]=("date",max(ev+[d["createdAt"][1]]))

NOSCALE|={"quantity","baseQuantity","sampleQuantity","significantProductionRunQuantity"}
STATUSDATE["released"]={"Released","Partially Released","In Progress","Completed","Closed","On Hold","Cancelled"}
CTXOF["billOfMaterialComponent"]=[5,5,5,5,6,6,2,0,5,5]
REFIDX.update({("billOfMaterialComponent","operationId"):[5,5,5,5,6,6,2,0,5,5],("billOfMaterialComponent","unitOfMeasureId"):[0]*7+[1,0,0],("equipment","supplierId"):[None]*10,("wipUnit","qualityHoldId"):[0]+[None]*9,
 ("container","containerTypeId"):[2,2,4,0,0,0,0,0,0,0],("container","ownerCustomerId"):[0]*10,("container","itemId"):[3,2,2,0,0,0,0,0,0,0],
 ("goodsReceiptLine","itemId"):[4,5,6,7,9,5,4,8,7,9],("goodsReceiptLine","lotId"):[4,5,6,7,8,9,None,None,None,None],
 ("materialMovement","itemId"):[4,5,4,7,2,0,0,0,6,5],("materialMovement","lotId"):[4,5,4,7,3,None,None,None,6,5],("materialMovement","fromLocationId"):[None,1,1,5,4,5,5,7,2,5],("materialMovement","toLocationId"):[1,2,5,1,5,9,7,8,2,6],
 ("materialMovement","fromStockStatusId"):[None,1,0,0,0,0,None,0,0,0],("materialMovement","toStockStatusId"):[1,0,0,0,0,9,0,0,0,2],("materialMovement","productionOrderId"):[None,None,0,0,2,7,9,None,None,None],
 ("materialMovement","goodsReceiptId"):[0,1]+[None]*8,("materialMovement","shipmentId"):[None]*7+[2,None,None],("materialMovement","kitId"):[None,None,0]+[None]*7,("materialMovement","reversalOfMaterialMovementId"):[None]*10})
PARENTIDX["goodsReceiptLine"]=list(range(10)); CTXOF["materialMovement"]=[5,5,5,6,4,7,9,9,5,5]
for _k in [("materialMovement","productionOrderId"),("materialMovement","goodsReceiptId"),("materialMovement","shipmentId"),("materialMovement","kitId"),("materialMovement","reversalOfMaterialMovementId")]: NULLWHEN.pop(_k,None)
NULLWHEN[("materialMovement","containerId")]=lambda i,j,s: i not in(6,7)
_GQ=["5000","10000","10000","8000","1500.000","10000","5000","4000","8000","1500.000"]; _GS=["Accepted","Accepted","Accepted","Accepted","Accepted","Accepted","Pending","Accepted Under Deviation","Rejected","Accepted"]
VAL.update({("billOfMaterialComponent","quantity"):["1","1","1","1","1","2","1","2.350","1","1"],("billOfMaterialComponent","traceLevel"):["Lot"]*10,("billOfMaterialComponent","scrapPct"):["0.5","0.2","1.0","1.0","0.5","0.2","3.0","6.0","0.5","0.2"],
 ("equipment","serialNo"):["LK-GDC-190457","AFE-T6-18-0221","MAK-A61-203318","DUR-ECW-21-0074","GAL-ANO-17-0012","PRO-EMAP-22-1187","AC-PF6-2231907","ATQ-F620-21-5540","TRU-TM5-23-0931","KEY-XGX-22-4416"],
 ("equipment","controllerMake"):["Siemens","Siemens","FANUC","Siemens","Siemens","Promess","Atlas Copco","ATEQ","Trumpf","Keyence"],("equipment","controllerModel"):["S7-1500","S7-1200 with Stange SE-607","31i-B5","S7-1500","S7-1200","UltraPRO","Power Focus 6000","F620","TruControl 1000","XG-X2800"],
 ("spcSample","subgroupNo"):[147+k for k in range(10)],
 ("goodsReceiptLine","supplierLotNo"):["KPP-260905-07","ES-260905-11","ES-260828-04","BF-260901-22","WAA-H26-3418","ES-260912-02","KPP-260918-03","SGP-260910-15","BF-260915-08","WAA-H26-3477"],("goodsReceiptLine","orderedQuantity"):_GQ,("goodsReceiptLine","receivedQuantity"):_GQ,
 ("goodsReceiptLine","acceptedQuantity"):[q if s.startswith("Accepted") else "0" for q,s in zip(_GQ,_GS)],("goodsReceiptLine","rejectedQuantity"):[q if s=="Rejected" else "0" for q,s in zip(_GQ,_GS)],("goodsReceiptLine","inspectionStatus"):_GS,("goodsReceiptLine","lineNo"):[10]*10,
 ("shipment","shipToCode"):lambda e: "%s-D%d"%(code(MASTER["customer"][[0,0,0,1,0,0,2,0,7,0][e["i"]]]),2+e["i"]%3),("shipment","totalContainers"):lambda e: max(1,int(e["doc"]["totalQuantity"][1]//24)) if isinstance(e["doc"].get("totalQuantity"),tuple) else 20,
 ("container","quantity"):[120,60,24,16,24,24,24,24,24,24],("container","capacity"):[120,60,24,24,24,24,24,24,24,24],
 ("materialMovement","quantity"):["5000","10000","696","120","232","1","24","480","4","9520"],
 ("maintenanceWorkOrder","downtimeMinutes"):DUR,("qualityHold","reasonText"):lambda e: "Hold pending disposition of nonconformance: %s"%(e["doc"].get("nonconformanceName") or "see nonconformance"),
 ("skillCertification","validTo"):lambda e: {"Valid":datetime.datetime(2027,3,31,18,29,59),"Expiring Soon":datetime.datetime(2026,10,8,18,29,59),"Expired":datetime.datetime(2026,8,31,18,29,59),"Revoked":datetime.datetime(2027,3,31,18,29,59)}[e["status"]],
 ("skillCertification","level"):[3,3,4,3,3,2,3,4,3,3],("serialNumber","dataMatrixPayload"):lambda e: "SM-3501-0421-LH#%s"%e["rec"],("serialNumber","markGrade"):lambda e: ["A","B"][e["i"]%2] if e["status"] in("Marked","Shipped") else None,
 ("wipUnit","castDateCode"):["26258A1","26258A2","26258A1","26258B2","26258B1","26258B2","26259A1","26259A2","26259B1","26259B2"]})
STATUSOF["materialMovement"]=["Posted"]*8+["Reversed","Posted"]
STATUSOF["maintenanceWorkOrder"]=["Completed","In Progress","Closed","Completed","Closed","Closed","Completed","Planned","Reported","Completed"]
ENUMRULE["releaseDecision"]=lambda env,en: "Released" if env["status"] in("Released","Partially Released") else None
NULLENUM.discard("releaseDecision")

_Q=[480,240,480,960,120,480,240,720,480,360]
VAL.update({("customerScheduleLine","quantity"):_Q,("shipmentLine","quantity"):_Q,("customerScheduleLine","shippedQuantity"):[480,240,480,480,0,480,240,360,0,0],("energyReading","consumption"):["41.6","38.2","44.9","12.4","27.8","9.6","6.1","5.4","3.9","4.7"],
 ("energyReading","unitsProduced"):[38,0,17,20,24,112,198,150,255,180],("andonEvent","responseSec"):[210,95,140,60,420,180,75,130,300,240],("andonEvent","resolutionSec"):[840,1260,600,300,0,900,2100,2880,0,1500],
 ("checkSheetItem","question"):lambda e: e["p"]["q"] if e["line"]==1 else "Is the red reject bin at %s empty and is the reaction plan displayed?"%nm(e["p"]["wc"]),("asBuiltRecordOperation","result"):["OK"]*10,("asBuiltRecord","leakTestVerdict"):lambda e: "Fail" if e["i"]==7 else "Pass"})
REFIDX.update({("energyReading","energyTypeId"):[0]*10,("andonEvent","andonTypeId"):[2,5,0,1,0,1,0,0,8,9]})
OBS="""
## Schema Observation

Nothing was added to or removed from any collection. These points were noticed while filling the documents and are reported only.

| # | Collection | Observation | What the samples do |
|---|---|---|---|
| 1 | u_mes_prod_recipe | recipeType has no allowed value for an assembly press program or a vision job | The recipes at those two positions are a second tightening program and a second laser marking layout; executions at the press and at final inspection carry no recipe |
| 2 | u_mes_plan_operationExecution | result is required, so an execution that is still running cannot be stored without a result | All ten executions are completed |
| 3 | u_mes_plan_container | ownerCustomerId is required, although in-plant trolleys and racks have no customer owner | All containers carry the customer of the part |
| 4 | u_mes_prod_operation, u_mes_prod_item | Exactly 10 documents: the eleventh operation (packing) and the items brake pad set and mounting bracket are not represented | Ten operations OP010 to OP100 and ten items |
| 5 | u_mes_prod_billOfMaterialComponent | The RH assembly BOM points to the LH body, because an RH body is not among the ten items | Left as is |
| 6 | all transaction collections | All documents belong to the Chakan plant; the other nine sites exist only in u_mes_mast_site | Plant is not varied in transactions, so that lines, work centers and equipment stay consistent with their site |

## How realistic the documents are

- Read through and corrected by hand: production orders, WIP units, operation executions, torque and leak results, lots, goods receipt lines, stock movements, inspection results, nonconformances, gauges, equipment, users, items, BOM components, routing steps, downtime events, serial numbers.
- Built by the same rules but not read line by line: the remaining collections. Their keys, types, references, allowed values and dates are checked by the table above; individual text or number combinations in them can still read oddly.
- Each collection has exactly ten documents, so stories are short: for example, ten leak tests are spread over four units.
"""
