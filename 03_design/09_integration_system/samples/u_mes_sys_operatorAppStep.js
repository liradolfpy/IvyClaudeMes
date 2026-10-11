// Sample document for u_mes_sys_operatorAppStep (illustrative; seed data is generated separately)
db.getCollection("u_mes_sys_operatorAppStep").insertOne({
  _id: "APP-APP-TRQ-01-S001",
  recordNo: "APP-TRQ-01-S001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  operatorAppId: "APP-APP-TRQ-01",
  operatorAppName: "Torque station operator app",
  stepNo: NumberInt(70),
  name: "Tighten and confirm result",
  widgetType: "Work Instruction",
  workInstructionId: "WI-WI-OP070-001",
  workInstructionName: "Bleed screw tightening - Front caliper LH",
  inspectionPlanId: "IP-OP030-INP-01",
  inspectionPlanName: "Machining in-process inspection, caliper body LH",
  nextStepNo: NumberInt(80),
  schemaVersion: NumberInt(1)
});
