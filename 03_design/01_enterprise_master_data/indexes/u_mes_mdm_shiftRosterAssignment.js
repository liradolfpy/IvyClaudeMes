// Indexes for u_mes_mdm_shiftRosterAssignment
db.getCollection("u_mes_mdm_shiftRosterAssignment").createIndex({ shiftRosterId: 1, sequenceNo: 1 }, { name: "ux_shiftRosterId_sequenceNo", unique: true });
db.getCollection("u_mes_mdm_shiftRosterAssignment").createIndex({ userId: 1 }, { name: "ix_userId" });
db.getCollection("u_mes_mdm_shiftRosterAssignment").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_mdm_shiftRosterAssignment").createIndex({ replacedUserId: 1 }, { name: "ix_replacedUserId" });
