// Indexes for u_mes_exe_lotParentLot
db.getCollection("u_mes_exe_lotParentLot").createIndex({ lotId: 1, parentLotId: 1 }, { name: "ux_lotId_parentLotId", unique: true });
db.getCollection("u_mes_exe_lotParentLot").createIndex({ parentLotId: 1, lotId: 1 }, { name: "ix_parentLotId_lotId" });
