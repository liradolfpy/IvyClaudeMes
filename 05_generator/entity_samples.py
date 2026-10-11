# Sample identity per entity collection: entity|recordNo|display value|second text (description where the entity has both)
# and an alternate sample (ALT) used when one document refers twice to the same entity (from/to, parent/child, component).
ES_TEXT = r'''
enterprise|VBS|Varuna Brake Systems Pvt. Ltd.
site|PN1|Chakan Plant, Pune
area|ASY|Assembly and Test
line|ASY-01|Caliper Assembly Line 1
workCenter|TRQ-01|Bleed Screw Torque Station
equipment|TRQ-01-NR1|DC Nutrunner Station 1
shift|A|Shift A
workCalendar|PN1-2026|Chakan Plant Calendar 2026
shiftRoster|20260929-A-ASY-01|
role|OPERATOR|Production Operator|Runs operations at an assigned station and records results
user|10231|Sunil Jadhav
skill|LEAK-TEST-OP|Leak Test Operation|Operate the pressure leak tester and react to a failed test
skillCertification|10231-LEAK-TEST-OP|
customer|SML|Sahyadri Motors Ltd.
supplier|S1042|Konkan Precision Pistons Pvt. Ltd.
unitOfMeasure|EA|Each
item|5110-10-0100|Front Brake Caliper Assembly, LH
productVariant|FBC-LH-STD|Front Caliper LH Standard
billOfMaterial|5110-10-0100-D-01|
operation|OP070|Bleed screw torque|Tighten the bleed screw to the specified torque with the DC nutrunner
routing|5110-10-0100-R01|Front caliper LH assembly routing
billOfProcess|5110-10-0100-BOP01|
workInstruction|WI-OP070-001|Bleed screw tightening - Front caliper LH
recipe|TRQ-PRG-07|Bleed screw M10 torque program
engineeringChange|2026-0031|Bleed screw torque window revised|Torque window changed from 13 +/- 2 N.m to 14 +/- 2 N.m on customer drawing revision D
customerSchedule|SML-DS-2026-40|
productionOrder|1000412|
productionSchedule|20260929-ASY-01-A|
dispatchList|20260929-TRQ-01-A|
operationExecution|20260929-000184|
stepCompletion|20260929-000911|
wipUnit|U260929A0184|
lot|L260928-GDC-014|
container|BIN-000731|
labourBooking|20260929-10231-01|
changeover|20260930-ASY-01-01|
shiftHandover|20260929-ASY-01-A|
storageLocation|LS-ASY-01|Line-side supermarket, Assembly 1
inventoryBalance|000482|
materialMovement|20260929-000233|
goodsReceipt|2026-000918|
kit|20260929-0007|
materialRequest|20260929-0012|
materialConsumption|20260929-001205|
packagingSpecification|5110-10-0100-SML-01|
labelTemplate|SML-BIN-A5|Sahyadri Motors bin label A5
label|20260929-000412|
shipment|2026-000377|
serialNumber|VB26272A00184|
genealogyLink|20260929-000551|
componentLotLink|20260928-000037|
asBuiltRecord|VB26272A00184|
characteristic|5110-20-0110-C012|Piston bore diameter
controlPlan|5110-10-0100-PROD|
inspectionPlan|OP030-INP-01|Machining in-process inspection, caliper body LH
samplingPlan|AQL-1.0-II|AQL 1.0, general inspection level II
checkSheet|TRQ-01-SOS|Start of shift check, torque station
checkSheetResult|20260929-A-TRQ-01|
inspectionResult|20260929-000342|
spcChart|C012-CNC-01|Piston bore diameter, X-bar R, CNC-01
spcSample|C012-CNC-01-0147|
defectCode|LK01|Leak at piston seal|Pressure decay above limit traced to the piston seal
nonconformance|2026-000118|Leak test failures on caliper LH|Six units failed the 140 bar stage on shift A; pressure drop between 62 and 110 Pa against a limit of 50 Pa
reworkOrder|2026-000052|
scrapRecord|2026-000203|
qualityHold|2026-000021|
deviationPermit|2026-0006|Anodising thickness upper limit deviation|Coating thickness up to 16.5 um accepted against 16.0 um maximum for 2,000 pieces
capa|2026-0014|8D - Leak at piston seal
pfmea|5110-10-0100-PF|Process FMEA, Front Brake Caliper Assembly LH
ppapSubmission|5110-10-0100-D-L3|
gauge|G-BG-054|Bore gauge 50-75 mm
gaugeCalibration|G-BG-054-2026-02|
msaStudy|2026-0009|
audit|LPA-2026-0931|Layered process audit, Assembly line 1, week 40
customerComplaint|2026-0004|Bleed screw cap missing on three calipers at customer line
reasonCode|MECH-NR-02|Nutrunner socket worn
equipmentState|20260929-000077|
downtimeEvent|20260929-0009|
productionCount|20260929-TRQ-01-08|
oeeRecord|20260929-A-TRQ-01-NR1|
processTag|PN1.GDC01.DIE_TEMP_UPPER|Die temperature, upper half, casting machine 1
processReading|20260929-00417733|
alarm|20260929-000031|
torqueResult|20260929-000184|
leakTestResult|20260929-000184|
maintenancePlan|PM-LKT-01-M|Leak tester monthly preventive maintenance
maintenanceWorkOrder|2026-000341|Nutrunner rundown fault, station 1
sparePart|SP-004417|Socket 10 mm, 3/8 inch drive, for bleed screw nutrunner
tool|SKT-10-0007|Nutrunner socket 10 mm, torque station 1
toolLifeRecord|20260929-000019|Usage
erpMessage|20260929-000871|
integrationConnector|ERP-PRD|ERP production interface
iotDevice|NR-CTRL-01|Nutrunner controller, torque station 1
operatorApp|APP-TRQ-01|Torque station operator app
businessEvent|20260929-00031877|Operation Completed
auditTrail|20260929-00004412|
electronicSignature|20260929-000207|
notification|20260929-000096|Quality andon not acknowledged
controlledDocument|DRW-5110-10-0100-D|Drawing 5110-10-0100 revision D, Front Brake Caliper Assembly LH
numberRange|SERIAL-FBC-LH|Serial numbers, front caliper LH
systemConfiguration|oee.plannedTimeBasis|Time basis used as the denominator of availability
energyReading|20260929-EM03-0031|
andonEvent|20260929-0005|Leak test rejects repeating at station LKT-01
safetyIncident|2026-0003|Coolant spill near HMC-01 walkway|Coolant hose leak left a wet patch on the walkway; no one slipped
statusDefinition|productionOrder.IN_PROGRESS|In Progress|Order has at least one unit started
statusTransition|productionOrder.RELEASED-IN_PROGRESS|Start production
enumerationValue|operationExecution.result.OK|OK|Operation finished within all limits
department|PROD|Production|All manufacturing lines from casting to packing
designation|ASM-OPR|Assembly Operator|Operator on assembly and test stations
employmentType|PERM|Permanent|On the company payroll without end date
costCenter|5120|Assembly Line 1
manufacturer|ATLAS-COPCO|Atlas Copco
equipmentType|DC-NUTRUNNER|DC Nutrunner|Electric tightening spindle with torque and angle control
skillCategory|PROCESS|Process
permission|operationExecution.complete|Complete an operation
signatureMeaning|APPROVED|Approved|The signer approves the content
currency|INR|Indian Rupee
country|IN|India
language|en|English
transporter|DRC|Deccan Road Carriers
commodity|MACH-STEEL|Machined Steel Parts
itemGroup|CALIPER|Brake Caliper
itemFamily|FRONT-CALIPER|Front Caliper
ppeItem|SAFETY-GLASSES|Safety Glasses
market|DOM|Domestic
padCompound|NAO-CER|NAO-Ceramic
surfaceFinish|ANOD-NAT|Anodised Natural
vehicleModel|SM-X42|Sahyadri X42
indirectActivity|WAIT-MAT|Waiting For Material
containerType|RB-6040|Returnable Bin 600 x 400
movementType|ISSUE-LINE|Issue To Line|Issue of components from stores to a line-side location
stockStatus|UNR|Unrestricted|Free to use
packType|BIN|Bin
defectGroup|LEAK|Leak
gaugeType|BORE-GAUGE|Bore Gauge
dispositionType|REWORK|Rework|Bring the part back to specification on the rework routing
complaintType|LINE-REJ|Line Rejection
lossCategory|BREAKDOWN|Breakdown|Unplanned equipment failure
reasonCategory|MECH|Mechanical
toolType|SOCKET|Nutrunner Socket
documentType|DRAWING|Drawing
deviceType|NR-CTRL|Nutrunner Controller
notificationType|ANDON-ESC|Andon Escalation
andonType|QUALITY|Quality|Operator needs quality support at the station
incidentType|NEAR-MISS|Near Miss
energyType|ELEC|Electricity
bodyPart|HAND|Hand
injuryType|CUT|Cut
'''
ALT_TEXT = r'''
user|10087|Anita Kulkarni
item|5110-30-0010|Piston, dia 54 mm, steel, chrome plated
lot|S260914-PST-007|
storageLocation|WH-A-R02-B14|Warehouse A, rack 02, bin 14
productionOrder|1000409|
statusDefinition|productionOrder.RELEASED|Released
operation|OP080|Pressure leak test
workCenter|LKT-01|Pressure Leak Test Station
area|PRD|Production
equipment|ASY-01|Assembly Cell 1
customerSchedule|SML-DS-2026-39|
materialMovement|20260929-000229|
operatorApp|APP-TRQ-01-V2|Torque station operator app
routing|5110-10-0100-RW1|Front caliper LH rework routing
reasonCode|MECH-NR|Nutrunner
enterprise|VIG|Varuna Industries Group
stockStatus|QI|Quality Inspection
department|MFG|Manufacturing
customer|SMG|Sahyadri Motors Group
'''
USERS = {  # role -> (recordNo, name)
 "operator":("10231","Sunil Jadhav"),"quality":("10087","Anita Kulkarni"),"supervisor":("10045","Rajesh Patil"),
 "maintenance":("10112","Imran Shaikh"),"manager":("10019","Meera Deshpande"),"stores":("10150","Vikram Pawar"),"system":("SYSTEM","MES System")}
