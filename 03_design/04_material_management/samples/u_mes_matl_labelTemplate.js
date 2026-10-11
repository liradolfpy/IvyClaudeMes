// Sample document for u_mes_matl_labelTemplate (illustrative; seed data is generated separately)
db.getCollection("u_mes_matl_labelTemplate").insertOne({
  _id: "LBT-SML-BIN-A5",
  recordNo: "SML-BIN-A5",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Sahyadri Motors bin label A5",
  labelType: "Container Label",
  customerId: "CUS-SML",
  customerName: "Sahyadri Motors Ltd.",
  standard: "IATF 16949:2016",
  widthMm: NumberDecimal("400.0"),
  heightMm: NumberDecimal("280.0"),
  printerLanguage: "ZPL",
  symbology: "Data Matrix ECC200",
  payloadPattern: "[)>{RS}06{GS}P{customerPartNo}{GS}Q{quantity}{GS}1T{lotNo}{RS}{EOT}",
  version: NumberInt(3),
  copies: NumberInt(1),
  effectiveFrom: ISODate("2026-03-31T18:30:00.000+0000"),
  status: "Released",
  schemaVersion: NumberInt(1)
});
