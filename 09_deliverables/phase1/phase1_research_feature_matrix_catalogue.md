# MES on MongoDB - Phase 1: research findings, feature matrix, collection catalogue

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

Total: 104 collections in 10 domains.

| Domain | Collections |
|---|---|
| 1 Enterprise and master data | 16 |
| 2 Product definition | 9 |
| 3 Planning and execution | 12 |
| 4 Materials | 11 |
| 5 Traceability | 4 |
| 6 Quality | 23 |
| 7 Equipment and performance | 10 |
| 8 Maintenance and tooling | 5 |
| 9 Integration and system | 11 |
| 10 Energy, safety and andon | 3 |

### Domain 1 Enterprise and master data

| # | Collection | Purpose | Inspired by | Relationships (references to) | Estimated volume per year | Storage |
|---|---|---|---|---|---|---|
| 1 | enterprises | Legal entities of the group (ISA-95 Enterprise level); tax and registration data | Opcenter, Proficy | none (top of hierarchy) | <20 total | standard |
| 2 | sites | Plants and warehouses (ISA-95 Site); timezone, address, IATF certificate | Proficy, CM, Infor | enterprises | <20 total | standard |
| 3 | areas | Production and support areas inside a site (ISA-95 Area) | Proficy, CM | sites | 10-30 per site | standard |
| 4 | lines | Production lines / cells (ISA-95 Production Line / Work Cell) | Proficy, Tulip | sites, areas | 10-40 per site | standard |
| 5 | work_centres | Stations where operations are executed and booked; ERP work centre mapping | SAP DM, Infor, Tulip | sites, areas, lines | 50-200 per site | standard |
| 6 | equipment | Machines, furnaces, testers (ISA-95 Unit / Equipment); hierarchy, make, model, capability | CM, Proficy, Tulip, SAP DM | sites, lines, work_centres, suppliers | 200-1,000 per site | standard |
| 7 | shifts | Shift patterns with start/end and breaks | CM, Infor, Proficy | sites | 3-10 per site | standard |
| 8 | calendars | Working calendars with holidays and exception days per site / line | CM, Infor | sites, shifts, lines | 1-20 per site per year | standard |
| 9 | shift_rosters | Crew assignment per production day, shift and line (who is planned where) | CM, NoMuda | sites, shifts, lines, users, work_centres | ~10,000 | standard |
| 10 | roles | Named sets of permissions (operator, setter, quality engineer ...) | Tulip, SAP DM | sites | 10-40 | standard |
| 11 | users | People and system accounts; badge id, role, home work centre | Tulip, CM, NoMuda | sites, roles, shifts, work_centres | 300-1,500 per site | standard |
| 12 | skills | Skill definitions required by operations (e.g. leak-test operation, CMM programming) | NoMuda, CM | sites, operations | 50-300 | standard |
| 13 | certifications | Skills-matrix entries: user x skill, level, valid-from/to, assessor; used for operator lock-out | NoMuda, CM | sites, users, skills | 5,000-20,000 | standard |
| 14 | customers | OEMs and aftermarket customers; ship-to addresses, label and ASN requirements | Plex, CM | sites | 10-100 | standard |
| 15 | suppliers | Material, tooling and service suppliers; approval status, certificates, PPM rating | Plex, Aegis | sites | 100-500 | standard |
| 16 | units_of_measure | Units and conversion factors (EA, kg, N.m, bar, mm, um, kWh) | SAP DM, Proficy | sites | 30-80 | standard |

### Domain 2 Product definition

