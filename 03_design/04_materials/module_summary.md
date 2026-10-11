# Materials (mat) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_mat_storageLocation | Entity | master | 24 | 16 | 2 | 5 |
| 2 | u_mes_mat_inventoryBalance | Entity | transaction | 33 | 24 | 1 | 9 |
| 3 | u_mes_mat_materialMovement | Entity | transaction | 48 | 23 | 2 | 8 |
| 4 | u_mes_mat_goodsReceipt | Entity | transaction | 25 | 20 | 1 | 4 |
| 5 | u_mes_mat_goodsReceiptLine | Child | transaction | 29 | 24 | 1 | 4 |
| 6 | u_mes_mat_goodsReceiptLineInspectionResult | Relationship | transaction | 16 | 16 | 0 | 2 |
| 7 | u_mes_mat_kit | Entity | transaction | 28 | 23 | 2 | 6 |
| 8 | u_mes_mat_kitLine | Child | transaction | 23 | 19 | 0 | 4 |
| 9 | u_mes_mat_materialRequest | Entity | transaction | 39 | 29 | 4 | 8 |
| 10 | u_mes_mat_materialConsumption | Entity | transaction | 43 | 30 | 2 | 8 |
| 11 | u_mes_mat_packagingSpecification | Entity | master | 28 | 23 | 1 | 7 |
| 12 | u_mes_mat_packagingSpecificationLevel | Child | master | 14 | 14 | 0 | 2 |
| 13 | u_mes_mat_labelTemplate | Entity | master | 19 | 17 | 4 | 3 |
| 14 | u_mes_mat_labelTemplateField | Child | master | 14 | 13 | 1 | 1 |
| 15 | u_mes_mat_label | Entity | transaction | 41 | 26 | 3 | 9 |
| 16 | u_mes_mat_shipment | Entity | transaction | 39 | 30 | 1 | 7 |
| 17 | u_mes_mat_shipmentLine | Child | transaction | 18 | 18 | 0 | 2 |
| 18 | u_mes_mat_shipmentLineContainer | Relationship | transaction | 16 | 16 | 0 | 2 |
| 19 | u_mes_mat_shipmentLineLot | Relationship | transaction | 16 | 16 | 0 | 2 |
| 20 | u_mes_mat_movementType | Entity | master | 12 | 11 | 2 | 2 |
| 21 | u_mes_mat_stockStatus | Entity | master | 11 | 10 | 1 | 2 |
| 22 | u_mes_mat_packType | Entity | master | 9 | 9 | 1 | 2 |
