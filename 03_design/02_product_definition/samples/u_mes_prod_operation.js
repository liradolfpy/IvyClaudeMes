// Sample document for u_mes_prod_operation (illustrative; seed data is generated separately)
db.getCollection("u_mes_prod_operation").insertOne({
  _id: "OPN-OP070",
  recordNo: "OP070",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Bleed screw torque",
  operationType: "Assembly",
  description: "Tighten the bleed screw to the specified torque with the DC nutrunner",
  defaultWorkCenterId: "WC-TRQ-01",
  defaultWorkCenterName: "Bleed Screw Torque Station",
  trackingGrain: "Unit",
  standardCycleTimeSec: NumberDecimal("32.0"),
  standardSetupTimeMin: NumberInt(15),
  standardManning: NumberInt(1),
  isInspection: false,
  isSpecialProcess: false,
  specialProcessStandard: "CQI-9",
  requiresFirstOffApproval: true,
  erpControlKey: "PP01",
  sequenceHint: NumberInt(70),
  status: "Active",
  schemaVersion: NumberInt(1)
});
