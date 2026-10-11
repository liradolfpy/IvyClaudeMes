// Sample document for u_mes_qual_inspectionPlanLine (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_inspectionPlanLine").insertOne({
  _id: "IP-OP030-INP-01-L001",
  recordNo: "OP030-INP-01-L001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  inspectionPlanId: "IP-OP030-INP-01",
  inspectionPlanName: "Machining in-process inspection, caliper body LH",
  lineNo: NumberInt(10),
  characteristicId: "CHR-5110-20-0110-C012",
  characteristicName: "Piston bore diameter",
  gaugeId: "GAU-G-BG-054",
  gaugeName: "Bore gauge 50-75 mm",
  sampleSize: NumberInt(5),
  frequencyType: "Every N Units",
  frequencyValue: NumberDecimal("50"),
  recordType: "Measured Value",
  autoNcOnFail: true,
  defectCodeId: "DEF-LK01",
  defectCodeName: "Leak at piston seal",
  overrideAllowed: false,
  schemaVersion: NumberInt(1)
});
