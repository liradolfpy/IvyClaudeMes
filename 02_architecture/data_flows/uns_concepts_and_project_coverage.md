# Unified Namespace (UNS): concepts and how this project addresses them

Version 1.0 | 19 October 2026 | Model version 3.0 (372 collections, 8,703 keys) | Decisions D081, D082, D083
Companion to `02_architecture/data_flows/unified_namespace_design.md` (the design: namespace tree, payloads, services, security). This document explains the concepts behind the design and shows where each concept lives in the project: data model, sample data, UI configurations, generator sources and governance files.

## 1. What a Unified Namespace is

A Unified Namespace is an architecture pattern for plant data. Every system that produces information about the plant (controllers, machines, the MES, quality and maintenance systems) publishes it once, into one shared, event-driven hub, under a name that says where in the plant the information belongs. Every system that needs the information subscribes to it there, instead of connecting to each producer separately.

Without a UNS, integration grows point to point: the MES talks to each PLC, SCADA talks to the same PLCs, the historian talks to SCADA, the quality system talks to the leak tester, and so on. Each new consumer adds new links, and each link has its own format, polling cycle and failure mode. With a UNS, a producer is connected once and a new consumer is added without touching any producer.

The term was made popular in industrial IoT practice around 2020. It is a pattern, not a product and not a database.

## 2. Core principles

| Principle | Meaning |
|---|---|
| Single hub | All plant information meets in one place. Producers and consumers know the hub, not each other. |
| Hierarchical naming | Information is addressed by where it happens in the plant, following the ISA-95 / IEC 62264 equipment hierarchy: enterprise, site, area, line, work cell, equipment. |
| Current state first | The hub always shows the latest known state of every node (machine running or down, current order, last value of a tag). A late consumer gets the current picture at once. History is kept by the consumers that need it (historian, MES database, data lake). |
| Report by exception | A producer sends a value when it changes (beyond a deadband), not on a fixed poll. Traffic stays low and every message means something. |
| Event driven | Consumers react to messages as they arrive instead of polling databases. |
| Edge driven | Data is normalised as close to the source as possible (at an edge gateway), so every consumer receives the same structure. |
| Producers do not know consumers | A leak tester publishes its result once; the MES, SPC, andon boards and analytics all use it without any change at the tester. |
| Context travels with the data | Machine values alone say what happened; the MES adds why (order, item, operation, recipe, unit, operator, shift), so all consumers receive labelled data. |
| Open, documented structure | Names and payloads follow a published standard, so new systems can join without reverse engineering. |

## 3. Related concepts

| Concept | Relation to the UNS |
|---|---|
| ISA-95 / IEC 62264 | Supplies the equipment hierarchy used as the namespace structure, and the split between level 2 (control), level 3 (MES) and level 4 (ERP). |
| MQTT | The messaging protocol most UNS implementations use (publish / subscribe, topics, retained messages). |
| Sparkplug B | A payload and topic specification on top of MQTT for device state and metrics. Its topic structure does not carry the ISA-95 hierarchy, so it is often used only between devices and the edge. |
| Edge gateway | Software near the machines that reads controller protocols (OPC UA, Open Protocol, Modbus TCP, Profinet, EtherNet/IP) and publishes into the UNS. |
| Digital twin | A current-state model of an asset. In a UNS the current state of each node is its digital twin in the simplest sense. |
| Data lake | Long-term store of everything the UNS carries, for analytics and reporting outside the operational systems. |
| Historian | Time-series store of process values, a consumer of the UNS. |

## 4. What a UNS is not

| Not | Why it matters |
|---|---|
| A database or system of record | The hub holds current state and passes events; records of record (genealogy, signed batch records, quality decisions) are stored and proven in the MES database. |
| A transaction channel | Business transactions with ERP need acknowledgement, retry, idempotency and audit per transaction; they keep a dedicated, guaranteed channel. |
| A command bus to machines | Writing recipes or programs to equipment must be acknowledged and verified by the target; broadcasting commands through a hub is a safety risk. |
| A product you install | It is a structure and a set of rules. A broker or IoT service is only the transport. |

