# Master Data Management (mast) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_mast_enterprise | Entity | master | 27 | 23 | 3 | 5 |
| 2 | u_mes_mast_enterpriseContact | Child | master | 13 | 11 | 1 | 1 |
| 3 | u_mes_mast_site | Entity | master | 31 | 28 | 3 | 7 |
| 4 | u_mes_mast_siteCertificate | Child | master | 13 | 12 | 1 | 1 |
| 5 | u_mes_mast_area | Entity | master | 21 | 15 | 4 | 5 |
| 6 | u_mes_mast_line | Entity | master | 23 | 17 | 3 | 7 |
| 7 | u_mes_mast_lineDefaultShift | Relationship | master | 11 | 11 | 1 | 2 |
| 8 | u_mes_mast_lineIdealRate | Child | master | 13 | 13 | 1 | 2 |
| 9 | u_mes_mast_workCenter | Entity | master | 25 | 19 | 4 | 7 |
| 10 | u_mes_mast_workCenterEquipment | Relationship | master | 11 | 11 | 1 | 2 |
| 11 | u_mes_mast_workCenterOperation | Relationship | master | 11 | 11 | 1 | 2 |
| 12 | u_mes_mast_workCenterRequiresSkill | Relationship | master | 11 | 11 | 1 | 2 |
| 13 | u_mes_mast_equipment | Entity | master | 54 | 39 | 9 | 7 |
| 14 | u_mes_mast_equipmentIotDevice | Relationship | master | 11 | 11 | 1 | 2 |
| 15 | u_mes_mast_shift | Entity | master | 15 | 15 | 2 | 2 |
| 16 | u_mes_mast_shiftBreak | Child | master | 13 | 13 | 1 | 1 |
| 17 | u_mes_mast_shiftWorkingDay | Value list | master | 10 | 10 | 2 | 1 |
| 18 | u_mes_mast_workCalendar | Entity | master | 12 | 11 | 2 | 2 |
| 19 | u_mes_mast_workCalendarLine | Relationship | master | 11 | 11 | 1 | 2 |
| 20 | u_mes_mast_workCalendarShift | Relationship | master | 11 | 11 | 1 | 2 |
| 21 | u_mes_mast_workCalendarWeeklyOffDay | Value list | master | 10 | 10 | 2 | 1 |
| 22 | u_mes_mast_workCalendarException | Child | master | 13 | 13 | 2 | 1 |
| 23 | u_mes_mast_workCalendarExceptionShift | Relationship | master | 11 | 11 | 1 | 2 |
| 24 | u_mes_mast_shiftRoster | Entity | transaction | 26 | 24 | 2 | 6 |
| 25 | u_mes_mast_shiftRosterAssignment | Child | transaction | 27 | 20 | 4 | 4 |
| 26 | u_mes_mast_role | Entity | master | 13 | 12 | 3 | 2 |
| 27 | u_mes_mast_rolePermission | Relationship | master | 11 | 11 | 1 | 2 |
| 28 | u_mes_mast_roleSignatureMeaning | Relationship | master | 11 | 11 | 1 | 2 |
| 29 | u_mes_mast_user | Entity | master | 36 | 25 | 3 | 9 |
| 30 | u_mes_mast_userRole | Relationship | master | 11 | 11 | 1 | 2 |
| 31 | u_mes_mast_skill | Entity | master | 17 | 15 | 3 | 4 |
| 32 | u_mes_mast_skillOperation | Relationship | master | 11 | 11 | 1 | 2 |
| 33 | u_mes_mast_skillLevelScale | Child | master | 11 | 11 | 1 | 1 |
| 34 | u_mes_mast_skillCertification | Entity | transaction | 35 | 26 | 4 | 8 |
| 35 | u_mes_mast_customer | Entity | master | 27 | 24 | 3 | 5 |
| 36 | u_mes_mast_customerShipTo | Child | master | 17 | 17 | 1 | 1 |
| 37 | u_mes_mast_customerContact | Child | master | 13 | 11 | 2 | 1 |
| 38 | u_mes_mast_supplier | Entity | master | 27 | 26 | 3 | 5 |
| 39 | u_mes_mast_supplierContact | Child | master | 13 | 11 | 2 | 1 |
| 40 | u_mes_mast_supplierCertificate | Child | master | 12 | 11 | 1 | 1 |
| 41 | u_mes_mast_supplierSuppliedItem | Relationship | master | 13 | 12 | 2 | 2 |
| 42 | u_mes_mast_unitOfMeasure | Entity | master | 18 | 15 | 4 | 3 |
| 43 | u_mes_mast_department | Entity | master | 16 | 12 | 2 | 5 |
| 44 | u_mes_mast_designation | Entity | master | 14 | 14 | 2 | 3 |
| 45 | u_mes_mast_employmentType | Entity | master | 11 | 11 | 2 | 2 |
| 46 | u_mes_mast_costCenter | Entity | master | 12 | 11 | 2 | 2 |
| 47 | u_mes_mast_manufacturer | Entity | master | 13 | 9 | 2 | 3 |
| 48 | u_mes_mast_equipmentType | Entity | master | 10 | 10 | 2 | 2 |
| 49 | u_mes_mast_skillCategory | Entity | master | 10 | 10 | 2 | 2 |
| 50 | u_mes_mast_permission | Entity | master | 12 | 12 | 2 | 2 |
| 51 | u_mes_mast_signatureMeaning | Entity | master | 10 | 10 | 2 | 2 |
| 52 | u_mes_mast_currency | Entity | master | 12 | 12 | 2 | 2 |
| 53 | u_mes_mast_country | Entity | master | 11 | 11 | 2 | 2 |
| 54 | u_mes_mast_language | Entity | master | 10 | 10 | 2 | 2 |
| 55 | u_mes_mast_transporter | Entity | master | 12 | 10 | 2 | 2 |
| 56 | u_mes_mast_commodity | Entity | master | 10 | 10 | 2 | 2 |
| 57 | u_mes_mast_roleRequiredSkill | Relationship | master | 12 | 12 | 1 | 2 |
