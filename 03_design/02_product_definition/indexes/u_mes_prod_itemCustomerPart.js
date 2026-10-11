// Indexes for u_mes_prod_itemCustomerPart
db.getCollection("u_mes_prod_itemCustomerPart").createIndex({ itemId: 1, sequenceNo: 1 }, { name: "ux_itemId_sequenceNo", unique: true });
db.getCollection("u_mes_prod_itemCustomerPart").createIndex({ customerId: 1 }, { name: "ix_customerId" });
