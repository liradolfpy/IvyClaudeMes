// Indexes for u_mes_qual_inspectionPlanLine
db.getCollection("u_mes_qual_inspectionPlanLine").createIndex({ inspectionPlanId: 1, lineNo: 1 }, { name: "ux_inspectionPlanId_lineNo", unique: true });
db.getCollection("u_mes_qual_inspectionPlanLine").createIndex({ characteristicId: 1 }, { name: "ix_characteristicId" });
db.getCollection("u_mes_qual_inspectionPlanLine").createIndex({ gaugeId: 1 }, { name: "ix_gaugeId" });
db.getCollection("u_mes_qual_inspectionPlanLine").createIndex({ defectCodeId: 1 }, { name: "ix_defectCodeId" });
