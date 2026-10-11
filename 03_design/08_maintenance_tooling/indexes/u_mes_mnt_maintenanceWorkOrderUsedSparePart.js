// Indexes for u_mes_mnt_maintenanceWorkOrderUsedSparePart
db.getCollection("u_mes_mnt_maintenanceWorkOrderUsedSparePart").createIndex({ maintenanceWorkOrderId: 1, sequenceNo: 1 }, { name: "ux_maintenanceWorkOrderId_sequenceNo", unique: true });
db.getCollection("u_mes_mnt_maintenanceWorkOrderUsedSparePart").createIndex({ sparePartId: 1 }, { name: "ix_sparePartId" });
