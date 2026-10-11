// Sample document for u_mes_prd_routingStep (illustrative; seed data is generated separately)
db.getCollection("u_mes_prd_routingStep").insertOne({
  _id: "RTG-5110-10-0100-R01-S001",
  recordNo: "5110-10-0100-R01-S001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  routingId: "RTG-5110-10-0100-R01",
  routingName: "Front caliper LH assembly routing",
  stepNo: NumberInt(70),
  operationId: "OPN-OP070",
  operationName: "Bleed screw torque",
  workCenterId: "WC-TRQ-01",
  workCenterName: "Bleed Screw Torque Station",
  cycleTimeSec: NumberDecimal("34.2"),
  setupTimeMin: NumberInt(15),
  isMilestone: true,
  isOptional: false,
  reworkReturnStepNo: NumberInt(80),
  maxQueueTimeMin: NumberInt(240),
  maxReworkCount: NumberInt(2),
  schemaVersion: NumberInt(1)
});
