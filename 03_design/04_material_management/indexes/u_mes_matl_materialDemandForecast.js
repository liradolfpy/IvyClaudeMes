// Indexes for u_mes_matl_materialDemandForecast
db.getCollection("u_mes_matl_materialDemandForecast").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_matl_materialDemandForecast").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_matl_materialDemandForecast").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_matl_materialDemandForecast").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_matl_materialDemandForecast").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_matl_materialDemandForecast").createIndex({ analyticsModelId: 1 }, { name: "ix_analyticsModelId" });
db.getCollection("u_mes_matl_materialDemandForecast").createIndex({ siteId: 1, productionDate: -1 }, { name: "ix_siteId_productionDate" });
