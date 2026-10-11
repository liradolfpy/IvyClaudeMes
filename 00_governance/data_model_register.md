# data_model_register.md

MES on MongoDB - Front Brake Caliper Assembly LH - Pune
Register version: 1.1 (Phase 1 plus key list) | Date: 11 October 2026 | Database: mes | Collections: 104

This file is the single reference for collection names, keys and master IDs. Phase 2 specifications and the Phase 3 generator must agree with it. It is updated at the end of every phase.

## 1. Conventions

- Collection names: lowercase snake_case, plural.
- _id: string, format PREFIX-businessKey (for example ITM-5110-10-0100). Never an ObjectId.
- Every document carries: _id, its business key field, siteId, status, schemaVersion (Int32), createdAt (Date), createdBy (users._id), updatedAt (Date), updatedBy (users._id).
- Reference fields are named <entity>Id (single) or <entity>Ids (array) and hold the _id string of the target document.
- Polymorphic references (event_logs, audit_trails, electronic_signatures, quality_holds, labels) use a pair: refCollection + refId.
- Types: Date for all times (UTC), Decimal128 for measurements, quantities with fractions and money, Int32 for counts, Int64 for lifetime counters, Boolean for flags.
- Global masters (enterprises, units_of_measure, roles) carry siteId of the owning site and scope = ENTERPRISE.
- System account for automated writes: USR-SYSTEM (exists in users).

## 2. Seed-data frame

| Item | Value |
|---|---|
| Enterprise | ENT-VBS - Varuna Brake Systems Pvt. Ltd. (fictional) |
| Site | SITE-PN1 - Chakan Plant, Pune, Maharashtra (timezone Asia/Kolkata) |
| OEM customer | CUS-SML - Sahyadri Motors Ltd. (fictional) |
| Production period | Mon 28 Sep 2026 06:00 IST to Sat 10 Oct 2026 22:00 IST |
| Non-working days | Fri 2 Oct 2026 (Gandhi Jayanti), Sun 4 Oct 2026 (weekly off) |
| Shifts | SH-A 06:00-14:00, SH-B 14:00-22:00, SH-C 22:00-06:00 IST (UTC starts 00:30, 08:30, 16:30) |
| Documents per collection | 10 (operations and items: pending decision, see section 5) |

## 3. Master ID registry (fixed in Phase 1)

### 3.1 Items

| _id | itemNo | Description | Type | Drawing rev |
|---|---|---|---|---|
| ITM-5110-10-0100 | 5110-10-0100 | Front Brake Caliper Assembly, LH | Finished good | D |
| ITM-5110-10-0200 | 5110-10-0200 | Front Brake Caliper Assembly, RH | Finished good | D |
| ITM-5110-20-0110 | 5110-20-0110 | Caliper Body, LH, machined and anodised | Semi-finished | C |
| ITM-5110-20-0105 | 5110-20-0105 | Caliper Body Casting, LH, T6 | Semi-finished | B |
| ITM-5110-30-0010 | 5110-30-0010 | Piston, dia 54 mm, steel, chrome plated | Purchased | B |
| ITM-5110-30-0020 | 5110-30-0020 | Piston Seal, square section, EPDM | Purchased | A |
| ITM-5110-30-0030 | 5110-30-0030 | Dust Boot, EPDM | Purchased | A |
| ITM-5110-30-0040 | 5110-30-0040 | Bleed Screw M10 x 1.0 with cap | Purchased | A |
| ITM-5110-30-0050 | 5110-30-0050 | Guide Pin with boot | Purchased | B |
| ITM-RM-A356 | RM-A356 | Aluminium alloy ingot AlSi7Mg0.3 (A356) | Raw material | - |

Brake pad set (ITM-5110-30-0060) and mounting bracket (ITM-5110-30-0070) are also BOM components of the finished caliper, which makes 12 items. Recommended: 12 documents in items. If the rule of 10 must hold, the RH assembly is dropped (RH stays as a variant of the LH item) and the casting and machined body become one item with two processing stages, so that pad set and bracket fit. See open decision 2.

