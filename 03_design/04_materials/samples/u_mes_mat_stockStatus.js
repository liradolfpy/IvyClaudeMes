// Sample document for u_mes_mat_stockStatus (illustrative; seed data is generated separately)
db.getCollection("u_mes_mat_stockStatus").insertOne({
  _id: "STS-UNR",
  recordNo: "UNR",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Unrestricted",
  description: "Free to use",
  isUsable: true,
  erpStockType: "Unrestricted-use",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
