// Sample document for u_mes_prod_operationRequiredSkill (illustrative; seed data is generated separately)
db.getCollection("u_mes_prod_operationRequiredSkill").insertOne({
  _id: "OPN-OP070-RS001",
  recordNo: "OP070-RS001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  operationId: "OPN-OP070",
  operationName: "Bleed screw torque",
  sequenceNo: NumberInt(1),
  requiredSkillId: "SKL-LEAK-TEST-OP",
  requiredSkillName: "Leak Test Operation",
  schemaVersion: NumberInt(1)
});