| # | Collection | Purpose | Inspired by | Relationships (references to) | Estimated volume per year | Storage |
|---|---|---|---|---|---|---|
| 17 | items | Parts: finished caliper, semi-finished body, purchased components, raw material, consumables; drawing revision | Plex, SAP DM, CM | sites, units_of_measure, customers, suppliers, engineering_changes | 500-5,000 | standard |
| 18 | variants | Product variants (LH/RH, piston diameter, pad compound, market) that drive BOM, instruction and label selection | NoMuda, Opcenter | sites, items, customers | 10-200 | standard |
| 19 | boms | Multi-level bills of material per item revision with effectivity | Opcenter, CM, SAP DM | sites, items, units_of_measure, variants, engineering_changes | 500-3,000 | standard |
| 20 | operations | Standard operation library (casting, T6, machining ... packing) reused by routings | SAP DM, Eyelit | sites, work_centres, skills | 50-500 | standard |
| 21 | routings | Sequence of operations per item, including rework / disposition routings and alternate paths | SAP DM, Eyelit, Opcenter, CM | sites, items, operations, work_centres, engineering_changes | 500-3,000 | standard |
| 22 | bills_of_process | Per routing step: required equipment, tools, recipe, work instruction, data collection, consumed components, cycle time | Opcenter, Aegis, CM | sites, items, routings, operations, equipment, tools, recipes, work_instructions, inspection_plans, boms, skills | 500-3,000 | standard |
| 23 | work_instructions | Versioned visual work instructions with steps, media, cautions, variant applicability, required checks | NoMuda, Tulip, Aegis, SAP DM | sites, items, operations, variants, documents, characteristics, tools, engineering_changes | 1,000-5,000 | standard |
| 24 | recipes | Machine parameter sets with set-points and limits (die temperature, furnace profile, CNC program, torque program, leak-test program) | CM, Infor, Opcenter | sites, equipment, items, operations, process_tags, engineering_changes | 500-3,000 | standard |
| 25 | engineering_changes | Engineering change notices with affected objects, approvals and effectivity (cut-in serial / date) | Aegis, Opcenter | sites, items, users, customers, documents | 200-1,000 | standard |

### Domain 3 Planning and execution

| # | Collection | Purpose | Inspired by | Relationships (references to) | Estimated volume per year | Storage |
|---|---|---|---|---|---|---|
| 26 | customer_schedules | OEM delivery schedules / releases (demand that drives production orders and shipments) | Infor, CM, Plex | sites, customers, items | 5,000-20,000 | standard |
| 27 | production_orders | Shop orders from ERP: item, quantity, routing/BOM version, partial releases, status | SAP DM, Infor, Proficy, NoMuda | sites, items, boms, routings, lines, customer_schedules, erp_messages | 8,000-15,000 | standard |
| 28 | production_schedules | Finite schedule per line and shift with sequenced orders, planned start/end | Proficy, CM, Eyelit, Aegis | sites, lines, shifts, production_orders, calendars | ~10,000 | standard |
| 29 | dispatch_lists | Prioritised work queue per work centre shown to the operator | Opcenter, CM, SAP DM | sites, work_centres, production_orders, lots, shifts | ~100,000 | standard |
| 30 | operation_executions | Start / complete record of an operation on a unit or lot: who, where, when, result, cycle time (track-in / track-out) | SAP DM, CM, Eyelit, Infor | sites, production_orders, wip_units, lots, operations, routings, work_centres, equipment, users, shifts, recipes | ~4.3 million | standard, partitioned by month |
| 31 | step_completions | Completion record for each work-instruction step: values entered, confirmations, duration, device data | Tulip, NoMuda | sites, operation_executions, work_instructions, wip_units, users, work_centres | ~20 million | standard, archive after 15 months |
| 32 | wip_units | Serialised unit in production (shop-floor control number): current operation, status, quality state | SAP DM, CM, Eyelit | sites, production_orders, items, variants, lots, serial_numbers, routings, operations, containers | ~720,000 | standard |
| 33 | lots | Lots and batches: supplier lots, melt/heat lots, casting lots, heat-treatment charges, anodising loads | Plex, CM, Eyelit, Infor | sites, items, suppliers, goods_receipts, production_orders, storage_locations | ~40,000 | standard |
| 34 | containers | Bins, trolleys, returnable crates and pallets with contents and nesting | CM, Opcenter, Plex | sites, items, lots, storage_locations, packaging_specifications, customers | ~60,000 active and historic | standard |
| 35 | labour_bookings | Clock-on / clock-off of people against orders, operations and indirect activities | Infor, NoMuda, CM | sites, users, production_orders, operations, work_centres, shifts | ~350,000 | standard |
| 36 | changeovers | Changeover from one item / variant to another: planned vs actual duration, checklist, first-off approval | Infor, Proficy | sites, lines, work_centres, equipment, production_orders, items, users, tools, check_sheet_results | ~3,000 | standard |
| 37 | shift_handovers | Shift logbook: output, open issues, safety and quality notes, acknowledgements | CM, Infor | sites, lines, shifts, users, production_orders, downtime_events, nonconformances | ~10,000 | standard |

