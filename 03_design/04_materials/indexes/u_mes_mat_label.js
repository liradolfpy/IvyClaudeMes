// Indexes for u_mes_mat_label
db.getCollection("u_mes_mat_label").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mat_label").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mat_label").createIndex({ labelTemplateId: 1 }, { name: "ix_labelTemplateId" });
db.getCollection("u_mes_mat_label").createIndex({ wipUnitId: 1 }, { name: "ix_wipUnitId" });
db.getCollection("u_mes_mat_label").createIndex({ containerId: 1 }, { name: "ix_containerId" });
db.getCollection("u_mes_mat_label").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_mat_label").createIndex({ shipmentId: 1 }, { name: "ix_shipmentId" });
db.getCollection("u_mes_mat_label").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_mat_label").createIndex({ siteId: 1, printedAt: -1 }, { name: "ix_siteId_printedAt" });
