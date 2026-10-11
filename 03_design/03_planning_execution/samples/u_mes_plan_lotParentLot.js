// Sample document for u_mes_plan_lotParentLot (illustrative; seed data is generated separately)
db.getCollection("u_mes_plan_lotParentLot").insertOne({
  _id: "LOT-L260928-GDC-014-PL001",
  recordNo: "L260928-GDC-014-PL001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  lotId: "LOT-L260928-GDC-014",
  lotName: "L260928-GDC-014",
  sequenceNo: NumberInt(1),
  parentLotId: "LOT-S260914-PST-007",
  parentLotName: "S260914-PST-007",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
