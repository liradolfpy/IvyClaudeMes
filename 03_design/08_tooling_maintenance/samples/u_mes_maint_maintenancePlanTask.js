// Sample document for u_mes_maint_maintenancePlanTask (illustrative; seed data is generated separately)
db.getCollection("u_mes_maint_maintenancePlanTask").insertOne({
  _id: "MP-PM-LKT-01-M-T001",
  recordNo: "PM-LKT-01-M-T001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  maintenancePlanId: "MP-PM-LKT-01-M",
  maintenancePlanName: "Leak tester monthly preventive maintenance",
  taskNo: NumberInt(10),
  description: "Verify tester with the 0.5 sccm master leak and record the reading",
  standardMinutes: NumberInt(15),
  requiresShutdown: false,
  acceptanceCriteria: "Master leak 0.5 sccm detected within plus or minus 10 percent",
  schemaVersion: NumberInt(1)
});