### 3.2 Operations and work centres

| Step | operations._id | Operation | work_centres._id | lines._id | areas._id | Tracking grain |
|---|---|---|---|---|---|---|
| OP010 | OPN-OP010 | Gravity die casting | WC-GDC-01 | LN-GDC-01 | AR-FDY | Lot |
| OP020 | OPN-OP020 | Heat treatment T6 | WC-HT-01 | LN-HT-01 | AR-HT | Lot |
| OP030 | OPN-OP030 | CNC machining | WC-CNC-01 | LN-MC-01 | AR-MC | Lot |
| OP040 | OPN-OP040 | Washing | WC-WSH-01 | LN-WSH-01 | AR-SF | Lot |
| OP050 | OPN-OP050 | Anodising | WC-ANO-01 | LN-ANO-01 | AR-SF | Lot |
| OP060 | OPN-OP060 | Piston and seal assembly | WC-ASY-01 | LN-ASY-01 | AR-ASY | Unit |
| OP070 | OPN-OP070 | Bleed screw torque | WC-TRQ-01 | LN-ASY-01 | AR-ASY | Unit |
| OP080 | OPN-OP080 | Pressure leak test | WC-LKT-01 | LN-ASY-01 | AR-ASY | Unit |
| OP090 | OPN-OP090 | Laser marking (serial and 2D code) | WC-LSR-01 | LN-ASY-01 | AR-ASY | Unit |
| OP100 | OPN-OP100 | Final inspection | WC-FIP-01 | LN-FIP-01 | AR-FIP | Unit |
| OP110 | OPN-OP110 | Packing | WC-FIP-01 | LN-PKG-01 | AR-FIP | Container |

Dispatch is recorded in shipments from area AR-WH; it is not a routing operation.

### 3.3 Areas (10) and lines (10)

Areas: AR-FDY Foundry, AR-HT Heat treatment, AR-MC Machining, AR-SF Surface treatment (washing and anodising), AR-ASY Assembly and test, AR-FIP Final inspection and packing, AR-WH Stores and dispatch, AR-QL Quality laboratory, AR-TR Tool room, AR-UT Utilities.

Lines: LN-GDC-01, LN-GDC-02, LN-HT-01, LN-MC-01, LN-MC-02, LN-WSH-01, LN-ANO-01, LN-ASY-01, LN-FIP-01, LN-PKG-01.

### 3.4 IDs to be fixed in Phase 2

Equipment, users, roles, suppliers, remaining customers, gauges, tools, characteristics, defect codes and reason codes are assigned in the Phase 2 reply that specifies their collection and are added to this section at that point. No Phase 1 text refers to an ID that is not listed above.

## 4. Collection register


### 1 Enterprise and master data

