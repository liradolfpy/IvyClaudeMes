## u_mes_trac_asBuiltRecord - As-Built Records (Reports)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_trac_asBuiltRecord.json | _id: mes_trac_asBuiltRecordStable | rel: CL20261018-23:51 | samples: 20 | columns: 32 | total width: 5560px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | wipUnitName | WIP Unit | String | 20 | 160px | left |
| 3 | serialNumberName | Serial Number | String | 13 | 140px | left |
| 4 | itemName | Item | String | 49 | 300px | left |
| 5 | itemRevision | Item Revision | String | 1 | 140px | left |
| 6 | productVariantName | Product Variant | String | 44 | 300px | left |
| 7 | productionOrderName | Production Order | String | 10 | 160px | left |
| 8 | customerName | Customer | String | 42 | 300px | left |
| 9 | builtAt | Built At | Date/Datetime | 19 | 160px | center |
| 10 | torqueTorqueResultName | Torque Torque Result | String | 15 | 180px | left |
| 11 | torqueFinalTorqueNm | Torque Final Torque Nm | Decimal128 | 4 | 200px | right |
| 12 | torqueFinalAngleDeg | Torque Final Angle Deg | Decimal128 | 5 | 200px | right |
| 13 | leakTestLeakTestResultName | Leak Test Leak Test Result | String | 15 | 230px | left |
| 14 | leakTestVerdict | Leak Test Verdict | String | 4 | 160px | left |
| 15 | leakTestLeakRate | Leak Test Leak Rate | Decimal128 | 5 | 180px | right |
| 16 | bodyLotName | Body Lot | String | 15 | 130px | left |
| 17 | castingLotName | Casting Lot | String | 15 | 130px | left |
| 18 | heatTreatmentLotName | Heat Treatment Lot | String | 14 | 170px | left |
| 19 | reworkCount | Rework Count | Int32 | 1 | 130px | right |
| 20 | deviationPermitName | Deviation Permit | String | 0 | 160px | left |
| 21 | containerName | Container | String | 10 | 110px | left |
| 22 | shipmentName | Shipment | String | 15 | 130px | left |
| 23 | finalReleaseBy | Final Release By | String | 0 | 160px | left |
| 24 | finalReleaseAt | Final Release At | Date/Datetime | 0 | 160px | center |
| 25 | recordHash | Record Hash | String | 64 | 300px | left |
| 26 | genealogyComplete | Genealogy Complete | Boolean | 3 | 170px | center |
| 27 | missingComponentCount | Missing Component Count | Int32 | 1 | 210px | right |
| 28 | status | Status | String | 9 | 90px | left |
| 29 | createdBy | Created By | String | 14 | 120px | left |
| 30 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 31 | updatedBy | Updated By | String | 14 | 120px | left |
| 32 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); wipUnitId (reference key, shown through wipUnitName); serialNumberId (reference key, shown through serialNumberName); itemId (reference key, shown through itemName); productVariantId (reference key, shown through productVariantName); productionOrderId (reference key, shown through productionOrderName); customerId (reference key, shown through customerName); torqueTorqueResultId (reference key, shown through torqueTorqueResultName); leakTestLeakTestResultId (reference key, shown through leakTestLeakTestResultName); bodyLotId (reference key, shown through bodyLotName); castingLotId (reference key, shown through castingLotName); heatTreatmentLotId (reference key, shown through heatTreatmentLotName); deviationPermitId (reference key, shown through deviationPermitName); containerId (reference key, shown through containerName); shipmentId (reference key, shown through shipmentName); finalReleaseById (reference key, shown through finalReleaseBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): deviationPermitName, finalReleaseBy, finalReleaseAt

