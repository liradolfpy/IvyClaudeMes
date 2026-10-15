# Module comparison matrix - ten MES products against the ClaudeMES modules

Prepared: 11 October 2026 | Module codes and names as set by the owner (decision D026)

## 1. Basis

- Products compared: the ten products of the Phase 1 research. The request said "the below softwares" but no list came with it, so this list is an assumption.
- Vendor names are written exactly as they appear on the vendor page read for this comparison (section 4). A name is used only if it was seen on a page that was opened; nothing is filled in from memory.
- "-" means no named module for that area was found on the pages read. It does not mean the product lacks the function.
- A vendor module can appear in more than one row when it spans several of our modules.
- Our modules are the ten module codes of `02_architecture/collection_inventory.md`.

## 2. Matrix

| ClaudeMES module | Siemens Opcenter | Rockwell Plex | GE Vernova Proficy Plant Applications | Tulip | Critical Manufacturing MES | Aegis FactoryLogix | Eyelit | Infor MES | SAP Digital Manufacturing | NoMuda VisualFactory |
|---|---|---|---|---|---|---|---|---|---|---|
| mast - MasterDataManagement | - | Human Capital Management | - | Scalability And Governance | Operator Training And Certification (Labor Management); Equipment Tracking (Resource Tracking) | - | Labor Management | Labor | Resource orchestration bundle | Operator Training Software |
| prod - ProductDefinition | Opcenter Execution (BOP and eProcedure shown in the product diagram) | - | Production Management; Batch Analysis | Apps; App Editor | Bill-of-Materials (BOM); Work Instructions / SOPs; Recipe Management; NPI | Digital Manufacturing Engineering | Process Definition | Links to Documents | Production process designer; Execution bundle | Digital Work Instructions; Digital Guidance |
| plan - PlanningAndExecution (includes andon) | Opcenter Execution; Opcenter APS | Production Management; Production Finite Scheduling | Production Management (with the Order Management app) | Apps; Composable App Suites | Batch, Lot And Unit Tracking; Routing and Dispatching; Order Management; Advanced Planning And Scheduling; Task Management | Manufacturing Process Execution; Planning And Scheduling | Manufacturing Execution System; Advanced Planning and Scheduling; Live Execution Against Your Production Schedule; Real-Time Paperless Production Visibility; Labor Management | Scheduling; Job Tracking; Production Counting; Labor | Execution bundle; Production Operator Dashboard; Order Report; SFC Report | Manufacturing Execution System (MES); Work Order Processing; Production And Operations Management |
| matl - MaterialManagement | Opcenter Intra Plant Logistics | Inventory Management | - | - | Materials Management (Material Logistics); Consumables Management; Label And Document Printing | Lean Materials Management | Inventory and Materials Management | Inventory Management; Label Printing; Warehouse - Logistics | Resource orchestration bundle | - |
| trac - Traceability | Opcenter Execution | Inventory Management | Production Management (with the Genealogy app) | - | Traceability And Genealogy | Traceability And Compliance | Inventory and Materials Management; Quality and Compliance Management | Traceability - Consumption; Build Traceability | SFC Report | Traceability and Compliance |
| qual - QualityManagement | Opcenter Quality (shown as Opcenter X Quality on the product page) | Plex QMS (Core QMS, Advanced QMS, Supplier QMS, Total QMS); Closed-Loop Quality Management | Quality Management | GxP Capabilities | Statistical Process Control (SPC); Corrective And Preventive Action (CAPA) / Exception Management; Non-Conformance Reporting And Dispositions; Sampling Based Inspection / AQL; Calibration; Data Collection And Acquisition | Quality Management | Quality and Compliance Management | Quality; SPC; Concerns and CAPA; Customer Complaints; Supplier Complaints | Execution bundle; Manage Data Collections | Quality Management System |
| perf - PerformanceManagement (includes energy) | Opcenter Intelligence | Plex Production Monitoring (OEE Optimization) | Efficiency Management | Analytics; Factory Playback | Equipment Tracking (Resource Tracking); Alarm Management; Dashboards; Reporting and Analytics | Manufacturing Intelligence | Asset Performance Management; Manufacturing KPIs and Performance Analytics | Downtime; OEE; Waste; Process Monitoring; Energy Management | Insights bundle | Shop Floor Productivity; Visual Control Systems |
| maint - ToolingAndMaintenance | - | - | - | - | Maintenance Management; Tooling Management | - | Asset Performance Management | Asset Register; Maintenance; Repairs; Tool Management | Resource orchestration bundle | Total Productive Maintenance |
| syst - SystemAndIntegration | - | Unified Edge to Cloud; Plex MES A&O | - | Connectors And Integrations; Automations; Edge Devices; Agents; Common Data Model | Equipment Integration (Connect IoT); Factory Automation; Enterprise Integration (ERP, PLM); Document Management; Electronic Signatures | Connectivity And IIoT | Agent EyeQ | - | Production process designer; Manufacturing Data Objects | Smart Manufacturing |
| ehs - EnvironmentHealthAndSafety | - | - | - | - | - | - | - | - | - | - |

## 3. Vendor modules with no counterpart in ClaudeMES

