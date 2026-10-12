// Indexes for u_mes_qual_curveEnvelope
db.getCollection("u_mes_qual_curveEnvelope").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_curveEnvelope").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_curveEnvelope").createIndex({ characteristicId: 1 }, { name: "ix_characteristicId" });
db.getCollection("u_mes_qual_curveEnvelope").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qual_curveEnvelope").createIndex({ productVariantId: 1 }, { name: "ix_productVariantId" });
db.getCollection("u_mes_qual_curveEnvelope").createIndex({ operationId: 1 }, { name: "ix_operationId" });
db.getCollection("u_mes_qual_curveEnvelope").createIndex({ recipeId: 1 }, { name: "ix_recipeId" });
