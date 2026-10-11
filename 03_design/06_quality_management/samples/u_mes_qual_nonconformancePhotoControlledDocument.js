// Sample document for u_mes_qual_nonconformancePhotoControlledDocument (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_nonconformancePhotoControlledDocument").insertOne({
  _id: "NCR-2026-000118-PCD001",
  recordNo: "2026-000118-PCD001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  nonconformanceId: "NCR-2026-000118",
  nonconformanceName: "Leak test failures on caliper LH",
  sequenceNo: NumberInt(1),
  photoControlledDocumentId: "DOC-PHT-20260929-0031",
  photoControlledDocumentName: "Photo, leak at piston seal, unit U260929A0171",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
