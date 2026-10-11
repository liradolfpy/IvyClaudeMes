// Indexes for u_mes_prod_billOfProcessStepInterlock
db.getCollection("u_mes_prod_billOfProcessStepInterlock").createIndex({ billOfProcessStepId: 1, sequenceNo: 1 }, { name: "ux_billOfProcessStepId_sequenceNo", unique: true });
