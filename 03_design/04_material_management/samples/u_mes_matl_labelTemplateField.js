// Sample document for u_mes_matl_labelTemplateField (illustrative; seed data is generated separately)
db.getCollection("u_mes_matl_labelTemplateField").insertOne({
  _id: "LBT-SML-BIN-A5-F001",
  recordNo: "SML-BIN-A5-F001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  labelTemplateId: "LBT-SML-BIN-A5",
  labelTemplateName: "Sahyadri Motors bin label A5",
  sequenceNo: NumberInt(1),
  fieldName: "customerPartNo",
  source: "MES Terminal",
  fieldFormat: "%s",
  positionXMm: NumberDecimal("8.0"),
  positionYMm: NumberDecimal("12.5"),
  isBarcode: true,
  schemaVersion: NumberInt(1)
});
