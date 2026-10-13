// Indexes for u_mes_syst_computerisedSystem
db.getCollection("u_mes_syst_computerisedSystem").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_computerisedSystem").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_computerisedSystem").createIndex({ systemOwnerUserId: 1 }, { name: "ix_systemOwnerUserId" });
db.getCollection("u_mes_syst_computerisedSystem").createIndex({ processOwnerUserId: 1 }, { name: "ix_processOwnerUserId" });
db.getCollection("u_mes_syst_computerisedSystem").createIndex({ supplierId: 1 }, { name: "ix_supplierId" });
db.getCollection("u_mes_syst_computerisedSystem").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
