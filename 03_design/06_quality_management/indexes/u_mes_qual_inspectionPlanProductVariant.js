// Indexes for u_mes_qual_inspectionPlanProductVariant
db.getCollection("u_mes_qual_inspectionPlanProductVariant").createIndex({ inspectionPlanId: 1, productVariantId: 1 }, { name: "ux_inspectionPlanId_productVariantId", unique: true });
db.getCollection("u_mes_qual_inspectionPlanProductVariant").createIndex({ productVariantId: 1, inspectionPlanId: 1 }, { name: "ix_productVariantId_inspectionPlanId" });
