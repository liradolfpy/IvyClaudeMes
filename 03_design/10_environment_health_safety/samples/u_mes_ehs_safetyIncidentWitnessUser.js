// Sample document for u_mes_ehs_safetyIncidentWitnessUser (illustrative; seed data is generated separately)
db.getCollection("u_mes_ehs_safetyIncidentWitnessUser").insertOne({
  _id: "SAF-2026-0003-WU001",
  recordNo: "2026-0003-WU001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  safetyIncidentId: "SAF-2026-0003",
  safetyIncidentName: "Coolant spill near HMC-01 walkway",
  sequenceNo: NumberInt(1),
  witnessUserId: "USR-10019",
  witnessUserName: "Meera Deshpande",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
