// Indexes for u_mes_qual_controlPlanLine
db.getCollection("u_mes_qual_controlPlanLine").createIndex({ controlPlanId: 1, lineNo: 1 }, { name: "ux_controlPlanId_lineNo", unique: true });
db.getCollection("u_mes_qual_controlPlanLine").createIndex({ operationId: 1 }, { name: "ix_operationId" });
db.getCollection("u_mes_qual_controlPlanLine").createIndex({ characteristicId: 1 }, { name: "ix_characteristicId" });
db.getCollection("u_mes_qual_controlPlanLine").createIndex({ gaugeId: 1 }, { name: "ix_gaugeId" });
