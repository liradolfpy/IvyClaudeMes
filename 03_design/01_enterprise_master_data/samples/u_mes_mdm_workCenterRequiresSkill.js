// Sample document for u_mes_mdm_workCenterRequiresSkill (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_workCenterRequiresSkill").insertOne({
  _id: "WC-TRQ-01-RS001",
  recordNo: "TRQ-01-RS001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  workCenterId: "WC-TRQ-01",
  workCenterName: "Bleed Screw Torque Station",
  sequenceNo: NumberInt(1),
  requiresSkillId: "SKL-LEAK-TEST-OP",
  requiresSkillName: "Leak Test Operation",
  schemaVersion: NumberInt(1)
});
