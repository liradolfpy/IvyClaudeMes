// Sample document for u_mes_prd_recipeParameter (illustrative; seed data is generated separately)
db.getCollection("u_mes_prd_recipeParameter").insertOne({
  _id: "RCP-TRQ-PRG-07-P001",
  recordNo: "TRQ-PRG-07-P001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  recipeId: "RCP-TRQ-PRG-07",
  recipeName: "Bleed screw M10 torque program",
  sequenceNo: NumberInt(1),
  name: "Target torque",
  processTagId: "TAG-PN1.GDC01.DIE_TEMP_UPPER",
  processTagName: "Die temperature, upper half, casting machine 1",
  setPoint: NumberDecimal("14.0"),
  lowerLimit: NumberDecimal("12.0"),
  upperLimit: NumberDecimal("16.0"),
  unitOfMeasureId: "UOM-NM",
  unitOfMeasureName: "Newton metre",
  isCritical: true,
  downloadToController: true,
  schemaVersion: NumberInt(1)
});
