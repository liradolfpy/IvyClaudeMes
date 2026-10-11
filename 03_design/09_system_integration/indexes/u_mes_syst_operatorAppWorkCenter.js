// Indexes for u_mes_syst_operatorAppWorkCenter
db.getCollection("u_mes_syst_operatorAppWorkCenter").createIndex({ operatorAppId: 1, workCenterId: 1 }, { name: "ux_operatorAppId_workCenterId", unique: true });
db.getCollection("u_mes_syst_operatorAppWorkCenter").createIndex({ workCenterId: 1, operatorAppId: 1 }, { name: "ix_workCenterId_operatorAppId" });
