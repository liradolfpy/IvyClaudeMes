// Indexes for u_mes_qual_customerComplaintCommunication
db.getCollection("u_mes_qual_customerComplaintCommunication").createIndex({ customerComplaintId: 1, sequenceNo: 1 }, { name: "ux_customerComplaintId_sequenceNo", unique: true });
db.getCollection("u_mes_qual_customerComplaintCommunication").createIndex({ authorUserId: 1 }, { name: "ix_authorUserId" });
