// Indexes for u_mes_ehs_safetyIncident
db.getCollection("u_mes_ehs_safetyIncident").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_ehs_safetyIncident").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_ehs_safetyIncident").createIndex({ incidentTypeId: 1 }, { name: "ix_incidentTypeId" });
db.getCollection("u_mes_ehs_safetyIncident").createIndex({ areaId: 1 }, { name: "ix_areaId" });
db.getCollection("u_mes_ehs_safetyIncident").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_ehs_safetyIncident").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_ehs_safetyIncident").createIndex({ injuredUserId: 1 }, { name: "ix_injuredUserId" });
db.getCollection("u_mes_ehs_safetyIncident").createIndex({ siteId: 1, occurredAt: -1 }, { name: "ix_siteId_occurredAt" });
