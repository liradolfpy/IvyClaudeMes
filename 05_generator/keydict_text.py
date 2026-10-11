# key|example|allowed values (; separated, empty = free text)|description (optional)
# A key followed by ? may be null. Used by gen_specs.py.
TEXT = r'''
name|(entity)
legalName|Varuna Brake Systems Private Limited
scope|Enterprise|Enterprise;Site|Whether the record applies to the whole enterprise or to one site
cin|U34300PN2009PTC134567||Corporate identification number
gstin|27AAACV4521K1Z6||Goods and services tax identification number
pan|AAACV4521K||Permanent account number
industryCode|29301||National industrial classification code
registeredAddressLine1|Plot B-14, Chakan MIDC Phase II
registeredAddressLine2?|Village Khalumbre, Taluka Khed
registeredAddressCity|Pune
registeredAddressState|Maharashtra
registeredAddressPostalCode|410501
registeredAddressCountry|IN||ISO 3166-1 alpha-2 country code
baseCurrency|INR||ISO 4217 currency code
website?|https://www.varunabrakes.example
designation|Plant Head
email?|sunil.jadhav@varunabrakes.example
phone?|+91-2135-555-0142
siteType|Manufacturing Plant|Manufacturing Plant;Warehouse;Technical Center;Head Office
timezone|Asia/Kolkata||IANA time zone name
addressLine1|Plot B-14, Chakan MIDC Phase II
addressLine2?|Village Khalumbre, Taluka Khed
addressCity|Pune
addressDistrict|Pune
addressState|Maharashtra
addressPostalCode|410501
addressCountry|IN
factoryLicenceNo|MH/PUN/2(m)(i)/34300/2011/0871
erpPlantCode|PN01
currency|INR
language|en||ISO 639-1 language code
standard|IATF 16949:2016||Standard or specification the record refers to
certificateNo|IATF-0412877
areaType|Production|Production;Storage;Quality;Maintenance;Utility
costCenter|CC-5120||Cost center charged with the activity
lineType|Assembly|Casting;Heat Treatment;Machining;Surface Treatment;Assembly;Inspection;Packing
itemFamily|Front Caliper
workCenterType|Machine Station|Machine Station;Manual Station;Test Station;Inspection Station;Batch Process
erpWorkCenterCode|PN01-TRQ01
trackingGrain|Unit|Lot;Unit;Container|Level at which material is tracked at this point
equipmentType|DC Nutrunner|Gravity Die Casting Machine;Heat Treatment Furnace;CNC Machining Center;Washing Machine;Anodising Line;Assembly Press;DC Nutrunner;Leak Tester;Laser Marker;Coordinate Measuring Machine
equipmentClass|Production Equipment|Production Equipment;Test Equipment;Measuring Equipment;Utility
manufacturer|Atlas Copco
model|PF6000 with ETV STR61
serialNo|AC-PF6-2231907
assetNo|FA-PN1-004512
controllerMake|Atlas Copco
controllerModel|Power Focus 6000
controllerIpAddress|10.21.6.41
controllerProtocol|Open Protocol|OPC UA;Open Protocol;Modbus TCP;Profinet;MQTT;Ethernet/IP
criticality|A|A;B;C|A = failure stops the line or affects safety, B = reduced output, C = no immediate effect
currentState|Running|Running;Idle;Setup;Down;Starved;Blocked;Planned Stop
safetyCategory|PL d|PL a;PL b;PL c;PL d;PL e|Performance level of the safety function (ISO 13849-1)
startTimeLocal|06:00||Local start time, 24-hour HH:mm
endTimeLocal|14:00||Local end time, 24-hour HH:mm
workingDay|Monday|Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday
weeklyOffDay|Sunday|Monday;Tuesday;Wednesday;Thursday;Friday;Saturday;Sunday
exceptionType|Public Holiday|Public Holiday;Plant Shutdown;Extra Working Day;Reduced Shift
description|(entity)
remarks?|No abnormality observed
roleInCrew|Operator|Operator;Setter;Line Leader;Quality Inspector;Material Handler
attendance|Present|Present;Absent;Leave;Overtime
permission|operationExecution.complete||Permission code in the form resource.action
signatureMeaning|Approved|Approved;Reviewed;Released;Verified;Rejected
userName|sunil.jadhav
fullName|(entity)
userType|Employee|Employee;Contractor;System
department|Production|Production;Quality;Maintenance;Stores;Engineering;Planning;Safety
badgeNo|B-0010231||Number encoded on the operator badge used for station login
mobile?|+91-98220-55142
employmentType|Permanent|Permanent;Contract;Trainee;Apprentice
skillCategory|Process|Process;Quality;Maintenance;Safety;Material Handling
assessmentMethod|Practical Test|Practical Test;Written Test;Observation;On the Job
restrictions?|Not certified for master leak verification
revokedReason?|
customerType|OEM|OEM;Tier 1;Aftermarket
parentCustomerCode?|SMG||Code of the customer's parent group
billingAddressLine1|Survey No. 212, Talegaon Industrial Area
billingAddressCity|Pune
billingAddressState|Maharashtra
billingAddressPostalCode|410507
billingAddressCountry|IN
supplierCodeAtCustomer|V10487||Vendor code the customer uses for this plant
portalUrl?|https://supplier.sahyadrimotors.example
shipToCode|SML-TLG-D4
line1|Gate 3, Chassis Assembly Shop
city|Pune
state|Maharashtra
postalCode|410507
dockCode|D4
businessFunction|Quality|Quality;Purchasing;Logistics;Engineering;Production;Finance
supplierType|Direct Material|Direct Material;Indirect Material;Tooling;Service;Calibration Laboratory
commodity|Machined Steel Parts
symbol|N.m
dimension|Torque|Count;Mass;Length;Torque;Pressure;Temperature;Time;Energy;Volume;Hardness;Leak Rate
isoCode?|NU||UN/ECE Recommendation 20 unit code
itemType|Finished Good|Finished Good;Semi Finished;Purchased Component;Raw Material;Consumable;Packaging
itemGroup|Brake Caliper
drawingNo|5110-10-0100
drawingRevision|D
materialSpecification?|EN 1706 AC-42100
materialGrade?|AlSi7Mg0.3 T6
procurementType|In House|In House;Purchased;Subcontracted
hsnCode|87083000||Harmonised system of nomenclature code
erpMaterialNo|000000000051101001
revision|D
customerPartNo|SM-3501-0421-LH
customerRevision|04
optionsHand|LH|LH;RH
optionsPadCompound|NAO-Ceramic|NAO-Ceramic;Low-Metallic;Semi-Metallic
optionsMarket|Domestic|Domestic;Export
optionsSurfaceFinish|Anodised Natural|Anodised Natural;Anodised Black;Painted
optionsColour?|Silver
modelCode|SM-X42
labelSuffix|L
itemRevision|D
bomType|Production|Production;Engineering;Rework
erpBomNo|00051101-01
traceLevel|Lot|None;Lot;Serial|Level at which the consumed component must be recorded
referenceDesignator?|P1||Position reference on the drawing
operationType|Assembly|Casting;Heat Treatment;Machining;Cleaning;Surface Treatment;Assembly;Test;Marking;Inspection;Packing
specialProcessStandard?|CQI-9||AIAG special process assessment that applies
erpControlKey|PP01
routingType|Standard|Standard;Rework;Alternate
erpRoutingNo|50001101-01
nextStepCondition|Result OK|Result OK;Result Not OK;Rework Complete;Always
interlockType|Skill|Skill;Recipe;Tool Life;Gauge Calibration;Previous Step;Component Scan;Maintenance Due
title|(entity)
safetyNotes?|Keep hands clear of the nutrunner socket during rundown
instructionText|Place the bleed screw in the socket and press both start buttons
inputType|Confirmation|None;Confirmation;Number;Text;Scan;Photo;Device Value
caution?|Do not reuse a bleed screw that has been tightened once
ppeItem|Safety Glasses|Safety Glasses;Safety Shoes;Cut Resistant Gloves;Ear Plugs;Heat Resistant Gloves;Face Shield;Apron
keyPoint|Bleed screw seat must be dry and free of chips
recipeType|Tightening Program|Die Casting Parameters;Furnace Profile;CNC Program;Washing Program;Anodising Program;Tightening Program;Leak Test Program;Laser Marking Program
programNo|PSET-07
checksum|9f2c4a1be07d53c6||Checksum of the parameter set used to detect an unapproved change at the controller
changeType|Process Change|Design Change;Process Change;Material Change;Supplier Change;Tooling Change;Document Change
reasonCodeText|Customer request after field study of bleed screw seepage
originator|Customer|Customer;Internal;Supplier
customerChangeRef?|SML-ECR-2026-118
effectivityType|Date|Date;Serial Number;Lot;Stock Run Out
cutInSerialNo?|VB26272A00001
stockDisposition|Use As Is|Use As Is;Rework;Scrap;Return To Supplier
fromRevision|C
toRevision|D
changeAction|Update|Create;Update;Obsolete
decision|Approved|Approved;Rejected;Approved With Conditions
comment?|Verified against customer drawing revision D
scheduleType|Delivery Schedule|Forecast;Delivery Schedule;Just In Time Call Off
customerOrderNo|4500218734
erpSalesOrderNo|0020041877
firmness|Firm|Firm;Forecast
erpOrderNo|000100041200
orderType|Production|Production;Rework;Trial;PPAP Run
priority|Normal|Low;Normal;High;Urgent
rule|Earliest Due Date|Earliest Due Date;First In First Out;Critical Ratio;Priority
executionType|Production|Production;Rework;Retest;Setup
result|OK|OK;Not OK
enteredText?|Seat checked, dry
scannedCode?|5110300040/L260921-BS-003
deviceSource?|Nutrunner Controller|Manual Entry;Scanner;Nutrunner Controller;Leak Tester;Gauge Interface;PLC
overrideReason?|
qualityStatus|Released|Released;Under Inspection;On Hold;Rejected
castDateCode|26272A1||Date, shift and cavity code cast into the body
lotType|Casting Lot|Supplier Lot;Melt Lot;Casting Lot;Heat Treatment Charge;Machining Lot;Anodising Load;Finished Goods Lot
supplierLotNo?|KPP-260914-07
heatNo?|H26-3418||Heat number of the alloy melt
attributesDieNo?|DIE-5110-LH-02
attributesFurnaceChargeNo?|HT-260928-03
attributesAnodisingLoadNo?|AN-260929-02
attributesCavityNo|1
containerType|Returnable Bin|Returnable Bin;Trolley;Pallet;Corrugated Box;Rack
bookingType|Direct|Direct;Indirect
indirectActivity?||Cleaning;Training;Meeting;Waiting For Material;Waiting For Maintenance;5S
erpConfirmationNo?|0000871245
source|MES Terminal|MES Terminal;PLC;Scanner;ERP;Device;Manual Entry|Where the record originated
changeoverType|Variant Change|Variant Change;Item Change;Tool Change;Die Change
lossReason?|Socket for RH variant not at point of use
internalExternal|Internal|Internal;External|Internal steps need the equipment stopped; external steps are done while it runs
qualityNotes?|Two leak test rejects on unit serials ending 0171 and 0178, NCR raised
maintenanceNotes?|Nutrunner socket replaced at 09:40
materialNotes?|Piston seal lot changeover at 11:15
locationType|Line Side|Warehouse Rack;Line Side;Quarantine;Dispatch Bay;Receiving Bay;Tool Crib;Scrap Yard
zone|ASY
rack?|R02
bin?|B14
erpStorageLocation|LS01
barcode|LOC-LS-ASY-01
stockStatus|Unrestricted|Unrestricted;Quality Inspection;Blocked;Reserved
movementType|Issue To Line|Goods Receipt;Putaway;Issue To Line;Return From Line;Transfer;Scrap;Finished Goods Receipt;Shipment;Stock Adjustment
fromStockStatus?|Unrestricted|Unrestricted;Quality Inspection;Blocked;Reserved
toStockStatus?|Unrestricted|Unrestricted;Quality Inspection;Blocked;Reserved
scanSource|Handheld Scanner|Handheld Scanner;Fixed Scanner;Manual Entry
reasonText?|Replenishment against kanban call
erpDocumentNo?|4900318842
erpMovementType?|261
purchaseOrderNo|4500117302
supplierInvoiceNo|KPP/26-27/1842
deliveryChallanNo|DC-07713
vehicleNo|MH14 GT 4471
gateEntryNo|GE-260925-0044
erpGrnNo?|5000209117
inspectionStatus|Accepted|Pending;Accepted;Rejected;Accepted Under Deviation
kitType|Order Kit|Order Kit;Shift Kit;Rework Kit
requestType|Kanban|Kanban;Andon Call;Manual
triggerSource|Minimum Level Sensor|Minimum Level Sensor;Operator;Schedule
componentSerialNo?|
consumptionType|Scanned|Scanned;Backflush;Manual
dunnage?|Moulded tray, 8 pockets per layer
packType|Bin|Unit Bag;Tray;Bin;Pallet
labelType|Container Label|Unit Mark;Container Label;Shipping Label;Hold Tag;Location Label
printerLanguage|ZPL|ZPL;EPL;PDF
symbology|Data Matrix ECC200|Data Matrix ECC200;QR Code;Code 128;Code 39;PDF417
payloadPattern|[)>{RS}06{GS}P{customerPartNo}{GS}Q{quantity}{GS}1T{lotNo}{RS}{EOT}
fieldName|customerPartNo
fieldFormat?|%s
payload|[)>06PSM-3501-0421-LHQ241TL260929-FG-002
humanReadable|SM-3501-0421-LH  QTY 24  LOT L260929-FG-002
reprintReason?|
verificationGrade?|B|A;B;C;D;F|ISO/IEC 15415 or 29158 overall symbol grade
invoiceNo|VBS/26-27/004128
asnNo?|ASN-260930-0071
eWayBillNo|271004417732
transporter|Deccan Road Carriers
driverName|Ganesh More
lrNo|DRC-771204||Lorry receipt number
dataMatrixPayload|SM-3501-0421-LH#VB26272A00184
markGrade?|A|A;B;C;D;F
voidReason?|
childType|Lot|Lot;Serial
childSerialNo?|
linkType|Assembled|Assembled;Replaced;Split;Merge;Transformed
removedReason?|
leakTestVerdict|Pass|Pass;Fail
recordHash|c41d7be29a630f5e8b7a12d4f09c33aa71e5d60b2f8c94a1d3e7b65f0a2c4d18||SHA-256 hash of the frozen record
characteristicType|Product|Product;Process
classification|Critical|Critical;Significant;Standard|Special characteristic class from the drawing or PFMEA
drawingZone?|C4
balloonNo|12
dataType|Variable|Variable;Attribute
toleranceType|Bilateral|Bilateral;Unilateral Upper;Unilateral Lower
measurementMethod|Bore gauge, two-point, three positions
gaugeType|Bore Gauge|Bore Gauge;Micrometer;Vernier Caliper;Height Gauge;Plug Gauge;Thread Gauge;Coordinate Measuring Machine;Hardness Tester;Coating Thickness Tester;Torque Analyser;Pressure Calibrator;Roughness Tester;Visual
attributeAcceptance?|No porosity visible on sealing face
reactionPlan|Stop, segregate parts since last good check, inform line leader, raise NCR
phase|Production|Prototype;Pre Launch;Production
processName|CNC machining of piston bore
equipmentText|Horizontal machining center HMC-01
specification|54.000 +0.046 / 0 mm
measurementTechnique|Air gauge
sampleFrequency|Every 2 hours
controlMethod|X-bar R chart
responsible|Operator
planType|In Process|Incoming;In Process;First Off;Final;Dock Audit;Layout
collectionTrigger|Operation Complete|Operation Start;Operation Complete;Time Interval;Unit Count;Goods Receipt;Changeover
frequencyType|Every N Units|Every Unit;Every N Units;Every N Minutes;Per Lot;Per Shift;First Off
recordType|Measured Value|Measured Value;Pass Fail;Count
samplingType|Attribute AQL|Attribute AQL;Fixed Sample;Hundred Percent;Skip Lot
inspectionLevel|II|S-1;S-2;S-3;S-4;I;II;III
switchingRules?|Tightened after 2 of 5 lots rejected; normal after 5 consecutive accepted
checkSheetType|Start Of Shift|Start Of Shift;Poka Yoke Verification;First Off Approval;Autonomous Maintenance;Layered Process Audit;Changeover
frequency|Per Shift|Per Shift;Daily;Weekly;Per Changeover;Per Lot
question|Is the master leak part detected as Not OK by the tester?
answerType|Yes No|Yes No;Number;Text
expectedAnswer?|Yes
unitText?|N.m
reactionOnFail?|Stop the station and call the line leader
overallResult|Pass|Pass;Fail
reactionTaken?|
answerText?|Yes
inspectionType|In Process|Incoming;In Process;First Off;Final;Audit
attributeResult?|Pass|Pass;Fail
chartType|X-bar R|X-bar R;X-bar S;I-MR;p;np;c;u
subgroupFrequency|Every 2 hours
assignableCause?|
correctiveAction?|
defectGroup|Leak|Casting;Machining;Surface;Assembly;Leak;Torque;Marking;Handling;Supplier
defaultDisposition|Rework|Use As Is;Rework;Scrap;Return To Supplier;Sort
scrapCostCategory|Assembly Scrap|Casting Scrap;Machining Scrap;Assembly Scrap;Supplier Chargeable
customerDefectCode?|SM-Q-0417
pfmeaFailureMode?|Fluid leak past piston seal
ncType|Internal|Internal;Supplier;Customer
rootCauseSummary?|Seal groove burr from worn grooving insert
disposition|Rework|Use As Is;Rework;Scrap;Return To Supplier;Sort
reworkType|Replace Component|Replace Component;Retighten;Re-machine;Re-anodise;Re-mark;Clean
instruction|Dismantle piston, replace seal with new lot, reassemble and repeat leak test
reinspectionResult?|Pass|Pass;Fail
scrapType|Process Scrap|Process Scrap;Setup Scrap;Material Defect;Destructive Test
disposalMethod|Remelt|Remelt;Sell As Scrap;Return To Supplier
holdType|Quality|Quality;Customer;Engineering;Supplier
releaseDecision?|Released|Released;Rework;Scrap;Return To Supplier
releaseComment?|100 percent leak retest completed, 2 units reworked
deviationType|Product|Product;Process;Material
customerApprovalRef?|SML/DEV/2026/044
limitType|Quantity|Quantity;Date
markingRequirement?|Green dot on bin label
capaType|Corrective|Corrective;Preventive
d2ProblemDescription|Leak test failures at 140 bar stage on caliper LH, 6 of 480 units on 29 Sep 2026 shift A
d4RootCauseOccurrence?|Burr on seal groove edge after grooving insert exceeded tool life
d4RootCauseEscape?|Visual check of groove not in control plan; leak test detects only at end of line
d4RootCauseMethod?|5 Why|5 Why;Fishbone;Fault Tree;Is Is Not
d7PreventionLessonsLearned?|Tool life interlock to be enforced on all grooving operations
d7PreventionHorizontalDeployment?|Apply to rear caliper line LN-MC-02
currentDiscipline|D5|D1;D2;D3;D4;D5;D6;D7;D8
roleInTeam|Champion|Champion;Leader;Member
methodology|AIAG-VDA|AIAG-VDA;AIAG 4th Edition
processFunction|Seal the piston to the bore
failureMode|Seal cut during piston insertion
failureEffect|External brake fluid leak, reduced braking performance
failureCause|Burr on seal groove edge
preventionControl|Tool life counter with forced insert change
detectionControl|100 percent pressure leak test at 5 bar and 140 bar
actionPriority|High|High;Medium;Low
recommendedAction?|Add groove edge vision check after machining
actionTaken?|Vision check installed on HMC-01 unload station
submissionReason|Engineering Change|Initial Submission;Engineering Change;Tooling Transfer;Correction Of Discrepancy;Tooling Inactive Over One Year;Sub Supplier Change
customerDecision?|Approved|Approved;Interim Approved;Rejected
customerRemarks?|
calibrationSource|External|Internal;External
calibrationType|Periodic|Initial;Periodic;After Repair;After Shock Or Damage
masterStandardRef|Setting ring 54.000 mm, cert NABL-CC-2231
traceability|NABL accredited laboratory, traceable to NPL India
asFoundResult|Within Tolerance|Within Tolerance;Out Of Tolerance
asLeftResult|Within Tolerance|Within Tolerance;Out Of Tolerance
studyType|Gauge R and R|Gauge R and R;Bias;Linearity;Stability;Attribute Agreement
studyMethod|ANOVA|ANOVA;Average And Range;Kappa
conclusion|Acceptable|Acceptable;Conditionally Acceptable;Not Acceptable
auditType|Layered Process Audit|Layered Process Audit;Process Audit;Product Audit;System Audit;Customer Audit;Supplier Audit
scopeText|Assembly line 1, torque and leak test stations
overallRating?|A|A;B;C
clause?|8.5.1.1
grade|Minor|Major;Minor;Observation;Opportunity For Improvement
customerRefNo|SML-QN-2026-0932
complaintType|Line Rejection|Line Rejection;Zero Kilometre;Warranty;Logistics
defectDescription|Bleed screw cap missing on 3 calipers at customer line
customerLocation|Sahyadri Motors, Talegaon, Chassis Assembly Shop
vehicleModel?|SM-X42
direction|Inbound|Inbound;Outbound
communicationSummary|Containment report with sorting result sent to customer SQA
reasonType|Downtime|Downtime;Scrap;Hold;Andon;Changeover Loss
pathText|Unplanned > Mechanical > Clamping > Clamp cylinder failure||Full path of the reason from level 1 to this level
category|Mechanical|Mechanical;Electrical;Process;Material;Quality;Organisation;Planned
lossCategory|Breakdown|Breakdown;Setup And Adjustment;Minor Stop;Reduced Speed;Startup Reject;Production Reject;Planned Stop|OEE loss category the reason counts towards
oeeImpact|Availability|Availability;Performance;Quality;None
responsibleDepartment|Maintenance|Production;Quality;Maintenance;Stores;Engineering;Planning
stateCode|Running|Running;Idle;Setup;Down;Starved;Blocked;Planned Stop
subStateCode?|Auto Cycle
plcStateCode?|3
downtimeType|Unplanned|Planned;Unplanned
faultCode?|E4107
faultText?|Rundown torque not reached, spindle 1
reasonPathText?|Unplanned > Mechanical > Nutrunner > Socket worn
actionText?|Socket replaced and verified with torque analyser
commentText|Spare socket taken from tool crib
gapReason?|Nutrunner socket change 18 minutes
sourceAddress|ns=3;s="DB_Process"."DieTempUpper"
tagClass|Process Value|Process Value;Setpoint;Counter;State;Alarm Bit;Energy
aggregation|Average|None;Average;Minimum;Maximum;Last;Sum
tagValueText?|
signalQuality|Good|Good;Uncertain;Bad
alarmCode|A2031
alarmText|Die temperature upper half above high limit
alarmClass|Process|Process;Machine;Safety;Quality
jointName|Bleed screw M10x1.0
strategy|Torque Control Angle Monitor|Torque Control;Torque Control Angle Monitor;Angle Control Torque Monitor;Yield Control
failureReason?|
controllerResultNo|PF6-000418871||Result identifier issued by the device controller
testMedium|Dry Air|Dry Air;Nitrogen;Helium
verdict|Pass|Pass;Fail
stageName|High Pressure|Low Pressure;High Pressure
stageResult|Pass|Pass;Fail
intervalType|Calendar|Calendar;Counter;Condition
intervalUom|Days|Days;Weeks;Months;Cycles;Shots;Run Hours
counterSource?|
ownerDepartment|Maintenance|Production;Maintenance;Tool Room;Quality
acceptanceCriteria?|Master leak 0.5 sccm detected within plus or minus 10 percent
workOrderType|Breakdown|Breakdown;Preventive;Predictive;Improvement;Calibration
problemDescription|Nutrunner stops with rundown torque not reached on every third cycle
rootCause?|Socket drive worn beyond limit
manufacturerPartNo|4220 3311 10
toolType|Die|Die;Fixture;Cutting Tool;Nutrunner Socket;Test Seal;Press Tool;Gauge Fixture
toolClass|Production Tooling|Production Tooling;Customer Owned Tooling;Consumable Tooling
mountedPosition?|Station 1
lifeUom|Shots|Shots;Cycles;Pieces;Run Hours
eventType|(entity)
conditionOnRemoval?|Normal wear
removalReason?|Life limit reached
messageType|Production Order Download|Production Order Download;Operation Confirmation;Goods Movement;Goods Receipt;Shipment Advice;Material Master;Quality Notification
idempotencyKey|ERP-PRD-000100041200-0001||Key that makes repeated delivery of the same message harmless
correlationNo|c7a41e06-2d1f-4b7e-9a52-0c5f3e8b1d44||Identifier shared by records that belong to the same business transaction
payloadFormat|JSON|JSON;XML;IDoc
payloadHash|5e1b0a7c9d3f42e8a6b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f9
errorCode?|
errorText?|
connectorType|ERP|ERP;PLM;OPC UA Server;Tool Controller;Label Printer;Leak Tester;Email Gateway
targetSystem|SAP S/4HANA
protocol|HTTPS REST|HTTPS REST;OPC UA;Open Protocol;Modbus TCP;MQTT;ZPL Over TCP;SMTP
endpoint|https://erp-prd.varunabrakes.example/api/mes
environment|Production|Production;Quality;Development
authMethod|OAuth2 Client Credentials|OAuth2 Client Credentials;Certificate;Basic;None
credentialRef|vault://mes/pn1/erp-prd||Pointer to the secret in the vault; the secret itself is never stored
healthStatus|Healthy|Healthy;Degraded;Down
functionName|postOperationConfirmation
endpointPath|/v1/confirmations
scheduleExpression?|*/5 * * * *||Cron expression for scheduled functions
deviceType|Nutrunner Controller|PLC;Edge Gateway;Nutrunner Controller;Leak Tester;Barcode Scanner;Label Printer;Energy Meter;Laser Marker Controller;Gauge Interface;HMI Terminal
firmwareVersion|3.9.12
ipAddress|10.21.6.41
macAddress|00:1B:2C:4D:6E:91
opcNodeAddress?|ns=3;s="NR1"
connectionStatus|Online|Online;Offline;Degraded
appType|Operator Station|Operator Station;Inspection;Material Handling;Maintenance;Andon Board
widgetType|Work Instruction|Work Instruction;Data Entry;Device Result;Scan;Checklist;Signature;Summary
triggerEvent|Device Result Received|Step Opened;Button Pressed;Scan Completed;Device Result Received;Value Out Of Limit;Timer Expired
triggerAction|Go To Step|Go To Step;Complete Operation;Raise Nonconformance;Raise Andon;Print Label;Block Station
triggerTarget?|30
purpose|Tightening result|Tightening result;Leak test result;Component scan;Label print;Measurement
eventCategory|Execution|Execution;Quality;Material;Maintenance;Integration;Security
messageText|Operation OP070 completed OK on unit U260929A0184
eventPayloadText?|{"finalTorqueNm":"14.2","attemptNo":1}||Event details as JSON text
clientIp|10.21.6.118
application|MES Operator Client 1.4.2
previousHash|a3f19c0e55d2b7a48c61e0f3d92b7c4a1e6f08d5b3c2a1908f7e6d5c4b3a2f10||Hash of the previous audit entry, forming a tamper-evident chain
entryHash|7b2e41d09c8f3a65e1d4c7b0a9f8e2d3c6b5a4f1e0d9c8b7a6f5e4d3c2b1a0f9
changedFieldName|upperSpecLimit
oldValue?|15.5
newValue?|16.0
meaning|Approved|Approved;Reviewed;Released;Verified;Rejected
authenticationMethod|Password And Badge|Password;Password And Badge;Single Sign On
contentHash|d0c1b2a3948576e5f4d3c2b1a0f9e8d7c6b5a4938271605f4e3d2c1b0a9f8e7d
workstation|PN1-ASY-HMI-07
notificationType|Andon Escalation|Andon Escalation;Quality Alert;Maintenance Due;Calibration Due;Order Late;Interface Failure;Certification Expiring
bodyText|Quality andon at WC-TRQ-01 not acknowledged within 5 minutes
channel|Mobile Push|Screen;Email;SMS;Mobile Push
documentType|Drawing|Drawing;Work Instruction Media;Certificate;Inspection Report;Photo;Calibration Certificate;Customer Specification;Tightening Curve;PPAP Element
fileName|5110-10-0100_revD.pdf
mimeType|application/pdf
storageProvider|S3|S3;GridFS;File Share
storageKey|pn1/drawings/5110-10-0100_revD.pdf
checksumSha256|2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae
tag|caliper
rangeType|Serial Number|Serial Number;Lot Number;Order Number;Label Number;Document Number
prefix|VB
formatMask|VB{YY}{DDD}{SHIFT}{NNNNN}
resetPolicy|Daily|Never;Daily;Monthly;Yearly
checkDigitMethod?|None|None;Modulo 10;Modulo 43
exampleValue|VB26272A00184
module|Performance|Master Data;Product Definition;Execution;Materials;Traceability;Quality;Performance;Maintenance;Integration;Safety
valueType|Text|Text;Number;Flag;JSON
configValueText?|Planned Production Time
configValueJson?|
lastChangedReason?|Aligned with corporate OEE definition
energyType|Electricity|Electricity;Compressed Air;Natural Gas;Water
andonType|Quality|Quality;Material;Maintenance;Safety;Supervisor
resolutionText?|Seal lot segregated, new lot issued
incidentType|Near Miss|Near Miss;Unsafe Condition;Unsafe Act;First Aid;Medical Treatment;Lost Time Injury;Property Damage
bodyPart?|
injuryType?|
immediateAction|Area cordoned, spill cleaned, operator briefed
collectionName|u_mes_exe_productionOrder
statusCode|IN_PROGRESS||Stable code for the status value, upper case with underscores
statusName|In Progress
colourCode?|#F5A623
transitionName|Start production
jobTitle|Plant Head||Job title of the contact person
resourceName|operationExecution||Object the permission applies to
actionName|complete||Action the permission allows on the resource
isoNumericCode|356||ISO 4217 numeric currency code
isoAlpha3Code|IND||ISO 3166-1 alpha-3 country code
dialCode|+91
nativeName|English||Name of the language in that language
supportPhone?|+91-20-5550-0188
platformCode?|X4
stockEffect|Decrease|Increase;Decrease;Transfer;None|Effect of the movement on stock on hand
erpStockType?|Unrestricted-use||Stock type the status maps to in ERP
erpCostCenterCode|PN015120
valueCode|OK||Stable code of the enumeration value
valueName|OK||Display text of the enumeration value
'''
