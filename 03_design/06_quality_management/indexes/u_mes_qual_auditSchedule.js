// Indexes for u_mes_qual_auditSchedule
db.getCollection("u_mes_qual_auditSchedule").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_auditSchedule").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_auditSchedule").createIndex({ areaId: 1 }, { name: "ix_areaId" });
db.getCollection("u_mes_qual_auditSchedule").createIndex({ lineId: 1 }, { name: "ix_lineId" });
db.getCollection("u_mes_qual_auditSchedule").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_qual_auditSchedule").createIndex({ checkSheetId: 1 }, { name: "ix_checkSheetId" });
db.getCollection("u_mes_qual_auditSchedule").createIndex({ auditorRoleId: 1 }, { name: "ix_auditorRoleId" });