### Domain 4 Materials

| # | Collection | Purpose | Inspired by | Relationships (references to) | Estimated volume per year | Storage |
|---|---|---|---|---|---|---|
| 38 | storage_locations | Warehouses, racks, line-side supermarkets, quarantine cage, dispatch bay | Plex, CM | sites, areas, work_centres | 500-5,000 | standard |
| 39 | inventory_balances | Stock on hand per item, lot, location and stock status | Plex, Infor, Eyelit | sites, items, lots, storage_locations, containers, units_of_measure | ~20,000 live rows | standard |
| 40 | material_movements | Every stock transaction: receipt, putaway, issue to line, return, scrap, transfer, shipment | Plex, CM, Aegis | sites, items, lots, containers, storage_locations, users, production_orders, goods_receipts, shipments | ~1.5 million | standard, partitioned by month |
| 41 | goods_receipts | Receipts from suppliers with lines, supplier lot, certificate, incoming inspection status | Aegis, Plex | sites, suppliers, items, lots, storage_locations, users, inspection_results | ~12,000 | standard |
| 42 | kits | Kits of components picked for an order / line-side delivery | Aegis, CM | sites, production_orders, items, lots, storage_locations, work_centres, users | ~25,000 | standard |
| 43 | material_requests | Line-side replenishment calls (e-kanban) from a work centre to stores | CM, NoMuda, Aegis | sites, work_centres, items, storage_locations, users, andon_events | ~80,000 | standard |
| 44 | material_consumptions | Component / lot consumed at an operation on a unit or lot (backflush or scanned) | SAP DM, CM, Plex | sites, operation_executions, production_orders, wip_units, lots, items, work_centres, units_of_measure | ~8 million | standard, partitioned by month |
| 45 | packaging_specifications | Pack instruction: container type, quantity per bin, layers, dunnage, label template | Plex, Infor | sites, items, customers, label_templates | 100-500 | standard |
| 46 | label_templates | Label layouts (unit 2D code, bin label, customer shipping label, hold tag) | Plex, CM | sites, customers | 20-100 | standard |
| 47 | labels | Printed label instances with payload, printer, reprint count | Plex, CM, Infor | sites, label_templates, wip_units, containers, lots, shipments, users, iot_devices | ~1 million | standard |
| 48 | shipments | Dispatch to customer: invoice / ASN, vehicle, containers shipped, proof of delivery | Plex, CM | sites, customers, customer_schedules, containers, items, users, storage_locations | ~3,500 | standard |

### Domain 5 Traceability

| # | Collection | Purpose | Inspired by | Relationships (references to) | Estimated volume per year | Storage |
|---|---|---|---|---|---|---|
| 49 | serial_numbers | Registry of every serial / 2D code issued: status, mark grade, unit and shipment linkage | SAP DM, CM, Eyelit | sites, items, wip_units, production_orders, number_ranges, labels, shipments | ~720,000 | standard |
| 50 | genealogy_links | As-built parent-child edges: unit to component serial or component lot, with operation and time | Opcenter, CM, Eyelit, Plex | sites, wip_units, serial_numbers, lots, items, operation_executions, material_consumptions | ~6.5 million | standard, partitioned by month |
| 51 | component_lot_links | Lot-to-lot lineage: ingot heat to melt to casting lot to heat-treatment charge to anodising load; split and merge | CM, Plex, Proficy | sites, lots, items, operation_executions | ~120,000 | standard |
| 52 | as_built_records | Device-history summary per shipped unit: components, key results, operators, sign-off (digital birth certificate) | NoMuda, Opcenter, Eyelit | sites, wip_units, serial_numbers, production_orders, items, genealogy_links, torque_results, leak_test_results, inspection_results, shipments | ~720,000 | standard |

