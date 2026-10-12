// Indexes for u_mes_syst_modelPrediction
db.getCollection("u_mes_syst_modelPrediction").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_modelPrediction").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_modelPrediction").createIndex({ analyticsModelId: 1 }, { name: "ix_analyticsModelId" });
db.getCollection("u_mes_syst_modelPrediction").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_syst_modelPrediction").createIndex({ productVariantId: 1 }, { name: "ix_productVariantId" });
db.getCollection("u_mes_syst_modelPrediction").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_syst_modelPrediction").createIndex({ notificationId: 1 }, { name: "ix_notificationId" });
db.getCollection("u_mes_syst_modelPrediction").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_syst_modelPrediction").createIndex({ siteId: 1, predictedAt: -1 }, { name: "ix_siteId_predictedAt" });
