// Sample document for u_mes_syst_operatorAppStepTrigger (illustrative; seed data is generated separately)
db.getCollection("u_mes_syst_operatorAppStepTrigger").insertOne({
  _id: "APP-APP-TRQ-01-S001-T001",
  recordNo: "APP-TRQ-01-S001-T001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  operatorAppStepId: "APP-APP-TRQ-01-S001",
  operatorAppStepName: "APP-TRQ-01-S001",
  sequenceNo: NumberInt(1),
  triggerEvent: "Device Result Received",
  triggerAction: "Go To Step",
  triggerTarget: "30",
  schemaVersion: NumberInt(1)
});
