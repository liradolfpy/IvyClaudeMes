// Sample document for u_mes_sys_statusTransition (illustrative; seed data is generated separately)
db.getCollection("u_mes_sys_statusTransition").insertOne({
  _id: "STT-productionOrder.RELEASED-IN_PROGRESS",
  recordNo: "productionOrder.RELEASED-IN_PROGRESS",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  collectionName: "u_mes_exe_productionOrder",
  fromStatusDefinitionId: "STD-productionOrder.RELEASED",
  fromStatusDefinitionName: "Released",
  toStatusDefinitionId: "STD-productionOrder.IN_PROGRESS",
  toStatusDefinitionName: "In Progress",
  transitionName: "Start production",
  requiresSignature: true,
  requiresReason: false,
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
