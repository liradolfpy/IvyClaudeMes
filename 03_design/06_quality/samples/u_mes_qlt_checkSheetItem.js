// Sample document for u_mes_qlt_checkSheetItem (illustrative; seed data is generated separately)
db.getCollection("u_mes_qlt_checkSheetItem").insertOne({
  _id: "CKS-TRQ-01-SOS-I001",
  recordNo: "TRQ-01-SOS-I001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  checkSheetId: "CKS-TRQ-01-SOS",
  checkSheetName: "Start of shift check, torque station",
  itemNo: NumberInt(1),
  question: "Is the master leak part detected as Not OK by the tester?",
  answerType: "Yes No",
  expectedAnswer: "Yes",
  lowerLimit: NumberDecimal("12.0"),
  upperLimit: NumberDecimal("16.0"),
  unitText: "N.m",
  isCritical: true,
  reactionOnFail: "Stop the station and call the line leader",
  schemaVersion: NumberInt(1)
});
