// Sample document for u_mes_mast_signatureMeaning (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_signatureMeaning").insertOne({
  _id: "SGM-APPROVED",
  recordNo: "APPROVED",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Approved",
  description: "The signer approves the content",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
