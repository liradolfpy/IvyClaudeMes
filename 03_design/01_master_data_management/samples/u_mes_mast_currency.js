// Sample document for u_mes_mast_currency (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_currency").insertOne({
  _id: "CUR-INR",
  recordNo: "INR",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Indian Rupee",
  symbol: "N.m",
  decimalPlaces: NumberInt(1),
  isoNumericCode: "356",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
