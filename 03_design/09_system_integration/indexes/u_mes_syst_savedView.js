// Indexes for u_mes_syst_savedView
db.getCollection("u_mes_syst_savedView").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_savedView").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_savedView").createIndex({ ownerUserId: 1 }, { name: "ix_ownerUserId" });
db.getCollection("u_mes_syst_savedView").createIndex({ roleId: 1 }, { name: "ix_roleId" });
