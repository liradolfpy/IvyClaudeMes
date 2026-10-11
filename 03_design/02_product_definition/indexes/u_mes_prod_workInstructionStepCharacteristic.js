// Indexes for u_mes_prod_workInstructionStepCharacteristic
db.getCollection("u_mes_prod_workInstructionStepCharacteristic").createIndex({ workInstructionStepId: 1, characteristicId: 1 }, { name: "ux_workInstructionStepId_characteristicId", unique: true });
db.getCollection("u_mes_prod_workInstructionStepCharacteristic").createIndex({ characteristicId: 1, workInstructionStepId: 1 }, { name: "ix_characteristicId_workInstructionStepId" });
