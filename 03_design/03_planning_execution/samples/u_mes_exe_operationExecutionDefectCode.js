// Sample document for u_mes_exe_operationExecutionDefectCode (illustrative; seed data is generated separately)
db.getCollection("u_mes_exe_operationExecutionDefectCode").insertOne({
  _id: "OPX-20260929-000184-DC001",
  recordNo: "20260929-000184-DC001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  operationExecutionId: "OPX-20260929-000184",
  operationExecutionName: "20260929-000184",
  sequenceNo: NumberInt(1),
  defectCodeId: "DEF-LK01",
  defectCodeName: "Leak at piston seal",
  schemaVersion: NumberInt(1),
  createdAt: ISODate("2026-09-29T00:30:00.000+0000"),
  createdById: "USR-10231",
  createdBy: "Sunil Jadhav",
  updatedAt: ISODate("2026-09-29T00:30:00.000+0000"),
  updatedById: "USR-10231",
  updatedBy: "Sunil Jadhav"
});
