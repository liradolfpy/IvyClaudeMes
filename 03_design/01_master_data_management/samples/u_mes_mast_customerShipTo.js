// Sample document for u_mes_mast_customerShipTo (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_customerShipTo").insertOne({
  _id: "CUS-SML-ST001",
  recordNo: "SML-ST001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  customerId: "CUS-SML",
  customerName: "Sahyadri Motors Ltd.",
  sequenceNo: NumberInt(1),
  shipToCode: "SML-TLG-D4",
  name: "Sahyadri Motors Talegaon Plant, Dock 4",
  line1: "Gate 3, Chassis Assembly Shop",
  city: "Pune",
  state: "Maharashtra",
  postalCode: "410507",
  dockCode: "D4",
  transitDays: NumberInt(1),
  schemaVersion: NumberInt(1)
});
