// Indexes for u_mes_qlt_checkSheetResultAnswer
db.getCollection("u_mes_qlt_checkSheetResultAnswer").createIndex({ checkSheetResultId: 1, itemNo: 1 }, { name: "ux_checkSheetResultId_itemNo", unique: true });