### Domain 6 Quality

| # | Collection | Purpose | Inspired by | Relationships (references to) | Estimated volume per year | Storage |
|---|---|---|---|---|---|---|
| 53 | characteristics | Product and process characteristics with nominal, tolerance, class (critical / significant), method | Plex, Proficy, SAP DM | sites, items, operations, units_of_measure, gauges | 2,000-10,000 | standard |
| 54 | control_plans | AIAG control plan per item and phase (prototype, pre-launch, production) | Plex | sites, items, routings, operations, characteristics, pfmeas, gauges, users, engineering_changes | 200-1,000 | standard |
| 55 | inspection_plans | Executable data-collection group per operation: which characteristics, sample size, frequency, reaction | SAP DM, CM, Plex | sites, control_plans, items, operations, characteristics, sampling_plans, gauges, work_centres | 1,000-5,000 | standard |
| 56 | sampling_plans | Sampling rules: AQL tables, skip-lot, time or counter based frequency | CM, Plex | sites | 20-100 | standard |
| 57 | check_sheets | Check sheet definitions: start-of-shift checks, poka-yoke verification, first-off, autonomous maintenance | Plex, CM, Tulip | sites, work_centres, equipment, operations, items | 200-1,000 | standard |
| 58 | check_sheet_results | Completed check sheets with answers, failures and reactions | Plex, Tulip | sites, check_sheets, work_centres, equipment, users, shifts, production_orders | ~150,000 | standard |
| 59 | inspection_results | Measured and attribute results per unit / lot / receipt against a characteristic | Plex, SAP DM, CM, Proficy | sites, inspection_plans, characteristics, wip_units, lots, operation_executions, gauges, users, work_centres, goods_receipts | ~12 million | standard, partitioned by month |
| 60 | spc_charts | Chart definition per characteristic and work centre: chart type, subgroup size, control limits, rules | Proficy, CM, Eyelit, Plex | sites, characteristics, work_centres, equipment, items | 500-2,000 | standard |
| 61 | spc_samples | Subgroups with readings, mean, range, rule violations and reaction | Proficy, CM, Plex, Infor | sites, spc_charts, characteristics, inspection_results, work_centres, users, nonconformances | ~900,000 | standard |
| 62 | defect_codes | Defect / NC code catalogue with group, default disposition routing and severity | SAP DM, Plex, Proficy | sites, operations, routings | 100-400 | standard |
| 63 | nonconformances | Nonconformance reports: what, where, quantity, containment, disposition (use-as-is, rework, scrap, return) | Opcenter, SAP DM, CM, Aegis, Infor | sites, defect_codes, wip_units, lots, items, operations, work_centres, users, suppliers, quality_holds, rework_orders, scrap_records, capas, inspection_results | ~9,000 | standard |
| 64 | rework_orders | Rework instruction and execution on the rework routing with re-inspection result | SAP DM, Eyelit, CM | sites, nonconformances, wip_units, lots, routings, operations, users, work_centres | ~5,000 | standard |
| 65 | scrap_records | Scrap declaration with quantity, weight, cost, defect code and operation of origin | Proficy, CM, Plex | sites, nonconformances, defect_codes, wip_units, lots, items, operations, work_centres, users | ~15,000 | standard |
| 66 | quality_holds | Hold / quarantine on units, lots, containers or locations with reason and release decision | Opcenter, CM, Plex, Eyelit | sites, lots, wip_units, containers, storage_locations, nonconformances, users | ~2,000 | standard |
| 67 | deviation_permits | Temporary deviations / concessions approved by the customer with quantity or date limit | Opcenter, Plex | sites, items, characteristics, customers, users, nonconformances, engineering_changes | ~100 | standard |
| 68 | capas | Corrective and preventive actions in 8D structure (D1-D8) with team, root cause, actions, verification | CM, Plex, Aegis, Infor, Eyelit | sites, nonconformances, customer_complaints, audits, users, pfmeas, control_plans, documents | ~300 | standard |
| 69 | pfmeas | Process FMEA per item / process: failure modes, effects, causes, S-O-D, action priority | Plex | sites, items, operations, characteristics, users, control_plans | 100-500 | standard |
| 70 | ppap_submissions | PPAP package: level, 18 elements with status, PSW, customer decision | Plex | sites, items, customers, control_plans, pfmeas, msa_studies, documents, users, engineering_changes | ~100 | standard |
| 71 | gauges | Gauges and measuring instruments: type, range, resolution, calibration interval and due date, status | CM, Plex, NoMuda | sites, storage_locations, work_centres, suppliers, users | 500-3,000 | standard |
| 72 | gauge_calibrations | Calibration events: as-found / as-left readings, standard used, result, certificate | CM, Plex | sites, gauges, users, suppliers, documents | ~3,000 | standard |
| 73 | msa_studies | Measurement system analysis: gauge R&R, bias, linearity, attribute agreement | Plex | sites, gauges, characteristics, users, items | ~200 | standard |
| 74 | audits | Layered process, process (VDA 6.3), product and system audits with findings | Plex | sites, areas, lines, users, customers, capas, check_sheets | ~1,500 | standard |
| 75 | customer_complaints | Customer complaints / line rejections / warranty returns with affected serials and PPM impact | Plex, Aegis | sites, customers, items, serial_numbers, shipments, nonconformances, capas, users | ~80 | standard |

