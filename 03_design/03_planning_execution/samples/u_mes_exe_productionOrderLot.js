// Sample document for u_mes_exe_productionOrderLot (illustrative; seed data is generated separately)
db.getCollection("u_mes_exe_productionOrderLot").insertOne({
  _id: "PO-1000412-L001",
  recordNo: "1000412-L001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  productionOrderId: "PO-1000412",
  productionOrderName: "1000412",
  sequenceNo: NumberInt(1),
  lotId: "LOT-L260928-GDC-014",
  lotName: "L260928-GDC-014",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
