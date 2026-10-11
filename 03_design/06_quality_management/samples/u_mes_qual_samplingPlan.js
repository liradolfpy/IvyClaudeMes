// Sample document for u_mes_qual_samplingPlan (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_samplingPlan").insertOne({
  _id: "SMP-AQL-1.0-II",
  recordNo: "AQL-1.0-II",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "AQL 1.0, general inspection level II",
  samplingType: "Attribute AQL",
  standard: "IATF 16949:2016",
  inspectionLevel: "II",
  aql: NumberDecimal("1.0"),
  frequencyType: "Every N Units",
  frequencyEveryNUnits: NumberInt(50),
  frequencyEveryMinutes: NumberInt(120),
  skipLotEnabled: false,
  skipLotConsecutiveAcceptedToSkip: NumberInt(10),
  skipLotSkipFraction: NumberDecimal("0.5"),
  switchingRules: "Tightened after 2 of 5 lots rejected; normal after 5 consecutive accepted",
  status: "Active",
  schemaVersion: NumberInt(1)
});