| # | Collection | _id pattern | Business key field | References (collection) | Storage | Embed / reference decision |
|---|---|---|---|---|---|---|
| 1 | enterprises | ENT-<enterpriseCode> | enterpriseCode | none | standard | Embeds addresses and registrations (bounded, read together) |
| 2 | sites | SITE-<siteCode> | siteCode | enterprises | standard | Embeds address, certificates; referenced by every document |
| 3 | areas | AR-<areaCode> | areaCode | sites | standard | Reference to site; small master |
| 4 | lines | LN-<lineCode> | lineCode | sites, areas | standard | Embeds ideal rates per item family (bounded) |
| 5 | work_centres | WC-<workCentreCode> | workCentreCode | sites, areas, lines | standard | Embeds capability list and ERP mapping; references equipment by id |
| 6 | equipment | EQ-<equipmentCode> | equipmentCode | sites, lines, work_centres, suppliers | standard | Embeds nameplate and counters; states, tags, downtime are separate (unbounded) |
| 7 | shifts | SH-<shiftCode> | shiftCode | sites | standard | Embeds breaks (bounded) |
| 8 | calendars | CAL-<calendarCode> | calendarCode | sites, shifts, lines | standard | Embeds exception days (bounded to a year) |
| 9 | shift_rosters | ROS-<rosterNo> | rosterNo | sites, shifts, lines, users, work_centres | standard | Embeds assignments for one day-shift-line (bounded) |
| 10 | roles | ROLE-<roleCode> | roleCode | sites | standard | Embeds permission list (bounded) |
| 11 | users | USR-<employeeNo> | employeeNo | sites, roles, shifts, work_centres | standard | References roles; certifications kept separately (they expire and grow) |
| 12 | skills | SKL-<skillCode> | skillCode | sites, operations | standard | Small master, referenced by operations and certifications |
| 13 | certifications | CERT-<certificationNo> | certificationNo | sites, users, skills | standard | One document per user-skill award; references both sides (many-to-many) |
| 14 | customers | CUS-<customerCode> | customerCode | sites | standard | Embeds ship-to addresses and contacts (bounded) |
| 15 | suppliers | SUP-<supplierCode> | supplierCode | sites | standard | Embeds certificates and contacts (bounded) |
| 16 | units_of_measure | UOM-<uomCode> | uomCode | sites | standard | Self-contained reference data |

### 2 Product definition

| # | Collection | _id pattern | Business key field | References (collection) | Storage | Embed / reference decision |
|---|---|---|---|---|---|---|
| 17 | items | ITM-<itemNo> | itemNo | sites, units_of_measure, customers, suppliers, engineering_changes | standard | Embeds revision history and customer part cross-reference (bounded) |
| 18 | variants | VAR-<variantCode> | variantCode | sites, items, customers | standard | Embeds option values; referenced by BOM lines and instruction steps |
| 19 | boms | BOM-<bomNo> | bomNo | sites, items, units_of_measure, variants, engineering_changes | standard | Embeds component lines (bounded, always read with the header) |
| 20 | operations | OPN-<operationCode> | operationCode | sites, work_centres, skills | standard | Small master; routings reference it |
| 21 | routings | RTG-<routingNo> | routingNo | sites, items, operations, work_centres, engineering_changes | standard | Embeds steps and next-step rules (bounded, versioned as a whole) |
| 22 | bills_of_process | BOP-<bopNo> | bopNo | sites, items, routings, operations, equipment, tools, recipes, work_instructions, inspection_plans, boms, skills | standard | Embeds per-step resource requirements; references the definitions it binds together |
| 23 | work_instructions | WI-<instructionNo> | instructionNo | sites, items, operations, variants, documents, characteristics, tools, engineering_changes | standard | Embeds steps (bounded); media stored as document references |
| 24 | recipes | RCP-<recipeNo> | recipeNo | sites, equipment, items, operations, process_tags, engineering_changes | standard | Embeds parameters (bounded); downloads are logged in event_logs |
| 25 | engineering_changes | ECN-<ecnNo> | ecnNo | sites, items, users, customers, documents | standard | Embeds affected-object list and approval steps (bounded) |

### 3 Planning and execution

