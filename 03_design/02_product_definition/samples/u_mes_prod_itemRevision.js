// Sample document for u_mes_prod_itemRevision (illustrative; seed data is generated separately)
db.getCollection("u_mes_prod_itemRevision").insertOne({
  _id: "ITM-5110-10-0100-R001",
  recordNo: "5110-10-0100-R001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  itemId: "ITM-5110-10-0100",
  itemName: "Front Brake Caliper Assembly, LH",
  sequenceNo: NumberInt(1),
  revision: "D",
  engineeringChangeId: "ECN-2026-0031",
  engineeringChangeName: "Bleed screw torque window revised",
  effectiveFrom: ISODate("2026-03-31T18:30:00.000+0000"),
  description: "Bleed screw torque window revised to 14 +/- 2 N.m",
  schemaVersion: NumberInt(1)
});
