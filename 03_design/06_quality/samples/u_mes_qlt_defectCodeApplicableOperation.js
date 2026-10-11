// Sample document for u_mes_qlt_defectCodeApplicableOperation (illustrative; seed data is generated separately)
db.getCollection("u_mes_qlt_defectCodeApplicableOperation").insertOne({
  _id: "DEF-LK01-AO001",
  recordNo: "LK01-AO001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  defectCodeId: "DEF-LK01",
  defectCodeName: "Leak at piston seal",
  sequenceNo: NumberInt(1),
  applicableOperationId: "OPN-OP070",
  applicableOperationName: "Bleed screw torque",
  schemaVersion: NumberInt(1)
});
