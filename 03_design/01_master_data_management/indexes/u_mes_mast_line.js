// Indexes for u_mes_mast_line
db.getCollection("u_mes_mast_line").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mast_line").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mast_line").createIndex({ areaId: 1 }, { name: "ix_areaId" });
db.getCollection("u_mes_mast_line").createIndex({ itemFamilyId: 1 }, { name: "ix_itemFamilyId" });
db.getCollection("u_mes_mast_line").createIndex({ workCalendarId: 1 }, { name: "ix_workCalendarId" });
db.getCollection("u_mes_mast_line").createIndex({ bottleneckWorkCenterId: 1 }, { name: "ix_bottleneckWorkCenterId" });
db.getCollection("u_mes_mast_line").createIndex({ costCenterId: 1 }, { name: "ix_costCenterId" });
