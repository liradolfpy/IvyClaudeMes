// Indexes for u_mes_qlt_pfmeaLine
db.getCollection("u_mes_qlt_pfmeaLine").createIndex({ pfmeaId: 1, lineNo: 1 }, { name: "ux_pfmeaId_lineNo", unique: true });
db.getCollection("u_mes_qlt_pfmeaLine").createIndex({ operationId: 1 }, { name: "ix_operationId" });
db.getCollection("u_mes_qlt_pfmeaLine").createIndex({ characteristicId: 1 }, { name: "ix_characteristicId" });
db.getCollection("u_mes_qlt_pfmeaLine").createIndex({ ownerUserId: 1 }, { name: "ix_ownerUserId" });