| # | Collection | _id pattern | Business key field | References (collection) | Storage | Embed / reference decision |
|---|---|---|---|---|---|---|
| 26 | customer_schedules | CSR-<releaseNo> | releaseNo | sites, customers, items | standard | Embeds schedule lines (bounded per release) |
| 27 | production_orders | PO-<orderNo> | orderNo | sites, items, boms, routings, lines, customer_schedules, erp_messages | standard | Embeds release history and quantity counters; units and executions are separate (unbounded) |
| 28 | production_schedules | SCH-<scheduleNo> | scheduleNo | sites, lines, shifts, production_orders, calendars | standard | Embeds the sequenced order slots for one line-shift (bounded) |
| 29 | dispatch_lists | DSP-<dispatchNo> | dispatchNo | sites, work_centres, production_orders, lots, shifts | standard | Embeds queue entries for one work centre-shift (bounded) |
| 30 | operation_executions | OPX-<executionNo> | executionNo | sites, production_orders, wip_units, lots, operations, routings, work_centres, equipment, users, shifts, recipes | standard, partitioned by month | References only; one document per unit/lot per operation (unbounded) |
| 31 | step_completions | STC-<completionNo> | completionNo | sites, operation_executions, work_instructions, wip_units, users, work_centres | standard, archive after 15 months | References the execution; unbounded so not embedded in it |
| 32 | wip_units | WU-<unitNo> | unitNo | sites, production_orders, items, variants, lots, serial_numbers, routings, operations, containers | standard | Embeds current position and a short status summary; history lives in operation_executions |
| 33 | lots | LOT-<lotNo> | lotNo | sites, items, suppliers, goods_receipts, production_orders, storage_locations | standard | Embeds lot attributes (heat number, expiry, certificates); movements separate |
| 34 | containers | CNT-<containerNo> | containerNo | sites, items, lots, storage_locations, packaging_specifications, customers | standard | Embeds current contents summary; unit membership is on wip_units |
| 35 | labour_bookings | LAB-<bookingNo> | bookingNo | sites, users, production_orders, operations, work_centres, shifts | standard | References only (unbounded) |
| 36 | changeovers | CHG-<changeoverNo> | changeoverNo | sites, lines, work_centres, equipment, production_orders, items, users, tools, check_sheet_results | standard | Embeds checklist steps (bounded) |
| 37 | shift_handovers | SHO-<handoverNo> | handoverNo | sites, lines, shifts, users, production_orders, downtime_events, nonconformances | standard | Embeds notes and open items (bounded) |

### 4 Materials

| # | Collection | _id pattern | Business key field | References (collection) | Storage | Embed / reference decision |
|---|---|---|---|---|---|---|
| 38 | storage_locations | LOC-<locationCode> | locationCode | sites, areas, work_centres | standard | Small master with parent reference (hierarchy) |
| 39 | inventory_balances | INV-<inventoryNo> | inventoryNo | sites, items, lots, storage_locations, containers, units_of_measure | standard | One row per item-lot-location-status; updated in place |
| 40 | material_movements | MM-<movementNo> | movementNo | sites, items, lots, containers, storage_locations, users, production_orders, goods_receipts, shipments | standard, partitioned by month | References only (unbounded ledger) |
| 41 | goods_receipts | GRN-<grnNo> | grnNo | sites, suppliers, items, lots, storage_locations, users, inspection_results | standard | Embeds receipt lines (bounded) |
| 42 | kits | KIT-<kitNo> | kitNo | sites, production_orders, items, lots, storage_locations, work_centres, users | standard | Embeds kit lines (bounded) |
| 43 | material_requests | MRQ-<requestNo> | requestNo | sites, work_centres, items, storage_locations, users, andon_events | standard | References only |
| 44 | material_consumptions | CON-<consumptionNo> | consumptionNo | sites, operation_executions, production_orders, wip_units, lots, items, work_centres, units_of_measure | standard, partitioned by month | References only (unbounded) |
| 45 | packaging_specifications | PKS-<packSpecNo> | packSpecNo | sites, items, customers, label_templates | standard | Embeds pack levels (bounded) |
| 46 | label_templates | LBT-<templateCode> | templateCode | sites, customers | standard | Embeds field mapping (bounded) |
| 47 | labels | LBL-<labelNo> | labelNo | sites, label_templates, wip_units, containers, lots, shipments, users, iot_devices | standard | References only (unbounded) |
| 48 | shipments | SHP-<shipmentNo> | shipmentNo | sites, customers, customer_schedules, containers, items, users, storage_locations | standard | Embeds shipment lines and container list (bounded) |

### 5 Traceability

