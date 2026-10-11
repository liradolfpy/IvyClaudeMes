// Sample document for u_mes_qual_pfmea (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_pfmea").insertOne({
  _id: "FMEA-5110-10-0100-PF",
  recordNo: "5110-10-0100-PF",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  title: "Process FMEA, Front Brake Caliper Assembly LH",
  itemId: "ITM-5110-10-0100",
  itemName: "Front Brake Caliper Assembly, LH",
  itemRevision: "D",
  version: NumberInt(3),
  methodology: "AIAG-VDA",
  controlPlanId: "CP-5110-10-0100-PROD",
  controlPlanName: "5110-10-0100-PROD",
  originalDate: ISODate("2026-03-31T18:30:00.000+0000"),
  revisionDate: ISODate("2026-03-31T18:30:00.000+0000"),
  approvedById: "USR-10019",
  approvedBy: "Meera Deshpande",
  approvedAt: ISODate("2026-03-31T18:30:00.000+0000"),
  status: "Released",
  schemaVersion: NumberInt(1)
});
