// Indexes for u_mes_qual_msaStudy
db.getCollection("u_mes_qual_msaStudy").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_msaStudy").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_msaStudy").createIndex({ gaugeId: 1 }, { name: "ix_gaugeId" });
db.getCollection("u_mes_qual_msaStudy").createIndex({ characteristicId: 1 }, { name: "ix_characteristicId" });
db.getCollection("u_mes_qual_msaStudy").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qual_msaStudy").createIndex({ siteId: 1, studyDate: -1 }, { name: "ix_siteId_studyDate" });
