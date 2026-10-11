// Sample document for u_mes_prd_workInstructionStep (illustrative; seed data is generated separately)
db.getCollection("u_mes_prd_workInstructionStep").insertOne({
  _id: "WI-WI-OP070-001-S001",
  recordNo: "WI-OP070-001-S001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  workInstructionId: "WI-WI-OP070-001",
  workInstructionName: "Bleed screw tightening - Front caliper LH",
  stepNo: NumberInt(70),
  title: "Tighten bleed screw",
  instructionText: "Place the bleed screw in the socket and press both start buttons",
  inputType: "Confirmation",
  expectedValue: NumberDecimal("14.0"),
  lowerLimit: NumberDecimal("12.0"),
  upperLimit: NumberDecimal("16.0"),
  isMandatory: true,
  requiresScan: true,
  caution: "Do not reuse a bleed screw that has been tightened once",
  standardTimeSec: NumberDecimal("12.0"),
  schemaVersion: NumberInt(1)
});
