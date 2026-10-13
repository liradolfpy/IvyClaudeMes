"""Pharma sample-data universe (app = "Gamp"): Paracetamol Tablets IP 500 mg, film-coated, oral solid dose.
Fictional company Indrayani Pharmaceuticals Ltd., Ranjangaon OSD Plant, Pune (site RJ1). Owner decision of 12 Oct 2026 (D060-D064).
Same structure as sample_universe.py: PROC is the process table (one row per routing operation); documents that share a process
context take their work center, equipment, recipe, tool, characteristic and so on from the same row.
Row positions follow the caliper table so that the generic rules keep their meaning:
row 6 is the torque operation (bottle capping), row 7 the leak test (blister vacuum decay), row 8 the marking operation (serialisation),
row 9 the final inspection (cartoning and checkweighing).
Scope lists: DUAL (collections that hold 10 Auto and 10 Gamp documents), GMPONLY (10 Gamp documents only), COMMONAPP (10 Common documents)."""

PROC = [
 dict(op="OP010|Dispensing", wc="DSP-01|Dispensing Booth 1", eq="DSP-01-B1|Downflow Dispensing Booth with 150 kg Platform Balance", eqt="DISP-BOOTH|Dispensing Booth", mfr="ESC|Esco Pharma", model="DFB-1800 with 150 kg platform", line=0, area=1, item=3, comp=4,
  rcp="DSP-PCM500-01|Dispensing sequence, Paracetamol 500 mg granulation", rcptype="Dispensing Program", prog="DSP-PCM-01", tool="SCP-SS-0012|Stainless steel scoop set 12", tlt="SCOOP|Dispensing Scoop", lifeuom="Cycles", lifelimit=5000,
  dev="BAL-DSP-01|Platform balance controller, dispensing booth 1", dvt="BALANCE|Weighing Terminal", skill="DSP-OP|Dispensing of raw materials", wi="Dispensing of API and excipients - Paracetamol 500 mg", instr="Verify the booth status label, tare the container, dispense to target and print the dispense label", key="Only one material may be open in the booth at a time",
  char="Net weight of Paracetamol API dispensed", ctype="Process", cclass="Critical", nom="150.000", lsl="149.250", usl="150.750", uom=1, gauge="G-BAL-150|Platform balance 150 kg, d = 10 g", gty="PLATFORM-BAL|Platform Balance", method="Gross minus tare on the calibrated platform balance", dp=3,
  tag="RJ1.DSP01.BOOTH_DP|Dispensing booth differential pressure", tuom=6, sp="0.15", lo="0.10", hi="0.25",
  defect="DS01|Dispensed quantity outside tolerance", dgroup="DISP|Dispensing", ddesc="Net weight outside +/- 0.5 percent of target", reason="EQP-DSP-01|Balance out of calibration", rcat=0, fault="B0104 Balance zero drift above limit", alarm="Dispensing booth differential pressure below low limit",
  pfn="Dispense each material to the batch formula quantity", pfm="Wrong quantity of API dispensed", pfe="Assay out of specification, batch rejection", pfc="Balance not checked before use", pfp="Daily balance performance check enforced by interlock", pfd="Second-person or system verification of every dispense", sev=9, occ=3, det=3,
  q="Is the daily performance check of the balance recorded and within limits?", problem="Balance shows zero drift and the dispense is blocked", root="Booth airflow disturbing the platform after filter change", action="Airflow baffle adjusted and balance recalibrated", cyc="600.0", setup=20, grain="Lot", optype="Dispensing", special=None),
 dict(op="OP020|Wet granulation", wc="RMG-01|Rapid Mixer Granulator Suite 1", eq="RMG-01-G1|Rapid Mixer Granulator 600 L", eqt="RMG|Rapid Mixer Granulator", mfr="SAM|Saral Pharma Machines", model="RMG 600 with top-drive impeller", line=1, area=2, item=3, comp=6,
  rcp="GRN-PCM500-02|Wet granulation, Paracetamol 500 mg", rcptype="Granulation Program", prog="RMG-PCM-02", tool="SPR-RMG-004|Binder spray nozzle set 4", tlt="NOZZLE|Spray Nozzle", lifeuom="Batches", lifelimit=500,
  dev="PLC-RMG-01|PLC, rapid mixer granulator 1", dvt="PLC|PLC", skill="RMG-OP|Wet granulation operation", wi="Dry mixing, binder addition and wet massing - Paracetamol 500 mg", instr="Load the dry mix, run dry mixing for 5 minutes, add the binder at the set rate and stop at end-point", key="Stop wet massing at the impeller power end-point, not by time alone",
  char="Wet massing time", ctype="Process", cclass="Significant", nom="4.0", lsl="3.5", usl="4.5", uom=8, gauge="G-STW-001|Digital stopwatch", gty="TIMER|Timer", method="Granulator cycle log", dp=1,
  tag="RJ1.RMG01.PRODUCT_TEMP|Wet mass temperature, granulator 1", tuom=7, sp="32.0", lo="25.0", hi="40.0",
  defect="GR01|Over-granulation", dgroup="GRAN|Granulation", ddesc="Hard, oversized granules after wet massing", reason="EQP-RMG-01|Impeller seal leakage", rcat=0, fault="G2210 Impeller seal purge pressure low", alarm="Wet mass temperature above high limit",
  pfn="Form granules of uniform size and density", pfm="Over-wet granules", pfe="Slow dissolution, hardness out of specification", pfc="Binder added too fast", pfp="Binder pump rate set by recipe", pfd="Granule bulk density and sieve analysis per batch", sev=7, occ=3, det=4,
  q="Is the impeller seal purge pressure above 1.5 bar?", problem="Impeller seal purge pressure drops and the granulator stops", root="Seal purge air filter blocked", action="Filter replaced and added to the preventive maintenance plan", cyc="1800.0", setup=60, grain="Lot", optype="Granulation", special=None),
 dict(op="OP030|Fluid bed drying", wc="FBD-01|Fluid Bed Dryer Suite 1", eq="FBD-01-D1|Fluid Bed Dryer 300 kg", eqt="FBD|Fluid Bed Dryer", mfr="GLT|Glatt", model="WSG 300", line=1, area=2, item=3, comp=3,
  rcp="FBD-PCM500-03|Drying profile, Paracetamol 500 mg granules", rcptype="Drying Program", prog="FBD-PCM-03", tool="FBG-FBD-002|Finger bag set 2, fluid bed dryer", tlt="FILTER-BAG|Filter Bag", lifeuom="Batches", lifelimit=200,
  dev="SCADA-FBD-01|SCADA node, fluid bed dryer 1", dvt="SCADA|SCADA Node", skill="FBD-OP|Fluid bed drying operation", wi="Drying of wet granules - Paracetamol 500 mg", instr="Charge the wet mass, dry at 60 degC inlet air until the product temperature reaches 42 degC and sample for LOD", key="Release the granules only when loss on drying is between 1.0 and 2.5 percent",
  char="Loss on drying of granules", ctype="Product", cclass="Critical", nom="1.75", lsl="1.00", usl="2.50", uom=3, gauge="G-MA-001|Halogen moisture analyser", gty="MOISTURE|Moisture Analyser", method="Halogen moisture analyser, 5 g at 105 degC", dp=2,
  tag="RJ1.FBD01.INLET_TEMP|Inlet air temperature, fluid bed dryer 1", tuom=7, sp="60.0", lo="55.0", hi="65.0",
  defect="DR01|Loss on drying above limit", dgroup="DRY|Drying", ddesc="Granule moisture above 2.5 percent after drying", reason="UTL-FBD-01|Inlet air heater fault", rcat=6, fault="D1132 Inlet air temperature not reached", alarm="Inlet air temperature below low limit",
  pfn="Dry the granules to the moisture limit", pfm="Moisture above limit", pfe="Sticking at compression, unstable tablets", pfc="Inlet air temperature too low", pfp="Product temperature end-point in the recipe", pfd="LOD of every batch before blending", sev=7, occ=3, det=3,
  q="Is the finger bag intact with no product in the exhaust plenum?", problem="Inlet air does not reach 60 degC and drying time doubles", root="Steam valve of the air handling unit stuck partly closed", action="Steam valve actuator replaced", cyc="3600.0", setup=45, grain="Lot", optype="Drying", special=None),
 dict(op="OP040|Sizing and lubrication blending", wc="BLN-01|Blending Suite 1", eq="BLN-01-O1|Octagonal Blender 1200 L", eqt="BLENDER|Blender", mfr="PRM|Prism Pharma Machinery", model="OCB 1200", line=1, area=2, item=3, comp=8,
  rcp="BLN-PCM500-04|Lubrication blending, Paracetamol 500 mg", rcptype="Blending Program", prog="BLN-PCM-04", tool="SCR-MLT-016|Multimill screen 1.5 mm", tlt="SCREEN|Mill Screen", lifeuom="Batches", lifelimit=300,
  dev="DRV-BLN-01|Drive controller, octagonal blender 1", dvt="DRIVE-CTRL|Drive Controller", skill="BLN-OP|Sizing and blending operation", wi="Sizing and lubrication - Paracetamol 500 mg", instr="Mill the dried granules through the 1.5 mm screen, add the sifted magnesium stearate and blend for 3 minutes at 12 rpm", key="Do not exceed 3 minutes lubrication; over-blending softens the tablets",
  char="Blend uniformity, relative standard deviation", ctype="Product", cclass="Critical", nom="2.0", lsl="0.0", usl="5.0", uom=3, gauge="G-HPLC-001|HPLC system, quality control laboratory", gty="HPLC|HPLC System", method="Ten thief samples, assay by HPLC", dp=1,
  tag="RJ1.BLN01.ROOM_RH|Relative humidity, blending suite 1", tuom=3, sp="45.0", lo="30.0", hi="55.0",
  defect="BL01|Blend not uniform", dgroup="BLEND|Blending", ddesc="Blend uniformity RSD above 5 percent", reason="PRC-BLN-01|Blender speed drift", rcat=3, fault="M0315 Blender drive speed deviation", alarm="Blending suite relative humidity above high limit",
  pfn="Distribute the lubricant evenly", pfm="Blend not uniform", pfe="Content uniformity failure", pfc="Blending time too short", pfp="Blending time and speed locked in the recipe", pfd="Blend uniformity on every validation batch and one batch per month", sev=8, occ=2, det=4,
  q="Is the blender bin earthing clamp connected?", problem="Blender drive speed drifts below 11 rpm", root="Drive belt slipping", action="Belt replaced and tension check added to the start-up check", cyc="900.0", setup=30, grain="Lot", optype="Blending", special=None),
 dict(op="OP050|Compression", wc="CMP-01|Compression Cubicle 1", eq="CMP-01-T1|Rotary Tablet Press 45 Station", eqt="TAB-PRESS|Rotary Tablet Press", mfr="FET|Fette Compacting", model="FE35 45 station", line=2, area=3, item=3, comp=3,
  rcp="CMP-PCM500-05|Compression, Paracetamol 500 mg cores", rcptype="Compression Program", prog="CMP-PCM-05", tool="PNC-D-19X9|Punch and die set, capsule shaped 19 x 9 mm", tlt="PUNCH-SET|Punch and Die Set", lifeuom="Tablets", lifelimit=20000000,
  dev="PLC-CMP-01|Tablet press controller 1", dvt="PRESS-CTRL|Press Controller", skill="CMP-OP|Tablet compression operation", wi="Compression of core tablets - Paracetamol 500 mg", instr="Set fill depth and main compression force from the recipe, run the start-up checks and release the press after first-off approval", key="Check weight, hardness and thickness every 30 minutes",
  char="Average weight of core tablet", ctype="Product", cclass="Critical", nom="600.0", lsl="570.0", usl="630.0", uom=2, gauge="G-BAL-220|Analytical balance 220 g, d = 0.1 mg", gty="ANALYTICAL-BAL|Analytical Balance", method="Average of 20 tablets on the analytical balance", dp=1,
  tag="RJ1.CMP01.MAIN_FORCE|Main compression force, tablet press 1", tuom=4, sp="18000.0", lo="15000.0", hi="21000.0",
  defect="CP01|Capping of tablets", dgroup="COMP|Compression", ddesc="Upper part of the tablet separates from the body", reason="TLG-CMP-01|Punch tip wear", rcat=2, fault="T4401 Main force outside window on station 17", alarm="Main compression force above high limit",
  pfn="Compress tablets of uniform weight and hardness", pfm="Tablet weight out of limits", pfe="Dose out of specification for the patient", pfc="Uneven granule flow into the press stations", pfp="Automatic weight control on compression force", pfd="In-process weight check every 30 minutes and checkweighing", sev=9, occ=3, det=3,
  q="Is the punch and die set within its tablet count limit?", problem="Station 17 rejects tablets with high force", root="Lower punch tip worn", action="Punch replaced and punch inspection frequency increased", cyc="0.02", setup=90, grain="Lot", optype="Compression", special=None),
 dict(op="OP060|Film coating", wc="COT-01|Coating Suite 1", eq="COT-01-C1|Automatic Coating Pan 48 inch", eqt="COATER|Coating Pan", mfr="GAC|Gansons", model="GAC 48 inch auto-coater", line=3, area=3, item=2, comp=9,
  rcp="COT-PCM500-06|Film coating, Paracetamol 500 mg", rcptype="Coating Program", prog="COT-PCM-06", tool="GUN-COT-003|Spray gun set 3, coater 1", tlt="SPRAY-GUN|Spray Gun", lifeuom="Batches", lifelimit=400,
  dev="TTX-COT-01|Exhaust temperature transmitter, coating pan 1", dvt="TEMP-TX|Temperature Transmitter", skill="COT-OP|Film coating operation", wi="Film coating of core tablets - Paracetamol 500 mg", instr="Warm the bed to 42 degC exhaust, spray the coating suspension at the recipe rate and dry for 10 minutes", key="Spray only when the exhaust temperature is between 38 and 46 degC",
  char="Coating weight gain", ctype="Process", cclass="Significant", nom="3.0", lsl="2.5", usl="3.5", uom=3, gauge="G-BAL-6200|Top-pan balance 6200 g, coating suite", gty="TOPPAN-BAL|Top-pan Balance", method="Weight of 100 tablets before and after coating", dp=1,
  tag="RJ1.COT01.EXHAUST_TEMP|Exhaust air temperature, coating pan 1", tuom=7, sp="42.0", lo="38.0", hi="46.0",
  defect="CT01|Tablet twinning", dgroup="COAT|Coating", ddesc="Two tablets stuck together by the film", reason="PRC-COT-01|Spray rate too high", rcat=3, fault="C0517 Atomising air pressure low", alarm="Exhaust air temperature below low limit",
  pfn="Apply a uniform film coat", pfm="Weight gain below 2.5 percent", pfe="Bitter taste, moisture uptake in storage", pfc="Spray suspension not stirred", pfp="Suspension stirrer interlock", pfd="Weight gain check at the end of every batch", sev=5, occ=3, det=3,
  q="Is the coating suspension stirrer running?", problem="Atomising air pressure drops and the guns spray coarse droplets", root="Air regulator diaphragm torn", action="Regulator replaced", cyc="5400.0", setup=60, grain="Lot", optype="Coating", special=None),
 dict(op="OP070|Bottle filling and capping", wc="BTL-01|Bottle Packing Line 1", eq="BTL-01-K1|Inline Capper with Torque Control", eqt="CAPPER|Bottle Capper", mfr="PAM|Pharma Automation Machines", model="Servo capper SC-120", line=4, area=4, item=1, comp=2,
  rcp="BTL-PCM500-07|Bottle fill 100 and cap torque, Paracetamol 500 mg", rcptype="Capping Program", prog="CAP-38-07", tool="CHK-38-0002|Capping chuck 38 mm", tlt="CHUCK|Capping Chuck", lifeuom="Cycles", lifelimit=2000000,
  dev="CAP-CTRL-01|Capper controller, bottle line 1", dvt="CAP-CTRL|Capper Controller", skill="BTL-OP|Bottle filling and capping", wi="Counting, filling and capping - Paracetamol 500 mg, bottle of 100", instr="Load the cap hopper, set count 100 and release the line after the first-off torque check", key="Removal torque of the first ten bottles must be checked with the torque tester",
  char="Cap application torque", ctype="Process", cclass="Critical", nom="1.60", lsl="1.20", usl="2.00", uom=5, gauge="G-CTT-001|Cap torque tester 0-5 N.m", gty="TORQUE|Torque Tester", method="Removal torque on the cap torque tester", dp=2,
  tag="RJ1.BTL01.CAP_TORQUE|Application torque, capper 1", tuom=5, sp="1.60", lo="1.20", hi="2.00",
  defect="BT01|Loose cap", dgroup="BTL|Bottle Packing", ddesc="Removal torque below 1.2 N.m", reason="TLG-BTL-01|Capping chuck worn", rcat=2, fault="K0712 Torque not reached on head 3", alarm="Application torque below low limit",
  pfn="Close the bottle tightly", pfm="Cap under-torqued", pfe="Moisture ingress, loss of seal", pfc="Worn chuck insert", pfp="Torque monitoring per head with reject", pfd="Removal torque check every hour", sev=6, occ=3, det=3,
  q="Does the capper reject the challenge bottle with a loose cap?", problem="Head 3 stops with torque not reached", root="Chuck insert worn", action="Chuck insert replaced", cyc="0.6", setup=40, grain="Unit", optype="Packing", special=None),
 dict(op="OP080|Blister packing and leak test", wc="BLS-01|Blister Packing Line 1", eq="BLS-01-P1|Alu-PVC Blister Packing Machine", eqt="BLISTER|Blister Packing Machine", mfr="ACG|ACG Pam", model="BMAX blister line", line=5, area=4, item=0, comp=2,
  rcp="BLS-PCM500-08|Blister 10 x 10 and vacuum leak test, Paracetamol 500 mg", rcptype="Blister Program", prog="BLS-10X10-08", tool="FRM-BLS-10X10|Forming and sealing tooling, 10 tablet blister", tlt="CHANGE-PARTS|Change Parts", lifeuom="Cycles", lifelimit=5000000,
  dev="LKT-CTRL-11|Vacuum leak tester, blister line 1", dvt="LEAK-CTRL|Leak Tester", skill="BLS-OP|Blister packing and leak test", wi="Blister packing and leak test - Paracetamol 500 mg 10 x 10", instr="Load foil and PVC rolls, heat the sealing roller to 210 degC and run the vacuum leak test on the first and every hourly sample", key="Every hourly blister sample must pass the vacuum leak test before the line continues",
  char="Vacuum decay at -500 mbar", ctype="Product", cclass="Critical", nom="2.0", lsl="0.0", usl="5.0", uom=6, gauge="G-VLT-001|Vacuum leak tester", gty="LEAK-TESTER|Leak Tester", method="Vacuum decay, 30 seconds hold at -500 mbar", dp=1,
  tag="RJ1.BLS01.SEAL_TEMP|Sealing roller temperature, blister line 1", tuom=7, sp="210.0", lo="200.0", hi="220.0",
  defect="BP01|Blister leak", dgroup="BLIST|Blister Packing", ddesc="Pocket fails the vacuum leak test", reason="TLG-BLS-01|Sealing roller knurl worn", rcat=2, fault="S0811 Sealing temperature not reached", alarm="Sealing roller temperature below low limit",
  pfn="Seal every tablet pocket", pfm="Leaking blister pocket passed", pfe="Moisture uptake, degradation, market complaint", pfc="Sealing temperature too low", pfp="Sealing temperature interlock", pfd="Vacuum leak test of hourly samples", sev=8, occ=3, det=4,
  q="Does the leak tester detect the reference leaking blister?", problem="Hourly samples fail the leak test after a foil roll change", root="Sealing roller knurl worn at one edge", action="Sealing roller replaced", cyc="0.5", setup=60, grain="Unit", optype="Packing", special=None),
 dict(op="OP090|Serialisation and printing", wc="SER-01|Serialisation Station, Blister Line 1", eq="SER-01-P1|Carton Coding and Serialisation Unit", eqt="SERIALISER|Serialisation Unit", mfr="OPT|Optel", model="Carton serialisation module", line=5, area=4, item=0, comp=0,
  rcp="SER-PCM500-09|Carton code layout: batch, expiry, 2D code", rcptype="Serialisation Program", prog="SER-CTN-09", tool="NST-SER-001|Carton guide set, serialisation unit", tlt="GUIDE|Carton Guide", lifeuom="Cycles", lifelimit=3000000,
  dev="SER-CTRL-01|Serialisation controller, blister line 1", dvt="SER-CTRL|Serialisation Controller", skill="SER-OP|Serialisation and code verification", wi="Carton coding and code verification - Paracetamol 500 mg", instr="Load the batch and expiry data from the order, print the challenge carton and confirm that the camera rejects it", key="The batch number and expiry date must come from the released order, never typed by hand",
  char="Printed batch and expiry text height", ctype="Product", cclass="Standard", nom="2.00", lsl="1.80", usl="2.20", uom=9, gauge="G-VRF-001|2D code verifier", gty="CODE-VERIFIER|Code Verifier", method="Code verifier and measuring loupe on the first carton", dp=2,
  tag="RJ1.SER01.PRINT_HEAD_TEMP|Print head temperature, serialisation unit", tuom=7, sp="45.0", lo="35.0", hi="55.0",
  defect="SR01|2D code not readable", dgroup="SER|Serialisation", ddesc="Code grade below C or code not readable", reason="PRC-SER-01|Print head contaminated", rcat=3, fault="V0905 Code verification grade below C", alarm="Print head temperature above high limit",
  pfn="Print a unique, readable code with batch and expiry", pfm="Wrong expiry date printed", pfe="Product used after expiry, regulatory recall", pfc="Expiry typed by hand", pfp="Batch and expiry downloaded from the order", pfd="Camera verification of every carton", sev=9, occ=2, det=2,
  q="Does the camera reject the challenge carton with the wrong expiry?", problem="Code grade drops to D during the shift", root="Ink residue on the print head", action="Print head cleaned and cleaning frequency increased", cyc="0.5", setup=15, grain="Unit", optype="Packing", special=None),
 dict(op="OP100|Cartoning and final inspection", wc="CTN-01|Cartoning and Checkweighing Station", eq="CTN-01-W1|Cartoner with Checkweigher", eqt="CHECKWEIGHER|Checkweigher", mfr="MET|Mettler Toledo", model="C3570 checkweigher", line=6, area=5, item=0, comp=0,
  rcp="CTN-PCM500-10|Cartoning and checkweighing, 10 x 10 carton", rcptype="Cartoning Program", prog="CTN-10X10-10", tool="CHP-CTN-010|Cartoner change parts, 10 x 10 carton", tlt="CTN-PARTS|Cartoner Change Parts", lifeuom="Cycles", lifelimit=5000000,
  dev="PRN-CTN-01|Shipper label printer, cartoning", dvt="PRINTER|Label Printer", skill="CTN-INSP|Cartoning, checkweighing and final inspection", wi="Cartoning, checkweighing and shipper packing - Paracetamol 500 mg", instr="Check the leaflet, carton print and checkweigher limits, then pack 50 cartons per shipper", key="Every carton must carry a leaflet before it enters the shipper",
  char="Tablet hardness at release", ctype="Product", cclass="Significant", nom="110.0", lsl="80.0", usl="140.0", uom=4, gauge="G-HRD-001|Tablet hardness tester", gty="HARDNESS|Hardness Tester", method="Ten tablets on the hardness tester", dp=1,
  tag="RJ1.CTN01.CHECKWEIGHT_MEAN|Checkweigher mean carton weight", tuom=1, sp="0.072", lo="0.070", hi="0.074",
  defect="FI01|Leaflet missing", dgroup="FINAL|Final Inspection", ddesc="Carton without leaflet", reason="EQP-CTN-01|Leaflet feeder misfeed", rcat=0, fault="W0102 Checkweigher reject bin full", alarm="Checkweigher mean carton weight below low limit",
  pfn="Confirm every carton is complete before shipper packing", pfm="Leaflet missing", pfe="Patient without dosage information, market complaint", pfc="Leaflet feeder misfeed not detected", pfp="Leaflet presence sensor and checkweigher", pfd="Checkweighing of every carton", sev=6, occ=3, det=2,
  q="Does the checkweigher reject the carton without a leaflet from the challenge set?", problem="Leaflet feeder misfeeds and the checkweigher rejects cartons", root="Leaflet suction cup worn", action="Suction cups replaced", cyc="0.4", setup=20, grain="Unit", optype="Inspection", special=None),
]