CHILD_TEXT = {
 ("enterpriseContact","name"):"Arvind Kelkar",("shiftBreak","name"):"Lunch break",("workCalendarException","description"):"Gandhi Jayanti",
 ("skillLevelScale","description"):"Works independently to standard and can react to abnormalities",("customerShipTo","name"):"Sahyadri Motors Talegaon Plant, Dock 4",
 ("customerContact","name"):"Priya Nair",("supplierContact","name"):"Mahesh Gawde",("itemRevision","description"):"Bleed screw torque window revised to 14 +/- 2 N.m",
 ("billOfProcessStepInterlock","description"):"Operator must hold a valid certification for skill LEAK-TEST-OP at level 3 or higher",
 ("billOfProcessStepProcessParameter","name"):"Final torque",("workInstructionStep","title"):"Tighten bleed screw",("recipeParameter","name"):"Target torque",
 ("recipeStage","name"):"Final tightening",("changeoverStep","description"):"Replace nutrunner socket with the RH variant socket",
 ("shiftHandoverOpenItem","description"):"Verify seal lot S260921-SEL-004 before use on shift B",("spcSampleViolation","description"):"One point beyond the upper control limit",
 ("nonconformanceContainmentAction","description"):"Hold all units assembled with seal lot S260921-SEL-004 and retest 100 percent",
 ("reworkOrderStep","description"):"Remove piston and seal, inspect groove, fit new seal",("capaContainmentAction","description"):"Sort finished goods stock and customer transit stock by leak retest",
 ("capaCorrectiveAction","description"):"Enforce tool life interlock on grooving insert at 400 pieces",("capaImplementationAction","description"):"Tool life counter activated on HMC-01 and verified over 2,000 pieces",
 ("ppapSubmissionElement","name"):"Process FMEA",("auditFinding","description"):"Torque analyser verification record not signed for 28 Sep shift C",
 ("maintenancePlanTask","description"):"Verify tester with the 0.5 sccm master leak and record the reading",("operatorAppStep","name"):"Tighten and confirm result",
 ("safetyIncidentAction","description"):"Replace coolant hose and add drip tray under the HMC-01 coupling",
 ("toolLifeRecord","eventType"):"Usage",("businessEvent","eventType"):"Operation Completed"}
