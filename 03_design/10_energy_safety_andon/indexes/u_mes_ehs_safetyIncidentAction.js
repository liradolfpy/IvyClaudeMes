// Indexes for u_mes_ehs_safetyIncidentAction
db.getCollection("u_mes_ehs_safetyIncidentAction").createIndex({ safetyIncidentId: 1, actionNo: 1 }, { name: "ux_safetyIncidentId_actionNo", unique: true });
db.getCollection("u_mes_ehs_safetyIncidentAction").createIndex({ ownerUserId: 1 }, { name: "ix_ownerUserId" });
