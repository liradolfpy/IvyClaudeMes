// Sample document for u_mes_exe_productionOrderRelease (illustrative; seed data is generated separately)
db.getCollection("u_mes_exe_productionOrderRelease").insertOne({
  _id: "PO-1000412-R001",
  recordNo: "1000412-R001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  productionOrderId: "PO-1000412",
  productionOrderName: "1000412",
  releaseNo: NumberInt(1),
  quantity: NumberInt(1),
  releasedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  releasedById: "USR-10019",
  releasedBy: "Meera Deshpande",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
