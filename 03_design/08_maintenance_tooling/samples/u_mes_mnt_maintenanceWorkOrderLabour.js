// Sample document for u_mes_mnt_maintenanceWorkOrderLabour (illustrative; seed data is generated separately)
db.getCollection("u_mes_mnt_maintenanceWorkOrderLabour").insertOne({
  _id: "MWO-2026-000341-L001",
  recordNo: "2026-000341-L001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  maintenanceWorkOrderId: "MWO-2026-000341",
  maintenanceWorkOrderName: "Nutrunner rundown fault, station 1",
  sequenceNo: NumberInt(1),
  userId: "USR-10112",
  userName: "Imran Shaikh",
  labourMinutes: NumberInt(35),
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10112",
  createdBy: "Imran Shaikh",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10112",
  updatedBy: "Imran Shaikh"
});
