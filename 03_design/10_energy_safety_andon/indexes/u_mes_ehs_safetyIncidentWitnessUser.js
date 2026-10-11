// Indexes for u_mes_ehs_safetyIncidentWitnessUser
db.getCollection("u_mes_ehs_safetyIncidentWitnessUser").createIndex({ safetyIncidentId: 1, witnessUserId: 1 }, { name: "ux_safetyIncidentId_witnessUserId", unique: true });
db.getCollection("u_mes_ehs_safetyIncidentWitnessUser").createIndex({ witnessUserId: 1, safetyIncidentId: 1 }, { name: "ix_witnessUserId_safetyIncidentId" });
