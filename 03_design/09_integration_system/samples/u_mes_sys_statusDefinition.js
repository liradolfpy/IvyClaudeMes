// Sample document for u_mes_sys_statusDefinition (illustrative; seed data is generated separately)
db.getCollection("u_mes_sys_statusDefinition").insertOne({
  _id: "STD-productionOrder.IN_PROGRESS",
  recordNo: "productionOrder.IN_PROGRESS",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  collectionName: "u_mes_exe_productionOrder",
  fieldName: "status",
  statusCode: "IN_PROGRESS",
  statusName: "In Progress",
  description: "Order has at least one unit started",
  sequenceNo: NumberInt(1),
  isInitial: false,
  isFinal: false,
  colourCode: "#F5A623",
  status: "Active",
  schemaVersion: NumberInt(1)
});