## 5. How the concepts are realised in this project

### 5.1 Decision trail

| Decision | Date | Content |
|---|---|---|
| D081 | 19 Oct 2026 | UNS design for the Chakan plant (PN1): ISA-95 tree from master data, namespaces edge / mes / kpi, JSON envelope, flows kept off the UNS, model change proposals, sample data findings |
| D082 | 19 Oct 2026 | Owner decision: Azure IoT Hub is the only UNS platform; no third-party MQTT broker. Design revised to version 7.0 with device twins, message enrichment, routing and client data lake synchronisation |
| D083 | 19 Oct 2026 | Model version 3.0: three new collections, `sourceMessageUuid` on nine collections, edge gateway reference on IoT devices, UI configurations and menu |

### 5.2 Concept to implementation on Azure IoT Hub

| UNS concept | Generic implementation (MQTT broker) | This project (Azure IoT Hub, D082) |
|---|---|---|
| Single hub | MQTT broker cluster | One Azure IoT Hub per site, `iothub-vbs-pn1`, region Central India |
| Hierarchical naming | Topic tree | ISA-95 path carried as message properties (`isa95Path` and five record-number properties), written as device twin tags by the MES and stamped on every message by IoT Hub message enrichment |
| Producer identity | MQTT client id | One IoT Hub device identity per piece of equipment (`PN1-<equipment recordNo>`), one per IoT Edge gateway, one for the MES publisher (`PN1-MES`) |
| Current state | Retained messages | Device twins: reported properties for state, last tag values and active alarms; desired properties for the MES context of the work center |
| Namespaces | Topic branches | Application property `ns` = edge, mes or kpi, with `msgType` |
| Subscription | Topic filters and shared subscriptions | IoT Hub message routing to the built-in endpoint with one consumer group per consumer (`mes-ingest`, `scada`, `historian`, `analytics`) |
| Online / offline | MQTT last will | IoT Hub device connection state events, routed to the MES |
| Delivery guarantee | QoS 1 | At-least-once delivery; consumers remove duplicates by message id |
| Report by exception | Deadband at the publisher | Deadband of `u_mes_perf_processTag` applied at the IoT Edge gateway |
| Edge | Edge gateway | Azure IoT Edge, one gateway per production area, identity translation per equipment, store and forward for 24 hours |
| History | Historian subscribes | MES collections (operational history), client data lake (complete history) |
| Data lake | Separate export | IoT Hub route to Azure Data Lake Storage Gen2, JSON, 300-second batches |

### 5.3 Namespace structure

```
VBS / PN1 / <area> / <line> / <workCenter> / <equipment>
```

Every segment is the `recordNo` of the master document at that level, so `VBS/PN1/ASY/ASY-01/TRQ-01/TRQ-01-N1` is the bleed screw nutrunner of Front Caliper Assembly Line 1. The path is derived, never stored in a MongoDB document (design decision U3), so it always matches master data.

| Namespace (`ns`) | Sent by | Carries |
|---|---|---|
| edge | IoT Edge gateways, per equipment identity | Equipment state, process tag values, alarms, cycle counts, results (tightening, curve, leak test, mark verification, inspection), energy intervals |
| mes | MES publisher | Work center and line context, business events (andon, interlock, recipe download, quality hold), master data changes for the data lake |
| kpi | MES publisher | Equipment OEE, station performance |

| Message class | Example | Current state held in |
|---|---|---|
| State | Equipment state, alarm, MES context | Device twin |
| Measurement | Process tag value | Device twin (`tags.<TAG>`) |
| Event | Tightening result, leak test, energy interval, business events | Not held; stored by consumers |

### 5.4 Master data that defines the namespace

