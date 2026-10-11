// Sample document for u_mes_qual_samplingPlanSizeRow (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_samplingPlanSizeRow").insertOne({
  _id: "SMP-AQL-1.0-II-SR001",
  recordNo: "AQL-1.0-II-SR001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  samplingPlanId: "SMP-AQL-1.0-II",
  samplingPlanName: "AQL 1.0, general inspection level II",
  sequenceNo: NumberInt(1),
  lotSizeFrom: NumberInt(281),
  lotSizeTo: NumberInt(500),
  sampleSize: NumberInt(5),
  acceptNumber: NumberInt(1),
  rejectNumber: NumberInt(2),
  schemaVersion: NumberInt(1)
});
