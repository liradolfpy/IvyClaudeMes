// Indexes for u_mes_matl_packagingSpecification
db.getCollection("u_mes_matl_packagingSpecification").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_matl_packagingSpecification").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_matl_packagingSpecification").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_matl_packagingSpecification").createIndex({ customerId: 1 }, { name: "ix_customerId" });
db.getCollection("u_mes_matl_packagingSpecification").createIndex({ containerTypeId: 1 }, { name: "ix_containerTypeId" });
db.getCollection("u_mes_matl_packagingSpecification").createIndex({ unitLabelTemplateId: 1 }, { name: "ix_unitLabelTemplateId" });
db.getCollection("u_mes_matl_packagingSpecification").createIndex({ containerLabelTemplateId: 1 }, { name: "ix_containerLabelTemplateId" });
