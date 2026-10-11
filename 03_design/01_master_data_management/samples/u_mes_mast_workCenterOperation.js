// Sample document for u_mes_mast_workCenterOperation (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_workCenterOperation").insertOne({
  _id: "WC-TRQ-01-O001",
  recordNo: "TRQ-01-O001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  workCenterId: "WC-TRQ-01",
  workCenterName: "Bleed Screw Torque Station",
  sequenceNo: NumberInt(1),
  operationId: "OPN-OP070",
  operationName: "Bleed screw torque",
  schemaVersion: NumberInt(1)
});
