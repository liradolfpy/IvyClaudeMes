// Indexes for u_mes_qlt_checkSheetItem
db.getCollection("u_mes_qlt_checkSheetItem").createIndex({ checkSheetId: 1, itemNo: 1 }, { name: "ux_checkSheetId_itemNo", unique: true });
