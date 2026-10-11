// Sample document for u_mes_prd_engineeringChangeControlledDocument (illustrative; seed data is generated separately)
db.getCollection("u_mes_prd_engineeringChangeControlledDocument").insertOne({
  _id: "ECN-2026-0031-CD001",
  recordNo: "2026-0031-CD001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  engineeringChangeId: "ECN-2026-0031",
  engineeringChangeName: "Bleed screw torque window revised",
  sequenceNo: NumberInt(1),
  controlledDocumentId: "DOC-DRW-5110-10-0100-D",
  controlledDocumentName: "Drawing 5110-10-0100 revision D, Front Brake Caliper Assembly LH",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
