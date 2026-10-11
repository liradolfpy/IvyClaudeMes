// Indexes for u_mes_plan_containerLot
db.getCollection("u_mes_plan_containerLot").createIndex({ containerId: 1, lotId: 1 }, { name: "ux_containerId_lotId", unique: true });
db.getCollection("u_mes_plan_containerLot").createIndex({ lotId: 1, containerId: 1 }, { name: "ix_lotId_containerId" });
