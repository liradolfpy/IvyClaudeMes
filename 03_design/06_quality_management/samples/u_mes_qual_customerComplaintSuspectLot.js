// Sample document for u_mes_qual_customerComplaintSuspectLot (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_customerComplaintSuspectLot").insertOne({
  _id: "CMP-2026-0004-SL001",
  recordNo: "2026-0004-SL001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  customerComplaintId: "CMP-2026-0004",
  customerComplaintName: "Bleed screw cap missing on three calipers at customer line",
  sequenceNo: NumberInt(1),
  suspectLotId: "LOT-L260928-GDC-014",
  suspectLotName: "L260928-GDC-014",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10087",
  createdBy: "Anita Kulkarni",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10087",
  updatedBy: "Anita Kulkarni"
});
