// Indexes for u_mes_mast_equipment
db.getCollection("u_mes_mast_equipment").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_mast_equipment").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_mast_equipment").createIndex({ equipmentTypeId: 1 }, { name: "ix_equipmentTypeId" });
db.getCollection("u_mes_mast_equipment").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_mast_equipment").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_mast_equipment").createIndex({ parentEquipmentId: 1 }, { name: "ix_parentEquipmentId" });
db.getCollection("u_mes_mast_equipment").createIndex({ manufacturerId: 1 }, { name: "ix_manufacturerId" });
