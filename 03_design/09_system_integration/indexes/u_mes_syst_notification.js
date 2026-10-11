// Indexes for u_mes_syst_notification
db.getCollection("u_mes_syst_notification").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_notification").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_notification").createIndex({ notificationTypeId: 1 }, { name: "ix_notificationTypeId" });
db.getCollection("u_mes_syst_notification").createIndex({ andonEventId: 1 }, { name: "ix_andonEventId" });
db.getCollection("u_mes_syst_notification").createIndex({ alarmId: 1 }, { name: "ix_alarmId" });
db.getCollection("u_mes_syst_notification").createIndex({ nonconformanceId: 1 }, { name: "ix_nonconformanceId" });
db.getCollection("u_mes_syst_notification").createIndex({ relatedCollectionName: 1, relatedEntityId: 1 }, { name: "ix_relatedCollectionName_relatedEntityId" });
db.getCollection("u_mes_syst_notification").createIndex({ siteId: 1, raisedAt: -1 }, { name: "ix_siteId_raisedAt" });