## u_mes_trac_asBuiltRecordComponent - As-Built Record Components (Reports)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_trac_asBuiltRecordComponent.json | _id: mes_trac_asBuiltRecordComponentStable | rel: CL20261018-23:51 | samples: 20 | columns: 12 | total width: 1790px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 21 | 170px | left |
| 2 | asBuiltRecordName | As Built Record | String | 17 | 150px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | itemName | Item | String | 46 | 300px | left |
| 5 | lotName | Lot | String | 15 | 130px | left |
| 6 | serialNo | Serial No | String | 14 | 120px | left |
| 7 | quantity | Quantity | Int32 | 1 | 100px | right |
| 8 | genealogyLinkName | Genealogy Link | String | 15 | 140px | left |
| 9 | createdBy | Created By | String | 14 | 120px | left |
| 10 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 11 | updatedBy | Updated By | String | 14 | 120px | left |
| 12 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); asBuiltRecordId (reference key, shown through asBuiltRecordName); itemId (reference key, shown through itemName); lotId (reference key, shown through lotName); genealogyLinkId (reference key, shown through genealogyLinkName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_trac_asBuiltRecordInspectionResult - As-Built Record Inspection Results (Reports)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_trac_asBuiltRecordInspectionResult.json | _id: mes_trac_asBuiltRecordInspectionResultStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1170px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | asBuiltRecordName | As Built Record | String | 17 | 150px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | inspectionResultName | Inspection Result | String | 14 | 160px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); asBuiltRecordId (reference key, shown through asBuiltRecordName); inspectionResultId (reference key, shown through inspectionResultName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_trac_asBuiltRecordOperation - As-Built Record Operations (Reports)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_trac_asBuiltRecordOperation.json | _id: mes_trac_asBuiltRecordOperationStable | rel: CL20261018-23:51 | samples: 20 | columns: 16 | total width: 2770px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 21 | 170px | left |
| 2 | asBuiltRecordName | As Built Record | String | 17 | 150px | left |
| 3 | stepNo | Step No | Int32 | 3 | 90px | right |
| 4 | operationName | Operation | String | 31 | 240px | left |
| 5 | workCenterName | Work Center | String | 37 | 280px | left |
| 6 | equipmentName | Equipment | String | 54 | 300px | left |
| 7 | operatorUserName | Operator User | String | 14 | 140px | left |
| 8 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 9 | result | Result | String | 2 | 90px | left |
| 10 | recipeName | Recipe | String | 56 | 300px | left |
| 11 | recipeVersion | Recipe Version | String | 1 | 140px | left |
| 12 | recipeChecksum | Recipe Checksum | String | 16 | 150px | left |
| 13 | createdBy | Created By | String | 14 | 120px | left |
| 14 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 15 | updatedBy | Updated By | String | 14 | 120px | left |
| 16 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); asBuiltRecordId (reference key, shown through asBuiltRecordName); operationId (reference key, shown through operationName); workCenterId (reference key, shown through workCenterName); equipmentId (reference key, shown through equipmentName); operatorUserId (reference key, shown through operatorUserName); recipeId (reference key, shown through recipeName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_trac_componentLotLink - Component Lot Links (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_trac_componentLotLink.json | _id: mes_trac_componentLotLinkStable | rel: CL20261018-23:51 | samples: 20 | columns: 18 | total width: 2810px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | parentLotName | Parent Lot | String | 15 | 130px | left |
| 3 | childLotName | Child Lot | String | 15 | 130px | left |
| 4 | parentItemName | Parent Item | String | 61 | 300px | left |
| 5 | childItemName | Child Item | String | 61 | 300px | left |
| 6 | linkType | Link Type | String | 9 | 110px | left |
| 7 | quantity | Quantity | Decimal128 | 1 | 100px | right |
| 8 | unitOfMeasureName | Unit of Measure | String | 4 | 150px | left |
| 9 | operationName | Operation | String | 31 | 240px | left |
| 10 | operationExecutionName | Operation Execution | String | 15 | 180px | left |
| 11 | linkedAt | Linked At | Date/Datetime | 19 | 160px | center |
| 12 | linkedBy | Linked By | String | 14 | 120px | left |
| 13 | yieldPct | Yield (%) | Decimal128 | 5 | 110px | right |
| 14 | status | Status | String | 6 | 90px | left |
| 15 | createdBy | Created By | String | 14 | 120px | left |
| 16 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 17 | updatedBy | Updated By | String | 14 | 120px | left |
| 18 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); parentLotId (reference key, shown through parentLotName); childLotId (reference key, shown through childLotName); parentItemId (reference key, shown through parentItemName); childItemId (reference key, shown through childItemName); unitOfMeasureId (reference key, shown through unitOfMeasureName); operationId (reference key, shown through operationName); operationExecutionId (reference key, shown through operationExecutionName); linkedById (reference key, shown through linkedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_trac_genealogyLink - Genealogy Links (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_trac_genealogyLink.json | _id: mes_trac_genealogyLinkStable | rel: CL20261018-23:51 | samples: 20 | columns: 25 | total width: 3940px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | parentWipUnitName | Parent WIP Unit | String | 20 | 160px | left |
| 3 | parentSerialNumberName | Parent Serial Number | String | 0 | 180px | left |
| 4 | parentItemName | Parent Item | String | 61 | 300px | left |
| 5 | childType | Child Type | String | 3 | 110px | left |
| 6 | childItemName | Child Item | String | 48 | 300px | left |
| 7 | childLotName | Child Lot | String | 15 | 130px | left |
| 8 | childSerialNo | Child Serial No | String | 0 | 150px | left |
| 9 | quantity | Quantity | Decimal128 | 1 | 100px | right |
| 10 | unitOfMeasureName | Unit of Measure | String | 4 | 150px | left |
| 11 | operationName | Operation | String | 26 | 210px | left |
| 12 | operationExecutionName | Operation Execution | String | 15 | 180px | left |
| 13 | materialConsumptionName | Material Consumption | String | 15 | 180px | left |
| 14 | linkedAt | Linked At | Date/Datetime | 19 | 160px | center |
| 15 | linkedBy | Linked By | String | 14 | 120px | left |
| 16 | linkType | Link Type | String | 9 | 110px | left |
| 17 | removedAt | Removed At | Date/Datetime | 19 | 160px | center |
| 18 | removedReason | Removed Reason | String | 0 | 140px | left |
| 19 | childSerialNumberName | Child Serial Number | String | 0 | 180px | left |
| 20 | childWipUnitName | Child WIP Unit | String | 0 | 140px | left |
| 21 | status | Status | String | 7 | 90px | left |
| 22 | createdBy | Created By | String | 14 | 120px | left |
| 23 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 24 | updatedBy | Updated By | String | 14 | 120px | left |
| 25 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); parentWipUnitId (reference key, shown through parentWipUnitName); parentSerialNumberId (reference key, shown through parentSerialNumberName); parentItemId (reference key, shown through parentItemName); childItemId (reference key, shown through childItemName); childLotId (reference key, shown through childLotName); unitOfMeasureId (reference key, shown through unitOfMeasureName); operationId (reference key, shown through operationName); operationExecutionId (reference key, shown through operationExecutionName); materialConsumptionId (reference key, shown through materialConsumptionName); linkedById (reference key, shown through linkedBy); childSerialNumberId (reference key, shown through childSerialNumberName); childWipUnitId (reference key, shown through childWipUnitName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): parentSerialNumberName, childSerialNo, removedReason, childSerialNumberName, childWipUnitName

## u_mes_trac_serialNumber - Serial Numbers (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_trac_serialNumber.json | _id: mes_trac_serialNumberStable | rel: CL20261018-23:51 | samples: 20 | columns: 26 | total width: 4710px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | itemName | Item | String | 49 | 300px | left |
| 3 | itemRevision | Item Revision | String | 1 | 140px | left |
| 4 | productVariantName | Product Variant | String | 44 | 300px | left |
| 5 | wipUnitName | WIP Unit | String | 20 | 160px | left |
| 6 | productionOrderName | Production Order | String | 10 | 160px | left |
| 7 | numberRangeName | Number Range | String | 33 | 260px | left |
| 8 | dataMatrixPayload | Data Matrix Payload | String | 59 | 300px | left |
| 9 | issuedAt | Issued At | Date/Datetime | 19 | 160px | center |
| 10 | markedAt | Marked At | Date/Datetime | 19 | 160px | center |
| 11 | markedAtEquipmentName | Marked At Equipment | String | 36 | 280px | left |
| 12 | markGrade | Mark Grade | String | 1 | 110px | left |
| 13 | markVerifiedAt | Mark Verified At | Date/Datetime | 19 | 160px | center |
| 14 | labelName | Label | String | 15 | 130px | left |
| 15 | containerName | Container | String | 10 | 110px | left |
| 16 | shipmentName | Shipment | String | 15 | 130px | left |
| 17 | shippedAt | Shipped At | Date/Datetime | 19 | 160px | center |
| 18 | customerName | Customer | String | 42 | 300px | left |
| 19 | voidReason | Void Reason | String | 0 | 120px | left |
| 20 | markingRecipeName | Marking Recipe | String | 42 | 300px | left |
| 21 | markingRecipeVersion | Marking Recipe Version | String | 1 | 200px | left |
| 22 | status | Status | String | 8 | 90px | left |
| 23 | createdBy | Created By | String | 14 | 120px | left |
| 24 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 25 | updatedBy | Updated By | String | 14 | 120px | left |
| 26 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); productVariantId (reference key, shown through productVariantName); wipUnitId (reference key, shown through wipUnitName); productionOrderId (reference key, shown through productionOrderName); numberRangeId (reference key, shown through numberRangeName); markedAtEquipmentId (reference key, shown through markedAtEquipmentName); labelId (reference key, shown through labelName); containerId (reference key, shown through containerName); shipmentId (reference key, shown through shipmentName); customerId (reference key, shown through customerName); markingRecipeId (reference key, shown through markingRecipeName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): voidReason

## u_mes_trac_traceInvestigation - Trace Investigations (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_trac_traceInvestigation.json | _id: mes_trac_traceInvestigationStable | rel: CL20261018-23:51 | samples: 20 | columns: 20 | total width: 3370px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | title | Title | String | 73 | 300px | left |
| 3 | direction | Direction | String | 7 | 110px | left |
| 4 | relatedCollectionName | Related Collection Name | String | 23 | 210px | left |
| 5 | relatedEntityName | Related Entity | String | 20 | 160px | left |
| 6 | depthLimit | Depth Limit | Int32 | 1 | 120px | right |
| 7 | resultCount | Result Count | Int32 | 1 | 130px | right |
| 8 | shippedCount | Shipped Count | Int32 | 1 | 140px | right |
| 9 | qualityHoldName | Quality Hold | String | 15 | 130px | left |
| 10 | nonconformanceName | Nonconformance | String | 56 | 300px | left |
| 11 | customerComplaintName | Customer Complaint | String | 58 | 300px | left |
| 12 | requestedBy | Requested By | String | 15 | 130px | left |
| 13 | requestedAt | Requested At | Date/Datetime | 19 | 160px | center |
| 14 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 15 | exportControlledDocumentName | Export Controlled Document | String | 0 | 230px | left |
| 16 | status | Status | String | 9 | 90px | left |
| 17 | createdBy | Created By | String | 14 | 120px | left |
| 18 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 19 | updatedBy | Updated By | String | 14 | 120px | left |
| 20 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); relatedEntityId (reference key, shown through relatedEntityName); qualityHoldId (reference key, shown through qualityHoldName); nonconformanceId (reference key, shown through nonconformanceName); customerComplaintId (reference key, shown through customerComplaintName); requestedById (reference key, shown through requestedBy); exportControlledDocumentId (reference key, shown through exportControlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): exportControlledDocumentName

