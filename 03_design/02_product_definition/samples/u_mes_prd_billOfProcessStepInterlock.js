// Sample document for u_mes_prd_billOfProcessStepInterlock (illustrative; seed data is generated separately)
db.getCollection("u_mes_prd_billOfProcessStepInterlock").insertOne({
  _id: "BOP-5110-10-0100-BOP01-S001-I001",
  recordNo: "5110-10-0100-BOP01-S001-I001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  billOfProcessStepId: "BOP-5110-10-0100-BOP01-S001",
  billOfProcessStepName: "5110-10-0100-BOP01-S001",
  sequenceNo: NumberInt(1),
  interlockType: "Skill",
  description: "Operator must hold a valid certification for skill LEAK-TEST-OP at level 3 or higher",
  enforced: true,
  schemaVersion: NumberInt(1)
});
