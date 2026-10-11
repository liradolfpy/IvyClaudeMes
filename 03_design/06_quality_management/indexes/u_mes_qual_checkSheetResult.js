// Indexes for u_mes_qual_checkSheetResult
db.getCollection("u_mes_qual_checkSheetResult").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_checkSheetResult").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_checkSheetResult").createIndex({ checkSheetId: 1 }, { name: "ix_checkSheetId" });
db.getCollection("u_mes_qual_checkSheetResult").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_qual_checkSheetResult").createIndex({ equipmentId: 1 }, { name: "ix_equipmentId" });
db.getCollection("u_mes_qual_checkSheetResult").createIndex({ shiftId: 1 }, { name: "ix_shiftId" });
db.getCollection("u_mes_qual_checkSheetResult").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_qual_checkSheetResult").createIndex({ siteId: 1, productionDate: -1 }, { name: "ix_siteId_productionDate" });