| Collection | Role in the UNS |
|---|---|
| `u_mes_mast_enterprise`, `u_mes_mast_site` | First two path segments (`VBS`, `PN1`) |
| `u_mes_mast_area`, `u_mes_mast_line`, `u_mes_mast_workCenter`, `u_mes_mast_equipment` | Remaining path segments; equipment carries no `areaId`, the area comes from the line |
| `u_mes_mast_workCenterEquipment` | Confirms which equipment belongs to which work center |
| `u_mes_mast_equipmentIotDevice` | Which controller device belongs to which equipment |
| `u_mes_syst_iotDevice` | Controllers and gateways, with protocol, address, certificate expiry and, since model 3.0, `edgeGatewayIotDeviceId` |
| `u_mes_syst_deviceType` | Kind of device (PLC, nutrunner controller, leak tester, edge gateway) |
| `u_mes_perf_processTag` | Tags under each equipment node; the last segment of `recordNo` (`PN1.TRQ01.FINAL_TORQUE`) names the tag in tag messages; deadband and limits |
| `u_mes_perf_alarmDefinition` | Alarm codes per equipment, matched to alarm messages |
| `u_mes_syst_integrationConnector` | The integration endpoints; value `Azure IoT Hub` added to `connectorType` for the UNS connector |

### 5.5 Collections added for the UNS (model version 3.0)

| Collection | Type | Holds | Sample documents |
|---|---|---|---|
| `u_mes_syst_unsMessageType` (1370) | Master | The message catalogue: namespace, message type, payload schema and version, message class, hierarchy level, sender type, target collection, twin property, ingested by MES, routed to data lake | 10 (edge.state to kpi.oee) |
| `u_mes_syst_iotHubIdentity` (1371) | Master | One IoT Hub identity: type, hub, equipment, device, parent gateway, authentication and certificate, provisioning status, last registry sync, twin tags version, connection state | 10 (3 gateways, 6 equipment, MES publisher) |
| `u_mes_syst_unsRejectedMessage` (1372) | Transaction | One message the ingestion service could not store: id, identity, type, path, schema, timestamps, reason and detail, payload, dead-letter path, resolution | 10 over the production fortnight |

### 5.6 Keys added to existing collections

| Key | Collections | Purpose |
|---|---|---|
| `sourceMessageUuid` | `u_mes_perf_equipmentState`, `u_mes_perf_processReading`, `u_mes_perf_alarm`, `u_mes_perf_torqueResult`, `u_mes_perf_leakTestResult`, `u_mes_perf_energyReading`, `u_mes_qual_measurementCurve`, `u_mes_qual_inspectionResult`, `u_mes_plan_operationExecution` | Id of the UNS message a document came from. At-least-once delivery can repeat a message; a unique partial index on `siteId` + `sourceMessageUuid` stores it once. The two time-series candidates (process readings, energy readings) have a plain index, because MongoDB time-series collections do not allow unique indexes; the ingestion service removes duplicates there. |
| `edgeGatewayIotDeviceId` / `edgeGatewayIotDeviceName` | `u_mes_syst_iotDevice` | The IoT Edge gateway a device reports through, separate from its own southbound connector |

Keys that hold a message id end in `Uuid`, not `Id`, because the generators treat every key ending in `Id` as a reference to another collection.

### 5.7 Where each message type is stored

| Message type | MES collection |
|---|---|
| edge.state | `u_mes_perf_equipmentState` (and `u_mes_perf_downtimeEvent` when the state becomes Down) |
| edge.tag | `u_mes_perf_processReading` (only tags with `historise` true) |
| edge.alarm | `u_mes_perf_alarm` |
| edge.count | `u_mes_perf_productionCount`, `u_mes_plan_operationExecution`, `u_mes_mast_equipment.lifetimeCycles` |
| edge.result.tightening | `u_mes_perf_torqueResult` |
| edge.result.curve | `u_mes_qual_measurementCurve` and the time-series `u_mes_qual_measurementCurvePoint` |
| edge.result.leakTest | `u_mes_perf_leakTestResult` and `u_mes_perf_leakTestResultStage` |
| edge.result.markVerification | `u_mes_trac_serialNumber` (mark keys updated) |
| edge.result.inspection | `u_mes_qual_inspectionResult` |
| edge.energy | `u_mes_perf_energyReading` |
| mes.* and kpi.* | Not stored again; they are produced from MongoDB by the publisher |

