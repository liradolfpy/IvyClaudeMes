// Indexes for u_mes_mdm_lineDefaultShift
db.getCollection("u_mes_mdm_lineDefaultShift").createIndex({ lineId: 1, defaultShiftId: 1 }, { name: "ux_lineId_defaultShiftId", unique: true });
db.getCollection("u_mes_mdm_lineDefaultShift").createIndex({ defaultShiftId: 1, lineId: 1 }, { name: "ix_defaultShiftId_lineId" });
