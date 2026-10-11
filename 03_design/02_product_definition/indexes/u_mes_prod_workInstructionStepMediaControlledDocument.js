// Indexes for u_mes_prod_workInstructionStepMediaControlledDocument
db.getCollection("u_mes_prod_workInstructionStepMediaControlledDocument").createIndex({ workInstructionStepId: 1, mediaControlledDocumentId: 1 }, { name: "ux_workInstructionStepId_mediaControlledDocumentId", unique: true });
db.getCollection("u_mes_prod_workInstructionStepMediaControlledDocument").createIndex({ mediaControlledDocumentId: 1, workInstructionStepId: 1 }, { name: "ix_mediaControlledDocumentId_workInstructionStepId" });
