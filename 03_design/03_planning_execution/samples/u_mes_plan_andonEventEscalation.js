// Sample document for u_mes_plan_andonEventEscalation (illustrative; seed data is generated separately)
db.getCollection("u_mes_plan_andonEventEscalation").insertOne({
  _id: "AND-20260929-0005-E001",
  recordNo: "20260929-0005-E001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  andonEventId: "AND-20260929-0005",
  andonEventName: "Leak test rejects repeating at station LKT-01",
  sequenceNo: NumberInt(1),
  level: NumberInt(3),
  escalatedAt: ISODate("2026-09-29T00:30:34.000+0000"),
  toUserId: "USR-10231",
  toUserName: "Sunil Jadhav",
  channel: "Mobile Push",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:30:34.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
