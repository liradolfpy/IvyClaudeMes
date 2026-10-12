// Indexes for u_mes_prod_workInstructionProductVariant
db.getCollection("u_mes_prod_workInstructionProductVariant").createIndex({ workInstructionId: 1, productVariantId: 1 }, { name: "ux_workInstructionId_productVariantId", unique: true });
db.getCollection("u_mes_prod_workInstructionProductVariant").createIndex({ productVariantId: 1, workInstructionId: 1 }, { name: "ix_productVariantId_workInstructionId" });
