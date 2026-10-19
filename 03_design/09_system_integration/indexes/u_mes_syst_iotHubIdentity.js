// Indexes for u_mes_syst_iotHubIdentity
db.getCollection("u_mes_syst_iotHubIdentity").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_iotHubIdentity").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_iotHubIdentity").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_syst_iotHubIdentity").createIndex({ iotDeviceId: 1 }, { name: "ix_iotDeviceId" });
db.getCollection("u_mes_syst_iotHubIdentity").createIndex({ parentIotHubIdentityId: 1 }, { name: "ix_parentIotHubIdentityId" });
db.getCollection("u_mes_syst_iotHubIdentity").createIndex({ provisioningStatus: 1 }, { name: "ix_provisioningStatus" });
