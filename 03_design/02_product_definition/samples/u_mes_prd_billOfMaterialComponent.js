// Sample document for u_mes_prd_billOfMaterialComponent (illustrative; seed data is generated separately)
db.getCollection("u_mes_prd_billOfMaterialComponent").insertOne({
  _id: "BOM-5110-10-0100-D-01-C001",
  recordNo: "5110-10-0100-D-01-C001",
  siteId: "SITE-PN1",
  siteName: "Chakan Plant, Pune",
  billOfMaterialId: "BOM-5110-10-0100-D-01",
  billOfMaterialName: "5110-10-0100-D-01",
  lineNo: NumberInt(10),
  componentItemId: "ITM-5110-30-0010",
  componentItemName: "Piston, dia 54 mm, steel, chrome plated",
  quantity: NumberDecimal("1"),
  unitOfMeasureId: "UOM-EA",
  unitOfMeasureName: "Each",
  scrapPct: NumberDecimal("0.5"),
  operationId: "OPN-OP070",
  operationName: "Bleed screw torque",
  isTraceable: true,
  traceLevel: "Lot",
  backflush: false,
  referenceDesignator: "P1",
  schemaVersion: NumberInt(1)
});
