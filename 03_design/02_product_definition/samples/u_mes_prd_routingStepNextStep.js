// Sample document for u_mes_prd_routingStepNextStep (illustrative; seed data is generated separately)
db.getCollection("u_mes_prd_routingStepNextStep").insertOne({
  _id: "RTG-5110-10-0100-R01-S001-NS001",
  recordNo: "5110-10-0100-R01-S001-NS001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  routingStepId: "RTG-5110-10-0100-R01-S001",
  routingStepName: "5110-10-0100-R01-S001",
  stepNo: NumberInt(70),
  nextStepCondition: "Result OK",
  schemaVersion: NumberInt(1)
});