ENUM_OVERRIDE = {("toolLifeRecord","eventType"):["Mounted","Usage","Dismounted","Regrind","Maintenance","Scrapped"],
 ("businessEvent","eventType"):["Order Released","Operation Started","Operation Completed","Recipe Downloaded","Hold Placed","Hold Released","Label Printed","Unit Scrapped","Shipment Dispatched","User Logged In"]}

# Reference overrides so that a sample fits its context: (root entity, key stem ending) -> (target _id, display)
REF_OVERRIDE = {
 ("characteristic","unitOfMeasure"):("UOM-MM","Millimetre"),("inspectionResult","unitOfMeasure"):("UOM-MM","Millimetre"),("gauge","UnitOfMeasure"):("UOM-MM","Millimetre"),
 ("processTag","unitOfMeasure"):("UOM-DEGC","Degree Celsius"),("energyReading","unitOfMeasure"):("UOM-KWH","Kilowatt hour"),("recipe","unitOfMeasure"):("UOM-NM","Newton metre"),
 ("billOfProcess","unitOfMeasure"):("UOM-NM","Newton metre"),("equipment","UnitOfMeasure"):("UOM-NM","Newton metre"),("processReading","processTag"):("TAG-PN1.GDC01.DIE_TEMP_UPPER","Die temperature, upper half, casting machine 1"),
 ("processTag","equipment"):("EQ-GDC-01","Gravity Die Casting Machine 1"),("processReading","equipment"):("EQ-GDC-01","Gravity Die Casting Machine 1"),("processTag","iotDevice"):("IOT-PLC-GDC-01","PLC, casting machine 1"),
 ("leakTestResult","equipment"):("EQ-LKT-01","Pressure Leak Tester 1"),("leakTestResult","IotDevice"):("IOT-LKT-CTRL-01","Leak tester controller 1"),("leakTestResult","recipe"):("RCP-LKT-PRG-03","Caliper leak test program, 5 bar and 140 bar"),
 ("leakTestResult","Tool"):("TL-TSL-54-0003","Test seal set, piston bore 54 mm"),("energyReading","IotDevice"):("IOT-EM-03","Energy meter, assembly line 1"),("label","IotDevice"):("IOT-PRN-FIP-01","Label printer, packing station"),
 ("alarm","equipment"):("EQ-GDC-01","Gravity Die Casting Machine 1"),("alarm","processTag"):("TAG-PN1.GDC01.DIE_TEMP_UPPER","Die temperature, upper half, casting machine 1"),("alarm","iotDevice"):("IOT-PLC-GDC-01","PLC, casting machine 1"),
 ("spcChart","equipment"):("EQ-CNC-01","Horizontal Machining Center 1"),("spcChart","workCenter"):("WC-CNC-01","CNC Machining Cell 1"),("spcSample","workCenter"):("WC-CNC-01","CNC Machining Cell 1"),
 ("inspectionResult","workCenter"):("WC-CNC-01","CNC Machining Cell 1"),("inspectionResult","operation"):("OPN-OP030","CNC machining"),("characteristic","operation"):("OPN-OP030","CNC machining"),
 ("characteristic","item"):("ITM-5110-20-0110","Caliper Body, LH, machined and anodised"),("inspectionResult","item"):("ITM-5110-20-0110","Caliper Body, LH, machined and anodised"),("spcChart","item"):("ITM-5110-20-0110","Caliper Body, LH, machined and anodised"),
 ("nonconformance","Operation"):("OPN-OP080","Pressure leak test"),("nonconformance","WorkCenter"):("WC-LKT-01","Pressure Leak Test Station"),
 ("reasonCode","Department"):("DEPT-MAINT","Maintenance"),("maintenancePlan","Department"):("DEPT-MAINT","Maintenance"),("energyType","unitOfMeasure"):("UOM-KWH","Kilowatt hour"),("andonType","Department"):("DEPT-QUAL","Quality"),
 ("lot","item"):("ITM-5110-20-0105","Caliper Body Casting, LH, T6"),("goodsReceipt","item"):("ITM-5110-30-0010","Piston, dia 54 mm, steel, chrome plated"),("supplier","item"):("ITM-5110-30-0010","Piston, dia 54 mm, steel, chrome plated")}
DOC_OVERRIDE = {"curve":("DOC-CRV-20260929-000184","Tightening curve, unit U260929A0184"),"photo":("DOC-PHT-20260929-0031","Photo, leak at piston seal, unit U260929A0171"),
 "certificate":("DOC-CRT-KPP-260914-07","Material certificate, piston lot KPP-260914-07"),"evidence":("DOC-TRN-10231-LEAK","Assessment sheet, Sunil Jadhav, leak test operation"),
 "training":("DOC-TRN-LEAK-TEST-OP","Training module, leak test operation"),"report":("DOC-RPT-LPA-2026-0931","Audit report LPA-2026-0931"),"instruction":("DOC-PKI-5110-10-0100","Packing instruction, front caliper LH"),
 "media":("DOC-WIM-OP070-02","Work instruction picture, bleed screw seating")}
VALUE_OVERRIDE = {("enumerationValue","fieldName"):"result",("statusDefinition","fieldName"):"status",("enumerationValue","collectionName"):"u_mes_exe_operationExecution",("user","designation"):"Assembly Operator",("supplierContact","designation"):"Quality Manager",("customerContact","designation"):"Supplier Quality Engineer"}
