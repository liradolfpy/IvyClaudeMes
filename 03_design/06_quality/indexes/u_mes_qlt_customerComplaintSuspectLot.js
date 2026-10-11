// Indexes for u_mes_qlt_customerComplaintSuspectLot
db.getCollection("u_mes_qlt_customerComplaintSuspectLot").createIndex({ customerComplaintId: 1, suspectLotId: 1 }, { name: "ux_customerComplaintId_suspectLotId", unique: true });
db.getCollection("u_mes_qlt_customerComplaintSuspectLot").createIndex({ suspectLotId: 1, customerComplaintId: 1 }, { name: "ix_suspectLotId_customerComplaintId" });
