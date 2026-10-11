// Indexes for u_mes_plan_container
db.getCollection("u_mes_plan_container").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_plan_container").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_plan_container").createIndex({ containerTypeId: 1 }, { name: "ix_containerTypeId" });
db.getCollection("u_mes_plan_container").createIndex({ packagingSpecificationId: 1 }, { name: "ix_packagingSpecificationId" });
db.getCollection("u_mes_plan_container").createIndex({ ownerCustomerId: 1 }, { name: "ix_ownerCustomerId" });
db.getCollection("u_mes_plan_container").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_plan_container").createIndex({ storageLocationId: 1 }, { name: "ix_storageLocationId" });
db.getCollection("u_mes_plan_container").createIndex({ siteId: 1, packedAt: -1 }, { name: "ix_siteId_packedAt" });
