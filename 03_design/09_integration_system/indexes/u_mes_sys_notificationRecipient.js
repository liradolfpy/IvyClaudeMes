// Indexes for u_mes_sys_notificationRecipient
db.getCollection("u_mes_sys_notificationRecipient").createIndex({ notificationId: 1, sequenceNo: 1 }, { name: "ux_notificationId_sequenceNo", unique: true });
db.getCollection("u_mes_sys_notificationRecipient").createIndex({ userId: 1 }, { name: "ix_userId" });
db.getCollection("u_mes_sys_notificationRecipient").createIndex({ roleId: 1 }, { name: "ix_roleId" });
