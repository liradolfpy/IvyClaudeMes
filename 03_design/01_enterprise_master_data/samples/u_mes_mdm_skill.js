// Sample document for u_mes_mdm_skill (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_skill").insertOne({
  _id: "SKL-LEAK-TEST-OP",
  recordNo: "LEAK-TEST-OP",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Leak Test Operation",
  skillCategoryId: "SKC-PROCESS",
  skillCategoryName: "Process",
  description: "Operate the pressure leak tester and react to a failed test",
  minimumLevelRequired: NumberInt(3),
  validityMonths: NumberInt(12),
  trainingControlledDocumentId: "DOC-TRN-LEAK-TEST-OP",
  trainingControlledDocumentName: "Training module, leak test operation",
  assessmentMethod: "Practical Test",
  isSafetyCritical: true,
  status: "Active",
  schemaVersion: NumberInt(1)
});
