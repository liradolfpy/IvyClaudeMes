// Sample document for u_mes_prd_billOfProcessStepRequiredSkill (illustrative; seed data is generated separately)
db.getCollection("u_mes_prd_billOfProcessStepRequiredSkill").insertOne({
  _id: "BOP-5110-10-0100-BOP01-S001-RS001",
  recordNo: "5110-10-0100-BOP01-S001-RS001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  billOfProcessStepId: "BOP-5110-10-0100-BOP01-S001",
  billOfProcessStepName: "5110-10-0100-BOP01-S001",
  sequenceNo: NumberInt(1),
  requiredSkillId: "SKL-LEAK-TEST-OP",
  requiredSkillName: "Leak Test Operation",
  schemaVersion: NumberInt(1)
});
