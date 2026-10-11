// Indexes for u_mes_prd_workInstruction
db.getCollection("u_mes_prd_workInstruction").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_prd_workInstruction").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_prd_workInstruction").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_prd_workInstruction").createIndex({ operationId: 1 }, { name: "ix_operationId" });
db.getCollection("u_mes_prd_workInstruction").createIndex({ languageId: 1 }, { name: "ix_languageId" });
db.getCollection("u_mes_prd_workInstruction").createIndex({ engineeringChangeId: 1 }, { name: "ix_engineeringChangeId" });
db.getCollection("u_mes_prd_workInstruction").createIndex({ authorUserId: 1 }, { name: "ix_authorUserId" });