### 5.8 Where the allocation of the namespace can be seen

| Question | Where |
|---|---|
| Which equipment is which IoT Hub identity, through which gateway | `u_mes_syst_iotHubIdentity` |
| The path of a node | Derived from the hierarchy masters (5.4); held in IoT Hub as device twin tags |
| Which namespace and message types apply at which level | `u_mes_syst_unsMessageType` |
| Which tags sit under an equipment node | `u_mes_perf_processTag` |
| The path a rejected message arrived with | `u_mes_syst_unsRejectedMessage.isa95Path` |

No collection lists every node with its path in one table. A read-only MongoDB view joining the hierarchy masters and the identities would give that list without storing a second copy of the path (open item O4).

### 5.9 Data flows

| Flow | Direction | Mechanism | MES component |
|---|---|---|---|
| Equipment data into the MES | Edge to MES | IoT Hub route, consumer group `mes-ingest`, event processor with checkpoints | UNS ingestion service: validates against `u_mes_syst_unsMessageType`, resolves master ids, adds MES context, writes the target collection, records rejects in `u_mes_syst_unsRejectedMessage` |
| Context, events and indicators out of the MES | MES to UNS | MongoDB change streams, device-to-cloud messages of `PN1-MES`, twin updates | UNS publisher; resume token in `u_mes_syst_systemConfiguration` (`uns.publisher.resumeToken`) |
| Namespace registry | MES to IoT Hub | IoT Hub service API | Registry sync service: identities and twin tags from master data; state kept in `u_mes_syst_iotHubIdentity` |
| Client data lake | UNS to data lake | IoT Hub route to Azure Data Lake Storage Gen2 | None; master data changes are sent by the publisher so the lake has the dimensions |
| ERP transactions | MES to and from ERP | `u_mes_syst_erpMessage`, connector ERP-PRD | Not through the UNS |
| Recipe and program download | MES to equipment | Direct OPC UA / Open Protocol write with checksum (`u_mes_plan_recipeDownload`) | Not through the UNS; only the verification event is sent |
| Signatures, audit trail, genealogy | Inside the MES | MongoDB | Not through the UNS |

### 5.10 Data conventions applied to UNS data

| Convention | Rule | Source |
|---|---|---|
| Time | Payload `ts` carries `+05:30`; the MES stores IST wall-clock digits with `+0000` | DATA-004 |
| Numbers | Plain JSON numbers parsed losslessly; Decimal128 for measurements, Double only for `tagValue` and `powerFactor` | D009, D070 |
| Identifiers | 16-digit string `_id`; business key `recordNo`; message ids as UUID text | D005, D029, D083 |
| Flat documents | Embedded payload arrays (for example leak test stages) become child collections | DATA-001 |
| Allowed values | Title Case (`Edge`, `MES`, `KPI` for `unsNamespace`); the payload property `ns` is sent in lower case | data_modeling_standard.md |

### 5.11 User interface

| Element | Content |
|---|---|
| Query screens and IvyConfigs | UNS Message Types (status, namespace, message class, sender type, ingested by MES); IoT Hub Identities (equipment, status, identity type, provisioning status, connection state, parent gateway); UNS Rejected Messages (received date range, equipment, status, identity, message type, rejection reason); IoT Devices gained an Edge Gateway filter; the nine collections with `sourceMessageUuid` carry it in their IvyConfig `post` list |
| Dynamic dropdown registry | `u_mes_syst_unsMessageType__id_name`, `u_mes_syst_iotHubIdentity__id_name` (150 registry documents in total) |
| MasterDict and cropdown | No new dictionary or cropdown; the new masters are small lists served by the registry (A028) |
| Stable tables | 3 new configurations; 10 regenerated for the new keys |
| Menu | SystemAndIntegration, section Unified Namespace (`2090_900`): UNS Message Types, IoT Hub Identities, UNS Rejected Messages |
| Labels | Acronyms IoT, UNS and MES in query labels |

