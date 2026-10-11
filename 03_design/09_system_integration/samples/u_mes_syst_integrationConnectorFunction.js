// Sample document for u_mes_syst_integrationConnectorFunction (illustrative; seed data is generated separately)
db.getCollection("u_mes_syst_integrationConnectorFunction").insertOne({
  _id: "ICN-ERP-PRD-F001",
  recordNo: "ERP-PRD-F001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  integrationConnectorId: "ICN-ERP-PRD",
  integrationConnectorName: "ERP production interface",
  sequenceNo: NumberInt(1),
  functionName: "postOperationConfirmation",
  direction: "Inbound",
  messageType: "Production Order Download",
  endpointPath: "/v1/confirmations",
  scheduleExpression: "*/5 * * * *",
  schemaVersion: NumberInt(1)
});
