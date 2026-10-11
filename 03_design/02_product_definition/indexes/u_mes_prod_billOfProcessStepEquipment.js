// Indexes for u_mes_prod_billOfProcessStepEquipment
db.getCollection("u_mes_prod_billOfProcessStepEquipment").createIndex({ billOfProcessStepId: 1, equipmentId: 1 }, { name: "ux_billOfProcessStepId_equipmentId", unique: true });
db.getCollection("u_mes_prod_billOfProcessStepEquipment").createIndex({ equipmentId: 1, billOfProcessStepId: 1 }, { name: "ix_equipmentId_billOfProcessStepId" });
