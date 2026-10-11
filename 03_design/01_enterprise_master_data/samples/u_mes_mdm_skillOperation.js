// Sample document for u_mes_mdm_skillOperation (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_skillOperation").insertOne({
  _id: "SKL-LEAK-TEST-OP-O001",
  recordNo: "LEAK-TEST-OP-O001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  skillId: "SKL-LEAK-TEST-OP",
  skillName: "Leak Test Operation",
  sequenceNo: NumberInt(1),
  operationId: "OPN-OP070",
  operationName: "Bleed screw torque",
  schemaVersion: NumberInt(1)
});
