// Indexes for u_mes_maint_maintenancePlanRequiredSparePart
db.getCollection("u_mes_maint_maintenancePlanRequiredSparePart").createIndex({ maintenancePlanId: 1, sequenceNo: 1 }, { name: "ux_maintenancePlanId_sequenceNo", unique: true });
db.getCollection("u_mes_maint_maintenancePlanRequiredSparePart").createIndex({ sparePartId: 1 }, { name: "ix_sparePartId" });
