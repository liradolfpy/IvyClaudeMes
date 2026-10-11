// Indexes for u_mes_prd_billOfProcessStepProcessParameter
db.getCollection("u_mes_prd_billOfProcessStepProcessParameter").createIndex({ billOfProcessStepId: 1, sequenceNo: 1 }, { name: "ux_billOfProcessStepId_sequenceNo", unique: true });
db.getCollection("u_mes_prd_billOfProcessStepProcessParameter").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
