// Indexes for u_mes_mdm_skillOperation
db.getCollection("u_mes_mdm_skillOperation").createIndex({ skillId: 1, operationId: 1 }, { name: "ux_skillId_operationId", unique: true });
db.getCollection("u_mes_mdm_skillOperation").createIndex({ operationId: 1, skillId: 1 }, { name: "ix_operationId_skillId" });
