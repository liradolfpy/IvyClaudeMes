// Sample document for u_mes_mast_employmentType (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_employmentType").insertOne({
  _id: "EMT-PERM",
  recordNo: "PERM",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Permanent",
  description: "On the company payroll without end date",
  isContract: true,
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
