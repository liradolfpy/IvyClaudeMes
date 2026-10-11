// Sample document for u_mes_syst_systemConfiguration (illustrative; seed data is generated separately)
db.getCollection("u_mes_syst_systemConfiguration").insertOne({
  _id: "CFG-oee.plannedTimeBasis",
  recordNo: "oee.plannedTimeBasis",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  module: "Performance",
  description: "Time basis used as the denominator of availability",
  valueType: "Text",
  configValueText: "Planned Production Time",
  configValueNumber: null,
  configValueFlag: false,
  configValueJson: null,
  scope: "Enterprise",
  isEditable: true,
  isSecret: false,
  validFrom: ISODate("2026-03-31T18:30:00.000+0000"),
  lastChangedReason: "Aligned with corporate OEE definition",
  status: "Active",
  schemaVersion: NumberInt(1)
});
