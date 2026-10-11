// Indexes for u_mes_qual_defectCodeApplicableOperation
db.getCollection("u_mes_qual_defectCodeApplicableOperation").createIndex({ defectCodeId: 1, applicableOperationId: 1 }, { name: "ux_defectCodeId_applicableOperationId", unique: true });
db.getCollection("u_mes_qual_defectCodeApplicableOperation").createIndex({ applicableOperationId: 1, defectCodeId: 1 }, { name: "ix_applicableOperationId_defectCodeId" });
