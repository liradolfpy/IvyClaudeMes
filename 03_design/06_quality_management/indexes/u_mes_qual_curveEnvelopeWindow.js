// Indexes for u_mes_qual_curveEnvelopeWindow
db.getCollection("u_mes_qual_curveEnvelopeWindow").createIndex({ curveEnvelopeId: 1, windowNo: 1 }, { name: "ux_curveEnvelopeId_windowNo", unique: true });
