// Sample document for u_mes_mdm_workCenterEquipment (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_workCenterEquipment").insertOne({
  _id: "WC-TRQ-01-E001",
  recordNo: "TRQ-01-E001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  workCenterId: "WC-TRQ-01",
  workCenterName: "Bleed Screw Torque Station",
  sequenceNo: NumberInt(1),
  equipmentId: "EQ-TRQ-01-NR1",
  equipmentName: "DC Nutrunner Station 1",
  schemaVersion: NumberInt(1)
});
