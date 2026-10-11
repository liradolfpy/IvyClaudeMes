// Sample document for u_mes_mat_shipmentLine (illustrative; seed data is generated separately)
db.getCollection("u_mes_mat_shipmentLine").insertOne({
  _id: "SHP-2026-000377-L001",
  recordNo: "2026-000377-L001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  shipmentId: "SHP-2026-000377",
  shipmentName: "2026-000377",
  lineNo: NumberInt(10),
  itemId: "ITM-5110-10-0100",
  itemName: "Front Brake Caliper Assembly, LH",
  customerPartNo: "SM-3501-0421-LH",
  quantity: NumberInt(1),
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10150",
  createdBy: "Vikram Pawar",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10150",
  updatedBy: "Vikram Pawar"
});
