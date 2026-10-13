// Indexes for u_mes_syst_systemPeriodicReview
db.getCollection("u_mes_syst_systemPeriodicReview").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_syst_systemPeriodicReview").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_syst_systemPeriodicReview").createIndex({ computerisedSystemId: 1 }, { name: "ix_computerisedSystemId" });
db.getCollection("u_mes_syst_systemPeriodicReview").createIndex({ siteId: 1, reviewPeriodFromDate: -1 }, { name: "ix_siteId_reviewPeriodFromDate" });
