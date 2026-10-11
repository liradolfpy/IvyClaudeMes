// Sample document for u_mes_sys_controlledDocumentTag (illustrative; seed data is generated separately)
db.getCollection("u_mes_sys_controlledDocumentTag").insertOne({
  _id: "DOC-DRW-5110-10-0100-D-T001",
  recordNo: "DRW-5110-10-0100-D-T001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  controlledDocumentId: "DOC-DRW-5110-10-0100-D",
  controlledDocumentName: "Drawing 5110-10-0100 revision D, Front Brake Caliper Assembly LH",
  sequenceNo: NumberInt(1),
  tag: "caliper",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
