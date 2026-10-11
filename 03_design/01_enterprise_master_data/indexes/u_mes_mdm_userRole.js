// Indexes for u_mes_mdm_userRole
db.getCollection("u_mes_mdm_userRole").createIndex({ userId: 1, roleId: 1 }, { name: "ux_userId_roleId", unique: true });
db.getCollection("u_mes_mdm_userRole").createIndex({ roleId: 1, userId: 1 }, { name: "ix_roleId_userId" });
