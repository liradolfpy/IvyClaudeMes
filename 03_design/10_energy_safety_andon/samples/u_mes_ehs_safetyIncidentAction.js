// Sample document for u_mes_ehs_safetyIncidentAction (illustrative; seed data is generated separately)
db.getCollection("u_mes_ehs_safetyIncidentAction").insertOne({
  _id: "SAF-2026-0003-A001",
  recordNo: "2026-0003-A001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  safetyIncidentId: "SAF-2026-0003",
  safetyIncidentName: "Coolant spill near HMC-01 walkway",
  actionNo: NumberInt(1),
  description: "Replace coolant hose and add drip tray under the HMC-01 coupling",
  ownerUserId: "USR-10087",
  ownerUserName: "Anita Kulkarni",
  dueAt: ISODate("2026-10-01T00:30:00.000+0000"),
  completedAt: ISODate("2026-09-29T00:35:00.000+0000"),
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-10-01T00:30:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