def rows(t): return [l for l in t.strip().split("\n")]

MASTER = {
"site": rows("""RJ1|Ranjangaon OSD Plant, Pune
RJ2|Ranjangaon Packing Plant, Pune
KR1|Kurkumbh API Plant, Pune
BD1|Baddi Formulation Plant, Himachal Pradesh
SK1|Sikkim Formulation Plant, Rangpo
GA1|Verna Formulation Plant, Goa
HY1|Genome Valley R and D Centre, Hyderabad
WH2|Talegaon Pharma Distribution Warehouse
QC1|Pune Central Quality Laboratory
HO2|Corporate Office, Pune"""),
"enterprise": rows("""IPL|Indrayani Pharmaceuticals Ltd.
IPG|Indrayani Pharma Group Ltd.
IAP|Indrayani API Pvt. Ltd.
IFL|Indrayani Formulations Ltd.
IPK|Indrayani Packaging Pvt. Ltd.
IRD|Indrayani Research Pvt. Ltd.
IDS|Indrayani Distribution Services Pvt. Ltd.
IEX|Indrayani Pharma Exports Pvt. Ltd.
ICL|Indrayani Clinical Supplies Ltd.
IHC|Indrayani Healthcare Ltd."""),
"area": rows("""WHS|Warehouse and Sampling
DSP|Dispensing Area
GRN|Granulation and Blending Area
CMC|Compression and Coating Area
PPK|Primary Packing Area
SPK|Secondary Packing Area
QCL|Quality Control Laboratory
QAA|Quality Assurance Documentation Area
ENG|Engineering Workshop
HVAC|HVAC and Purified Water Plant"""),
"line": rows("""DSP-01|Dispensing Suite 1
GRN-01|Granulation Suite 1
CMP-01|Compression Suite 1
COT-01|Coating Suite 1
BTL-01|Bottle Packing Line 1
BLS-01|Blister Packing Line 1
CTN-01|Secondary Packing Line 1
GRN-02|Granulation Suite 2
CMP-02|Compression Suite 2
BLS-02|Blister Packing Line 2"""),
"customer": rows("""MCH|Medicura Healthcare Ltd.
ARD|Arogya Distributors Pvt. Ltd.
KPD|Konkan Pharma Distributors
SHC|Sanjeevani Hospital Chain Ltd.
MKE|Medicura Healthcare Kenya Ltd.
NPL|Narmada Pharmacy Retail Ltd.
GMS|Godavari Medical Stores Pvt. Ltd.
TIN|Tender Institutional Supplies, Maharashtra
VPH|Vindhya Pharma Wholesale Pvt. Ltd.
SAH|Sahyog Pharma Exports"""),
"supplier": rows("""S2011|Deccan Fine Chemicals Ltd. (Paracetamol API)
S2034|Bharat Excipients Pvt. Ltd.
S2058|Krishna Polymers and Povidone Ltd.
S2071|Western Starch Derivatives Ltd.
S2093|Konkan Lubricants and Stearates Pvt. Ltd.
S2110|Indus Film Coatings Pvt. Ltd.
S2132|Pune Calibration and Validation Services
S2155|Maharashtra Foils and Laminates Ltd.
S2178|Shivneri Cartons and Printing Pvt. Ltd.
S2201|Sahyog Facility Services"""),
"item": rows("""FG-PCM500-B10|Paracetamol Tablets IP 500 mg, blister 10 x 10
FG-PCM500-H100|Paracetamol Tablets IP 500 mg, HDPE bottle of 100
BLK-PCM500-FCT|Paracetamol 500 mg film-coated tablets, bulk
BLK-PCM500-GRN|Paracetamol 500 mg lubricated granules and core tablets, bulk
RM-PCM-API|Paracetamol IP, active pharmaceutical ingredient
RM-MCC-101|Microcrystalline cellulose PH 101
RM-PVP-K30|Povidone K30
RM-SSG|Sodium starch glycolate
RM-MGST|Magnesium stearate
RM-COAT-WHT|Film coating system, white"""),
"productVariant": rows("""PCM500-B10-DOM|Paracetamol 500 mg 10 x 10 blister, domestic
PCM500-H100-DOM|Paracetamol 500 mg bottle of 100, domestic
PCM500-B10-KEN|Paracetamol 500 mg 10 x 10 blister, Kenya
PCM500-H100-KEN|Paracetamol 500 mg bottle of 100, Kenya
PCM500-B10-INS|Paracetamol 500 mg 10 x 10 blister, institutional
PCM500-H100-INS|Paracetamol 500 mg bottle of 100, institutional
PCM500-B10-HSP|Paracetamol 500 mg 10 x 10 blister, hospital pack
PCM500-H100-HSP|Paracetamol 500 mg bottle of 100, hospital pack
PCM500-B10-PHS|Paracetamol 500 mg 10 x 10 blister, physician sample
PCM500-H100-EXP|Paracetamol 500 mg bottle of 100, export general"""),
"routing": rows("""FG-PCM500-B10-R01|Paracetamol 500 mg blister, full process routing
FG-PCM500-H100-R01|Paracetamol 500 mg bottle, full process routing
BLK-PCM500-FCT-R01|Paracetamol 500 mg bulk, compression and coating
BLK-PCM500-GRN-R01|Paracetamol 500 mg granules, dispensing to blending
FG-PCM500-B10-RP1|Paracetamol 500 mg blister, repacking of rejected blisters
FG-PCM500-B10-RP2|Paracetamol 500 mg blister, carton re-coding
BLK-PCM500-FCT-RC1|Paracetamol 500 mg bulk, re-coating
FG-PCM500-B10-R02|Paracetamol 500 mg blister, alternate routing via blister line 2
FG-PCM500-B10-RP3|Paracetamol 500 mg blister, re-serialisation
FG-PCM500-B10-VAL|Paracetamol 500 mg blister, process validation routing"""),
"labelTemplate": rows("""MCH-SHIP-A5|Medicura Healthcare shipper label A5
MCH-PAL-A4|Medicura Healthcare pallet label A4
CTN-2D-14|Carton 2D code and batch print 14 x 14 mm
DSP-LBL-A6|Dispense label A6
QUAR-YEL-A6|Quarantine label, yellow
KEN-SHIP-A5|Kenya export shipper label A5
LOC-RACK-PH|Location label 100 x 50 mm, pharma warehouse
STAT-CLEAN-A6|Equipment status label, cleaned
REJ-RED-A6|Rejected label, red
REL-GRN-A6|Released label, green"""),
"documentType": rows("""SOP|Standard Operating Procedure
MMR-DOC|Master Manufacturing Record
BMR-COPY|Executed Batch Record Copy
COA|Certificate of Analysis
CAL-CERT|Calibration Certificate
VAL-PROT|Validation Protocol
VAL-RPT|Validation Report
SPEC|Specification
ART|Packaging Artwork
TRAINING|Training Record"""),
"numberRange": rows("""BATCH-PCM500|Batch numbers, Paracetamol 500 mg
SERIAL-CTN|Carton serial numbers
LOT-RM|Raw material lot numbers
LOT-GRN|Granulation lot numbers
PROD-ORDER-PH|Process order numbers
DEV|Deviation numbers
LABEL-PH|Label numbers
GRN-PH|Goods receipt numbers
SHIPMENT-PH|Shipment numbers
SHIPPER|Shipper numbers"""),
"storageLocation": rows("""WH-RM-QUAR|Raw material quarantine, warehouse
WH-RM-REL-A01|Released raw materials, rack A01
WH-RM-REL-A02|Released raw materials, rack A02
DSP-STG-01|Staging area, dispensing
GRN-STG-01|In-process staging, granulation
PKG-STG-01|Line staging, packing
QC-RSV-01|Reserve sample room, quality control
FG-QUAR-01|Finished goods quarantine
FG-REL-01|Finished goods released store
REJ-CAGE-01|Rejected material cage"""),
"costCenter": rows("""7010|Warehouse and Sampling
7020|Dispensing
7030|Granulation and Blending
7040|Compression and Coating
7120|Primary Packing
7130|Secondary Packing
7210|Quality Control
7310|Quality Assurance
7410|Engineering
7510|HVAC and Utilities"""),
"commodity": rows("""API|Active Pharmaceutical Ingredients
EXCIP|Excipients
BINDER|Binders
DISINT|Disintegrants
LUBR|Lubricants
COAT|Film Coating Systems
CALIB|Calibration and Validation Services
FOIL|Foils and Laminates
CARTON|Printed Cartons and Leaflets
SERVICES|Facility Services"""),
"itemFamily": rows("""ANALGESIC-TAB|Analgesic Tablets
ANALGESIC-SUSP|Analgesic Suspensions
BULK-TAB|Bulk Tablets
GRANULES|Granules
API|Active Ingredients
EXCIPIENT|Excipients
COATING|Coating Materials
PRIMARY-PACK|Primary Packaging Materials
SECONDARY-PACK|Secondary Packaging Materials
SAMPLE-PACK|Physician Sample Packs"""),
"itemGroup": rows("""FG-TAB|Finished Tablets
BULK|Bulk Tablets
GRANULE|Granules
API|Active Ingredient
FILLER|Filler
BINDER|Binder
DISINT|Disintegrant
LUBR|Lubricant
COAT|Coating
PACK|Packaging"""),
"department": rows("""PROD|Production
QA|Quality Assurance
ENGG|Engineering
WH|Warehouse
QC|Quality Control
PPIC|Production Planning
VAL|Validation
EHS|Environment Health and Safety
IT|Information Technology
HR|Human Resources"""),
"designation": rows("""PRD-OPR|Production Operator
PKG-OPR|Packing Operator
GRN-OPR|Granulation Operator
QA-OFF|QA Officer
PRD-EXE|Production Executive
ENG-TECH|Engineering Technician
QA-HEAD|Head Quality Assurance
WH-OFF|Warehouse Officer
CSV-ENG|Computer System Validation Engineer
SYS-ACC|System Account"""),
"role": rows("""PH-OPERATOR|Production Operator, OSD
PH-PKG-OPR|Packing Operator
PH-SUPERVISOR|Production Supervisor, OSD
PH-QA-REVIEW|QA Batch Record Reviewer
PH-QA-RELEASE|QA Release Authority
PH-QC-ANALYST|QC Analyst
PH-ENGINEER|Engineering Technician, OSD
PH-WAREHOUSE|Warehouse Officer
PH-CSV|Computer System Validation Engineer
PH-ADMIN|System Administrator, pharma"""),
"skillCategory": rows("""PH-PROCESS|Pharma Process
PH-QUALITY|Quality and GMP
PH-ENGG|Engineering
PH-SAFETY|Safety and Containment
PH-WH|Warehouse and Dispensing
PH-CLEAN|Cleaning and Line Clearance
PH-TEST|In-process Testing
PH-ASEPTIC|Hygiene and Gowning
PH-SUPERV|Supervision
PH-SYSTEM|System Use and Data Integrity"""),
"containerType": rows("""IBC-600|Intermediate Bulk Container 600 L
IBC-300|Intermediate Bulk Container 300 L
SSD-50|Stainless Steel Drum 50 L
HDPE-DRUM|HDPE Drum with Double Liner
POLY-BAG|Double Polybag Liner
PLT-PH|Pallet 1200 x 1000, plastic
SHIPPER-50|Shipper Carton 50 Cartons
CRATE-PKG|Packing Line Crate
REJ-BIN|Reject Bin, locked
SMP-BOX|Sample Box"""),
"packType": rows("""BLISTER|Blister
CARTON|Carton
BOTTLE|Bottle
SHIPPER|Shipper
PALLET|Pallet
LEAFLET|Leaflet
SHRINK|Shrink Wrap
DRUM|Drum
BAG|Polybag
IBC|Intermediate Bulk Container"""),
"movementType": rows("""GR-PO-PH|Goods Receipt Into Quarantine
REL-QC|Release After QC Approval
ISSUE-DSP|Issue To Dispensing
RETURN-DSP|Return From Dispensing
TRANSFER-PH|Location Transfer
REJECT-PH|Transfer To Rejected
GR-BATCH|Batch Receipt From Packing
SHIP-PH|Goods Issue For Dispatch
ADJUST-PH|Stock Adjustment
TO-QUAR-PH|Transfer To Quarantine"""),
"stockStatus": rows("""REL|Released
QUAR|Quarantine
REJ|Rejected
RES-PH|Reserved For Batch
RET-PH|Market Returns
TRN-PH|In Transit
RECALL|Recalled
SMP|Under Sampling
EXP|Expired
DEST|Pending Destruction"""),
"transporter": rows("""PCC|Pharma Cold and Cargo Carriers
MDX|Medlog Express
ITL|Indrayani Transport Logistics
KCL|Konkan Courier Lines
SLX|Safe Logistics Pharma
DGL|Deccan GDP Logistics
RTL|Rangpo Transport Lines
BFC|Bharat Freight Carriers
NLC|Nhava Sheva Logistics Co.
AFS|Airfreight Services Pune"""),
"workCalendar": rows("""RJ1-2026|Ranjangaon OSD Plant Calendar 2026
RJ1-2026-DSP|Dispensing Calendar 2026
RJ1-2026-GRN|Granulation Calendar 2026
RJ1-2026-CMP|Compression Calendar 2026
RJ1-2026-COT|Coating Calendar 2026
RJ1-2026-PKG|Packing Calendar 2026
RJ1-2026-QC|Quality Control Calendar 2026
RJ1-2026-WH|Warehouse Calendar 2026
RJ1-2026-ENG|Engineering Calendar 2026
RJ1-2027|Ranjangaon OSD Plant Calendar 2027"""),
"reasonCategory": rows("""EQP|Equipment
UTL|Utilities
TLG|Change Parts and Tooling
PRC|Process
MAT|Material
QCA|Quality Clearance
CLN|Cleaning
DOC|Documentation
CHG|Product Changeover
PLN|Planned"""),
"lossCategory": rows("""BREAKDOWN-PH|Breakdown
CLEANING|Cleaning And Line Clearance
MINOR-STOP-PH|Minor Stop
SPEED-PH|Reduced Speed
STARTUP-PH|Start-up Rejects
REJECT-PH|In-process Rejects
PLAN-MNT-PH|Planned Maintenance
QC-WAIT|Waiting For QC Release
NO-DEMAND-PH|No Demand
MAT-SHORT-PH|Material Shortage"""),
"dispositionType": rows("""RELEASE-PH|Release
REPROCESS|Reprocess
REJECT-DESTROY|Reject And Destroy
RTS-PH|Return To Supplier
REINSPECT|100 Percent Reinspection
REPACK|Repack
RELABEL|Relabel
QUAR-HOLD|Hold In Quarantine
DEV-RELEASE|Release Under Deviation
RETEST-PH|Retest"""),
"complaintType": rows("""PROD-QUAL|Product Quality
ADR|Adverse Drug Reaction Report
PACK-DEF|Packaging Defect
FOREIGN|Foreign Particle
LABEL-PH|Labelling Error
MIX-UP|Product Mix-up
SHORT-PH|Short Supply
DAMAGE|Transit Damage
DOC-PH|Documentation Error
REG-AUDIT|Regulatory Inspection Observation"""),
"ppeItem": rows("""GOWN-CR|Cleanroom Gown
HAIR-COVER|Hair Cover
SHOE-COVER|Shoe Cover
NITRILE-GLV|Nitrile Gloves
FACE-MASK|Face Mask
GOGGLES-PH|Safety Goggles
PAPR|Powered Air-Purifying Respirator
EAR-MUFF|Ear Muffs
ANTISTATIC-SHOES|Antistatic Shoes
BEARD-COVER|Beard Cover"""),
"samplingPlan": rows("""ISO2859-0.65-II|AQL 0.65, general inspection level II, packing
ISO2859-0.1-II|AQL 0.1, critical packing defects
ROOT-N-PLUS-1|Square root of n plus one containers
IPC-20-30M|20 tablets every 30 minutes
IPC-10-HR|10 tablets every hour
BU-10-LOC|Blend uniformity, 10 locations
FULL-PH|100 percent inspection
REDUCED-PH|Reduced sampling after 5 accepted lots
FIRST-OFF-PH|First-off, 20 tablets
DISP-1-SHIP|One shipper per dispatch"""),
"integrationConnector": rows("""ERP-PH|ERP process order interface
LIMS-PH|LIMS results interface
OPC-GRN|OPC UA server, granulation suite
OPC-CMP|OPC UA server, compression suite
BAL-SER|Balance serial interface, dispensing
LKT-PH|Blister leak tester interface
SER-L4|Serialisation level 4 interface
QR-GOV|Government track and trace upload
SMTP-PH|Notification e-mail gateway, pharma
DMS-PH|Document management system interface"""),
"shift": rows("""A|Shift A
B|Shift B
C|Shift C
G|General Shift
A-SAT|Shift A Saturday
B-SAT|Shift B Saturday
M1|Engineering Shift Day
M2|Engineering Shift Night
OT-A|Overtime Extension A
OT-B|Overtime Extension B"""),
"user": rows("""20311|Amol Shinde
20354|Pooja Kadam
20372|Rahul Waghmare
20108|Shalini Rao
20142|Nilesh Sawant
20219|Farhan Qureshi
20015|Vandana Iyer
20266|Prakash Jagtap
20187|Tejas Bapat
SYSTEM-PH|MES System, pharma"""),
"unitOfMeasure": rows("""EA|Each
KG|Kilogram
MG|Milligram
PCT|Percent
N|Newton
NM|Newton metre
MBAR|Millibar
DEGC|Degree Celsius
MIN|Minute
MM|Millimetre"""),
"engineeringChange": rows("""Tablet hardness limit revised to 80-140 N
Second source of microcrystalline cellulose approved
Coating weight gain target changed to 3.0 percent
Blister foil supplier changed
Carton artwork revised for new marketing authorisation number
Granulation end-point changed from time to impeller power
Bottle cap torque window revised to 1.2-2.0 N.m
Kenya export pack added
Shipper quantity changed from 40 to 50 cartons
Dispensing booth balance replaced with 150 kg model"""),
}

