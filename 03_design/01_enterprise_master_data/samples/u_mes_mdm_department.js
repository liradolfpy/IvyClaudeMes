// Sample document for u_mes_mdm_department (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_department").insertOne({
  _id: "DEPT-PROD",
  recordNo: "PROD",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Production",
  description: "All manufacturing lines from casting to packing",
  parentDepartmentId: "DEPT-MFG",
  parentDepartmentName: "Manufacturing",
  headUserId: "USR-10019",
  headUserName: "Meera Deshpande",
  costCenterId: "CC-5120",
  costCenterName: "Assembly Line 1",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
