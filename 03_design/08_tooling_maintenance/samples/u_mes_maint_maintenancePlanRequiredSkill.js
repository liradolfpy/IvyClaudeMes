// Sample document for u_mes_maint_maintenancePlanRequiredSkill (illustrative; seed data is generated separately)
db.getCollection("u_mes_maint_maintenancePlanRequiredSkill").insertOne({
  _id: "MP-PM-LKT-01-M-RS001",
  recordNo: "PM-LKT-01-M-RS001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  maintenancePlanId: "MP-PM-LKT-01-M",
  maintenancePlanName: "Leak tester monthly preventive maintenance",
  sequenceNo: NumberInt(1),
  requiredSkillId: "SKL-LEAK-TEST-OP",
  requiredSkillName: "Leak Test Operation",
  schemaVersion: NumberInt(1)
});
