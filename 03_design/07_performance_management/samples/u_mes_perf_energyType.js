// Sample document for u_mes_perf_energyType (illustrative; seed data is generated separately)
db.getCollection("u_mes_perf_energyType").insertOne({
  _id: "ENT-T-ELEC",
  recordNo: "ELEC",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Electricity",
  description: "Electricity",
  unitOfMeasureId: "UOM-KWH",
  unitOfMeasureName: "Kilowatt hour",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
