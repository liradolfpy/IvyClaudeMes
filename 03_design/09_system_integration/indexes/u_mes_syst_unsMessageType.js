// Indexes for u_mes_syst_unsMessageType
db.getCollection("u_mes_syst_unsMessageType").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_unsMessageType").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_unsMessageType").createIndex({ unsNamespace: 1, messageTypeCode: 1, payloadSchemaVersion: 1 }, { name: "ux_unsNamespace_messageTypeCode_payloadSchemaVersion", unique: true });
