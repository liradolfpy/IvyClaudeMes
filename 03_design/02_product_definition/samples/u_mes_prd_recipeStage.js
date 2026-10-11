// Sample document for u_mes_prd_recipeStage (illustrative; seed data is generated separately)
db.getCollection("u_mes_prd_recipeStage").insertOne({
  _id: "RCP-TRQ-PRG-07-S001",
  recordNo: "TRQ-PRG-07-S001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  recipeId: "RCP-TRQ-PRG-07",
  recipeName: "Bleed screw M10 torque program",
  stageNo: NumberInt(2),
  name: "Final tightening",
  durationSec: NumberInt(42),
  setPoint: NumberDecimal("14.0"),
  schemaVersion: NumberInt(1)
});
