// Indexes for u_mes_qlt_gaugeCalibrationReading
db.getCollection("u_mes_qlt_gaugeCalibrationReading").createIndex({ gaugeCalibrationId: 1, sequenceNo: 1 }, { name: "ux_gaugeCalibrationId_sequenceNo", unique: true });
