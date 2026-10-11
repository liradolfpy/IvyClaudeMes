// Indexes for u_mes_mdm_rolePermission
db.getCollection("u_mes_mdm_rolePermission").createIndex({ roleId: 1, permissionId: 1 }, { name: "ux_roleId_permissionId", unique: true });
db.getCollection("u_mes_mdm_rolePermission").createIndex({ permissionId: 1, roleId: 1 }, { name: "ix_permissionId_roleId" });
