// Sample document for u_mes_mat_shipmentLineLot (illustrative; seed data is generated separately)
db.getCollection("u_mes_mat_shipmentLineLot").insertOne({
  _id: "SHP-2026-000377-L001-L001",
  recordNo: "2026-000377-L001-L001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  shipmentLineId: "SHP-2026-000377-L001",
  shipmentLineName: "2026-000377-L001",
  sequenceNo: NumberInt(1),
  lotId: "LOT-L260928-GDC-014",
  lotName: "L260928-GDC-014",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10150",
  createdBy: "Vikram Pawar",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10150",
  updatedBy: "Vikram Pawar"
});
