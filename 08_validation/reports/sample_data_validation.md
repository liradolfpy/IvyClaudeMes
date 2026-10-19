# Sample data validation

Run: 12 October 2026 | Tool: 05_generator/gen_samples.py | Collections: 372 | Documents: 5420

| # | Check | Scope | Result | Findings |
|---|---|---|---|---|
| 1 | 10 documents per collection, 20 in dual Auto / Gamp collections | all collections | Pass | 0 |
| 2 | Every document has a unique _id | all collections | Pass | 0 |
| 3 | _id is a 16-digit numeric string | all collections | Pass | 0 |
| 4 | No ObjectId | all collections | Pass | 0 |
| 5 | No nested documents or arrays | all collections | Pass | 0 |
| 6 | All schema keys present, no extra keys, same order | all collections | Pass | 0 |
| 7 | Data types match the schema | all collections | Pass | 0 |
| 8 | Required keys are not null | all collections | Pass | 0 |
| 9 | Values are in the allowed list | all collections | Pass | 0 |
| 10 | Status values are approved | all collections | Pass | 0 |
| 11 | ID and display pairs are complete | all collections | Pass | 0 |
| 12 | Every reference points to an existing document | all collections | Pass | 0 |
| 13 | Display value equals the referenced document's display value | all collections | Pass | 0 |
| 14 | Business numbers (recordNo) unique per site in the collection | all collections | Pass | 0 |
| 15 | Parent and line number unique in child collections | all collections | Pass | 0 |
| 16 | Audit keys valid (transaction collections only) | all collections | Pass | 0 |
| 17 | Dates in logical order | all collections | Pass | 0 |
| 18 | Dates inside 2018-2027 | all collections | Pass | 0 |
| 19 | Quantities not negative | all collections | Pass | 0 |

Shell format: every Int32 is written with NumberInt(), Int64 with NumberLong(), Decimal128 as a plain number with its decimals kept (for example 1850.0, no NumberDecimal()), Double with Double(), dates with ISODate(); this is done by one formatting function for all files.

## Schema Observation

These points were noticed while filling the documents and are reported only. On 12 Oct 2026 the 44 collections and 212 keys of MES_ExternalRequirement_01 were added (D036-D042).

| # | Collection | Observation | What the samples do |
|---|---|---|---|
| 1 | u_mes_prod_recipe | Resolved on 12 Oct 2026 (MES_ExternalRequirement_01): recipeType now allows Press Program, Dispensing Program and Vision Job | The ten sample recipes are unchanged; executions at the press and at final inspection still carry no recipe |
| 2 | u_mes_plan_operationExecution | result is required, so an execution that is still running cannot be stored without a result | All ten executions are completed |
| 3 | u_mes_plan_container | ownerCustomerId is required, although in-plant trolleys and racks have no customer owner | All containers carry the customer of the part |
| 4 | u_mes_prod_operation, u_mes_prod_item | Exactly 10 documents: the eleventh operation (packing) and the items brake pad set and mounting bracket are not represented | Ten operations OP010 to OP100 and ten items |
| 5 | u_mes_prod_billOfMaterialComponent | The RH assembly BOM points to the LH body, because an RH body is not among the ten items | Left as is |
| 6 | all transaction collections | All documents belong to the Chakan plant; the other nine sites exist only in u_mes_mast_site | Plant is not varied in transactions, so that lines, work centers and equipment stay consistent with their site |
| 7 | u_mes_perf_reasonCode | The reason types added on 12 Oct 2026 (Hold Release, Interlock Override, Rework, Root Cause, Alarm Closure, Exposure Reset) have no sample reason code, because the ten sample codes are downtime causes | Hold, override, rework, root-cause, alarm-closure and reset references point to the downtime cause that fits the story |
| 8 | u_mes_qual_inspectionResult | positionNo, model and image keys are filled only where a sample result fits; no sample result was classified by a vision model | Model classifications are shown in u_mes_syst_modelPrediction |
| 9 | u_mes_mast_unitOfMeasure | The ten sample units have no newton, degree or millisecond | Curve envelope axis units are held as text (xUnitText, yUnitText), as delivered by the controller |
| 10 | u_mes_qual_measurementCurvePoint | A time-series collection; ten points of one press-in curve are shown, one second apart because the shell format carries whole seconds | Real curves carry 250 to 620 points each |
| 11 | u_mes_trac_genealogyLink | childSerialNumberId and childWipUnitId are empty, because all sample components are bought-in lots | Sub-assemblies serialised by the MES would use them |
| 12 | GMP_Pharma_01 collections | The ten sample electronic signatures all sign recipes, and no validation protocol, certificate of conformance or review report is among the ten controlled documents | electronicSignatureId and the protocol, report and certificate references of the GMP collections are null in the samples |
| 13 | u_mes_matl_dispenseRecord | No balance or scale is among the ten sample gauges | balanceGaugeId is null in the samples |
| 14 | u_mes_syst_computerisedSystem | No software supplier is among the ten sample suppliers | supplierId is null in the samples |
| 15 | u_mes_bmr_batchRelease, u_mes_qual_retentionSample | Assembly orders produce serialised units without a lot; release and retention of those units refer to the order or the serial number | lotId is null for assembly orders |
| 16 | u_mes_bmr_batchManufacturingRecord | No exported batch record is among the ten sample controlled documents | exportControlledDocumentId is null; the checksum, page count and export time of the four exported records are filled |
| 17 | u_mes_mmr_masterManufacturingRecord | Packaging specifications in the samples all carry the LH assembly as item | RH and body records reference the nearest specification or none |
| 18 | u_mes_syst_iotHubIdentity | The six IoT Edge gateway devices are not among the ten sample IoT devices | iotDeviceId is null for the three gateway identities and for the vision station, whose controller is not registered |
| 19 | UNS_01 keys | Only documents that came from the UNS carry sourceMessageUuid: machine states, readings, alarms, tightening and leak test results, energy readings and curves of the caliper universe, and operation executions captured by PLC signal | Documents of the pharma universe and documents entered in the MES have sourceMessageUuid null |

## How realistic the documents are

- Read through and corrected by hand: production orders, WIP units, operation executions, torque and leak results, lots, goods receipt lines, stock movements, inspection results, nonconformances, gauges, equipment, users, items, BOM components, routing steps, downtime events, serial numbers.
- Written collection by collection for MES_ExternalRequirement_01: the 44 new collections and the 212 added keys (05_generator/ext_req01_samples.py).
- Written collection by collection for GMP_Pharma_01: the 23 new collections and the 33 added keys (05_generator/gmp01_samples.py).
- Written collection by collection for UNS_01: the 3 new collections and the 10 added keys (05_generator/uns01_samples.py).
- Built by the same rules but not read line by line: the remaining collections. Their keys, types, references, allowed values and dates are checked by the table above; individual text or number combinations in them can still read oddly.
- Each collection has exactly ten documents, so stories are short: for example, ten leak tests are spread over four units.