TITLES = {
"nonconformance": rows("""Dispensed API weight outside tolerance, batch PCM5G26091
Wet mass over-granulated after binder pump fault
Loss on drying 2.9 percent on granules of batch PCM5G26092
Blend uniformity RSD 5.6 percent on validation batch
Tablet weight drift on station 17, compression
Twinning of tablets after spray rate excursion
Bottle cap removal torque below 1.2 N.m on head 3
Blister leak test failures after foil roll change
2D code grade D on cartons after print head contamination
Leaflet missing in cartons found at final inspection"""),
"capa": rows("""CAPA - Balance drift in dispensing booth
CAPA - Over-granulation after binder pump fault
CAPA - High loss on drying
CAPA - Blend uniformity failure
CAPA - Tablet weight drift
CAPA - Tablet twinning in coating
CAPA - Loose bottle caps
CAPA - Blister leaks after foil change
CAPA - Unreadable carton codes
CAPA - Missing leaflet in carton"""),
"deviationPermit": rows("""Dispensing tolerance +/- 0.8 percent for one API lot with high moisture
Granulation with binder pump in manual mode for one batch
Drying end-point extended by 15 minutes for one batch
Blend uniformity sampling at 8 locations during thief repair
Tablet thickness 6.1 mm accepted on one batch
Coating weight gain 2.4 percent accepted on one batch
Cap torque 1.1-2.0 N.m during chuck trial
Leak test hold time 25 seconds for trial
Carton code font changed for one batch
Leaflet version 3 used until version 4 stock arrives"""),
"customerComplaint": rows("""Broken tablets found in blister strip, Medicura depot Nagpur
Discoloured tablets reported by a retail pharmacy
Bottle cap loose on arrival at hospital store
Foreign particle on tablet surface reported by a patient
Batch number not legible on carton
Blister pocket empty in one strip
Expiry date mismatch between carton and blister reported
Leaflet missing in carton at institutional supply
2D code not readable at the distributor scan
Short quantity in shipper at Kenya importer"""),
"maintenanceWorkOrder": rows("""Balance zero drift, dispensing booth 1
Impeller seal purge failure, granulator 1
Steam valve actuator failure, fluid bed dryer air handling unit
Blender drive belt replacement
Lower punch replacement, station 17, tablet press 1
Atomising air regulator replacement, coating pan 1
Capping chuck insert replacement, head 3
Sealing roller replacement, blister line 1
Serialisation print head cleaning and alignment
Leaflet feeder suction cup replacement, cartoner"""),
"controlledDocument": rows("""Master manufacturing record PCM500-B10 version 3
SOP cleaning of rapid mixer granulator SOP-PRD-014 revision 6
Specification Paracetamol 500 mg film-coated tablets SPEC-FP-PCM500 revision 4
SOP line clearance of packing lines SOP-PKG-003 revision 8
Validation report process validation PCM500 VR-PV-2026-07
Certificate of analysis Paracetamol IP lot DFC-260904-11
Executed batch record copy, batch PCM5B26091
Calibration certificate platform balance G-BAL-150, 15 September 2026
Packaging artwork carton PCM500 10 x 10 revision 5
SOP dispensing of raw materials SOP-WH-007 revision 9"""),
"traceInvestigation": rows("""Forward trace, API lot DFC-260904-11 after assay deviation
Reverse trace, carton serial 0890000400184 for leaflet missing complaint
Forward trace, MCC lot BEX-260830-07 after second source change
Reverse trace, bottle batch PCM5H26091 with loose caps
Forward trace, granulation lot PCM5G26091-S1 after high LOD
Forward trace, coated tablet lot PCM5F26091-P1 after tablet weight drift
Reverse trace, batch PCM5B26093 on quality hold
Forward trace, foil lot MFL-260902-03, supplier audit sample
Reverse trace, carton serial 0890000400301 for distributor audit
Forward trace, coated tablet lot PCM5F26091-P2 after twinning"""),
}

