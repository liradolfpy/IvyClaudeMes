// Indexes for u_mes_plan_dispatchListEntry
db.getCollection("u_mes_plan_dispatchListEntry").createIndex({ dispatchListId: 1, rank: 1 }, { name: "ux_dispatchListId_rank", unique: true });
db.getCollection("u_mes_plan_dispatchListEntry").createIndex({ productionOrderId: 1 }, { name: "ix_productionOrderId" });
db.getCollection("u_mes_plan_dispatchListEntry").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_plan_dispatchListEntry").createIndex({ itemId: 1 }, { name: "ix_itemId" });
