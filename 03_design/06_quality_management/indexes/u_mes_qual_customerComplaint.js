// Indexes for u_mes_qual_customerComplaint
db.getCollection("u_mes_qual_customerComplaint").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qual_customerComplaint").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qual_customerComplaint").createIndex({ customerId: 1 }, { name: "ix_customerId" });
db.getCollection("u_mes_qual_customerComplaint").createIndex({ complaintTypeId: 1 }, { name: "ix_complaintTypeId" });
db.getCollection("u_mes_qual_customerComplaint").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qual_customerComplaint").createIndex({ vehicleModelId: 1 }, { name: "ix_vehicleModelId" });
db.getCollection("u_mes_qual_customerComplaint").createIndex({ nonconformanceId: 1 }, { name: "ix_nonconformanceId" });
db.getCollection("u_mes_qual_customerComplaint").createIndex({ siteId: 1, reportedAt: -1 }, { name: "ix_siteId_reportedAt" });
