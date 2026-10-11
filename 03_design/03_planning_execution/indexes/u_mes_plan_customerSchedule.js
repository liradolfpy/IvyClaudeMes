// Indexes for u_mes_plan_customerSchedule
db.getCollection("u_mes_plan_customerSchedule").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_customerSchedule").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_customerSchedule").createIndex({ customerId: 1 }, { name: "ix_customerId" });
db.getCollection("u_mes_plan_customerSchedule").createIndex({ supersedesCustomerScheduleId: 1 }, { name: "ix_supersedesCustomerScheduleId" });
db.getCollection("u_mes_plan_customerSchedule").createIndex({ siteId: 1, receivedAt: -1 }, { name: "ix_siteId_receivedAt" });