## u_mes_trac_traceInvestigationResult - Trace Investigation Results (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_trac_traceInvestigationResult.json | _id: mes_trac_traceInvestigationResultStable | rel: CL20261018-23:51 | samples: 10 | columns: 16 | total width: 2730px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | traceInvestigationName | Trace Investigation | String | 73 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | relatedCollectionName | Related Collection Name | String | 18 | 210px | left |
| 5 | relatedEntityName | Related Entity | String | 15 | 140px | left |
| 6 | genealogyDepth | Genealogy Depth | Int32 | 1 | 150px | right |
| 7 | itemName | Item | String | 39 | 300px | left |
| 8 | statusAtRun | Status At Run | String | 10 | 140px | left |
| 9 | storageLocationName | Storage Location | String | 33 | 260px | left |
| 10 | shipmentName | Shipment | String | 15 | 130px | left |
| 11 | customerName | Customer | String | 20 | 160px | left |
| 12 | quantity | Quantity | Decimal128 | 4 | 100px | right |
| 13 | createdBy | Created By | String | 14 | 120px | left |
| 14 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 15 | updatedBy | Updated By | String | 14 | 120px | left |
| 16 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); traceInvestigationId (reference key, shown through traceInvestigationName); relatedEntityId (reference key, shown through relatedEntityName); itemId (reference key, shown through itemName); storageLocationId (reference key, shown through storageLocationName); shipmentId (reference key, shown through shipmentName); customerId (reference key, shown through customerName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))
