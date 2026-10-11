// Sample document for u_mes_ehs_andonType (illustrative; seed data is generated separately)
db.getCollection("u_mes_ehs_andonType").insertOne({
  _id: "ANT-QUALITY",
  recordNo: "QUALITY",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Quality",
  description: "Operator needs quality support at the station",
  colourCode: "#F5A623",
  responsibleDepartmentId: "DEPT-QUAL",
  responsibleDepartmentName: "Quality",
  targetResponseSec: NumberInt(300),
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
