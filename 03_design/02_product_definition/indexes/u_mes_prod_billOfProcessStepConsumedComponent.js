// Indexes for u_mes_prod_billOfProcessStepConsumedComponent
db.getCollection("u_mes_prod_billOfProcessStepConsumedComponent").createIndex({ billOfProcessStepId: 1, sequenceNo: 1 }, { name: "ux_billOfProcessStepId_sequenceNo", unique: true });
db.getCollection("u_mes_prod_billOfProcessStepConsumedComponent").createIndex({ itemId: 1 }, { name: "ix_itemId" });
