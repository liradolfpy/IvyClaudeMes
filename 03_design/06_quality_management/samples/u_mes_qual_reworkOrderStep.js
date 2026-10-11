// Sample document for u_mes_qual_reworkOrderStep (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_reworkOrderStep").insertOne({
  _id: "RWK-2026-000052-S001",
  recordNo: "2026-000052-S001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  reworkOrderId: "RWK-2026-000052",
  reworkOrderName: "2026-000052",
  stepNo: NumberInt(70),
  operationId: "OPN-OP070",
  operationName: "Bleed screw torque",
  description: "Remove piston and seal, inspect groove, fit new seal",
  completedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  completedById: "USR-10087",
  completedBy: "Anita Kulkarni",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
