// Sample document for u_mes_syst_notificationType (illustrative; seed data is generated separately)
db.getCollection("u_mes_syst_notificationType").insertOne({
  _id: "NTT-ANDON-ESC",
  recordNo: "ANDON-ESC",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  name: "Andon Escalation",
  description: "Andon Escalation",
  sequenceNo: NumberInt(1),
  status: "Active",
  schemaVersion: NumberInt(1)
});
