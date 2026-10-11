// Sample document for u_mes_maint_maintenancePlanRequiredSparePart (illustrative; seed data is generated separately)
db.getCollection("u_mes_maint_maintenancePlanRequiredSparePart").insertOne({
  _id: "MP-PM-LKT-01-M-RSP001",
  recordNo: "PM-LKT-01-M-RSP001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  maintenancePlanId: "MP-PM-LKT-01-M",
  maintenancePlanName: "Leak tester monthly preventive maintenance",
  sequenceNo: NumberInt(1),
  sparePartId: "SPR-SP-004417",
  sparePartName: "Socket 10 mm, 3/8 inch drive, for bleed screw nutrunner",
  quantity: NumberDecimal("1"),
  schemaVersion: NumberInt(1)
});
