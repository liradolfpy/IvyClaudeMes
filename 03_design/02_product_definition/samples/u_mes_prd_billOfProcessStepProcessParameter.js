// Sample document for u_mes_prd_billOfProcessStepProcessParameter (illustrative; seed data is generated separately)
db.getCollection("u_mes_prd_billOfProcessStepProcessParameter").insertOne({
  _id: "BOP-5110-10-0100-BOP01-S001-PP001",
  recordNo: "5110-10-0100-BOP01-S001-PP001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  billOfProcessStepId: "BOP-5110-10-0100-BOP01-S001",
  billOfProcessStepName: "5110-10-0100-BOP01-S001",
  sequenceNo: NumberInt(1),
  name: "Final torque",
  nominal: NumberDecimal("14.0"),
  lowerLimit: NumberDecimal("12.0"),
  upperLimit: NumberDecimal("16.0"),
  unitOfMeasureId: "UOM-NM",
  unitOfMeasureName: "Newton metre",
  schemaVersion: NumberInt(1)
});
