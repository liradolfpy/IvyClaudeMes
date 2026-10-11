// Sample document for u_mes_ehs_incidentType (illustrative; seed data is generated separately)
db.getCollection("u_mes_ehs_incidentType").insertOne({
  _id: "ICT-NEAR-MISS",
  recordNo: "NEAR-MISS",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Near Miss",
  description: "Near Miss",
  isInjury: true,
  reportableToAuthority: false,
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
