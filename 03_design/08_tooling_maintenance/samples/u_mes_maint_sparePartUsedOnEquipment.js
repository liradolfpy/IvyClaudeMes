// Sample document for u_mes_maint_sparePartUsedOnEquipment (illustrative; seed data is generated separately)
db.getCollection("u_mes_maint_sparePartUsedOnEquipment").insertOne({
  _id: "SPR-SP-004417-UOE001",
  recordNo: "SP-004417-UOE001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  sparePartId: "SPR-SP-004417",
  sparePartName: "Socket 10 mm, 3/8 inch drive, for bleed screw nutrunner",
  sequenceNo: NumberInt(1),
  usedOnEquipmentId: "EQ-TRQ-01-NR1",
  usedOnEquipmentName: "DC Nutrunner Station 1",
  schemaVersion: NumberInt(1)
});
