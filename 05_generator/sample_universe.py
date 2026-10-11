"""Sample-data universe: the hand-written content behind the 10 sample documents per collection.
PROC is the process table (one row per routing operation); documents that share a process context
take their work center, equipment, recipe, tool, characteristic and so on from the same row."""
PROC=[
 dict(op="OP010|Gravity die casting",wc="GDC-01|Gravity Die Casting Cell 1",eq="GDC-01-M1|Gravity Die Casting Machine 1",eqt="GDC-MACHINE|Gravity Die Casting Machine",mfr="LKM|LK Machinery",model="GDC-600T tilting",line=0,area=0,item=3,comp=9,
  rcp="GDC-5110-LH-01|Caliper body LH casting parameters",rcptype="Die Casting Parameters",prog="GDC-P12",tool="DIE-5110-LH-02|Gravity die, caliper body LH, die 2",tlt="DIE|Die",lifeuom="Shots",lifelimit=80000,
  dev="PLC-GDC-01|PLC, casting machine 1",dvt="PLC|PLC",skill="GDC-OP|Gravity die casting operation",wi="Pouring and die cycle - Caliper body LH",instr="Skim the ladle, pour in one continuous stream and start the tilt cycle",key="Die face temperature must be above 380 degC before the first pour",
  char="Casting wall thickness at bridge",ctype="Product",cclass="Significant",nom="8.00",lsl="7.50",usl="8.50",uom=2,gauge="G-UT-001|Ultrasonic thickness gauge 1-25 mm",gty="UT-GAUGE|Ultrasonic Thickness Gauge",method="Ultrasonic thickness, three points on the bridge",dp=2,
  tag="PN1.GDC01.DIE_TEMP_UPPER|Die temperature, upper half, casting machine 1",tuom=7,sp="400.0",lo="380.0",hi="420.0",
  defect="CS01|Shrinkage porosity",dgroup="CAST|Casting",ddesc="Porosity visible on machined face or found by X-ray sampling",reason="MECH-GDC-01|Die ejector pin stuck",rcat=0,fault="E1107 Ejector not returned to home position",alarm="Die temperature upper half above high limit",
  pfn="Fill the die cavity completely with sound metal",pfm="Shrinkage porosity in the bridge section",pfe="Reduced strength of caliper body, possible fluid seepage",pfc="Die temperature too low at pour",pfp="Die temperature interlock on pour release",pfd="X-ray sampling, 1 per 50 castings",sev=8,occ=4,det=5,
  q="Is the die coating intact on both die halves?",problem="Ejector pin sticks on cavity 2 and the casting does not release",root="Ejector pin galled after die coating build-up",action="Ejector pin polished and die coat thickness corrected",cyc="95.0",setup=45,grain="Lot",optype="Casting",special="CQI-27"),
 dict(op="OP020|Heat treatment T6",wc="HT-01|T6 Heat Treatment Line",eq="HT-01-F1|T6 Solution and Ageing Furnace",eqt="HT-FURNACE|Heat Treatment Furnace",mfr="AFE|Aichelin Furnace Engineering",model="Drop bottom T6 line 1.5 t",line=1,area=1,item=3,comp=3,
  rcp="HT-T6-A356-02|T6 profile for A356 caliper body",rcptype="Furnace Profile",prog="T6-02",tool="BSK-HT-014|Heat treatment basket 14",tlt="BASKET|Furnace Basket",lifeuom="Cycles",lifelimit=1500,
  dev="TC-HT-01|Furnace temperature controller",dvt="TEMP-CTRL|Temperature Controller",skill="HT-OP|Heat treatment furnace operation",wi="Loading and T6 cycle - Caliper body castings",instr="Load castings in a single layer, bridge side up, and start profile T6-02",key="Quench delay from furnace door open to water must not exceed 15 seconds",
  char="Brinell hardness after T6",ctype="Product",cclass="Critical",nom="95.0",lsl="85.0",usl="105.0",uom=8,gauge="G-HT-001|Brinell hardness tester HBW 5/250",gty="HARDNESS|Hardness Tester",method="Brinell HBW 5/250 on the test pad",dp=1,
  tag="PN1.HT01.ZONE2_TEMP|Solution furnace zone 2 temperature",tuom=7,sp="535.0",lo="530.0",hi="540.0",
  defect="HT01|Hardness below specification",dgroup="HEAT|Heat Treatment",ddesc="Brinell hardness below 85 HBW after ageing",reason="ELEC-HT-01|Furnace zone heater failure",rcat=1,fault="F2203 Zone 2 heater current low",alarm="Solution furnace zone 2 temperature below low limit",
  pfn="Bring the casting to T6 temper",pfm="Hardness below 85 HBW",pfe="Caliper body deflects under pressure, pedal travel increases",pfc="Solution temperature below 530 degC",pfp="Zone temperature alarm with automatic cycle hold",pfd="Hardness test, 3 pieces per furnace charge",sev=9,occ=3,det=4,
  q="Is the quench water temperature between 60 and 80 degC?",problem="Zone 2 does not reach set temperature and the cycle is held",root="One heater element open circuit in zone 2",action="Heater element replaced and temperature uniformity survey repeated",cyc="28800.0",setup=20,grain="Lot",optype="Heat Treatment",special="CQI-9"),
 dict(op="OP030|CNC machining",wc="CNC-01|CNC Machining Cell 1",eq="CNC-01-H1|Horizontal Machining Center 1",eqt="HMC|CNC Machining Center",mfr="MAK|Makino",model="a61nx",line=2,area=2,item=2,comp=3,
  rcp="CNC-5110-20-0110-C|Caliper body LH machining program",rcptype="CNC Program",prog="O5110",tool="BOR-54-0031|Finish boring bar 54 mm",tlt="CUTTING|Cutting Tool",lifeuom="Pieces",lifelimit=400,
  dev="CNC-CTRL-01|CNC controller, machining center 1",dvt="CNC-CTRL|CNC Controller",skill="CNC-OP|CNC machining center operation",wi="Loading and bore machining - Caliper body LH",instr="Clean the fixture locators, load the casting against the stops and close the clamps",key="Blow off the locators at every load; a chip under the casting shifts the bore",
  char="Piston bore diameter",ctype="Product",cclass="Critical",nom="54.023",lsl="54.000",usl="54.046",uom=2,gauge="G-BG-054|Bore gauge 50-75 mm",gty="BORE-GAUGE|Bore Gauge",method="Two-point bore gauge at three depths",dp=3,
  tag="PN1.CNC01.COOLANT_PRESS|Through-spindle coolant pressure",tuom=5,sp="20.0",lo="15.0",hi="25.0",
  defect="MC01|Bore diameter oversize",dgroup="MACH|Machining",ddesc="Piston bore above 54.046 mm",reason="TOOL-CNC-01|Boring insert broken",rcat=2,fault="A3041 Tool load limit exceeded, T12",alarm="Through-spindle coolant pressure below low limit",
  pfn="Machine the piston bore to size and finish",pfm="Bore diameter oversize",pfe="Seal does not retract piston, brake drag or fluid leak",pfc="Boring insert worn beyond tool life",pfp="Tool life counter with forced insert change at 400 pieces",pfd="Bore gauge check every 2 hours with X-bar R chart",sev=9,occ=3,det=3,
  q="Is the tool life counter for the finish boring bar below 400 pieces?",problem="Finish boring insert broke and three bodies were machined with a rough bore",root="Insert ran 60 pieces past tool life after the counter was reset by mistake",action="Insert changed, counter reset locked with supervisor password",cyc="210.0",setup=35,grain="Lot",optype="Machining",special=None),
 dict(op="OP040|Washing",wc="WSH-01|Component Washing Station",eq="WSH-01-W1|Aqueous Spray Washer 1",eqt="WASHER|Washing Machine",mfr="DUR|Durr Ecoclean",model="EcoCWave",line=3,area=3,item=2,comp=2,
  rcp="WSH-ALU-03|Aluminium body wash program",rcptype="Washing Program",prog="W03",tool="FIX-WSH-006|Wash basket fixture 6",tlt="WASH-FIX|Wash Fixture",lifeuom="Cycles",lifelimit=20000,
  dev="EM-SF-01|Energy meter, surface treatment line",dvt="ENERGY-METER|Energy Meter",skill="WSH-OP|Washing machine operation",wi="Washing and drying - Caliper body LH",instr="Place bodies bore-down in the basket, one per pocket, and start program W03",key="Bore must face down so that chips drain out",
  char="Largest residual particle",ctype="Product",cclass="Significant",nom="300.0",lsl="0.0",usl="600.0",uom=3,gauge="G-PM-001|Particle analysis microscope",gty="MICROSCOPE|Microscope",method="Filter membrane analysis per cleanliness instruction",dp=1,
  tag="PN1.WSH01.BATH_TEMP|Wash bath temperature",tuom=7,sp="60.0",lo="55.0",hi="65.0",
  defect="WS01|Residual chips in bore",dgroup="CLEAN|Cleaning",ddesc="Metallic particle larger than 600 micrometres found in the bore",reason="PROC-WSH-01|Wash filter clogged",rcat=3,fault="W0412 Differential pressure across filter high",alarm="Wash bath temperature below low limit",
  pfn="Remove chips and coolant from the body",pfm="Chips remain in the piston bore",pfe="Seal damage at assembly, leak at leak test",pfc="Spray nozzle blocked",pfp="Filter differential pressure alarm",pfd="Cleanliness test, 1 body per shift",sev=7,occ=4,det=5,
  q="Is the filter differential pressure below 0.8 bar?",problem="Wash pressure drops during the cycle and bodies come out with chips",root="Bag filter not changed at the planned interval",action="Filter changed, change interval added to autonomous maintenance sheet",cyc="180.0",setup=10,grain="Lot",optype="Cleaning",special=None),
 dict(op="OP050|Anodising",wc="ANO-01|Anodising Line",eq="ANO-01-L1|Sulphuric Acid Anodising Line",eqt="ANODISING|Anodising Line",mfr="GAL|Galvatek",model="Hoist line 8 tanks",line=4,area=3,item=2,comp=2,
  rcp="ANO-SA-12UM|Sulphuric anodising 12 micrometre",rcptype="Anodising Program",prog="A12",tool="RCK-ANO-021|Titanium anodising rack 21",tlt="RACK|Anodising Rack",lifeuom="Cycles",lifelimit=3000,
  dev="RC-ANO-01|Rectifier controller, anodising tank",dvt="RECTIFIER|Rectifier Controller",skill="ANO-OP|Anodising line operation",wi="Racking and anodising - Caliper body LH",instr="Rack 24 bodies per flight bar with firm contact and start program A12",key="A loose contact burns the part; tug each body after racking",
  char="Anodic coating thickness",ctype="Product",cclass="Significant",nom="12.0",lsl="8.0",usl="16.0",uom=3,gauge="G-CT-002|Eddy current coating thickness tester",gty="COATING|Coating Thickness Tester",method="Eddy current, five points on the outer face",dp=1,
  tag="PN1.ANO01.BATH_TEMP|Anodising bath temperature",tuom=7,sp="20.0",lo="18.0",hi="22.0",
  defect="AN01|Coating thickness low",dgroup="SURF|Surface Treatment",ddesc="Anodic coating below 8 micrometres",reason="ELEC-ANO-01|Rectifier trip",rcat=1,fault="R0308 Rectifier over-temperature trip",alarm="Anodising bath temperature above high limit",
  pfn="Build a corrosion resistant anodic layer",pfm="Coating thickness below 8 micrometres",pfe="Corrosion in the field, customer appearance complaint",pfc="Current density too low for the load size",pfp="Recipe sets current by number of racks",pfd="Coating thickness, 5 bodies per load",sev=6,occ=3,det=4,
  q="Is the anodising bath temperature between 18 and 22 degC?",problem="Rectifier trips in the middle of the anodising step",root="Cooling fan of the rectifier cabinet failed",action="Fan replaced, cabinet temperature added to daily check",cyc="3600.0",setup=15,grain="Lot",optype="Surface Treatment",special="CQI-11"),
 dict(op="OP060|Piston and seal assembly",wc="ASY-01|Piston and Seal Assembly Station",eq="ASY-01-P1|Piston Assembly Press 1",eqt="PRESS|Assembly Press",mfr="PRO|Promess",model="EMAP 5 kN",line=5,area=4,item=0,comp=4,
  rcp="ASY-PST-54|Piston insertion 54 mm",rcptype="Press Program",prog="P54",tool="SLV-54-0008|Seal insertion sleeve 54 mm",tlt="SLEEVE|Assembly Sleeve",lifeuom="Cycles",lifelimit=50000,
  dev="PR-CTRL-01|Press controller, assembly station 1",dvt="PRESS-CTRL|Press Controller",skill="ASY-OP|Piston and seal assembly",wi="Seal, piston and dust boot assembly - Front caliper LH",instr="Fit the seal in the groove without twist, wet with assembly fluid and press the piston home",key="Seal must sit flat in the groove before the piston is pressed",
  char="Dust boot seating height",ctype="Product",cclass="Significant",nom="3.00",lsl="2.70",usl="3.30",uom=2,gauge="G-HG-003|Digital height gauge 0-300 mm",gty="HEIGHT|Height Gauge",method="Height gauge from the bore face to the boot lip",dp=2,
  tag="PN1.ASY01.PRESS_POSITION|Press stroke end position",tuom=2,sp="42.0",lo="41.5",hi="42.5",
  defect="AS01|Seal twisted or cut",dgroup="ASSY|Assembly",ddesc="Piston seal twisted in the groove or cut at insertion",reason="MATL-ASY-01|Seal feeder jam",rcat=4,fault="P0115 Press force outside window at 30 mm",alarm="Press stroke end position below low limit",
  pfn="Seal the piston to the bore",pfm="Seal cut during piston insertion",pfe="External brake fluid leak, reduced braking performance",pfc="Burr on the seal groove edge",pfp="Force-displacement window on the press",pfd="100 percent pressure leak test at 5 bar and 140 bar",sev=10,occ=3,det=2,
  q="Is the assembly fluid level above the minimum mark?",problem="Seal feeder jams every few cycles and the operator fits seals by hand",root="Seal lot with flash on the outer diameter",action="Seal lot segregated and returned, feeder track cleaned",cyc="32.0",setup=15,grain="Unit",optype="Assembly",special=None),
 dict(op="OP070|Bleed screw torque",wc="TRQ-01|Bleed Screw Torque Station",eq="TRQ-01-N1|DC Nutrunner Station 1",eqt="NUTRUNNER|DC Nutrunner",mfr="ATC|Atlas Copco",model="Power Focus 6000 with ETV STR61",line=5,area=4,item=0,comp=7,
  rcp="TRQ-PSET-07|Bleed screw M10 torque program",rcptype="Tightening Program",prog="PSET-07",tool="SKT-10-0007|Nutrunner socket 10 mm, station 1",tlt="SOCKET|Nutrunner Socket",lifeuom="Cycles",lifelimit=100000,
  dev="NR-CTRL-01|Nutrunner controller, torque station 1",dvt="NR-CTRL|Nutrunner Controller",skill="TRQ-OP|DC nutrunner operation",wi="Bleed screw tightening - Front caliper LH",instr="Start the bleed screw two turns by hand, place the socket and press both start buttons",key="Bleed screw seat must be dry and free of chips",
  char="Bleed screw tightening torque",ctype="Process",cclass="Critical",nom="14.0",lsl="12.0",usl="16.0",uom=4,gauge="G-TA-001|Torque analyser 2-25 N.m",gty="TORQUE|Torque Analyser",method="Dynamic torque from the nutrunner transducer",dp=1,
  tag="PN1.TRQ01.FINAL_TORQUE|Final torque, nutrunner station 1",tuom=4,sp="14.0",lo="12.0",hi="16.0",
  defect="TQ01|Torque below minimum",dgroup="TORQ|Torque",ddesc="Final torque below 12 N.m or angle outside window",reason="TOOL-TRQ-01|Nutrunner socket worn",rcat=2,fault="E4107 Rundown torque not reached, spindle 1",alarm="Final torque below low limit on three consecutive cycles",
  pfn="Close the bleed port with the specified clamp load",pfm="Bleed screw under-torqued",pfe="Fluid seepage at the bleed screw, soft pedal",pfc="Worn socket slips on the hexagon",pfp="Socket change by cycle counter",pfd="100 percent torque and angle monitoring by the controller",sev=9,occ=2,det=2,
  q="Does the torque analyser read within 0.3 N.m of the controller on the check joint?",problem="Nutrunner stops with rundown torque not reached on every third cycle",root="Socket drive worn beyond limit",action="Socket replaced and verified with the torque analyser",cyc="18.0",setup=10,grain="Unit",optype="Assembly",special=None),
 dict(op="OP080|Pressure leak test",wc="LKT-01|Pressure Leak Test Station",eq="LKT-01-T1|Pressure Leak Tester 1",eqt="LEAK-TESTER|Leak Tester",mfr="ATQ|ATEQ",model="F620 with 160 bar booster",line=5,area=4,item=0,comp=0,
  rcp="LKT-PRG-03|Caliper leak test 5 bar and 140 bar",rcptype="Leak Test Program",prog="LT-03",tool="TSL-54-0003|Test seal set, piston bore 54 mm",tlt="TEST-SEAL|Test Seal",lifeuom="Cycles",lifelimit=25000,
  dev="LKT-CTRL-01|Leak tester controller 1",dvt="LEAK-CTRL|Leak Tester",skill="LEAK-TEST-OP|Leak test operation",wi="Pressure leak test - Front caliper LH",instr="Clamp the caliper in the nest, connect the inlet adaptor and start program LT-03",key="A failed part goes to the red bin at once; never retest without the line leader",
  char="Pressure drop at 140 bar",ctype="Product",cclass="Critical",nom="20.0",lsl="0.0",usl="50.0",uom=6,gauge="G-PC-001|Pressure calibrator 0-200 bar",gty="PRESSURE|Pressure Calibrator",method="Pressure decay over 5 seconds after stabilisation",dp=1,
  tag="PN1.LKT01.TEST_PRESSURE|High-pressure stage test pressure",tuom=5,sp="140.0",lo="138.0",hi="142.0",
  defect="LK01|Leak at piston seal",dgroup="LEAK|Leak",ddesc="Pressure decay above limit traced to the piston seal",reason="TOOL-LKT-01|Test seal worn",rcat=2,fault="T0221 Fill pressure not reached",alarm="High-pressure stage test pressure below low limit",
  pfn="Detect any leak path before dispatch",pfm="Leaking caliper passed as good",pfe="Brake fluid loss in the vehicle, safety recall",pfc="Tester not verified with the master leak",pfp="Master leak verification at start of every shift",pfd="Master leak part must fail before production is released",sev=10,occ=2,det=2,
  q="Is the master leak part detected as Not OK by the tester?",problem="Tester rejects good parts with fill pressure not reached",root="Inlet test seal worn and leaking",action="Test seal set replaced, tester verified with the master leak",cyc="24.0",setup=10,grain="Unit",optype="Test",special=None),
 dict(op="OP090|Laser marking",wc="LSR-01|Laser Marking Station",eq="LSR-01-L1|Fibre Laser Marker 1",eqt="LASER|Laser Marker",mfr="TRU|Trumpf",model="TruMark 5020",line=5,area=4,item=0,comp=0,
  rcp="LSR-DM-5110|Serial and 2D code layout, front caliper",rcptype="Laser Marking Program",prog="DM-5110",tool="FIX-LSR-002|Marking nest, front caliper",tlt="MARK-FIX|Marking Fixture",lifeuom="Cycles",lifelimit=200000,
  dev="LSR-CTRL-01|Laser marker controller 1",dvt="LASER-CTRL|Laser Marker Controller",skill="LSR-OP|Laser marking operation",wi="Serial and 2D code marking - Front caliper LH",instr="Seat the caliper in the nest, close the safety door and start marking",key="Marking area must be dry; fluid residue gives a low-contrast code",
  char="Laser mark depth",ctype="Product",cclass="Standard",nom="50.0",lsl="30.0",usl="80.0",uom=3,gauge="G-DM-001|Depth micrometer 0-25 mm",gty="DEPTH|Depth Gauge",method="Depth micrometer on the first character",dp=1,
  tag="PN1.LSR01.HEAD_TEMP|Marking head temperature",tuom=7,sp="32.0",lo="20.0",hi="45.0",
  defect="LM01|2D code unreadable",dgroup="MARK|Marking",ddesc="Data matrix grade below C or code not readable",reason="PROC-LSR-01|Marking lens contaminated",rcat=3,fault="L0507 Verification grade below limit",alarm="Marking head temperature above high limit",
  pfn="Mark a unique serial number and 2D code",pfm="2D code not readable",pfe="Traceability lost at the customer line, line rejection",pfc="Protective lens contaminated",pfp="Lens cleaning in autonomous maintenance",pfd="In-line code verification after marking",sev=7,occ=3,det=2,
  q="Is the protective lens clean and free of spatter?",problem="Verification grade drops to D and parts are rejected at the reader",root="Protective lens contaminated with assembly fluid mist",action="Lens cleaned and extraction duct repositioned",cyc="14.0",setup=10,grain="Unit",optype="Marking",special=None),
 dict(op="OP100|Final inspection",wc="FIN-01|Final Inspection and Packing Cell",eq="FIN-01-V1|Final Inspection Vision Station",eqt="VISION|Vision Inspection Station",mfr="KEY|Keyence",model="XG-X2800",line=6,area=5,item=0,comp=0,
  rcp="FIN-VIS-5110|Final inspection vision job, front caliper",rcptype="Vision Job",prog="VJ-11",tool="FIX-FIN-001|Final inspection fixture, front caliper",tlt="INSP-FIX|Inspection Fixture",lifeuom="Cycles",lifelimit=300000,
  dev="PRN-FIN-01|Label printer, packing station",dvt="PRINTER|Label Printer",skill="FIN-INSP|Final inspection and packing",wi="Final inspection and packing - Front caliper LH",instr="Check boot seating, bleed screw cap and marking, then place the caliper in the tray pocket",key="Every caliper must carry a bleed screw cap before it enters the bin",
  char="Mounting hole pitch",ctype="Product",cclass="Significant",nom="142.00",lsl="141.85",usl="142.15",uom=2,gauge="G-CMM-001|Coordinate measuring machine",gty="CMM|Coordinate Measuring Machine",method="CMM program FBC-LH-01",dp=2,
  tag="PN1.FIN01.AIR_PRESSURE|Inspection cell air pressure",tuom=5,sp="6.0",lo="5.5",hi="6.5",
  defect="FI01|Bleed screw cap missing",dgroup="FINAL|Final Inspection",ddesc="Bleed screw cap not fitted",reason="ELEC-FIN-01|Vision camera fault",rcat=1,fault="V0102 Camera 2 image acquisition timeout",alarm="Inspection cell air pressure below low limit",
  pfn="Confirm the caliper is complete before packing",pfm="Bleed screw cap missing",pfe="Dirt enters the bleed port, customer line rejection",pfc="Cap presence not checked by the vision job",pfp="Cap feeder with presence sensor",pfd="Vision check of cap presence on every caliper",sev=6,occ=3,det=3,
  q="Does the vision station reject the caliper with the missing cap from the challenge set?",problem="Camera 2 times out and the station stops",root="Camera cable damaged by the fixture clamp",action="Cable replaced and rerouted in a drag chain",cyc="20.0",setup=10,grain="Unit",optype="Inspection",special=None),
]
def rows(t): return [l for l in t.strip().split("\n")]
# code|name per master entity (10 each). The name feeds the display field (name / title / description / fullName).
MASTER={k:rows(v) for k,v in {
"enterprise":"""VBS|Varuna Brake Systems Pvt. Ltd.
VIG|Varuna Industries Group Ltd.
VCS|Varuna Castings Pvt. Ltd.
VFS|Varuna Friction Systems Pvt. Ltd.
VPS|Varuna Precision Seals Pvt. Ltd.
VAL|Varuna Aluminium Ltd.
VTC|Varuna Technical Centre Pvt. Ltd.
VLS|Varuna Logistics Services Pvt. Ltd.
VNJ|Varuna Nisshin Brake JV Pvt. Ltd.
VEX|Varuna Brake Exports Pvt. Ltd.""",
"site":"""PN1|Chakan Plant, Pune
PN2|Ranjangaon Machining Plant, Pune
TN1|Oragadam Plant, Chennai
GJ1|Sanand Plant, Ahmedabad
HR1|Manesar Plant, Gurugram
UK1|Pantnagar Plant, Rudrapur
KA1|Narasapura Plant, Kolar
WH1|Talegaon Finished Goods Warehouse
TC1|Pune Technical Centre
HO1|Corporate Office, Pune""",
"area":"""FDY|Foundry
HT|Heat Treatment
MC|Machining
SF|Surface Treatment
ASY|Assembly and Test
FIP|Final Inspection and Packing
WH|Stores and Dispatch
QL|Quality Laboratory
TR|Tool Room
UT|Utilities""",
"line":"""GDC-01|Gravity Die Casting Line 1
HT-01|T6 Heat Treatment Line 1
MC-01|Caliper Body Machining Line 1
WSH-01|Washing Line 1
ANO-01|Anodising Line 1
ASY-01|Front Caliper Assembly Line 1
FIP-01|Final Inspection and Packing Line 1
GDC-02|Gravity Die Casting Line 2
MC-02|Caliper Body Machining Line 2
ASY-02|Rear Caliper Assembly Line 1""",
"shift":"""A|Shift A
B|Shift B
C|Shift C
G|General Shift
A-SAT|Shift A Saturday
B-SAT|Shift B Saturday
M1|Maintenance Shift Day
M2|Maintenance Shift Night
OT-A|Overtime Extension A
OT-B|Overtime Extension B""",
"workCalendar":"""PN1-2026|Chakan Plant Calendar 2026
PN1-2026-FDY|Foundry Continuous Calendar 2026
PN1-2026-HT|Heat Treatment Continuous Calendar 2026
PN1-2026-MC|Machining Calendar 2026
PN1-2026-SF|Surface Treatment Calendar 2026
PN1-2026-ASY|Assembly Calendar 2026
PN1-2026-FIP|Final Inspection and Packing Calendar 2026
PN1-2026-WH|Stores and Dispatch Calendar 2026
PN1-2026-MNT|Maintenance Calendar 2026
PN1-2027|Chakan Plant Calendar 2027""",
"role":"""OPERATOR|Production Operator
SETTER|Machine Setter
LINE-LEADER|Line Leader
SUPERVISOR|Production Supervisor
QUALITY-INSP|Quality Inspector
QUALITY-ENG|Quality Engineer
MAINT-TECH|Maintenance Technician
STORES|Stores Operator
PROCESS-ENG|Process Engineer
ADMIN|System Administrator""",
"user":"""10231|Sunil Jadhav
10344|Kavita Bhosale
10402|Deepak Gaikwad
10087|Anita Kulkarni
10045|Rajesh Patil
10112|Imran Shaikh
10019|Meera Deshpande
10150|Vikram Pawar
10066|Sneha Joshi
SYSTEM|MES System""",
"customer":"""SML|Sahyadri Motors Ltd.
KAL|Konkan Automotive Ltd.
DMC|Deccan Motor Company
NEV|Narmada Electric Vehicles Pvt. Ltd.
GUV|Godavari Utility Vehicles Ltd.
ABS|Aravalli Brake Systems Ltd.
VAM|Vindhya Aftermarket Parts Pvt. Ltd.
SMX|Sahyadri Motors Exports
KCV|Kaveri Commercial Vehicles Ltd.
TMS|Tapti Mobility Solutions Pvt. Ltd.""",
"supplier":"""S1042|Konkan Precision Pistons Pvt. Ltd.
S1077|Elastoseal Rubber Products Pvt. Ltd.
S1103|Bharat Fasteners and Fittings Ltd.
S1018|Western Aluminium Alloys Ltd.
S1156|Shivneri Guide Pin Industries
S1201|Precision Dies and Moulds Pvt. Ltd.
S1230|Maharashtra Calibration Laboratory
S1264|Indus Cutting Tools Pvt. Ltd.
S1299|Pack-Well Returnable Packaging Pvt. Ltd.
S1311|Sahyog Manpower Services""",
"unitOfMeasure":"""EA|Each
KG|Kilogram
MM|Millimetre
UM|Micrometre
NM|Newton metre
BAR|Bar
PA|Pascal
DEGC|Degree Celsius
HBW|Brinell hardness
KWH|Kilowatt hour""",
"item":"""5110-10-0100|Front Brake Caliper Assembly, LH
5110-10-0200|Front Brake Caliper Assembly, RH
5110-20-0110|Caliper Body, LH, machined and anodised
5110-20-0105|Caliper Body Casting, LH, T6
5110-30-0010|Piston, dia 54 mm, steel, chrome plated
5110-30-0020|Piston Seal, square section, EPDM
5110-30-0030|Dust Boot, EPDM
5110-30-0040|Bleed Screw M10 x 1.0 with cap
5110-30-0050|Guide Pin with boot
RM-A356|Aluminium alloy ingot AlSi7Mg0.3 (A356)""",
"productVariant":"""FBC-LH-STD|Front Caliper LH, Standard
FBC-RH-STD|Front Caliper RH, Standard
FBC-LH-EXP|Front Caliper LH, Export
FBC-RH-EXP|Front Caliper RH, Export
FBC-LH-BLK|Front Caliper LH, Black Anodised
FBC-RH-BLK|Front Caliper RH, Black Anodised
FBC-LH-LM|Front Caliper LH, Low-Metallic Pad
FBC-RH-LM|Front Caliper RH, Low-Metallic Pad
FBC-LH-AM|Front Caliper LH, Aftermarket
FBC-RH-AM|Front Caliper RH, Aftermarket""",
"routing":"""5110-10-0100-R01|Front caliper LH, full process routing
5110-10-0200-R01|Front caliper RH, full process routing
5110-20-0110-R01|Caliper body LH, machining to anodising
5110-20-0105-R01|Caliper body casting LH, casting and T6
5110-10-0100-RW1|Front caliper LH, seal replacement rework
5110-10-0100-RW2|Front caliper LH, bleed screw retighten rework
5110-20-0110-RW1|Caliper body LH, re-anodise rework
5110-10-0100-R02|Front caliper LH, alternate routing via assembly line 2
5110-10-0100-RW3|Front caliper LH, re-mark rework
5110-10-0100-PT1|Front caliper LH, PPAP trial routing""",
"engineeringChange":"""Bleed screw torque window revised to 14 +/- 2 N.m
Piston seal material changed to EPDM grade E70
Anodising thickness tolerance widened to 8-16 micrometres
Second source approved for guide pins
Laser mark layout changed to include plant code
Casting die 2 gate geometry modified
Leak test high-pressure stage raised to 140 bar
Dust boot supplier changed
Packing quantity changed from 20 to 24 per bin
Work instruction pictures updated for RH variant""",
"storageLocation":"""WH-RM-01|Raw material yard, ingot bay
WH-A-R02-B14|Warehouse A, rack 02, bin 14
WH-A-R05-B03|Warehouse A, rack 05, bin 03
LS-FDY-01|Line-side store, foundry
LS-MC-01|Line-side supermarket, machining
LS-ASY-01|Line-side supermarket, assembly 1
QA-CAGE-01|Quarantine cage, quality
FG-R01|Finished goods rack 01
DSP-BAY-01|Dispatch bay 1
SCRAP-YD-01|Scrap yard, aluminium""",
"labelTemplate":"""SML-BIN-A5|Sahyadri Motors bin label A5
SML-SHIP-A4|Sahyadri Motors shipping label A4
UNIT-DM-12|Unit data matrix mark 12 x 12 mm
WIP-LOT-A6|WIP lot tag A6
HOLD-RED-A6|Quality hold tag, red
KAL-BIN-A5|Konkan Automotive bin label A5
LOC-RACK-100|Location label 100 x 50 mm
REWORK-YEL-A6|Rework tag, yellow
SCRAP-RED-A6|Scrap tag, red
GRN-LOT-A6|Goods receipt lot label A6""",
"samplingPlan":"""AQL-1.0-II|AQL 1.0, general inspection level II
AQL-0.65-II|AQL 0.65, general inspection level II
AQL-0.25-S3|AQL 0.25, special level S-3
C0-CRIT|Zero acceptance, critical characteristics
FIX-5-2H|Fixed sample of 5 every 2 hours
FIX-3-CHG|Fixed sample of 3 per furnace charge
FULL-100|100 percent inspection
SKIP-5|Skip lot after 5 accepted lots
FIRST-OFF-3|First-off, 3 pieces
DOCK-13|Dock audit, 13 pieces per shipment""",
"sparePart":"""SP-004417|Socket 10 mm, 3/8 inch drive, for bleed screw nutrunner
SP-002108|Heater element 6 kW, solution furnace
SP-003355|Boring insert CCGT 09T304, PCD
SP-001920|Bag filter 50 micrometre, washer
SP-005012|Cooling fan 230 V, rectifier cabinet
SP-004630|Test seal set, 54 mm bore, leak tester
SP-006201|Protective lens, laser marker
SP-006744|Camera cable 5 m, vision station
SP-001033|Ejector pin dia 8 x 200 mm, die 2
SP-003901|Servo drive, assembly press""",
"integrationConnector":"""ERP-PRD|ERP production interface
PLM-PRD|PLM engineering data interface
OPC-FDY|OPC UA server, foundry
OPC-MC|OPC UA server, machining
OP-TRQ|Open Protocol link, nutrunner controllers
LKT-TCP|Leak tester result interface
ZPL-PRN|Label printer interface
MQTT-EM|Energy meter MQTT broker
SMTP-NTF|Notification e-mail gateway
ERP-QAS|ERP quality system interface""",
"numberRange":"""SERIAL-FBC-LH|Serial numbers, front caliper LH
SERIAL-FBC-RH|Serial numbers, front caliper RH
LOT-CAST|Casting lot numbers
LOT-HT|Heat treatment charge numbers
PROD-ORDER|Production order numbers
NCR|Nonconformance report numbers
LABEL|Label numbers
GRN|Goods receipt numbers
SHIPMENT|Shipment numbers
WIP-UNIT|WIP unit numbers""",
"systemConfiguration":"""oee.plannedTimeBasis|Time basis used as the denominator of availability
spc.rules|SPC rules applied to control charts
label.defaultPrinter|Default label printer of the packing station
leakTest.maxRetests|Maximum number of leak retests per unit
torque.maxAttempts|Maximum tightening attempts per joint
andon.escalationMinutes|Minutes before an unacknowledged andon call is escalated
session.timeoutMinutes|Operator session timeout
trace.retentionYears|Retention period of traceability records
calibration.blockOverdue|Block the use of gauges with overdue calibration
erp.retryIntervalSeconds|Interval between retries of failed ERP messages""",
"department":"""PROD|Production
QUAL|Quality
MAINT|Maintenance
STORES|Stores and Logistics
ENGG|Process Engineering
PLAN|Production Planning
TOOL|Tool Room
EHS|Environment Health and Safety
IT|Information Technology
HR|Human Resources""",
"designation":"""ASM-OPR|Assembly Operator
FDY-OPR|Foundry Operator
CNC-OPR|CNC Operator
QA-ENG|Quality Engineer
PRD-SUP|Production Supervisor
MNT-TECH|Maintenance Technician
QA-MGR|Quality Manager
STR-OPR|Stores Operator
PRC-ENG|Process Engineer
SYS-ACC|System Account""",
"employmentType":"""PERM|Permanent
CONTRACT|Contract
TRAINEE|Trainee
APPRENTICE|Apprentice
PROBATION|On Probation
FIXED|Fixed Term
CONSULT|Consultant
INTERN|Intern
DEPUTED|Deputed From Group Company
SYSTEM|System Account""",
"costCenter":"""5010|Foundry
5020|Heat Treatment
5030|Machining
5040|Surface Treatment
5120|Assembly and Test
5130|Final Inspection and Packing
5210|Stores and Dispatch
5310|Quality Laboratory
5410|Tool Room
5510|Utilities""",
"skillCategory":"""PROCESS|Process
QUALITY|Quality
MAINT|Maintenance
SAFETY|Safety
MATL|Material Handling
SETUP|Setting and Changeover
TEST|Testing
SPECIAL|Special Process
SUPERV|Supervision
SYSTEM|System Use""",
"permission":"""operationExecution.start|Start an operation
operationExecution.complete|Complete an operation
nonconformance.create|Raise a nonconformance
nonconformance.disposition|Disposition nonconforming material
qualityHold.release|Release a quality hold
recipe.approve|Approve a recipe
productionOrder.release|Release a production order
maintenanceWorkOrder.close|Close a maintenance work order
materialMovement.post|Post a stock movement
user.administer|Administer users and roles""",
"signatureMeaning":"""APPROVED|Approved
REVIEWED|Reviewed
RELEASED|Released
VERIFIED|Verified
REJECTED|Rejected
AUTHORED|Authored
WITNESSED|Witnessed
ACKNOWLEDGED|Acknowledged
DISPOSITIONED|Dispositioned
CLOSED|Closed""",
"currency":"""INR|Indian Rupee
USD|US Dollar
EUR|Euro
JPY|Japanese Yen
GBP|Pound Sterling
CNY|Chinese Yuan
KRW|South Korean Won
THB|Thai Baht
AED|UAE Dirham
SGD|Singapore Dollar""",
"country":"""IN|India
DE|Germany
JP|Japan
US|United States
CN|China
KR|South Korea
TH|Thailand
IT|Italy
SE|Sweden
GB|United Kingdom""",
"language":"""en|English
mr|Marathi
hi|Hindi
ta|Tamil
gu|Gujarati
kn|Kannada
de|German
ja|Japanese
te|Telugu
bn|Bengali""",
"transporter":"""DRC|Deccan Road Carriers
SLG|Sahyadri Logistics
MHT|Maharashtra Highway Transport
KFL|Konkan Freight Lines
PXL|Pune Express Logistics
WGC|Western Ghats Cargo
BRT|Bharat Road Transport
SVL|Shivneri Lines
NTC|National Transport Corporation
TCL|TransCargo Logistics""",
"commodity":"""MACH-STEEL|Machined Steel Parts
RUBBER|Rubber Mouldings
FASTENER|Fasteners and Fittings
AL-ALLOY|Aluminium Alloys
GUIDE-PIN|Guide Pins and Bushes
TOOLING|Dies and Tooling
CALIB|Calibration Services
CUT-TOOL|Cutting Tools
PACKAGING|Returnable Packaging
MANPOWER|Contract Manpower""",
"itemGroup":"""CALIPER|Brake Caliper Assembly
BODY|Caliper Body
CASTING|Aluminium Casting
PISTON|Piston
SEAL|Seal
BOOT|Dust Boot
FASTENER|Fastener
GUIDE-PIN|Guide Pin
RAW-ALU|Raw Aluminium
PACK|Packaging""",
"itemFamily":"""FRONT-CALIPER|Front Caliper
REAR-CALIPER|Rear Caliper
CALIPER-BODY|Caliper Body
BODY-CASTING|Caliper Body Casting
BRACKET|Caliper Bracket
EPB-CALIPER|Electric Parking Brake Caliper
MASTER-CYL|Master Cylinder
WHEEL-CYL|Wheel Cylinder
KNUCKLE|Steering Knuckle
SERVICE-KIT|Service Kit""",
"ppeItem":"""SAFETY-GLASSES|Safety Glasses
SAFETY-SHOES|Safety Shoes
CUT-GLOVES|Cut Resistant Gloves
EAR-PLUGS|Ear Plugs
HEAT-GLOVES|Heat Resistant Gloves
FACE-SHIELD|Face Shield
APRON|Aluminised Apron
ACID-GLOVES|Acid Resistant Gloves
RESPIRATOR|Half Mask Respirator
LASER-GLASSES|Laser Safety Glasses""",
"market":"""DOM|Domestic
EXP-EU|Export Europe
EXP-ASEAN|Export ASEAN
EXP-MEA|Export Middle East and Africa
EXP-LATAM|Export Latin America
AM-DOM|Aftermarket Domestic
AM-EXP|Aftermarket Export
EXP-JP|Export Japan
EXP-UK|Export United Kingdom
EXP-SAARC|Export SAARC""",
"padCompound":"""NAO-CER|NAO Ceramic
LOW-MET|Low-Metallic
SEMI-MET|Semi-Metallic
NAO-ORG|NAO Organic
CER-PREM|Premium Ceramic
LOW-MET-EU|Low-Metallic ECE R90
CU-FREE|Copper-Free NAO
HD-SEMI|Heavy Duty Semi-Metallic
EV-LOWDUST|EV Low-Dust
AM-STD|Aftermarket Standard""",
"surfaceFinish":"""ANOD-NAT|Anodised Natural
ANOD-BLK|Anodised Black
ANOD-GRY|Anodised Grey
PAINT-RED|Painted Red
PAINT-BLK|Painted Black
PAINT-SIL|Painted Silver
ZN-NI|Zinc-Nickel Plated
E-COAT|Cathodic E-Coat
AS-MACH|As Machined
POWDER-YEL|Powder Coated Yellow""",
"vehicleModel":"""SM-X42|Sahyadri X42 Hatchback
SM-X45|Sahyadri X45 Sedan
SM-U60|Sahyadri U60 Utility
KA-K21|Konkan K21 Compact
KA-K33|Konkan K33 Crossover
DM-D7|Deccan D7 Sedan
NE-E1|Narmada E1 Electric
GU-G9|Godavari G9 Pickup
KC-L5|Kaveri L5 Light Truck
TM-T2|Tapti T2 City Car""",
"indirectActivity":"""WAIT-MAT|Waiting For Material
WAIT-MNT|Waiting For Maintenance
CLEAN|Cleaning and 5S
TRAIN|Training
MEET|Shift Meeting
CHG-OVER|Changeover Support
REWORK-SUP|Rework Support
QC-SORT|Sorting For Quality
KAIZEN|Kaizen Activity
STOCK-COUNT|Stock Count""",
"containerType":"""RB-6040|Returnable Bin 600 x 400
RB-4030|Returnable Bin 400 x 300
TRL-CAST|Casting Trolley
BSK-HT|Heat Treatment Basket
RCK-ANO|Anodising Rack
PLT-1210|Pallet 1200 x 1000
BOX-CORR|Corrugated Box Export
TRAY-8|Moulded Tray 8 Pockets
CAGE-SCRAP|Scrap Cage
BIN-RED|Red Reject Bin""",
"movementType":"""GR-PO|Goods Receipt Against Purchase Order
PUTAWAY|Putaway To Rack
ISSUE-LINE|Issue To Line
RETURN-LINE|Return From Line
TRANSFER|Location Transfer
SCRAP|Scrap Posting
GR-PROD|Finished Goods Receipt From Production
SHIP|Goods Issue For Shipment
ADJUST|Stock Adjustment
TO-QUAR|Transfer To Quarantine""",
"stockStatus":"""UNR|Unrestricted
QI|Quality Inspection
BLK|Blocked
RES|Reserved
RET|Returns
TRN|In Transit
RWK|Under Rework
CUS|Customer Consignment
SUB|At Subcontractor
SCR|Scrap Pending Disposal""",
"packType":"""BAG|VCI Bag
TRAY|Tray
BIN|Bin
PALLET|Pallet
LAYER|Layer Pad
BOX|Box
CRATE|Crate
SLEEVE|Sleeve
LID|Lid
STRAP|Strapped Load""",
"dispositionType":"""USE-AS-IS|Use As Is
REWORK|Rework
SCRAP|Scrap
RTS|Return To Supplier
SORT|Sort
REGRADE|Regrade
REPAIR|Repair
HOLD|Hold For Decision
DEVIATION|Use Under Deviation
RETEST|Retest""",
"complaintType":"""LINE-REJ|Line Rejection
ZERO-KM|Zero Kilometre
WARRANTY|Warranty
LOGISTICS|Logistics
LABEL|Labelling Error
MIXED|Mixed Parts
SHORT|Short Supply
PACK|Packaging Damage
DOC|Documentation Error
AUDIT|Customer Audit Finding""",
"lossCategory":"""BREAKDOWN|Breakdown
SETUP|Setup And Adjustment
MINOR-STOP|Minor Stop
SPEED|Reduced Speed
STARTUP|Startup Reject
REJECT|Production Reject
PLAN-MNT|Planned Maintenance
BREAK|Planned Break
NO-DEMAND|No Demand
MAT-SHORT|Material Shortage""",
"reasonCategory":"""MECH|Mechanical
ELEC|Electrical
TOOL|Tooling
PROC|Process
MATL|Material
QUAL|Quality
UTIL|Utilities
ORG|Organisation
CHG|Changeover
PLAN|Planned""",
"documentType":"""DRAWING|Drawing
WI-MEDIA|Work Instruction Media
CERT|Material Certificate
INSP-RPT|Inspection Report
PHOTO|Photo
CAL-CERT|Calibration Certificate
CUST-SPEC|Customer Specification
CURVE|Tightening Curve
PPAP|PPAP Element
TRAINING|Training Record""",
"notificationType":"""ANDON-ESC|Andon Escalation
QUAL-ALERT|Quality Alert
MNT-DUE|Maintenance Due
CAL-DUE|Calibration Due
ORDER-LATE|Order Late
IF-FAIL|Interface Failure
CERT-EXP|Certification Expiring
TOOL-LIFE|Tool Life Warning
HOLD-PLACED|Quality Hold Placed
SPC-VIOL|SPC Rule Violation""",
"andonType":"""QUALITY|Quality
MATERIAL|Material
MAINT|Maintenance
SAFETY|Safety
SUPERV|Supervisor
TOOLING|Tooling
PROCESS|Process Engineering
IT|IT Support
FIRST-OFF|First-Off Approval
LOGISTICS|Logistics""",
"incidentType":"""NEAR-MISS|Near Miss
UNSAFE-COND|Unsafe Condition
UNSAFE-ACT|Unsafe Act
FIRST-AID|First Aid Case
MED-TREAT|Medical Treatment Case
LTI|Lost Time Injury
PROPERTY|Property Damage
FIRE|Fire Incident
SPILL|Chemical Spill
ENVIRON|Environmental Release""",
"energyType":"""ELEC|Electricity
AIR|Compressed Air
GAS|Natural Gas
WATER|Process Water
DM-WATER|Demineralised Water
LPG|LPG
STEAM|Steam
CHILLED|Chilled Water
N2|Nitrogen
DIESEL|Diesel For Generator""",
"bodyPart":"""HAND|Hand
FINGER|Finger
EYE|Eye
FOOT|Foot
BACK|Back
ARM|Arm
LEG|Leg
HEAD|Head
SHOULDER|Shoulder
KNEE|Knee""",
"injuryType":"""CUT|Cut
BURN|Burn
BRUISE|Bruise
SPRAIN|Sprain
FRACTURE|Fracture
EYE-IRR|Eye Irritation
CHEM-BURN|Chemical Burn
CRUSH|Crush Injury
SLIP|Slip Or Fall Injury
ELEC-SHOCK|Electric Shock""",
}.items()}
# display texts for transaction entities whose display field is a title / description (10 each)
TITLES={k:rows(v) for k,v in {
"nonconformance":"""Shrinkage porosity found on casting lot from die 2
Hardness below 85 HBW on furnace charge HT-260917-02
Piston bore oversize after insert breakage
Residual chips found in bore at cleanliness test
Anodic coating below 8 micrometres on load AN-260918-01
Seal cut at piston insertion, supplier lot ES-260905-11
Bleed screw torque below minimum on three units
Leak test failures on caliper LH at 140 bar stage
2D code unreadable after lens contamination
Bleed screw cap missing at final inspection""",
"capa":"""8D - Shrinkage porosity in bridge section
8D - Low hardness after T6
8D - Piston bore oversize
8D - Residual chips after washing
8D - Low anodic coating thickness
8D - Seal cut at assembly
8D - Bleed screw under-torque
8D - Leak at piston seal
8D - Unreadable 2D code
8D - Bleed screw cap missing at customer line""",
"deviationPermit":"""Wall thickness 7.4 mm accepted on 500 castings
Hardness 83-85 HBW accepted on one furnace charge
Bore diameter up to 54.050 mm accepted on 120 bodies
Cleanliness limit 700 micrometres for trial lot
Anodising thickness upper limit 16.5 micrometres
Dust boot seating height 3.35 mm accepted on 300 units
Bleed screw torque 12.0-16.5 N.m during socket trial
Leak test stabilisation time reduced to 3.5 seconds for trial
Mark depth 25 micrometres accepted on 200 units
Mounting hole pitch 142.18 mm accepted on PPAP samples""",
"audit":"""Layered process audit, foundry, week 38
Special process audit CQI-9, heat treatment
Process audit VDA 6.3, machining line 1
Layered process audit, washing, week 38
Special process audit CQI-11, anodising
Layered process audit, assembly line 1, week 39
Product audit, front caliper LH, September
Layered process audit, leak test station, week 39
Customer process audit, Sahyadri Motors
IATF 16949 internal system audit, quality management""",
"customerComplaint":"""Porosity opened at customer machining of mounting face
Caliper body deflection above limit in customer bench test
Piston does not retract fully, two vehicles at end of line
Metallic particle found in brake fluid at customer fill station
White corrosion spots on anodised surface after transit
Fluid seepage at piston seal on one vehicle, zero kilometre
Bleed screw loose on one caliper at customer line
Brake fluid leak at warranty, vehicle at 4,200 km
2D code not readable at customer scanner, 12 calipers
Bleed screw cap missing on three calipers at customer line""",
"maintenanceWorkOrder":"""Ejector pin sticking, casting machine 1, die 2
Zone 2 heater failure, solution furnace
Boring bar insert seat damaged, machining center 1
Bag filter change, washer 1
Rectifier cabinet fan failure, anodising line
Seal feeder track jam, assembly press 1
Nutrunner rundown fault, station 1
Leak tester inlet seal replacement
Laser marker lens cleaning and extraction repair
Vision camera 2 cable replacement""",
"notification":"""Die temperature alarm not acknowledged
Furnace charge on hold for hardness
Tool life warning, finish boring bar at 90 percent
Washer filter change due
Coating thickness gauge calibration overdue
Seal lot placed on quality hold
Quality andon not acknowledged at torque station
SPC rule violation on pressure drop chart
ERP confirmation failed after five attempts
Operator certification expiring in 14 days""",
"controlledDocument":"""Drawing 5110-20-0105 revision B, Caliper Body Casting LH
T6 heat treatment specification VBS-HT-002 revision 3
Drawing 5110-20-0110 revision C, Caliper Body LH machined
Cleanliness instruction VBS-CL-001 revision 2
Anodising specification VBS-AN-004 revision 5
Material certificate, piston lot KPP-260905-07
Tightening curve, unit U260916A0184
Leak tester verification record, 16 September 2026
Customer specification SM-ES-3501 revision 04
Drawing 5110-10-0100 revision D, Front Brake Caliper Assembly LH""",
"andonEvent":"""Castings sticking in die 2, operator needs maintenance
Furnace basket damaged, needs replacement before next charge
Bore gauge reading near upper limit, quality support needed
Washer basket supply empty at loading point
Rack contact burn seen on two bodies
Piston seals running low at assembly station
Torque rejects repeating at station TRQ-01
Leak test rejects repeating at station LKT-01
First-off approval needed after marking program change
Bleed screw caps not delivered to packing cell""",
"safetyIncident":"""Molten metal splash near casting machine 1
Hot basket handled without heat resistant gloves
Coolant spill near machining center 1 walkway
Wet floor at washer unloading point
Acid mist noticed at anodising tank 3 when extraction stopped
Finger pinch at assembly press nest
Loose socket ejected from nutrunner
High-pressure hose fitting leak at leak tester
Laser safety door interlock bypassed with a magnet
Stacked bins toppled in packing cell""",
}.items()}
# generic 10-value pools for free-text keys that are not tied to a process row
KEYPOOL={k:rows(v) for k,v in {
"remarks":"""No abnormality observed
Completed after first-off approval
Short quantity carried to next shift
Delayed by 20 minutes for material
Checked with line leader
Run under deviation permit
Retest done after tester verification
Priority raised by planning
Verified against customer schedule
Handed over to shift B""",
"comment":"""Verified against customer drawing revision D
Approved after trial run of 300 pieces
Reviewed with the customer SQA
No impact on fit or function
Approved subject to PPAP resubmission
Checked against control plan
Capability study attached
Stock of old level to be consumed first
Tooling change confirmed by tool room
Training of all three shifts completed""",
"reasonText":"""Replenishment against kanban call
Putaway after incoming inspection
Issue against production order
Return of unused components at order close
Transfer to quarantine after quality hold
Scrap after nonconformance disposition
Finished goods receipt from packing
Goods issue against customer schedule
Cycle count correction
Move to dispatch bay for loading""",
"vehicleNo":"""MH14 GT 4471
MH12 KQ 7730
MH14 HU 2218
MH42 AQ 9054
MH12 RN 3317
MH14 JX 6642
GJ01 DZ 8125
MH04 KF 5096
MH14 LP 1783
TN22 CB 4409""",
"driverName":"""Ganesh More
Santosh Kale
Ramesh Yadav
Prakash Shinde
Anil Pawar
Mahesh Chavan
Bharat Solanki
Dattatray Mane
Vijay Kamble
Murugan Selvam""",
}.items()}
