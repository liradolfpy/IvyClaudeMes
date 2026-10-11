// Indexes for u_mes_matl_kitLine
db.getCollection("u_mes_matl_kitLine").createIndex({ kitId: 1, lineNo: 1 }, { name: "ux_kitId_lineNo", unique: true });
db.getCollection("u_mes_matl_kitLine").createIndex({ itemId: 1 }, { name: "ix_itemId" });
db.getCollection("u_mes_matl_kitLine").createIndex({ lotId: 1 }, { name: "ix_lotId" });
db.getCollection("u_mes_matl_kitLine").createIndex({ fromLocationId: 1 }, { name: "ix_fromLocationId" });
