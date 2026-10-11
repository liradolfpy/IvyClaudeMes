// Indexes for u_mes_plan_shiftHandoverDowntimeEvent
db.getCollection("u_mes_plan_shiftHandoverDowntimeEvent").createIndex({ shiftHandoverId: 1, downtimeEventId: 1 }, { name: "ux_shiftHandoverId_downtimeEventId", unique: true });
db.getCollection("u_mes_plan_shiftHandoverDowntimeEvent").createIndex({ downtimeEventId: 1, shiftHandoverId: 1 }, { name: "ix_downtimeEventId_shiftHandoverId" });