| Product | Vendor module | What it covers |
|---|---|---|
| Siemens Opcenter | Opcenter Research, Development And Laboratory | Formulated product development |
| Siemens Opcenter | Opcenter X Intosite | Cloud digital twin with 3D visualisation |
| Critical Manufacturing MES | Costing | Material, labour and resource cost absorption |
| Critical Manufacturing MES | Experiment Management | Designed experiments with enforced variations |
| Critical Manufacturing MES | Factory Digital Twin (fabLIVE); Augmented Reality | 3D plant view; AR overlay of MES data |
| Critical Manufacturing MES | Operational Data Store And Data Warehouse | Pre-aggregated analysis cubes |
| Aegis FactoryLogix | Maintenance, Repair And Overhaul | Repair and refurbishment of returned product (not equipment maintenance) |
| Aegis FactoryLogix | Simulation And Digital Twins | Simulation, delivered with Simio |
| Eyelit | Sales, Inventory and Operations Planning | Planning across sales, inventory and production |
| Tulip | Computer Vision | Camera-based detection |
| Rockwell Plex | Human Capital Management | Only its user and skill part is covered here; payroll and HR are not |

## 4. What this shows

- Nine of our ten modules have a named counterpart in at least one product. EnvironmentHealthAndSafety has none: no page read names a safety module. Energy (now in Performance Management) is named only by Infor MES, and no page read names an andon module.
- Maintenance and tooling is named by five products (Critical Manufacturing, Eyelit, Infor, SAP, NoMuda). Siemens, Plex, Proficy, Tulip and FactoryLogix did not name one on the pages read.
- Vendors do not split traceability and quality the way we do. Eyelit and FactoryLogix combine traceability with compliance; Plex puts genealogy under Inventory Management; Proficy puts it under Production Management.
- Costing and advanced planning (S&OP) are outside our scope. If either is wanted, it is a new module rather than an extension of an existing one.

## 5. Limits

- Siemens: the product page lists products, not the modules inside Opcenter Execution. BOP and eProcedure are labels from a fact-sheet diagram.
- Rockwell Plex: Asset Performance Management and Supply Chain Planning were not on any page read, so they are not in the matrix.
- Infor MES: the detailed names (Scheduling, Job Tracking, OEE and so on) come from a third-party listing; Infor's own documentation page read here names only six areas: Production, Inventory, Quality, Material handling, Maintenance, Energy. Infor's product page did not load.
- SAP: the SAP Help portal blocked reading, so app names are limited to those on SAP's product page, an SAP Learning lesson and an SAP Community post.
- NoMuda: the names are the solution and use-case menu items of the website, which is how NoMuda presents VisualFactory; they are not licensed modules.
- GE Vernova: the Smart Factory product page did not load; names come from the Plant Applications documentation and brochure.

## 6. Sources

- Siemens Opcenter products: https://www.siemens.com/en-us/products/opcenter/
- Siemens naming: https://teeptrak.com/en/siemens-mes-software-name-explained/
- Opcenter Execution fact sheet: https://www.plm.automation.siemens.com/media/global/en/Siemens-SW-Siemens-Opcenter-Execution-Medical-Device-and-Diagnostics-FS-45024-C13_tcm27-61667.pdf
- Plex products: https://plex.rockwellautomation.com/en-us/products.html
- Plex MES: https://plex.rockwellautomation.com/en-us/products/manufacturing-execution-system.html
- Plex Production Monitoring: https://plex.rockwellautomation.com/en-us/products/production-monitoring.html
- Proficy Plant Applications modules: https://www.gevernova.com/software/documentation/proficy-plant-applications/legacy/PAMasterHelp/Proficy_Modules.htm
- Proficy Plant Applications brochure: https://gevernova.com/software/sites/default/files/2024-10/proficy-plant-applications-from-ge-digital_0.pdf
- Tulip platform: https://tulip.co/platform/
- Critical Manufacturing modules: https://criticalmanufacturing.com/en/critical-manufacturing-mes/complete-modular-solution
- Aegis FactoryLogix: https://info.aiscorp.com/factorylogix-capterra-mes
- Eyelit MES: https://eyelit.com/manufacturing-execution-system/
- Infor MES overview: https://docs.infor.com/mes/2026.10/en-us/mesuaal/mesovg/egi1655887690346.html
- Infor MES listing: https://softwareconnect.com/products/infor-mes-software
- SAP Digital Manufacturing: https://www.sap.com/products/scm/digital-manufacturing.html
- SAP Learning, manufacturing data: https://learning.sap.com/courses/enabling-data-integrations-within-sap-digital-manufacturing-for-insights/utilizing-manufacturing-data-within-sap-digital-manufacturing
- SAP Learning, production orders: https://learning.sap.com/learning-journeys/executing-processes-for-discrete-industries-in-sap-digital-manufacturing/explaining-the-life-cycle-of-production-orders_cbc18198-d2f0-47ca-8e48-e5d60b20ac61
- SAP Community, data collection: https://blogs.sap.com/t5/product-lifecycle-management-blogs-by-sap/automatic-disposition-to-rework-after-out-of-limit-data-collection-within/ba-p/13574594
- NoMuda: https://nomuda.com/
