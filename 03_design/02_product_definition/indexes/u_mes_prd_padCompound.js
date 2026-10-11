// Indexes for u_mes_prd_padCompound
db.getCollection("u_mes_prd_padCompound").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_prd_padCompound").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
