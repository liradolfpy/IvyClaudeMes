// Indexes for u_mes_syst_controlledDocument
db.getCollection("u_mes_syst_controlledDocument").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_controlledDocument").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_controlledDocument").createIndex({ documentTypeId: 1 }, { name: "ix_documentTypeId" });
db.getCollection("u_mes_syst_controlledDocument").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_syst_controlledDocument").createIndex({ languageId: 1 }, { name: "ix_languageId" });
db.getCollection("u_mes_syst_controlledDocument").createIndex({ authorUserId: 1 }, { name: "ix_authorUserId" });
db.getCollection("u_mes_syst_controlledDocument").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_syst_controlledDocument").createIndex({ siteId: 1, approvedAt: -1 }, { name: "ix_siteId_approvedAt" });
