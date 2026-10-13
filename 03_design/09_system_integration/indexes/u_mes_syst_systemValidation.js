// Indexes for u_mes_syst_systemValidation
db.getCollection("u_mes_syst_systemValidation").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_systemValidation").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_systemValidation").createIndex({ computerisedSystemId: 1 }, { name: "ix_computerisedSystemId" });
db.getCollection("u_mes_syst_systemValidation").createIndex({ engineeringChangeId: 1 }, { name: "ix_engineeringChangeId" });
db.getCollection("u_mes_syst_systemValidation").createIndex({ riskAssessmentId: 1 }, { name: "ix_riskAssessmentId" });
db.getCollection("u_mes_syst_systemValidation").createIndex({ protocolControlledDocumentId: 1 }, { name: "ix_protocolControlledDocumentId" });
db.getCollection("u_mes_syst_systemValidation").createIndex({ reportControlledDocumentId: 1 }, { name: "ix_reportControlledDocumentId" });
db.getCollection("u_mes_syst_systemValidation").createIndex({ siteId: 1, plannedStartDate: -1 }, { name: "ix_siteId_plannedStartDate" });
