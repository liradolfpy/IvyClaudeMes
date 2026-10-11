// Sample document for u_mes_eqp_oeeRecordLoss (illustrative; seed data is generated separately)
db.getCollection("u_mes_eqp_oeeRecordLoss").insertOne({
  _id: "OEE-20260929-A-TRQ-01-NR1-L001",
  recordNo: "20260929-A-TRQ-01-NR1-L001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  oeeRecordId: "OEE-20260929-A-TRQ-01-NR1",
  oeeRecordName: "20260929-A-TRQ-01-NR1",
  sequenceNo: NumberInt(1),
  lossCategoryId: "LSC-BREAKDOWN",
  lossCategoryName: "Breakdown",
  reasonCodeId: "RSN-MECH-NR-02",
  reasonCodeName: "Nutrunner socket worn",
  lossMinutes: NumberInt(18),
  lossUnits: NumberInt(30),
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-SYSTEM",
  createdBy: "MES System",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-SYSTEM",
  updatedBy: "MES System"
});
