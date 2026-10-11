// Sample document for u_mes_qual_defectCode (illustrative; seed data is generated separately)
db.getCollection("u_mes_qual_defectCode").insertOne({
  _id: "DEF-LK01",
  recordNo: "LK01",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Leak at piston seal",
  defectGroupId: "DGR-LEAK",
  defectGroupName: "Leak",
  description: "Pressure decay above limit traced to the piston seal",
  severity: NumberInt(8),
  defaultDispositionTypeId: "DSP-T-REWORK",
  defaultDispositionTypeName: "Rework",
  dispositionRoutingId: "RTG-5110-10-0100-R01",
  dispositionRoutingName: "Front caliper LH assembly routing",
  isSafetyRelated: false,
  requiresPhoto: false,
  requiresHold: false,
  scrapCostCategory: "Assembly Scrap",
  customerDefectCode: "SM-Q-0417",
  pfmeaFailureMode: "Fluid leak past piston seal",
  status: "Active",
  schemaVersion: NumberInt(1)
});
