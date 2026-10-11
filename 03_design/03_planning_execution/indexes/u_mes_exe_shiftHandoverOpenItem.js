// Indexes for u_mes_exe_shiftHandoverOpenItem
db.getCollection("u_mes_exe_shiftHandoverOpenItem").createIndex({ shiftHandoverId: 1, itemNo: 1 }, { name: "ux_shiftHandoverId_itemNo", unique: true });
db.getCollection("u_mes_exe_shiftHandoverOpenItem").createIndex({ ownerUserId: 1 }, { name: "ix_ownerUserId" });
