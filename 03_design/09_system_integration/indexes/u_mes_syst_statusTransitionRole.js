// Indexes for u_mes_syst_statusTransitionRole
db.getCollection("u_mes_syst_statusTransitionRole").createIndex({ statusTransitionId: 1, roleId: 1 }, { name: "ux_statusTransitionId_roleId", unique: true });
db.getCollection("u_mes_syst_statusTransitionRole").createIndex({ roleId: 1, statusTransitionId: 1 }, { name: "ix_roleId_statusTransitionId" });
