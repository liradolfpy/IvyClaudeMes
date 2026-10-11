// Sample document for u_mes_mdm_designation (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_designation").insertOne({
  _id: "DSG-ASM-OPR",
  recordNo: "ASM-OPR",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Assembly Operator",
  description: "Operator on assembly and test stations",
  departmentId: "DEPT-PROD",
  departmentName: "Production",
  gradeLevel: NumberInt(3),
  isSupervisory: true,
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
