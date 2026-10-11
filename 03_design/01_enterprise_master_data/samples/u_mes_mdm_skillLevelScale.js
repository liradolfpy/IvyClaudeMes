// Sample document for u_mes_mdm_skillLevelScale (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_skillLevelScale").insertOne({
  _id: "SKL-LEAK-TEST-OP-LS001",
  recordNo: "LEAK-TEST-OP-LS001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  skillId: "SKL-LEAK-TEST-OP",
  skillName: "Leak Test Operation",
  sequenceNo: NumberInt(1),
  level: NumberInt(3),
  description: "Works independently to standard and can react to abnormalities",
  schemaVersion: NumberInt(1)
});
