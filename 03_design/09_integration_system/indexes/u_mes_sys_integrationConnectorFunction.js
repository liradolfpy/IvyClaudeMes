// Indexes for u_mes_sys_integrationConnectorFunction
db.getCollection("u_mes_sys_integrationConnectorFunction").createIndex({ integrationConnectorId: 1, sequenceNo: 1 }, { name: "ux_integrationConnectorId_sequenceNo", unique: true });
