// Indexes for u_mes_matl_packagingSpecificationLevel
db.getCollection("u_mes_matl_packagingSpecificationLevel").createIndex({ packagingSpecificationId: 1, levelNo: 1 }, { name: "ux_packagingSpecificationId_levelNo", unique: true });
db.getCollection("u_mes_matl_packagingSpecificationLevel").createIndex({ packTypeId: 1 }, { name: "ix_packTypeId" });
