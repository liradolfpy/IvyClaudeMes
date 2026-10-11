// Indexes for u_mes_mat_labelTemplateField
db.getCollection("u_mes_mat_labelTemplateField").createIndex({ labelTemplateId: 1, sequenceNo: 1 }, { name: "ux_labelTemplateId_sequenceNo", unique: true });
