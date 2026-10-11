// Indexes for u_mes_syst_iotDevice
db.getCollection("u_mes_syst_iotDevice").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_iotDevice").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_iotDevice").createIndex({ deviceTypeId: 1 }, { name: "ix_deviceTypeId" });
db.getCollection("u_mes_syst_iotDevice").createIndex({ manufacturerId: 1 }, { name: "ix_manufacturerId" });
db.getCollection("u_mes_syst_iotDevice").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_syst_iotDevice").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_syst_iotDevice").createIndex({ integrationConnectorId: 1 }, { name: "ix_integrationConnectorId" });