KEYPOOL = {
"remarks": rows("""No abnormality observed
Completed after line clearance verification
Short quantity carried to next shift
Delayed by 20 minutes for QC release of granules
Checked with the production supervisor
Run under planned deviation
Retest done after leak tester verification
Priority raised by planning for export order
Verified against the master manufacturing record
Handed over to shift B"""),
"comment": rows("""Verified against the master manufacturing record version 3
Approved after three validation batches
Reviewed with the QA head
No impact on product quality
Approved subject to stability data
Checked against the batch formula
Process capability data attached
Old artwork stock to be destroyed
Change parts confirmed by engineering
Training of all three shifts completed"""),
"reasonText": rows("""Issue to dispensing against process order
Release after QC approval
Issue to granulation suite
Return of unused excipient after dispensing
Transfer to quarantine after deviation
Rejection after QA disposition
Batch receipt from secondary packing
Goods issue against distributor order
Cycle count correction
Move to dispatch dock for loading"""),
"vehicleNo": rows("""MH12 PH 2231
MH14 QA 7718
MH12 LT 4406
MH42 BD 1907
MH12 SN 5524
MH14 KT 0369
GJ05 CU 7781
MH04 HD 3350
MH12 VR 8862
KA01 MF 2290"""),
"driverName": rows("""Sachin Gaikwad
Vinod Pawar
Rajendra Kale
Sunil Mhaske
Arjun Lokhande
Dinesh Patole
Hitesh Patel
Manoj Bhosale
Ravi Thorat
Shivakumar Gowda"""),
}

