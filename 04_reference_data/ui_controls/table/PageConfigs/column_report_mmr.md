## u_mes_mmr_masterManufacturingRecord - Master Manufacturing Records (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mmr_masterManufacturingRecord.json | _id: mes_mmr_masterManufacturingRecordStable | rel: CL20261018-23:51 | samples: 10 | columns: 31 | total width: 6330px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | title | Title | String | 84 | 300px | left |
| 3 | itemName | Item | String | 61 | 300px | left |
| 4 | itemRevisionName | Item Revision | String | 18 | 150px | left |
| 5 | productVariantName | Product Variant | String | 44 | 300px | left |
| 6 | version | Version | Int32 | 1 | 90px | right |
| 7 | previousMasterManufacturingRecordName | Previous Master Manufacturing Record | String | 84 | 300px | left |
| 8 | billOfMaterialName | Bill of Material | String | 21 | 170px | left |
| 9 | routingName | Routing | String | 51 | 300px | left |
| 10 | billOfProcessName | Bill of Process | String | 22 | 180px | left |
| 11 | controlPlanName | Control Plan | String | 28 | 220px | left |
| 12 | inspectionPlanName | Inspection Plan | String | 53 | 300px | left |
| 13 | packagingSpecificationName | Packaging Specification | String | 25 | 210px | left |
| 14 | labelTemplateName | Label Template | String | 36 | 280px | left |
| 15 | processValidationName | Process Validation | String | 76 | 300px | left |
| 16 | controlledDocumentName | Controlled Document | String | 78 | 300px | left |
| 17 | engineeringChangeName | Engineering Change | String | 57 | 300px | left |
| 18 | changeReasonText | Change Reason Text | String | 81 | 300px | left |
| 19 | standardBatchSize | Standard Batch Size | Int32 | 6 | 180px | right |
| 20 | unitOfMeasureName | Unit of Measure | String | 8 | 150px | left |
| 21 | theoreticalQuantity | Theoretical Quantity | Decimal128 | 6 | 180px | right |
| 22 | lowerLimitPct | Lower Limit (%) | Decimal128 | 4 | 150px | right |
| 23 | upperLimitPct | Upper Limit (%) | Decimal128 | 5 | 150px | right |
| 24 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 25 | effectiveTo | Effective to | Date/Date | 10 | 130px | center |
| 26 | authoredBy | Authored By | String | 11 | 120px | left |
| 27 | reviewedBy | Reviewed By | String | 11 | 120px | left |
| 28 | reviewedAt | Reviewed At | Date/Datetime | 19 | 160px | center |
| 29 | approvedBy | Approved By | String | 12 | 120px | left |
| 30 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 31 | status | Status | String | 14 | 120px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); itemRevisionId (reference key, shown through itemRevisionName); productVariantId (reference key, shown through productVariantName); previousMasterManufacturingRecordId (reference key, shown through previousMasterManufacturingRecordName); billOfMaterialId (reference key, shown through billOfMaterialName); routingId (reference key, shown through routingName); billOfProcessId (reference key, shown through billOfProcessName); controlPlanId (reference key, shown through controlPlanName); inspectionPlanId (reference key, shown through inspectionPlanName); packagingSpecificationId (reference key, shown through packagingSpecificationName); labelTemplateId (reference key, shown through labelTemplateName); processValidationId (reference key, shown through processValidationName); controlledDocumentId (reference key, shown through controlledDocumentName); engineeringChangeId (reference key, shown through engineeringChangeName); unitOfMeasureId (reference key, shown through unitOfMeasureName); authoredById (reference key, shown through authoredBy); reviewedById (reference key, shown through reviewedBy); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_mmr_masterManufacturingRecordRecipe - Master Record Recipes (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_mmr_masterManufacturingRecordRecipe.json | _id: mes_mmr_masterManufacturingRecordRecipeStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 900px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | masterManufacturingRecordName | Master Manufacturing Record | String | 84 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | recipeName | Recipe | String | 56 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); masterManufacturingRecordId (reference key, shown through masterManufacturingRecordName); recipeId (reference key, shown through recipeName); schemaVersion (excluded key (identifier, site, app or schema))
