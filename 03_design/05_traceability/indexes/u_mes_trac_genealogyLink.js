// Indexes for u_mes_trac_genealogyLink
db.getCollection("u_mes_trac_genealogyLink").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_trac_genealogyLink").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_trac_genealogyLink").createIndex({ parentWipUnitId: 1 }, { name: "ix_parentWipUnitId" });
db.getCollection("u_mes_trac_genealogyLink").createIndex({ parentSerialNumberId: 1 }, { name: "ix_parentSerialNumberId" });
db.getCollection("u_mes_trac_genealogyLink").createIndex({ parentItemId: 1 }, { name: "ix_parentItemId" });
db.getCollection("u_mes_trac_genealogyLink").createIndex({ childItemId: 1 }, { name: "ix_childItemId" });
db.getCollection("u_mes_trac_genealogyLink").createIndex({ childLotId: 1 }, { name: "ix_childLotId" });
db.getCollection("u_mes_trac_genealogyLink").createIndex({ siteId: 1, linkedAt: -1 }, { name: "ix_siteId_linkedAt" });
