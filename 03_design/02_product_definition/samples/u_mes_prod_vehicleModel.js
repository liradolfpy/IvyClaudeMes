// Sample document for u_mes_prod_vehicleModel (illustrative; seed data is generated separately)
db.getCollection("u_mes_prod_vehicleModel").insertOne({
  _id: "VHM-SM-X42",
  recordNo: "SM-X42",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Sahyadri X42",
  description: "Sahyadri X42",
  customerId: "CUS-SML",
  customerName: "Sahyadri Motors Ltd.",
  modelYear: NumberInt(2026),
  platformCode: "X4",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
