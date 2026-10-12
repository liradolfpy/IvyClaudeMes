// Indexes for u_mes_matl_replenishmentRule
db.getCollection("u_mes_matl_replenishmentRule").createIndex({ siteId: 1, recordNo: 1 }, { name: "ux_siteId_recordNo", unique: true });
db.getCollection("u_mes_matl_replenishmentRule").createIndex({ siteId: 1, status: 1 }, { name: "ix_siteId_status" });
db.getCollection("u_mes_matl_replenishmentRule").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_matl_replenishmentRule").createIndex({ toLocationId: 1 }, { name: "ix_toLocationId" });
db.getCollection("u_mes_matl_replenishmentRule").createIndex({ fromLocationId: 1 }, { name: "ix_fromLocationId" });
db.getCollection("u_mes_matl_replenishmentRule").createIndex({ workCenterId: 1 }, { name: "ix_workCenterId" });
db.getCollection("u_mes_matl_replenishmentRule").createIndex({ containerTypeId: 1 }, { name: "ix_containerTypeId" });
