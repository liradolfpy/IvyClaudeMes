// Sample document for u_mes_syst_auditTrailChange (illustrative; seed data is generated separately)
db.getCollection("u_mes_syst_auditTrailChange").insertOne({
  _id: "ADT-20260929-00004412-C001",
  recordNo: "20260929-00004412-C001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  auditTrailId: "ADT-20260929-00004412",
  auditTrailName: "20260929-00004412",
  sequenceNo: NumberInt(1),
  changedFieldName: "upperSpecLimit",
  oldValue: "15.5",
  newValue: "16.0",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-SYSTEM",
  createdBy: "MES System",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-SYSTEM",
  updatedBy: "MES System"
});