### Domain 7 Equipment and performance

| # | Collection | Purpose | Inspired by | Relationships (references to) | Estimated volume per year | Storage |
|---|---|---|---|---|---|---|
| 76 | reason_codes | Reason tree (up to 4 levels) for downtime, scrap, hold and andon with planned / unplanned category | Proficy, Eyelit | sites | 200-600 | standard |
| 77 | equipment_states | State intervals per equipment: running, idle, setup, down, starved, blocked | Tulip, CM, Proficy | sites, equipment, work_centres, production_orders, shifts | ~3 million | time-series candidate |
| 78 | downtime_events | Classified stops with fault, reason path, action taken, duration, responsible group | Proficy, Eyelit, Infor | sites, equipment, lines, work_centres, reason_codes, shifts, users, production_orders, maintenance_work_orders, alarms | ~120,000 | standard |
| 79 | production_counts | Hourly good / reject / rework counts per work centre against target (hour-by-hour board) | Proficy, Infor, Tulip | sites, work_centres, lines, shifts, production_orders, items | ~250,000 | time-series candidate |
| 80 | oee_records | OEE per equipment / line and shift: availability, performance, quality with the time and count basis | Proficy, Eyelit, Infor | sites, equipment, lines, shifts, items, production_orders | ~110,000 | standard |
| 81 | process_tags | Tag definitions: source address, unit, deadband, limits, equipment | Proficy, CM, Tulip | sites, equipment, iot_devices, units_of_measure | 5,000-20,000 | standard |
| 82 | process_data | Tag values over time (die temperature, furnace zone temperature, spindle load, bath pH, current) | Proficy, CM, Tulip, Infor | sites, process_tags, equipment | ~2 billion raw, down-sampled | time-series (recommended) |
| 83 | alarms | Alarm occurrences with severity, raised / acknowledged / cleared times | Proficy, CM, Infor | sites, equipment, process_tags, users, iot_devices | ~500,000 | standard |
| 84 | torque_results | Tightening results per unit: program, final torque, angle, status, curve reference | NoMuda | sites, wip_units, operation_executions, equipment, tools, recipes, users, iot_devices | ~1.5 million | standard |
| 85 | leak_test_results | Leak test per unit: stage pressures, decay, leak rate, limits, verdict, retest counter | NoMuda, CM | sites, wip_units, operation_executions, equipment, recipes, users, iot_devices | ~760,000 | standard |

### Domain 8 Maintenance and tooling

