// Indexes for u_mes_mnt_sparePartUsedOnEquipment
db.getCollection("u_mes_mnt_sparePartUsedOnEquipment").createIndex({ sparePartId: 1, usedOnEquipmentId: 1 }, { name: "ux_sparePartId_usedOnEquipmentId", unique: true });
db.getCollection("u_mes_mnt_sparePartUsedOnEquipment").createIndex({ usedOnEquipmentId: 1, sparePartId: 1 }, { name: "ix_usedOnEquipmentId_sparePartId" });