| # | Collection | _id pattern | Business key field | References (collection) | Storage | Embed / reference decision |
|---|---|---|---|---|---|---|
| 49 | serial_numbers | SN-<serialNo> | serialNo | sites, items, wip_units, production_orders, number_ranges, labels, shipments | standard | One row per serial; uniqueness enforced by index |
| 50 | genealogy_links | GEN-<linkNo> | linkNo | sites, wip_units, serial_numbers, lots, items, operation_executions, material_consumptions | standard, partitioned by month | Edge collection so forward and backward trace are both a single indexed query |
| 51 | component_lot_links | CLL-<lotLinkNo> | lotLinkNo | sites, lots, items, operation_executions | standard | Edge collection (a lot can have many parents and children) |
| 52 | as_built_records | ABR-<recordNo> | recordNo | sites, wip_units, serial_numbers, production_orders, items, genealogy_links, torque_results, leak_test_results, inspection_results, shipments | standard | Deliberately denormalised read model, frozen at dispatch for fast OEM queries |

### 6 Quality

| # | Collection | _id pattern | Business key field | References (collection) | Storage | Embed / reference decision |
|---|---|---|---|---|---|---|
| 53 | characteristics | CHR-<characteristicCode> | characteristicCode | sites, items, operations, units_of_measure, gauges | standard | Master referenced by plans, results and SPC |
| 54 | control_plans | CP-<controlPlanNo> | controlPlanNo | sites, items, routings, operations, characteristics, pfmeas, gauges, users, engineering_changes | standard | Embeds control plan lines (bounded, approved as one document) |
| 55 | inspection_plans | IP-<inspectionPlanNo> | inspectionPlanNo | sites, control_plans, items, operations, characteristics, sampling_plans, gauges, work_centres | standard | Embeds plan lines (bounded) |
| 56 | sampling_plans | SMP-<samplingPlanCode> | samplingPlanCode | sites | standard | Embeds sample-size table (bounded) |
| 57 | check_sheets | CKS-<checkSheetCode> | checkSheetCode | sites, work_centres, equipment, operations, items | standard | Embeds check items (bounded) |
| 58 | check_sheet_results | CKR-<checkResultNo> | checkResultNo | sites, check_sheets, work_centres, equipment, users, shifts, production_orders | standard | Embeds answers for one completion (bounded by the definition) |
| 59 | inspection_results | IR-<resultNo> | resultNo | sites, inspection_plans, characteristics, wip_units, lots, operation_executions, gauges, users, work_centres, goods_receipts | standard, partitioned by month | References only (unbounded) |
| 60 | spc_charts | SPC-<chartNo> | chartNo | sites, characteristics, work_centres, equipment, items | standard | Embeds control-limit revisions (bounded) |
| 61 | spc_samples | SPS-<sampleNo> | sampleNo | sites, spc_charts, characteristics, inspection_results, work_centres, users, nonconformances | standard | Embeds subgroup readings (fixed size 3-5) |
| 62 | defect_codes | DEF-<defectCode> | defectCode | sites, operations, routings | standard | Small master |
| 63 | nonconformances | NCR-<ncrNo> | ncrNo | sites, defect_codes, wip_units, lots, items, operations, work_centres, users, suppliers, quality_holds, rework_orders, scrap_records, capas, inspection_results | standard | Embeds affected objects, containment actions and disposition decisions (bounded) |
| 64 | rework_orders | RWK-<reworkNo> | reworkNo | sites, nonconformances, wip_units, lots, routings, operations, users, work_centres | standard | Embeds rework steps (bounded) |
| 65 | scrap_records | SCR-<scrapNo> | scrapNo | sites, nonconformances, defect_codes, wip_units, lots, items, operations, work_centres, users | standard | References only |
| 66 | quality_holds | HLD-<holdNo> | holdNo | sites, lots, wip_units, containers, storage_locations, nonconformances, users | standard | Embeds held-object list (bounded); hold flag is mirrored on the held objects |
| 67 | deviation_permits | DEV-<deviationNo> | deviationNo | sites, items, characteristics, customers, users, nonconformances, engineering_changes | standard | Embeds approvals (bounded) |
| 68 | capas | CAPA-<capaNo> | capaNo | sites, nonconformances, customer_complaints, audits, users, pfmeas, control_plans, documents | standard | Embeds the eight disciplines and action list (bounded) |
| 69 | pfmeas | FMEA-<pfmeaNo> | pfmeaNo | sites, items, operations, characteristics, users, control_plans | standard | Embeds failure-mode lines (bounded) |
| 70 | ppap_submissions | PPAP-<ppapNo> | ppapNo | sites, items, customers, control_plans, pfmeas, msa_studies, documents, users, engineering_changes | standard | Embeds the element checklist (fixed 18) |
| 71 | gauges | GAU-<gaugeNo> | gaugeNo | sites, storage_locations, work_centres, suppliers, users | standard | Embeds current calibration status; history is separate |
| 72 | gauge_calibrations | GCAL-<calibrationNo> | calibrationNo | sites, gauges, users, suppliers, documents | standard | References gauge (grows for the life of the gauge) |
| 73 | msa_studies | MSA-<msaNo> | msaNo | sites, gauges, characteristics, users, items | standard | Embeds trial data (bounded: appraisers x parts x trials) |
| 74 | audits | AUD-<auditNo> | auditNo | sites, areas, lines, users, customers, capas, check_sheets | standard | Embeds findings (bounded) |
| 75 | customer_complaints | CMP-<complaintNo> | complaintNo | sites, customers, items, serial_numbers, shipments, nonconformances, capas, users | standard | Embeds affected serials and communication log (bounded) |

