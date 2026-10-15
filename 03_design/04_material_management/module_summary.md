# MaterialManagement (matl) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_matl_storageLocation | Entity | master | 25 | 17 | 3 | 5 |
| 2 | u_mes_matl_inventoryBalance | Entity | transaction | 34 | 25 | 2 | 9 |
| 3 | u_mes_matl_materialMovement | Entity | transaction | 49 | 24 | 3 | 8 |
| 4 | u_mes_matl_goodsReceipt | Entity | transaction | 26 | 21 | 2 | 4 |
| 5 | u_mes_matl_goodsReceiptLine | Child | transaction | 30 | 25 | 2 | 4 |
| 6 | u_mes_matl_goodsReceiptLineInspectionResult | Relationship | transaction | 17 | 17 | 1 | 2 |
| 7 | u_mes_matl_kit | Entity | transaction | 29 | 24 | 3 | 6 |
| 8 | u_mes_matl_kitLine | Child | transaction | 30 | 21 | 2 | 4 |
| 9 | u_mes_matl_materialRequest | Entity | transaction | 42 | 30 | 5 | 8 |
| 10 | u_mes_matl_materialConsumption | Entity | transaction | 44 | 31 | 3 | 8 |
| 11 | u_mes_matl_packagingSpecification | Entity | master | 29 | 24 | 2 | 7 |
| 12 | u_mes_matl_packagingSpecificationLevel | Child | master | 15 | 15 | 1 | 2 |
| 13 | u_mes_matl_labelTemplate | Entity | master | 20 | 18 | 5 | 3 |
| 14 | u_mes_matl_labelTemplateField | Child | master | 15 | 14 | 2 | 1 |
| 15 | u_mes_matl_label | Entity | transaction | 42 | 27 | 4 | 9 |
| 16 | u_mes_matl_shipment | Entity | transaction | 40 | 31 | 2 | 7 |
| 17 | u_mes_matl_shipmentLine | Child | transaction | 19 | 19 | 1 | 2 |
| 18 | u_mes_matl_shipmentLineContainer | Relationship | transaction | 17 | 17 | 1 | 2 |
| 19 | u_mes_matl_shipmentLineLot | Relationship | transaction | 17 | 17 | 1 | 2 |
| 20 | u_mes_matl_movementType | Entity | master | 13 | 12 | 3 | 2 |
| 21 | u_mes_matl_stockStatus | Entity | master | 12 | 11 | 2 | 2 |
| 22 | u_mes_matl_packType | Entity | master | 10 | 10 | 2 | 2 |
| 23 | u_mes_matl_exposureTimer | Entity | transaction | 32 | 22 | 3 | 8 |
| 24 | u_mes_matl_replenishmentRule | Entity | master | 28 | 21 | 3 | 7 |
| 25 | u_mes_matl_materialDemandForecast | Entity | transaction | 31 | 28 | 3 | 7 |
| 26 | u_mes_matl_storageLocationAllowedItem | Relationship | master | 13 | 9 | 1 | 2 |
| 27 | u_mes_matl_dispenseRecord | Entity | transaction | 42 | 34 | 4 | 8 |
