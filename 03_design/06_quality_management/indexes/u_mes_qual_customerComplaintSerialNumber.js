// Indexes for u_mes_qual_customerComplaintSerialNumber
db.getCollection("u_mes_qual_customerComplaintSerialNumber").createIndex({ customerComplaintId: 1, serialNumberId: 1 }, { name: "ux_customerComplaintId_serialNumberId", unique: true });
db.getCollection("u_mes_qual_customerComplaintSerialNumber").createIndex({ serialNumberId: 1, customerComplaintId: 1 }, { name: "ix_serialNumberId_customerComplaintId" });