### 5.12 Sample data

The ten sample identities were provisioned on 14 September 2026, the evening before the production fortnight. The vision station identity is in Sync Failed because no vision controller is registered. The leak tester disconnected on 25 September at 14:02. The ten rejected messages tie to real sample events or commissioning issues:
- the alarm A2031 sent on 17 September in an unregistered schema version;
- a PLC clock running ahead after a power interruption;
- a curve that arrived before its leak test result;
- a supplier test tool sending without sequence numbers;
- a counter reset after a firmware restart;
- a body truncated when the connection dropped.

`sourceMessageUuid` is filled only on documents that came from the UNS: machine states, readings, alarms, tightening and leak test results, energy readings and curves of the caliper universe, and operation executions captured by PLC signal. The pharma universe (RJ1) is outside the UNS scope (A027).

### 5.13 Generator and files

| File | Role |
|---|---|
| `05_generator/uns01.py` | Requirement set UNS_01: the three collections, ten added keys, allowed-value addition; merged through `ext_req01.py` |
| `05_generator/uns01_samples.py` | Sample rules of the set, merged through `sample_rules.py` |
| `05_generator/gen_specs.py` | Index rules for the new collections and the partial unique index on `sourceMessageUuid` |
| `05_generator/query_screens.py` | Query screen entries, label overrides, acronyms |
| `05_generator/gen_menu.py` | Menu section Unified Namespace |
| `02_architecture/data_flows/unified_namespace_design.md` | The design (version 7.0) |
| Reference PDF LIR-DF-UNS-REF-001 | Formal reference version of the design, delivered to the owner |
| `00_governance/decision_log.md`, `assumptions_log.md` | D081 to D083, A026 to A028 |

## 6. Open items

| No. | Item |
|---|---|
| O1 | Sample data findings F1 to F11 and F13 of the design (device-to-connector shift, device models, addresses, certificate expiry, tag addresses, connector targets, shift code in `shiftId`, event timing, energy equipment, marking station, OEE calculation time, RJ1 line areas) |
| O2 | Commissioning data: connector UNS-PN1, six IoT Edge gateway devices, UNS configuration entries |
| O3 | Owner decision on `shiftId` (shift code, as used by the Shift filter, or shift `_id`, as the reference rule requires) |
| O4 | Optional read-only view listing every namespace node with its path, identity and provisioning state |
| O5 | RJ1 (Ranjangaon OSD Plant) joining the UNS, with GMP validation of the UNS path |
| O6 | One IoT Hub per site or one enterprise hub; data lake format and retention agreed with the client |

## 7. Glossary

| Term | Meaning |
|---|---|
| Consumer group | Independent reader position on the IoT Hub event stream; each consumer reads all messages at its own pace |
| Device twin | JSON document per IoT Hub identity holding tags (set by the back end), desired properties (set by the back end, read by the device) and reported properties (set by the device) |
| Enrichment | Property that IoT Hub adds to every routed message, here taken from the twin tags of the sender |
| Identity translation | IoT Edge pattern in which a module sends messages for each downstream device under that device's own identity |
| ISA-95 path | Enterprise / site / area / line / work center / equipment, built from master record numbers |
| Message envelope | Common payload frame: schema, msgId, ts, tsSource, producer, seq, data |
| Report by exception | Sending a value only when it changes by more than the deadband |
| Store and forward | Local buffering at the edge while the hub is unreachable |
