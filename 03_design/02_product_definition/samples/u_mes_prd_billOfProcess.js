// Sample document for u_mes_prd_billOfProcess (illustrative; seed data is generated separately)
db.getCollection("u_mes_prd_billOfProcess").insertOne({
  _id: "BOP-5110-10-0100-BOP01",
  recordNo: "5110-10-0100-BOP01",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  itemId: "ITM-5110-10-0100",
  itemName: "Front Brake Caliper Assembly, LH",
  itemRevision: "D",
  routingId: "RTG-5110-10-0100-R01",
  routingName: "Front caliper LH assembly routing",
  bopVersion: NumberInt(1),
  effectiveFrom: ISODate("2026-03-31T18:30:00.000+0000"),
  effectiveTo: ISODate("2027-03-31T18:29:59.000+0000"),
  billOfMaterialId: "BOM-5110-10-0100-D-01",
  billOfMaterialName: "5110-10-0100-D-01",
  approvedById: "USR-10019",
  approvedBy: "Meera Deshpande",
  approvedAt: ISODate("2026-03-31T18:30:00.000+0000"),
  status: "Released",
  schemaVersion: NumberInt(1)
});
