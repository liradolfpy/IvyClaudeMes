// Sample document for u_mes_qual_customerComplaintShipment (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_customerComplaintShipment").insertOne({
  _id: "CMP-2026-0004-S001",
  recordNo: "2026-0004-S001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  customerComplaintId: "CMP-2026-0004",
  customerComplaintName: "Bleed screw cap missing on three calipers at customer line",
  sequenceNo: NumberInt(1),
  shipmentId: "SHP-2026-000377",
  shipmentName: "2026-000377",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
