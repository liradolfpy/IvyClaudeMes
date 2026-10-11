// Sample document for u_mes_qlt_gaugeCalibrationReading (illustrative; seed data is generated separately)
db.getCollection("u_mes_qlt_gaugeCalibrationReading").insertOne({
  _id: "GCAL-G-BG-054-2026-02-R001",
  recordNo: "G-BG-054-2026-02-R001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  gaugeCalibrationId: "GCAL-G-BG-054-2026-02",
  gaugeCalibrationName: "G-BG-054-2026-02",
  sequenceNo: NumberInt(1),
  nominal: NumberDecimal("14.0"),
  asFound: NumberDecimal("54.001"),
  asLeft: NumberDecimal("54.000"),
  tolerance: NumberDecimal("0.002"),
  withinTolerance: true,
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
