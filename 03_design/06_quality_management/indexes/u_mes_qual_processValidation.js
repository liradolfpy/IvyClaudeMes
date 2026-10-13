// Indexes for u_mes_qual_processValidation
db.getCollection("u_mes_qual_processValidation").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_processValidation").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_processValidation").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qual_processValidation").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_qual_processValidation").createIndex({ engineeringChangeId: 1 }, { name: "ix_engineeringChangeId" });
db.getCollection("u_mes_qual_processValidation").createIndex({ protocolControlledDocumentId: 1 }, { name: "ix_protocolControlledDocumentId" });
db.getCollection("u_mes_qual_processValidation").createIndex({ reportControlledDocumentId: 1 }, { name: "ix_reportControlledDocumentId" });
db.getCollection("u_mes_qual_processValidation").createIndex({ siteId: 1, plannedStartDate: -1 }, { name: "ix_siteId_plannedStartDate" });
