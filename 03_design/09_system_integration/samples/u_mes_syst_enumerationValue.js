// Sample document for u_mes_syst_enumerationValue (illustrative; seed data is generated separately)
db.getCollection("u_mes_syst_enumerationValue").insertOne({
  _id: "ENV-operationExecution.result.OK",
  recordNo: "operationExecution.result.OK",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  collectionName: "u_mes_plan_operationExecution",
  fieldName: "result",
  valueCode: "OK",
  valueName: "OK",
  description: "Operation finished within all limits",
  sequenceNo: NumberInt(1),
  isDefault: true,
  status: "Active",
  schemaVersion: NumberInt(1)
});
