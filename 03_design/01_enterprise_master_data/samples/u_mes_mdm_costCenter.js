// Sample document for u_mes_mdm_costCenter (illustrative; seed data is generated separately)
db.getCollection("u_mes_mdm_costCenter").insertOne({
  _id: "CC-5120",
  recordNo: "5120",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Assembly Line 1",
  description: "Assembly Line 1",
  erpCostCenterCode: "PN015120",
  validFrom: ISODate("2026-03-31T18:30:00.000+0000"),
  validTo: ISODate("2027-03-31T18:29:59.000+0000"),
  status: "Active",
  schemaVersion: NumberInt(1)
});