# ---- scope (owner decision of 12 Oct 2026): computed from the BMR / MMR common lists and their required references (D061)
COMMONAPP = ["u_mes_mast_country", "u_mes_mast_currency", "u_mes_mast_employmentType", "u_mes_mast_language", "u_mes_mast_signatureMeaning",
 "u_mes_syst_notificationType", "u_mes_syst_statusDefinition", "u_mes_syst_statusTransition"]
GMPONLY = ["u_mes_bmr_batchManufacturingRecord", "u_mes_bmr_batchRecordReview", "u_mes_bmr_batchRecordReviewException", "u_mes_bmr_batchRelease", "u_mes_bmr_yieldReconciliation",
 "u_mes_maint_cleaningRecord", "u_mes_maint_equipmentQualification", "u_mes_maint_logbookEntry", "u_mes_matl_dispenseRecord", "u_mes_mmr_masterManufacturingRecord",
 "u_mes_mmr_masterManufacturingRecordRecipe", "u_mes_plan_lineClearance", "u_mes_qual_environmentalMonitoringPoint", "u_mes_qual_environmentalMonitoringResult",
 "u_mes_qual_processValidation", "u_mes_qual_productQualityReview", "u_mes_qual_productRecall", "u_mes_qual_productRecallLot", "u_mes_qual_retentionSample",
 "u_mes_qual_riskAssessment", "u_mes_syst_auditTrailReview", "u_mes_syst_computerisedSystem", "u_mes_syst_systemPeriodicReview", "u_mes_syst_systemValidation",
 "u_mes_syst_userAccessReview", "u_mes_syst_userAccessReviewLine"]
