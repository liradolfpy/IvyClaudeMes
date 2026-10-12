// Indexes for u_mes_plan_setupVerificationItem
db.getCollection("u_mes_plan_setupVerificationItem").createIndex({ setupVerificationId: 1, itemNo: 1 }, { name: "ux_setupVerificationId_itemNo", unique: true });
db.getCollection("u_mes_plan_setupVerificationItem").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
