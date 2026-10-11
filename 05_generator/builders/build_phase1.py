import collections
from catalogue import C
OUT="/mnt/user-data/outputs/"
doms=collections.OrderedDict()
for c in C: doms.setdefault(c[1],[]).append(c)

RESEARCH = r'''# MES on MongoDB - Phase 1: research findings, feature matrix, collection catalogue

Project: ClaudeMes1 - Front Brake Caliper Assembly LH, Tier-1 plant, Pune
Prepared: 11 October 2026 | Status: Phase 1 complete, awaiting confirmation

## 0. How to read this document

Everything in sections 1 and 2 is drawn from public pages that were opened and read in this session; each claim is followed by its source. Where a public page did not confirm something you asked about, that is said plainly rather than filled in from memory. The data model in section 4 is my own design: the vendors' ideas are used as concepts, no vendor table or field names are copied, and the plant hierarchy follows the ISA-95 / IEC 62264 equipment model directly from the standard.

## 1. Research findings by product

### 1.1 Siemens Opcenter Execution
Entities and fields identified: product genealogy with forward and backward trace of products, components and materials; a self-auditing electronic device history record; nonconformance with automatic creation and notification, triage, quarantine, structured failure analysis, root cause and final disposition; structured data collection of product, process and quality data; enforcement of the correct operator, machine, material and recipe at each step; in-specification enforcement and SPC; electronic procedures executed in sequence; a workflow router and dispatch; multi-level BOMs. In the nonconformance integration with Teamcenter Quality an NC carries failure modes and a list of containers, each container gets its own containment action and its own disposition, and ownership can pass between MES and the quality system.
Sources: [Opcenter Execution Medical Device and Diagnostics fact sheet](https://www.plm.automation.siemens.com/media/global/en/Siemens-SW-Siemens-Opcenter-Execution-Medical-Device-and-Diagnostics-FS-45024-C13_tcm27-61667.pdf), [Expanded nonconformance management (Siemens blog)](https://blogs.sw.siemens.com/opcenter/expanded-nonconformance-management-for-semiconductor-manufacturing/), [Opcenter Execution Discrete in industrial machinery (white paper page)](https://resources.sw.siemens.com/en-US/white-paper-opcenter-execution-discrete-in-industrial-machinery/), [Opcenter Execution profile (FitGap)](https://us.fitgap.com/products/opcenter-execution).
Not confirmed: "bill of process" appears only as a label in the fact-sheet diagram and as one sentence in the white-paper page (closed-loop communication with PLM gives more detail in the bill of process); no public page read here describes its structure. None of the pages read mentions ISA-95 by name.

### 1.2 Rockwell Plex
Entities and fields identified: inventory managed by lot with lot and heat data, date attributes, and lot attributes with allowed values and tolerances that can block use or sale; barcoded labels for packages and master units, with label templates linked to customer, customer address or product; barcoded locations; every shop-floor operation and inventory movement logged as a transaction at the time it happens; upstream and downstream genealogy. In quality: process control plans with inspection instructions tied to product specifications; electronic check sheets; in-process inspection data feeding SPC with Cp/Cpk; first-piece, final inspection, dock audit and dimensional layout sheets; direct gauge and scale connection; problem reports using 8D and 5-Why with CAPA tracking; audit management with checklists; controlled documents with review and sign-off.
Sources: [Plex inventory management](https://plex.rockwellautomation.com/en-us/products/manufacturing-execution-system/inventory-management.html), [Plex quality management system](https://plex.rockwellautomation.com/en-us/quality-management-system-capterra.html).
Not confirmed: serial-number tracking, the word "container", PPAP and FMEA are not on the two pages read.

### 1.3 GE Vernova Proficy Smart Factory (Plant Applications)
Entities and fields identified: a plant model of departments, lines and units; OEE built from specification targets per product and unit, historian tags that capture downtime, waste and production events, and alarms on availability, performance, quality and OEE; a downtime event with start time, end time, location (department, line, machine), fault code, a reason with four levels filled from the reason tree, an action with four levels, and a comment that can be made mandatory; quality variables (measured, manual or calculated) with specification limits that take effect from a date and keep their history; SPC alarms with X-bar/R, X-bar/S, X-MR, P and U charts; alarms that record cause, duration, acknowledgement and action; process orders downloaded from ERP with a schedule view of planned versus actual; genealogy across manufacturing steps.
Sources: [OEE configuration overview](https://www.gevernova.com/software/documentation/proficy-plant-applications/legacy/ProficyPAManagingEfficiency/oee_config_overview.htm), [Add a downtime event](https://www.ge.com/digital/documentation/proficy-plant-applications/version2022/t_dos_add_downtime_event.html), [Quality monitoring in MES (VIX Automation, Proficy integrator)](https://vix.com.pl/en/quality-monitoring-in-mes/), [Proficy production module (E Tech Group)](https://etechgroup.com/blog/manufacturing/proficy-production-module/).

### 1.4 Tulip Interfaces
Entities and fields identified (from Tulip's own validation specification): app and app version; step and step group, a step being a named view reached through trigger logic and operator actions; triggers for apps and for machines; tables, records and record fields, with linked-record fields between tables; the completion record, described as a persistent log of app execution metrics and state; connectors, connector functions and connector environments; machines as digital twins, machine attributes that map raw data to a machine, and machine activity as a running history of machine state; stations and station groups that bind a player to machines and devices; approval types and app approvals before publishing; e-signature form steps; users, roles and groups. Tulip's guidance for work-instruction apps is one table for procedures, one for tasks and one for parameters, linked by record references.
Sources: [Tulip product specifications (GxP documentation)](https://gxp-docs.tulip.co/lts12-rev5/product_specs.html), [Table structure for work-instruction apps](https://support.tulip.co/docs/table-structure-for-work-instructions-apps).

### 1.5 Critical Manufacturing MES
Entities and fields identified: materials as lots, batches and serialised units with sub-materials; material transactions track-in, track-out, move-next, split, merge, hold, release, rework, change flow, temporary off-flow, with minimum and maximum time limits between steps; hierarchical containers with positions and store, retrieve, dock and undock transactions; full history and genealogy; data collections triggered at track-in or track-out by context, with parameters, limit sets and instruments; recipe management with versioning and deployment; hierarchical equipment with state history; maintenance plans that block equipment when overdue; calibration that blocks expired instruments; tooling life and usage; SPC with actions on violation; CAPA and exception workflows; nonconformance with lot-by-lot scrap or rework disposition; counter, time and AQL based sampling; pick lists, transfer orders and replenishment; label and document printing; operator certification, shift planning and shift logbook; alarm management with severity and distribution lists; Connect IoT equipment integration; queued bidirectional ERP and PLM integration; document management with read-and-sign; electronic signatures.
Sources: [Complete modular solution](https://criticalmanufacturing.com/en/critical-manufacturing-mes/complete-modular-solution), [Materials and containers data sheet](https://www.criticalmanufacturing.com/wp-content/uploads/2022/02/CMF211865-Data-Sheet-Materials-Containers.pdf), [Data collection module guide](https://help.criticalmanufacturing.com/tutorials/modules/data-collection/index.md).
Not confirmed: the exception-management help page that would describe the protocol states did not load, so the 8D mapping of its protocols is not confirmed from a primary source here. The 8D structure in this model comes from the automotive 8D method itself.

### 1.6 Aegis FactoryLogix
Entities and fields identified: digital manufacturing engineering with process definition, CAD and BOM import, electronic revision approval and offline machine programs; work-instruction authoring with a document repository and interactive operator guidance; material receiving and inspection, lean materials management, kitting and dispatch, mobile stock and kitting transactions, shortage resolution; traceability covering product history, sub-assembly genealogy, material lot content and inspection and test results; SPC, supplier quality, nonconformance lifecycle, CAPA and failure reporting; repair and returns; machine data acquisition over OPC UA and CFX; conveyor tracking used for process interlocking.
Source: [FactoryLogix brochure](https://info.aiscorp.com/hubfs/FactoryLogix%20Brochure/English/FactoryLogix_brochure_en.pdf?hsLang=ru).
Not confirmed: operator certification is not in the brochure.

### 1.7 Eyelit
Entities and fields identified: version-controlled routings built by process modelling, with parallel and conditional flows and re-entry for rework, re-inspection, test and repair; genealogy at serial, lot, batch, kit and sub-assembly level; asset management covering equipment availability, preventive maintenance, tooling and durables, with tools recorded against the controlled history record; a real-time SPC engine; nonconformance and CAPA; electronic device history record; downtime analysis and OEE; a schedule received from planning with a WIP feedback loop; lot hold status and reason.
Sources: [Eyelit manufacturing execution system](https://eyelit.com/manufacturing-execution-system/), [Eyelit MES and QMS listing (GetApp)](https://www.getapp.ca/software/2078576/eyelit-mes-and-qms).
Not confirmed: the rework and durables statements come from the third-party listing; Eyelit's own page does not spell them out.

### 1.8 Infor MES
Entities and fields identified: production orders and optionally routings downloaded from ERP, with operation confirmations returned; orders released digitally with documents and instructions attached; production runs started and stopped by an OPC or PLC signal; barcode scan and enforced sign-off per operation; alerts when an order is off-track and when a job is nearly complete; machine parameters and set-points; nonconformance and CAPA recording; quality checks that fall due, with gauge, file or manual input and SPC; OEE; planned, operator-led and condition-based maintenance; bidirectional traceability and label printing; energy monitoring of plant equipment; continued operation during an ERP outage with later resynchronisation.
Sources: [Infor MES overview (documentation)](https://docs.infor.com/mes/2026.10/en-us/mesuaal/mesovg/egi1655887690346.html), [Infor MES production orders (documentation)](https://docs.infor.com/mes/2026.x/en-us/mesuaal/mesovg/foq1738152989231.html), [Infor MES brochure](https://dam.infor.com/api/public/content/b9f2dccd2ec44dd6ad2830362b511502?v=530d0482).
Not confirmed: the pages read do not describe a labour time-booking function or a changeover function as such; changeover appears only as an alert that a job is nearly complete. The labour and changeover collections in this model are therefore my own design from shop-floor practice, not derived from Infor.

### 1.9 SAP Digital Manufacturing
Entities and fields identified: the shop order with full or partial, repeatable release; the SFC (shop floor control number) as the instance being built, one per serialised unit or one per lot; a routing referenced at release that queues SFCs at the first operation and moves them on, or to a special operation when defect data requires it; work centre and resource entered at operation start; the production operator dashboard for start, complete, work instructions, component consumption, data collection and nonconformance logging; data collection groups with header, parameters and assignment to manufacturing objects; parameters with name, prompt, unit, target, minimum and maximum, an override flag and automatic NC logging on override; NC codes that carry a disposition routing, for example a rework routing.
Sources: [Life cycle of production orders (SAP Learning)](https://learning.sap.com/learning-journeys/executing-processes-for-discrete-industries-in-sap-digital-manufacturing/explaining-the-life-cycle-of-production-orders_cbc18198-d2f0-47ca-8e48-e5d60b20ac61), [Automatic disposition to rework after out-of-limit data collection (SAP Community)](https://blogs.sap.com/t5/product-lifecycle-management-blogs-by-sap/automatic-disposition-to-rework-after-out-of-limit-data-collection-within/ba-p/13574594).

### 1.10 NoMuda VisualFactory
Entities and fields identified: step-by-step visual instructions with components, tools, checks, warnings, drawings and video, adapting automatically to product variant and routing data; the next instruction released only after the previous step is verified; tools scanned before use and exchanged when out of calibration; integration with torque tools, gauges and measurement devices; operators logging in with a badge tied to trained operations and refused at stations they are not qualified for, with skills held at task level and supervisor sign-off; a digital birth certificate per product listing steps, technicians, times, build settings and full parts list; capture of labour hours, stoppages, cycle times and rework rates; andon calls triggered by conditions such as low material; work orders and configuration synchronised from ERP with execution data returned.
Sources: [NoMuda digital work instructions](https://nomuda.com/mes-solutions/digital-work-instructions/), [NoMuda operator training](https://nomuda.com/mes-solutions/operator-training-software/), [NoMuda work order processing](https://nomuda.com/mes-solutions/work-order-processing/), [VisualFactory 20.3 release note](https://nomuda.com/blog/work-smarter-with-nomuda-visualfactory-20-3/), [VisualFactory profile (Zenoot)](https://zenoot.com/company/nomuda-visualfactory/), [Carnegie Robotics case study (Zenoot)](https://zenoot.com/articles/a-perfect-marriage-with-our-manufacturing-processes-how-nomuda-visualfactory-enables-carnegie-robotics-to-continue-pushing-boundaries/).
Not confirmed: kitting is not mentioned on any NoMuda page read, and the term "skills matrix" is not used (skills are described at task level).

## 2. Feature matrix

Legend: ● = stated in the public sources read in this session; ◐ = partly or indirectly stated; ○ = not found in the sources read. ○ does not mean the product lacks the feature, only that the pages listed in section 1 do not show it.

| # | Feature | Opcenter | Plex | Proficy | Tulip | Critical Mfg | FactoryLogix | Eyelit | Infor MES | SAP DM | VisualFactory |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Plant hierarchy / plant model | ○ | ○ | ● | ◐ | ● | ○ | ○ | ◐ | ◐ | ○ |
| 2 | Production / shop order management | ◐ | ○ | ● | ○ | ● | ○ | ◐ | ● | ● | ● |
| 3 | Routing with rework and disposition paths | ● | ○ | ○ | ◐ | ● | ◐ | ● | ◐ | ● | ◐ |
| 4 | Bill of process / process definition | ◐ | ○ | ○ | ◐ | ● | ● | ● | ◐ | ◐ | ◐ |
| 5 | Scheduling and dispatch list | ● | ○ | ● | ○ | ● | ● | ● | ◐ | ◐ | ○ |
| 6 | Serialised unit tracking | ◐ | ○ | ○ | ○ | ● | ◐ | ● | ○ | ● | ◐ |
| 7 | Lot / batch tracking | ◐ | ● | ◐ | ○ | ● | ● | ● | ● | ● | ○ |
| 8 | Container tracking | ● | ◐ | ○ | ○ | ● | ○ | ○ | ○ | ○ | ○ |
| 9 | Genealogy / as-built record | ● | ● | ● | ◐ | ● | ● | ● | ● | ◐ | ● |
| 10 | Digital work instructions | ● | ◐ | ○ | ● | ● | ● | ○ | ● | ● | ● |
| 11 | Variant-driven instructions | ◐ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| 12 | Step enforcement / process verification / interlock | ● | ◐ | ○ | ● | ● | ● | ○ | ● | ◐ | ● |
| 13 | Data collection with limits | ● | ● | ● | ◐ | ● | ● | ○ | ● | ● | ● |
| 14 | SPC | ● | ● | ● | ○ | ● | ● | ● | ● | ○ | ○ |
| 15 | Control plans / check sheets | ○ | ● | ○ | ○ | ◐ | ○ | ○ | ◐ | ○ | ◐ |
| 16 | Nonconformance and disposition | ● | ● | ◐ | ○ | ● | ● | ● | ● | ● | ● |
| 17 | Hold / quarantine | ● | ◐ | ○ | ○ | ● | ○ | ◐ | ○ | ○ | ○ |
| 18 | CAPA / 8D | ◐ | ● | ○ | ○ | ● | ● | ● | ● | ○ | ○ |
| 19 | Gauge calibration / instrument control | ○ | ◐ | ○ | ○ | ● | ○ | ○ | ◐ | ○ | ● |
| 20 | Audits and document control | ○ | ● | ○ | ◐ | ● | ◐ | ○ | ◐ | ○ | ○ |
| 21 | Inventory, locations, movements | ○ | ● | ○ | ○ | ● | ● | ● | ● | ◐ | ○ |
| 22 | Kitting / line-side logistics | ○ | ○ | ○ | ○ | ◐ | ● | ◐ | ○ | ○ | ○ |
| 23 | Label printing | ○ | ● | ○ | ○ | ● | ○ | ○ | ● | ○ | ○ |
| 24 | OEE | ◐ | ○ | ● | ◐ | ○ | ○ | ● | ● | ○ | ◐ |
| 25 | Downtime with reason tree | ○ | ○ | ● | ◐ | ◐ | ○ | ◐ | ○ | ○ | ◐ |
| 26 | Machine connectivity, tags, historian | ◐ | ◐ | ● | ● | ● | ● | ○ | ● | ○ | ● |
| 27 | Recipes / machine parameters | ● | ◐ | ○ | ○ | ● | ◐ | ◐ | ● | ○ | ○ |
| 28 | Torque / smart tool integration | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● |
| 29 | Preventive maintenance | ○ | ○ | ○ | ○ | ● | ○ | ● | ● | ○ | ○ |
| 30 | Tooling and durables | ○ | ○ | ○ | ○ | ● | ○ | ● | ○ | ○ | ◐ |
| 31 | Labour, skills, certification | ○ | ○ | ○ | ◐ | ● | ○ | ○ | ◐ | ○ | ● |
| 32 | Changeover | ○ | ○ | ◐ | ○ | ○ | ○ | ○ | ◐ | ○ | ○ |
| 33 | ERP / PLM integration | ◐ | ◐ | ● | ● | ● | ○ | ○ | ● | ◐ | ● |
| 34 | Electronic signature / approvals | ◐ | ● | ○ | ● | ● | ● | ◐ | ● | ○ | ◐ |
| 35 | Alarms, notifications, andon | ● | ○ | ● | ○ | ● | ○ | ○ | ● | ○ | ● |
| 36 | Energy monitoring | ○ | ○ | ○ | ○ | ○ | ○ | ○ | ● | ○ | ○ |
| 37 | Composable operator apps | ○ | ○ | ○ | ● | ◐ | ○ | ○ | ○ | ○ | ○ |

## 3. Best-of-breed ideas adopted and where they appear

| Product | Idea adopted (concept only) | Where it appears in this model |
|---|---|---|
| Siemens Opcenter | One nonconformance covering several containers or units, each with its own containment action and its own disposition; quarantine as a state separate from the NC; an electronic history record assembled per unit | nonconformances (affected objects array with per-object disposition), quality_holds, as_built_records |
| Siemens Opcenter | Enforcing the right operator, machine, material and recipe at each step by binding them in one process definition | bills_of_process (per-step required equipment, tool, recipe, skill, instruction, inspection plan) |
| Rockwell Plex | Control plan and check sheet as first-class shop-floor objects; lot attributes with tolerances that block use; label templates resolved by customer, ship-to or product; every movement a transaction | control_plans, check_sheets, check_sheet_results, lots, label_templates, labels, material_movements |
| GE Vernova Proficy | Downtime event with fault plus a four-level reason path plus an action path; product-specific targets as the OEE basis; specification limits that become effective from a date | reason_codes (materialised path), downtime_events, oee_records, lines (ideal rates), characteristics and spc_charts (dated limit revisions), process_tags, process_data |
| Tulip | The completion record as an immutable log of what happened at each step; versioned operator apps made of steps and triggers; machine attributes as the mapping layer between raw signals and a machine; connector definitions kept as data | step_completions, operator_apps, process_tags, equipment_states, integration_connectors, iot_devices |
| Critical Manufacturing | Track-in / track-out as the execution grain; hold, split, merge and rework as explicit transactions; containers with positions; equipment blocked by overdue maintenance or expired calibration; sampling by counter, time or AQL; shift logbook | operation_executions, component_lot_links, containers, maintenance_plans, gauges, sampling_plans, shift_handovers, recipes |
| Aegis FactoryLogix | Receiving inspection linked to the supplier lot; kitting and dispatch to the line; revision approval of process definitions; process interlocking | goods_receipts, kits, material_requests, engineering_changes, bills_of_process |
| Eyelit | Rework as a re-entry path inside the routing rather than a free-text loop; tools and durables with life tracked against the product history | routings (rework and alternate steps), rework_orders, tools, tool_life_records |
| Infor MES | ERP messages kept as a queue so the shop floor keeps running when ERP is down; operation sign-off; energy as a monitored quantity; job-nearly-complete alert as the changeover trigger | erp_messages (idempotency key, retry state), electronic_signatures, energy_readings, changeovers, notifications |
| SAP Digital Manufacturing | The unit-in-process identifier distinct from the customer serial; partial order release; data collection groups assigned to operations; NC codes that carry a disposition routing | wip_units versus serial_numbers, production_orders (release history), inspection_plans, defect_codes (default disposition routing) |
| NoMuda VisualFactory | Instruction steps filtered by variant; torque and gauge results captured into the step; operator lock-out from skills; the digital birth certificate; andon call from a station | work_instructions (variant applicability per step), variants, torque_results, certifications, skills, as_built_records, andon_events |

Added from automotive practice rather than from any of the ten products (none of the pages read covers them): PFMEA, PPAP, MSA, deviation permits, customer complaints with PPM, leak test results, safety incidents and customer delivery schedules. These follow the AIAG core tools and IATF 16949 clauses directly.

## 4. Collection catalogue (deliverable A)

'''
TAIL = r'''
## 5. Assumptions made in Phase 1

1. Company and customer names are fictional. The plant is modelled as Varuna Brake Systems Pvt. Ltd., Chakan Plant, Pune (site code PN1); the OEM is modelled as Sahyadri Motors Ltd. No real OEM part numbers or specifications are used.
2. Volume estimates assume 2,400 calipers per day (LH and RH together) over three shifts and 300 working days, about 720,000 units per year, at the Pune site only.
3. Tracking grain: casting, heat treatment, machining, washing and anodising are tracked by lot (casting lot, furnace charge, anodising load). A unit identifier is created when the body enters piston and seal assembly, and the customer serial and 2D code are marked at laser marking. This is why wip_units and serial_numbers are separate collections.
4. Seed-data timeline: Monday 28 September 2026 to Saturday 10 October 2026, with Friday 2 October (Gandhi Jayanti) as a holiday and Sunday 4 October as the weekly off. Shifts A 06:00-14:00, B 14:00-22:00, C 22:00-06:00 IST, stored as UTC (00:30, 08:30, 16:30 UTC starts).
5. The "exactly 10 documents" rule applies to master collections too. enterprises will hold 10 group legal entities and sites 10 group locations, but all transactions belong to the Pune site. work_centres and equipment are limited to 10 each, so final inspection and packing share one work centre (WC-FIP-01) while remaining two separate operations.
6. Global reference data (enterprises, units_of_measure, roles) still carries a siteId, set to the owning site, plus a scope field with value ENTERPRISE, so the "every document has a site reference" rule holds without exception.
7. _id is a string of the form PREFIX-businessKey (for example PO-1000412). In the seed data, event collections use readable sequential keys; for production I recommend a time-sortable key such as a ULID behind the same prefix.
8. Time-series: process_data and energy_readings are recommended as MongoDB time-series collections, and equipment_states and production_counts are candidates. MongoDB does not allow a JSON Schema validator on a time-series collection, so for those four the validator in Phase 2 is documentation enforced by the application. The seed .bson files restore as ordinary collections; create_indexes.js will include the optional time-series creation commands.
9. Process values (bleed screw torque, leak-test pressures and limits, T6 temperatures) will be representative engineering values for a single-piston floating caliper, not any OEM's actual specification. They are fixed in the register in Phase 2 before any data is generated.

## 6. Two points that need your decision

The process has 11 routing operations (OP010 casting to OP110 packing; dispatch is a shipment, not an operation), but the seed rule is exactly 10 documents per collection. For the operations collection only, either (a) allow 11 documents so each operation has its own master record, which I recommend, or (b) keep 10 by holding final inspection and packing as one operation with two steps. The same applies to items: the caliper BOM plus the raw ingot and the RH variant comes to 12 items, so I recommend 12 documents there (the strict-10 alternative is in the register, section 3.1). Every other collection fits the rule of 10.

## 7. What comes next

Phase 2 covers the 104 collections in 11 replies of 8 to 10 collections, in the domain order above, each with field dictionary, embed-versus-reference justification, indexes, JSON Schema validator and one full Extended JSON sample. The Mermaid entity relationship diagram and the one-page order-to-dispatch data flow are delivered with the last Phase 2 reply. Phase 3 generates, validates and zips the BSON files.
'''
def cat():
    s="Total: %d collections in %d domains.\n\n"%(len(C),len(doms))
    s+="| Domain | Collections |\n|---|---|\n"
    for d,v in doms.items(): s+="| %s | %d |\n"%(d,len(v))
    n=0
    for d,v in doms.items():
        s+="\n### Domain %s\n\n| # | Collection | Purpose | Inspired by | Relationships (references to) | Estimated volume per year | Storage |\n|---|---|---|---|---|---|---|\n"%d
        for c in v:
            n+=1
            s+="| %d | %s | %s | %s | %s | %s | %s |\n"%(n,c[0],c[4],c[5],", ".join(c[6]) or "none (top of hierarchy)",c[7],c[8])
    return s
open(OUT+"phase1_research_feature_matrix_catalogue.md","w").write(RESEARCH+cat()+TAIL)

REG='''# data_model_register.md

MES on MongoDB - Front Brake Caliper Assembly LH - Pune
Register version: 1.1 (Phase 1 plus key list) | Date: 11 October 2026 | Database: mes | Collections: %d

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

'''%len(C)
def reg():
    s=""; n=0
    for d,v in doms.items():
        s+="\n### %s\n\n| # | Collection | _id pattern | Business key field | References (collection) | Storage | Embed / reference decision |\n|---|---|---|---|---|---|---|\n"%d
        for c in v:
            n+=1
            s+="| %d | %s | %s-<%s> | %s | %s | %s | %s |\n"%(n,c[0],c[2],c[3],c[3],", ".join(c[6]) or "none",c[8],c[9])
    return s
REGT='''
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
'''
open(OUT+"data_model_register.md","w").write(REG+reg()+REGT)
