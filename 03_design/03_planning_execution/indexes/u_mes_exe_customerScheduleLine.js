// Indexes for u_mes_exe_customerScheduleLine
db.getCollection("u_mes_exe_customerScheduleLine").createIndex({ customerScheduleId: 1, lineNo: 1 }, { name: "ux_customerScheduleId_lineNo", unique: true });
db.getCollection("u_mes_exe_customerScheduleLine").createIndex({ itemId: 1 }, { name: "ix_itemId" });
