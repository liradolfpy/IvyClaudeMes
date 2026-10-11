// Indexes for u_mes_qlt_nonconformancePhotoControlledDocument
db.getCollection("u_mes_qlt_nonconformancePhotoControlledDocument").createIndex({ nonconformanceId: 1, photoControlledDocumentId: 1 }, { name: "ux_nonconformanceId_photoControlledDocumentId", unique: true });
db.getCollection("u_mes_qlt_nonconformancePhotoControlledDocument").createIndex({ photoControlledDocumentId: 1, nonconformanceId: 1 }, { name: "ix_photoControlledDocumentId_nonconformanceId" });
