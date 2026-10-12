// Indexes for u_mes_syst_simulationStudy
db.getCollection("u_mes_syst_simulationStudy").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_simulationStudy").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_simulationStudy").createIndex({ recommendedRecipeId: 1 }, { name: "ix_recommendedRecipeId" });
db.getCollection("u_mes_syst_simulationStudy").createIndex({ rolloutProductionOrderId: 1 }, { name: "ix_rolloutProductionOrderId" });
db.getCollection("u_mes_syst_simulationStudy").createIndex({ resultControlledDocumentId: 1 }, { name: "ix_resultControlledDocumentId" });
db.getCollection("u_mes_syst_simulationStudy").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_syst_simulationStudy").createIndex({ siteId: 1, inputSnapshotAt: -1 }, { name: "ix_siteId_inputSnapshotAt" });
