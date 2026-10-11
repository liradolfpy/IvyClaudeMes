// Indexes for u_mes_prd_workInstructionStepProductVariant
db.getCollection("u_mes_prd_workInstructionStepProductVariant").createIndex({ workInstructionStepId: 1, productVariantId: 1 }, { name: "ux_workInstructionStepId_productVariantId", unique: true });
db.getCollection("u_mes_prd_workInstructionStepProductVariant").createIndex({ productVariantId: 1, workInstructionStepId: 1 }, { name: "ix_productVariantId_workInstructionStepId" });
