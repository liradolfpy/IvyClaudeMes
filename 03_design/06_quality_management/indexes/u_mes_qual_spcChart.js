// Indexes for u_mes_qual_spcChart
db.getCollection("u_mes_qual_spcChart").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_spcChart").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_spcChart").createIndex({ characteristicId: 1 }, { name: "ix_characteristicId" });
db.getCollection("u_mes_qual_spcChart").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qual_spcChart").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_qual_spcChart").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_qual_spcChart").createIndex({ ownerUserId: 1 }, { name: "ix_ownerUserId" });
