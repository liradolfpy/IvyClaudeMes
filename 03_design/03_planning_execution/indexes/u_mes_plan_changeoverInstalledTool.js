// Indexes for u_mes_plan_changeoverInstalledTool
db.getCollection("u_mes_plan_changeoverInstalledTool").createIndex({ changeoverId: 1, installedToolId: 1 }, { name: "ux_changeoverId_installedToolId", unique: true });
db.getCollection("u_mes_plan_changeoverInstalledTool").createIndex({ installedToolId: 1, changeoverId: 1 }, { name: "ix_installedToolId_changeoverId" });
