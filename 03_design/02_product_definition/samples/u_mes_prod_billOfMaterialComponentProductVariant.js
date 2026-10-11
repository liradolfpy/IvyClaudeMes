// Sample document for u_mes_prod_billOfMaterialComponentProductVariant (illustrative; seed data is generated separately)
db.getCollection("u_mes_prod_billOfMaterialComponentProductVariant").insertOne({
  _id: "BOM-5110-10-0100-D-01-C001-PV001",
  recordNo: "5110-10-0100-D-01-C001-PV001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  billOfMaterialComponentId: "BOM-5110-10-0100-D-01-C001",
  billOfMaterialComponentName: "5110-10-0100-D-01-C001",
  sequenceNo: NumberInt(1),
  productVariantId: "VAR-FBC-LH-STD",
  productVariantName: "Front Caliper LH Standard",
  schemaVersion: NumberInt(1)
});
