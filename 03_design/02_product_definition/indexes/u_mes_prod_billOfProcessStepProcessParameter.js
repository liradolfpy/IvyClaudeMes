// Indexes for u_mes_prod_billOfProcessStepProcessParameter
db.getCollection("u_mes_prod_billOfProcessStepProcessParameter").createIndex({ billOfProcessStepId: 1, sequenceNo: 1 }, { name: "ux_billOfProcessStepId_sequenceNo", unique: true });
db.getCollection("u_mes_prod_billOfProcessStepProcessParameter").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
