// Sample document for u_mes_prod_engineeringChangeAffectedItem (illustrative; seed data is generated separately)
db.getCollection("u_mes_prod_engineeringChangeAffectedItem").insertOne({
  _id: "ECN-2026-0031-AI001",
  recordNo: "2026-0031-AI001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  engineeringChangeId: "ECN-2026-0031",
  engineeringChangeName: "Bleed screw torque window revised",
  sequenceNo: NumberInt(1),
  itemId: "ITM-5110-10-0100",
  itemName: "Front Brake Caliper Assembly, LH",
  fromRevision: "C",
  toRevision: "D",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
