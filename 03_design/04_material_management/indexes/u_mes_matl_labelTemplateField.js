// Indexes for u_mes_matl_labelTemplateField
db.getCollection("u_mes_matl_labelTemplateField").createIndex({ labelTemplateId: 1, sequenceNo: 1 }, { name: "ux_labelTemplateId_sequenceNo", unique: true });
