// Sample document for u_mes_mast_roleSignatureMeaning (illustrative; seed data is generated separately)
db.getCollection("u_mes_mast_roleSignatureMeaning").insertOne({
  _id: "ROLE-OPERATOR-SM001",
  recordNo: "OPERATOR-SM001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  roleId: "ROLE-OPERATOR",
  roleName: "Production Operator",
  sequenceNo: NumberInt(1),
  signatureMeaningId: "SGM-APPROVED",
  signatureMeaningName: "Approved",
  schemaVersion: NumberInt(1)
});
