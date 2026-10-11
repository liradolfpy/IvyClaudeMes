// Sample document for u_mes_plan_shiftHandoverOpenItem (illustrative; seed data is generated separately)
db.getCollection("u_mes_plan_shiftHandoverOpenItem").insertOne({
  _id: "SHO-20260929-ASY-01-A-OI001",
  recordNo: "20260929-ASY-01-A-OI001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  shiftHandoverId: "SHO-20260929-ASY-01-A",
  shiftHandoverName: "20260929-ASY-01-A",
  itemNo: NumberInt(1),
  description: "Verify seal lot S260921-SEL-004 before use on shift B",
  ownerUserId: "USR-10087",
  ownerUserName: "Anita Kulkarni",
  dueAt: ISODate("2026-10-01T00:30:00.000+0000"),
  closed: false,
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-10-01T00:30:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
