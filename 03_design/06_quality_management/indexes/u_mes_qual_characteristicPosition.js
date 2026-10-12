// Indexes for u_mes_qual_characteristicPosition
db.getCollection("u_mes_qual_characteristicPosition").createIndex({ characteristicId: 1, positionNo: 1 }, { name: "ux_characteristicId_positionNo", unique: true });
db.getCollection("u_mes_qual_characteristicPosition").createIndex({ unitOfMeasureId: 1 }, { name: "ix_unitOfMeasureId" });
db.getCollection("u_mes_qual_characteristicPosition").createIndex({ curveEnvelopeId: 1 }, { name: "ix_curveEnvelopeId" });
