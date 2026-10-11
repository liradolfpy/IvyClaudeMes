// Sample document for u_mes_ehs_injuryType (illustrative; seed data is generated separately)
db.getCollection("u_mes_ehs_injuryType").insertOne({
  _id: "INJ-CUT",
  recordNo: "CUT",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Cut",
  description: "Cut",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
