// Indexes for u_mes_mdm_roleSignatureMeaning
db.getCollection("u_mes_mdm_roleSignatureMeaning").createIndex({ roleId: 1, signatureMeaningId: 1 }, { name: "ux_roleId_signatureMeaningId", unique: true });
db.getCollection("u_mes_mdm_roleSignatureMeaning").createIndex({ signatureMeaningId: 1, roleId: 1 }, { name: "ix_signatureMeaningId_roleId" });