### 7 Equipment and performance

| # | Collection | _id pattern | Business key field | References (collection) | Storage | Embed / reference decision |
|---|---|---|---|---|---|---|
| 76 | reason_codes | RSN-<reasonCode> | reasonCode | sites | standard | Self-reference to parent; path materialised for fast roll-up |
| 77 | equipment_states | EST-<stateEventNo> | stateEventNo | sites, equipment, work_centres, production_orders, shifts | time-series candidate | References only; time-ordered |
| 78 | downtime_events | DT-<downtimeNo> | downtimeNo | sites, equipment, lines, work_centres, reason_codes, shifts, users, production_orders, maintenance_work_orders, alarms | standard | Embeds reason path snapshot and comments (bounded) |
| 79 | production_counts | PC-<countNo> | countNo | sites, work_centres, lines, shifts, production_orders, items | time-series candidate | One bucket per work centre-hour |
| 80 | oee_records | OEE-<oeeRecordNo> | oeeRecordNo | sites, equipment, lines, shifts, items, production_orders | standard | Pre-aggregated; embeds loss breakdown (bounded) |
| 81 | process_tags | TAG-<tagName> | tagName | sites, equipment, iot_devices, units_of_measure | standard | Master for time-series values |
| 82 | process_data | PD-<readingNo> | readingNo | sites, process_tags, equipment | time-series (recommended) | Bucketed by tag; never embedded |
| 83 | alarms | ALM-<alarmNo> | alarmNo | sites, equipment, process_tags, users, iot_devices | standard | References only |
| 84 | torque_results | TRQ-<torqueResultNo> | torqueResultNo | sites, wip_units, operation_executions, equipment, tools, recipes, users, iot_devices | standard | One document per tightening (unbounded) |
| 85 | leak_test_results | LKT-<leakTestNo> | leakTestNo | sites, wip_units, operation_executions, equipment, recipes, users, iot_devices | standard | Embeds test stages (2-3 per test) |

### 8 Maintenance and tooling

