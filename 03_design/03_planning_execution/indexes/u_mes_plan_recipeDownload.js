// Indexes for u_mes_plan_recipeDownload
db.getCollection("u_mes_plan_recipeDownload").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_recipeDownload").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_recipeDownload").createIndex({ recipeId: 1 }, { name: "ix_recipeId" });
db.getCollection("u_mes_plan_recipeDownload").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_plan_recipeDownload").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_plan_recipeDownload").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_plan_recipeDownload").createIndex({ productVariantId: 1 }, { name: "ix_productVariantId" });
db.getCollection("u_mes_plan_recipeDownload").createIndex({ siteId: 1, downloadedAt: -1 }, { name: "ix_siteId_downloadedAt" });
