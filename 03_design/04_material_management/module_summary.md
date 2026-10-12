# Material Management (matl) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_matl_storageLocation | Entity | master | 24 | 16 | 2 | 5 |
| 2 | u_mes_matl_inventoryBalance | Entity | transaction | 33 | 24 | 1 | 9 |
| 3 | u_mes_matl_materialMovement | Entity | transaction | 48 | 23 | 2 | 8 |
| 4 | u_mes_matl_goodsReceipt | Entity | transaction | 25 | 20 | 1 | 4 |
| 5 | u_mes_matl_goodsReceiptLine | Child | transaction | 29 | 24 | 1 | 4 |
| 6 | u_mes_matl_goodsReceiptLineInspectionResult | Relationship | transaction | 16 | 16 | 0 | 2 |
| 7 | u_mes_matl_kit | Entity | transaction | 28 | 23 | 2 | 6 |
| 8 | u_mes_matl_kitLine | Child | transaction | 29 | 20 | 1 | 4 |
| 9 | u_mes_matl_materialRequest | Entity | transaction | 41 | 29 | 4 | 8 |
| 10 | u_mes_matl_materialConsumption | Entity | transaction | 43 | 30 | 2 | 8 |
| 11 | u_mes_matl_packagingSpecification | Entity | master | 28 | 23 | 1 | 7 |
| 12 | u_mes_matl_packagingSpecificationLevel | Child | master | 14 | 14 | 0 | 2 |
| 13 | u_mes_matl_labelTemplate | Entity | master | 19 | 17 | 4 | 3 |
| 14 | u_mes_matl_labelTemplateField | Child | master | 14 | 13 | 1 | 1 |
| 15 | u_mes_matl_label | Entity | transaction | 41 | 26 | 3 | 9 |
| 16 | u_mes_matl_shipment | Entity | transaction | 39 | 30 | 1 | 7 |
| 17 | u_mes_matl_shipmentLine | Child | transaction | 18 | 18 | 0 | 2 |
| 18 | u_mes_matl_shipmentLineContainer | Relationship | transaction | 16 | 16 | 0 | 2 |
| 19 | u_mes_matl_shipmentLineLot | Relationship | transaction | 16 | 16 | 0 | 2 |
| 20 | u_mes_matl_movementType | Entity | master | 12 | 11 | 2 | 2 |
| 21 | u_mes_matl_stockStatus | Entity | master | 11 | 10 | 1 | 2 |
| 22 | u_mes_matl_packType | Entity | master | 9 | 9 | 1 | 2 |
| 23 | u_mes_matl_exposureTimer | Entity | transaction | 31 | 21 | 2 | 8 |
| 24 | u_mes_matl_replenishmentRule | Entity | master | 27 | 20 | 2 | 7 |
| 25 | u_mes_matl_materialDemandForecast | Entity | transaction | 30 | 27 | 2 | 7 |
| 26 | u_mes_matl_storageLocationAllowedItem | Relationship | master | 12 | 8 | 0 | 2 |
