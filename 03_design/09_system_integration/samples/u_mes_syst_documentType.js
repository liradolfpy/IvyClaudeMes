// Sample document for u_mes_syst_documentType (illustrative; seed data is generated separately)
db.getCollection("u_mes_syst_documentType").insertOne({
  _id: "DCT-DRAWING",
  recordNo: "DRAWING",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Drawing",
  description: "Drawing",
  retentionYears: NumberInt(15),
  isControlled: true,
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
