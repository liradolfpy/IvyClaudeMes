// Indexes for u_mes_mast_skillLevelScale
db.getCollection("u_mes_mast_skillLevelScale").createIndex({ skillId: 1, level: 1 }, { name: "ux_skillId_level", unique: true });
