// Sample document for u_mes_qual_qualityHoldHeldObject (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_qualityHoldHeldObject").insertOne({
  _id: "HLD-2026-000021-HO001",
  recordNo: "2026-000021-HO001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  qualityHoldId: "HLD-2026-000021",
  qualityHoldName: "2026-000021",
  sequenceNo: NumberInt(1),
  relatedCollectionName: "u_mes_plan_wipUnit",
  relatedEntityId: "WU-U260929A0184",
  relatedEntityName: "U260929A0184",
  quantity: NumberInt(1),
  releasedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  releaseDecision: "Released",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
