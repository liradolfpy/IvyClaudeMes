// Indexes for u_mes_qlt_inspectionPlan
db.getCollection("u_mes_qlt_inspectionPlan").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_qlt_inspectionPlan").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_qlt_inspectionPlan").createIndex({ controlPlanId: 1 }, { name: "ix_controlPlanId" });
db.getCollection("u_mes_qlt_inspectionPlan").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_qlt_inspectionPlan").createIndex({ operationId: 1 }, { name: "ix_operationId" });
db.getCollection("u_mes_qlt_inspectionPlan").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_qlt_inspectionPlan").createIndex({ samplingPlanId: 1 }, { name: "ix_samplingPlanId" });
