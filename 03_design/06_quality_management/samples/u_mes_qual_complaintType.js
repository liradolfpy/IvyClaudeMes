// Sample document for u_mes_qual_complaintType (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_complaintType").insertOne({
  _id: "CPT-LINE-REJ",
  recordNo: "LINE-REJ",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Line Rejection",
  description: "Line Rejection",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
