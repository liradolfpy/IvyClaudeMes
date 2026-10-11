// Sample document for u_mes_mast_area (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_area").insertOne({
  _id: "AR-ASY",
  recordNo: "ASY",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Assembly and Test",
  areaType: "Production",
  parentAreaId: "AR-PRD",
  parentAreaName: "Production",
  costCenterId: "CC-5120",
  costCenterName: "Assembly Line 1",
  supervisorUserId: "USR-10045",
  supervisorUserName: "Rajesh Patil",
  floorAreaSqm: NumberDecimal("1850.0"),
  isProductionArea: true,
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