DUAL = ['u_mes_maint_maintenanceWorkOrder', 'u_mes_maint_tool', 'u_mes_maint_toolType', 'u_mes_mast_area', 'u_mes_mast_commodity', 'u_mes_mast_costCenter', 'u_mes_mast_customer', 'u_mes_mast_department', 'u_mes_mast_designation', 'u_mes_mast_enterprise', 'u_mes_mast_equipment', 'u_mes_mast_equipmentType', 'u_mes_mast_line', 'u_mes_mast_manufacturer', 'u_mes_mast_role', 'u_mes_mast_shift', 'u_mes_mast_site', 'u_mes_mast_skill', 'u_mes_mast_skillCategory', 'u_mes_mast_supplier', 'u_mes_mast_supplierSuppliedItem', 'u_mes_mast_transporter', 'u_mes_mast_unitOfMeasure', 'u_mes_mast_user', 'u_mes_mast_workCalendar', 'u_mes_mast_workCenter', 'u_mes_matl_exposureTimer', 'u_mes_matl_goodsReceipt', 'u_mes_matl_kit', 'u_mes_matl_kitLine', 'u_mes_matl_label', 'u_mes_matl_labelTemplate', 'u_mes_matl_labelTemplateField', 'u_mes_matl_materialConsumption', 'u_mes_matl_materialMovement', 'u_mes_matl_movementType', 'u_mes_matl_packType', 'u_mes_matl_packagingSpecification', 'u_mes_matl_packagingSpecificationLevel', 'u_mes_matl_shipment', 'u_mes_matl_stockStatus', 'u_mes_matl_storageLocation', 'u_mes_perf_leakTestResult', 'u_mes_perf_leakTestResultStage', 'u_mes_perf_lossCategory', 'u_mes_perf_processReading', 'u_mes_perf_processTag', 'u_mes_perf_reasonCategory', 'u_mes_perf_reasonCode', 'u_mes_perf_torqueResult', 'u_mes_plan_changeover', 'u_mes_plan_container', 'u_mes_plan_containerType', 'u_mes_plan_documentAcknowledgement', 'u_mes_plan_interlockEvent', 'u_mes_plan_labourBooking', 'u_mes_plan_lot', 'u_mes_plan_lotParentLot', 'u_mes_plan_operationExecution', 'u_mes_plan_operationExecutionDefectCode', 'u_mes_plan_operationExecutionTool', 'u_mes_plan_operatorSession', 'u_mes_plan_productionOrder', 'u_mes_plan_productionOrderLot', 'u_mes_plan_productionOrderRelease', 'u_mes_plan_recipeDownload', 'u_mes_plan_setupVerification', 'u_mes_plan_setupVerificationItem', 'u_mes_plan_stepCompletion', 'u_mes_plan_wipUnit', 'u_mes_prod_billOfMaterial', 'u_mes_prod_billOfMaterialComponent', 'u_mes_prod_billOfMaterialComponentAlternateItem', 'u_mes_prod_billOfMaterialComponentProductVariant', 'u_mes_prod_billOfProcess', 'u_mes_prod_billOfProcessStep', 'u_mes_prod_billOfProcessStepConsumedComponent', 'u_mes_prod_billOfProcessStepEquipment', 'u_mes_prod_billOfProcessStepInterlock', 'u_mes_prod_billOfProcessStepProcessParameter', 'u_mes_prod_billOfProcessStepRequiredSkill', 'u_mes_prod_billOfProcessStepTool', 'u_mes_prod_engineeringChange', 'u_mes_prod_engineeringChangeAffectedItem', 'u_mes_prod_engineeringChangeAffectedObject', 'u_mes_prod_engineeringChangeApproval', 'u_mes_prod_engineeringChangeControlledDocument', 'u_mes_prod_item', 'u_mes_prod_itemFamily', 'u_mes_prod_itemGroup', 'u_mes_prod_itemRevision', 'u_mes_prod_operation', 'u_mes_prod_ppeItem', 'u_mes_prod_productVariant', 'u_mes_prod_recipe', 'u_mes_prod_recipeControlledDocument', 'u_mes_prod_recipeParameter', 'u_mes_prod_recipeProductVariant', 'u_mes_prod_recipeStage', 'u_mes_prod_routing', 'u_mes_prod_routingStep', 'u_mes_prod_routingStepAlternateWorkCenter', 'u_mes_prod_routingStepNextStep', 'u_mes_prod_workInstruction', 'u_mes_prod_workInstructionKeyPoint', 'u_mes_prod_workInstructionPpeItem', 'u_mes_prod_workInstructionProductVariant', 'u_mes_prod_workInstructionStep', 'u_mes_prod_workInstructionStepCharacteristic', 'u_mes_prod_workInstructionStepMediaControlledDocument', 'u_mes_prod_workInstructionStepProductVariant', 'u_mes_prod_workInstructionStepTool', 'u_mes_prod_workInstructionWorkCenter', 'u_mes_qual_capa', 'u_mes_qual_characteristic', 'u_mes_qual_characteristicPosition', 'u_mes_qual_checkSheet', 'u_mes_qual_checkSheetItem', 'u_mes_qual_checkSheetResult', 'u_mes_qual_checkSheetResultAnswer', 'u_mes_qual_complaintType', 'u_mes_qual_controlPlan', 'u_mes_qual_controlPlanCoreTeamUser', 'u_mes_qual_controlPlanLine', 'u_mes_qual_curveEnvelope', 'u_mes_qual_curveEnvelopeWindow', 'u_mes_qual_customerComplaint', 'u_mes_qual_defectCode', 'u_mes_qual_defectGroup', 'u_mes_qual_defectRecord', 'u_mes_qual_deviationPermit', 'u_mes_qual_dispositionType', 'u_mes_qual_gauge', 'u_mes_qual_gaugeCalibration', 'u_mes_qual_gaugeCalibrationReading', 'u_mes_qual_gaugeType', 'u_mes_qual_inspectionPlan', 'u_mes_qual_inspectionPlanLine', 'u_mes_qual_inspectionPlanProductVariant', 'u_mes_qual_inspectionResult', 'u_mes_qual_measurementCurve', 'u_mes_qual_nonconformance', 'u_mes_qual_pfmea', 'u_mes_qual_qualityHold', 'u_mes_qual_reworkOrder', 'u_mes_qual_samplingPlan', 'u_mes_qual_samplingPlanSizeRow', 'u_mes_qual_scrapRecord', 'u_mes_qual_spcChart', 'u_mes_qual_spcSample', 'u_mes_syst_auditTrail', 'u_mes_syst_auditTrailChange', 'u_mes_syst_controlledDocument', 'u_mes_syst_deviceType', 'u_mes_syst_documentType', 'u_mes_syst_electronicSignature', 'u_mes_syst_enumerationValue', 'u_mes_syst_integrationConnector', 'u_mes_syst_interlockRule', 'u_mes_syst_iotDevice', 'u_mes_syst_numberRange', 'u_mes_syst_recordPolicy', 'u_mes_trac_asBuiltRecord', 'u_mes_trac_asBuiltRecordComponent', 'u_mes_trac_asBuiltRecordInspectionResult', 'u_mes_trac_asBuiltRecordOperation', 'u_mes_trac_componentLotLink', 'u_mes_trac_genealogyLink', 'u_mes_trac_serialNumber', 'u_mes_trac_traceInvestigation']

TITLES["engineeringChange"] = MASTER.pop("engineeringChange")
