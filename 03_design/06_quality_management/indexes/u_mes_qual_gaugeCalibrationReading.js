// Indexes for u_mes_qual_gaugeCalibrationReading
db.getCollection("u_mes_qual_gaugeCalibrationReading").createIndex({ gaugeCalibrationId: 1, sequenceNo: 1 }, { name: "ux_gaugeCalibrationId_sequenceNo", unique: true });
