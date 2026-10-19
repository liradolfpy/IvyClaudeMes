// Indexes for u_mes_syst_unsRejectedMessage
db.getCollection("u_mes_syst_unsRejectedMessage").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_unsRejectedMessage").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_unsRejectedMessage").createIndex({ iotHubIdentityId: 1 }, { name: "ix_iotHubIdentityId" });
db.getCollection("u_mes_syst_unsRejectedMessage").createIndex({ unsMessageTypeId: 1 }, { name: "ix_unsMessageTypeId" });
db.getCollection("u_mes_syst_unsRejectedMessage").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_syst_unsRejectedMessage").createIndex({ siteId: 1, messageTimestamp: -1 }, { name: "ix_siteId_messageTimestamp" });
db.getCollection("u_mes_syst_unsRejectedMessage").createIndex({ messageUuid: 1 }, { name: "ux_messageUuid", unique: true });
db.getCollection("u_mes_syst_unsRejectedMessage").createIndex({ siteId: 1, status: 1, receivedAt: -1 }, { name: "ix_siteId_status_receivedAt" });