| # | Collection | _id pattern | Business key field | References (collection) | Storage | Embed / reference decision |
|---|---|---|---|---|---|---|
| 86 | maintenance_plans | MP-<planNo> | planNo | sites, equipment, tools, spare_parts, skills | standard | Embeds task list (bounded) |
| 87 | maintenance_work_orders | MWO-<workOrderNo> | workOrderNo | sites, equipment, tools, maintenance_plans, downtime_events, users, spare_parts, reason_codes | standard | Embeds labour and spare-part lines (bounded) |
| 88 | spare_parts | SPR-<sparePartNo> | sparePartNo | sites, suppliers, storage_locations, equipment, units_of_measure | standard | Embeds where-used list (bounded) |
| 89 | tools | TL-<toolNo> | toolNo | sites, items, equipment, suppliers, storage_locations | standard | Embeds life counters; usage log is separate |
| 90 | tool_life_records | TLR-<toolLifeNo> | toolLifeNo | sites, tools, equipment, production_orders, users, maintenance_work_orders | standard | References tool (unbounded over tool life) |

### 9 Integration and system

| # | Collection | _id pattern | Business key field | References (collection) | Storage | Embed / reference decision |
|---|---|---|---|---|---|---|
| 91 | erp_messages | MSG-<messageNo> | messageNo | sites, integration_connectors, production_orders, goods_receipts, shipments | standard, TTL archive | Embeds payload; idempotency key indexed |
| 92 | integration_connectors | ICN-<connectorCode> | connectorCode | sites | standard | Embeds endpoint functions (bounded); no secrets stored |
| 93 | iot_devices | IOT-<deviceCode> | deviceCode | sites, equipment, work_centres, integration_connectors | standard | Embeds network and firmware data |
| 94 | operator_apps | APP-<appCode> | appCode | sites, work_centres, operations, work_instructions, inspection_plans, users | standard | Embeds step / widget layout and triggers (bounded) |
| 95 | event_logs | EVT-<eventNo> | eventNo | sites, users, iot_devices | standard, TTL or time-series candidate | Polymorphic subject reference (collection + id) |
| 96 | audit_trails | ADT-<auditTrailNo> | auditTrailNo | sites, users, electronic_signatures | standard, immutable | Polymorphic target reference; never updated |
| 97 | electronic_signatures | SIG-<signatureNo> | signatureNo | sites, users, roles | standard, immutable | Polymorphic target reference |
| 98 | notifications | NTF-<notificationNo> | notificationNo | sites, users, roles, andon_events, alarms, nonconformances | standard, TTL | Embeds recipients and delivery attempts (bounded) |
| 99 | documents | DOC-<documentNo> | documentNo | sites, users, items | standard | Metadata only; binary content outside MongoDB (GridFS or S3) |
| 100 | number_ranges | NR-<rangeCode> | rangeCode | sites, items | standard | One document per range, atomically incremented |
| 101 | system_configurations | CFG-<configKey> | configKey | sites | standard | Embeds typed value |

### 10 Energy, safety and andon

| # | Collection | _id pattern | Business key field | References (collection) | Storage | Embed / reference decision |
|---|---|---|---|---|---|---|
| 102 | energy_readings | ENR-<energyReadingNo> | energyReadingNo | sites, iot_devices, equipment, lines, shifts, units_of_measure | time-series (recommended) | Bucketed by meter |
| 103 | andon_events | AND-<andonNo> | andonNo | sites, work_centres, lines, users, reason_codes, downtime_events, shifts | standard | Embeds escalation steps (bounded) |
| 104 | safety_incidents | SAF-<incidentNo> | incidentNo | sites, areas, work_centres, users, equipment, capas | standard | Embeds actions and witnesses (bounded) |

## 5. Open decisions

| # | Decision | Default if not answered |
|---|---|---|
| 1 | operations collection: 11 documents (one per operation) or 10 (final inspection and packing merged) | 11 documents |
| 2 | items collection: 12 documents (adds brake pad set and bracket) or strictly 10 (see section 3.1) | 12 documents |

## 6. Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 11 Oct 2026 | Phase 1: 104 collections registered, conventions, seed frame, items / operations / work centres / areas / lines fixed |
| 1.1 | 11 Oct 2026 | Key list for all 104 collections added as collection_keys.md (source: keys.py); wip_units business key renamed unitId to unitNo so that only references end in Id |
