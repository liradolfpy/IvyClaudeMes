// Sample document for u_mes_prod_engineeringChangeAffectedObject (illustrative; seed data is generated separately)
db.getCollection("u_mes_prod_engineeringChangeAffectedObject").insertOne({
  _id: "ECN-2026-0031-AO001",
  recordNo: "2026-0031-AO001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  engineeringChangeId: "ECN-2026-0031",
  engineeringChangeName: "Bleed screw torque window revised",
  sequenceNo: NumberInt(1),
  relatedCollectionName: "u_mes_plan_wipUnit",
  relatedEntityId: "WU-U260929A0184",
  relatedEntityName: "U260929A0184",
  changeAction: "Update",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