| # | Collection | Purpose | Inspired by | Relationships (references to) | Estimated volume per year | Storage |
|---|---|---|---|---|---|---|
| 86 | maintenance_plans | Preventive / condition-based plans per equipment or tool with tasks, interval and next due | CM, Eyelit, Infor | sites, equipment, tools, spare_parts, skills | 500-2,000 | standard |
| 87 | maintenance_work_orders | Breakdown, preventive and improvement work orders with labour, parts used, root cause | CM, Eyelit, Infor | sites, equipment, tools, maintenance_plans, downtime_events, users, spare_parts, reason_codes | ~8,000 | standard |
| 88 | spare_parts | Maintenance spares with stock, minimum, location, where-used | CM, Infor | sites, suppliers, storage_locations, equipment, units_of_measure | 2,000-8,000 | standard |
| 89 | tools | Dies, fixtures, cutting tools, nutrunner spindles, test seals: life limit, life used, status, location | Eyelit, CM, NoMuda | sites, items, equipment, suppliers, storage_locations | 1,000-5,000 | standard |
| 90 | tool_life_records | Tool mount / dismount / usage / regrind events with shots or cycles consumed | Eyelit, CM | sites, tools, equipment, production_orders, users, maintenance_work_orders | ~60,000 | standard |

### Domain 9 Integration and system

| # | Collection | Purpose | Inspired by | Relationships (references to) | Estimated volume per year | Storage |
|---|---|---|---|---|---|---|
| 91 | erp_messages | Inbound and outbound interface messages (order download, confirmation, goods movement) with payload, status, retries | Infor, SAP DM, CM, NoMuda | sites, integration_connectors, production_orders, goods_receipts, shipments | ~2 million | standard, TTL archive |
| 92 | integration_connectors | Connector definitions to ERP, PLM, OPC UA servers, tool controllers, label printers | Tulip, CM, Aegis | sites | 20-80 | standard |
| 93 | iot_devices | Registry of PLCs, gateways, nutrunner controllers, leak testers, scanners, printers, energy meters | Tulip, CM, Aegis | sites, equipment, work_centres, integration_connectors | 300-1,500 | standard |
| 94 | operator_apps | Composable operator screen definitions (versioned) bound to work centres and operations | Tulip, SAP DM | sites, work_centres, operations, work_instructions, inspection_plans, users | 50-300 | standard |
| 95 | event_logs | Business event stream (order released, unit started, recipe downloaded, hold placed) | CM, Tulip, Proficy | sites, users, iot_devices | ~30 million | standard, TTL or time-series candidate |
| 96 | audit_trails | Field-level change history of master and quality data (who, when, old, new, reason) | Tulip, CM, Infor, Opcenter | sites, users, electronic_signatures | ~3 million | standard, immutable |
| 97 | electronic_signatures | Signature records for approvals and releases with meaning and signed-content hash | Tulip, CM, Aegis, Infor | sites, users, roles | ~200,000 | standard, immutable |
| 98 | notifications | Alerts and escalations sent to users / groups with delivery and acknowledgement status | CM, Infor, Proficy, Opcenter | sites, users, roles, andon_events, alarms, nonconformances | ~400,000 | standard, TTL |
| 99 | documents | Controlled documents and attachments metadata (drawings, certificates, photos, reports); file in object store | CM, Plex, Aegis, Infor | sites, users, items | ~150,000 | standard |
| 100 | number_ranges | Counters and format masks for serials, lots, orders, labels, NCRs | SAP DM, Plex | sites, items | 30-100 | standard |
| 101 | system_configurations | Site and module settings (OEE basis, SPC rules, retention, label printer mapping) | Tulip, CM, Proficy | sites | 100-500 | standard |

### Domain 10 Energy, safety and andon

| # | Collection | Purpose | Inspired by | Relationships (references to) | Estimated volume per year | Storage |
|---|---|---|---|---|---|---|
| 102 | energy_readings | Interval energy, compressed air and gas consumption per meter and equipment | Infor | sites, iot_devices, equipment, lines, shifts, units_of_measure | ~3.5 million | time-series (recommended) |
| 103 | andon_events | Help calls from stations (quality, material, maintenance, safety) with response and escalation times | NoMuda, Tulip, Proficy | sites, work_centres, lines, users, reason_codes, downtime_events, shifts | ~40,000 | standard |
| 104 | safety_incidents | Near misses, unsafe conditions, first-aid and lost-time incidents with investigation and actions | CM, Infor | sites, areas, work_centres, users, equipment, capas | ~400 | standard |

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
