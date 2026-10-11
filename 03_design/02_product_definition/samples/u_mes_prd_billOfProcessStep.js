// Sample document for u_mes_prd_billOfProcessStep (illustrative; seed data is generated separately)
db.getCollection("u_mes_prd_billOfProcessStep").insertOne({
  _id: "BOP-5110-10-0100-BOP01-S001",
  recordNo: "5110-10-0100-BOP01-S001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  billOfProcessId: "BOP-5110-10-0100-BOP01",
  billOfProcessName: "5110-10-0100-BOP01",
  stepNo: NumberInt(70),
  operationId: "OPN-OP070",
  operationName: "Bleed screw torque",
  recipeId: "RCP-TRQ-PRG-07",
  recipeName: "Bleed screw M10 torque program",
  workInstructionId: "WI-WI-OP070-001",
  workInstructionName: "Bleed screw tightening - Front caliper LH",
  inspectionPlanId: "IP-OP030-INP-01",
  inspectionPlanName: "Machining in-process inspection, caliper body LH",
  cycleTimeSec: NumberDecimal("34.2"),
  manning: NumberInt(1),
  schemaVersion: NumberInt(1)
});
