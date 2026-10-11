// Indexes for u_mes_eqp_downtimeEventComment
db.getCollection("u_mes_eqp_downtimeEventComment").createIndex({ downtimeEventId: 1, sequenceNo: 1 }, { name: "ux_downtimeEventId_sequenceNo", unique: true });
db.getCollection("u_mes_eqp_downtimeEventComment").createIndex({ authorUserId: 1 }, { name: "ix_authorUserId" });
