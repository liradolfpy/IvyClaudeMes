// Sample document for u_mes_prod_billOfProcessStepConsumedComponent (illustrative; seed data is generated separately)
db.getCollection("u_mes_prod_billOfProcessStepConsumedComponent").insertOne({
  _id: "BOP-5110-10-0100-BOP01-S001-CC001",
  recordNo: "5110-10-0100-BOP01-S001-CC001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  billOfProcessStepId: "BOP-5110-10-0100-BOP01-S001",
  billOfProcessStepName: "5110-10-0100-BOP01-S001",
  sequenceNo: NumberInt(1),
  itemId: "ITM-5110-10-0100",
  itemName: "Front Brake Caliper Assembly, LH",
  quantity: NumberDecimal("1"),
  verifyByScan: true,
  schemaVersion: NumberInt(1)
});
