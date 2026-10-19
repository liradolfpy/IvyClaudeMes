## u_mes_qual_audit - Audits (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_audit.json | _id: mes_qual_auditStable | rel: CL20261018-23:51 | samples: 10 | columns: 30 | total width: 5150px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | title | Title | String | 52 | 300px | left |
| 3 | auditType | Audit Type | String | 21 | 170px | left |
| 4 | standard | Standard | String | 15 | 130px | left |
| 5 | scopeText | Scope Text | String | 46 | 300px | left |
| 6 | areaName | Area | String | 28 | 220px | left |
| 7 | lineName | Line | String | 35 | 270px | left |
| 8 | customerName | Customer | String | 23 | 190px | left |
| 9 | layer | Layer | Int32 | 1 | 80px | right |
| 10 | leadAuditorUserName | Lead Auditor User | String | 14 | 160px | left |
| 11 | auditeeUserName | Auditee User | String | 14 | 130px | left |
| 12 | plannedDate | Planned Date | Date/Date | 10 | 130px | center |
| 13 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 14 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 15 | checkSheetName | Check Sheet | String | 54 | 300px | left |
| 16 | questionsCount | Questions Count | Int32 | 2 | 150px | right |
| 17 | conformingCount | Conforming Count | Int32 | 2 | 160px | right |
| 18 | scorePct | Score (%) | Decimal128 | 4 | 110px | right |
| 19 | overallRating | Overall Rating | String | 0 | 140px | left |
| 20 | reportControlledDocumentName | Report Controlled Document | String | 64 | 300px | left |
| 21 | nextAuditDueAt | Next Audit Due At | Date/Date | 10 | 160px | center |
| 22 | auditScheduleName | Audit Schedule | String | 48 | 300px | left |
| 23 | dueDate | Due Date | Date/Date | 10 | 100px | center |
| 24 | isMissed | Missed | Boolean | 3 | 90px | center |
| 25 | escalationLevel | Escalation Level | Int32 | 1 | 160px | right |
| 26 | status | Status | String | 11 | 100px | left |
| 27 | createdBy | Created By | String | 14 | 120px | left |
| 28 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 29 | updatedBy | Updated By | String | 14 | 120px | left |
| 30 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); areaId (reference key, shown through areaName); lineId (reference key, shown through lineName); customerId (reference key, shown through customerName); leadAuditorUserId (reference key, shown through leadAuditorUserName); auditeeUserId (reference key, shown through auditeeUserName); checkSheetId (reference key, shown through checkSheetName); reportControlledDocumentId (reference key, shown through reportControlledDocumentName); auditScheduleId (reference key, shown through auditScheduleName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): overallRating

## u_mes_qual_auditAuditorUser - Audit Auditors (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_auditAuditorUser.json | _id: mes_qual_auditAuditorUserStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1260px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | auditName | Audit | String | 52 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | auditorUserName | Auditor User | String | 14 | 130px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); auditId (reference key, shown through auditName); auditorUserId (reference key, shown through auditorUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_auditFinding - Audit Findings (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_auditFinding.json | _id: mes_qual_auditFindingStable | rel: CL20261018-23:51 | samples: 10 | columns: 14 | total width: 2450px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | auditName | Audit | String | 43 | 300px | left |
| 3 | findingNo | Finding No | Int32 | 1 | 110px | right |
| 4 | clause | Clause | String | 7 | 90px | left |
| 5 | description | Description | String | 104 | 300px | left |
| 6 | grade | Grade | String | 27 | 210px | left |
| 7 | ownerUserName | Owner User | String | 14 | 120px | left |
| 8 | dueAt | Due At | Date/Datetime | 19 | 160px | center |
| 9 | closedAt | Closed At | Date/Datetime | 19 | 160px | center |
| 10 | capaName | CAPA | String | 41 | 300px | left |
| 11 | createdBy | Created By | String | 14 | 120px | left |
| 12 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 13 | updatedBy | Updated By | String | 14 | 120px | left |
| 14 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); auditId (reference key, shown through auditName); ownerUserId (reference key, shown through ownerUserName); capaId (reference key, shown through capaName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_auditSchedule - Audit Schedules (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_auditSchedule.json | _id: mes_qual_auditScheduleStable | rel: CL20261018-23:51 | samples: 10 | columns: 18 | total width: 3100px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | name | Name | String | 50 | 300px | left |
| 3 | auditType | Audit Type | String | 21 | 170px | left |
| 4 | layer | Layer | Int32 | 1 | 80px | right |
| 5 | areaName | Area | String | 28 | 220px | left |
| 6 | lineName | Line | String | 35 | 270px | left |
| 7 | workCenterName | Work Center | String | 32 | 250px | left |
| 8 | checkSheetName | Check Sheet | String | 55 | 300px | left |
| 9 | frequencyType | Frequency Type | String | 7 | 140px | left |
| 10 | frequencyValue | Frequency Value | Decimal128 | 1 | 150px | right |
| 11 | auditorRoleName | Auditor Role | String | 21 | 170px | left |
| 12 | auditorUserName | Auditor User | String | 14 | 130px | left |
| 13 | toleranceHours | Tolerance (h) | Int32 | 3 | 140px | right |
| 14 | escalationRuleName | Escalation Rule | String | 28 | 220px | left |
| 15 | nextDueDate | Next Due Date | Date/Date | 10 | 140px | center |
| 16 | validFrom | Valid From | Date/Date | 10 | 110px | center |
| 17 | validTo | Valid to | Date/Date | 10 | 100px | center |
| 18 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); areaId (reference key, shown through areaName); lineId (reference key, shown through lineName); workCenterId (reference key, shown through workCenterName); checkSheetId (reference key, shown through checkSheetName); auditorRoleId (reference key, shown through auditorRoleName); auditorUserId (reference key, shown through auditorUserName); escalationRuleId (reference key, shown through escalationRuleName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_capa - CAPA (8D) (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_capa.json | _id: mes_qual_capaStable | rel: CL20261018-23:51 | samples: 20 | columns: 28 | total width: 5770px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | title | Title | String | 47 | 300px | left |
| 3 | capaType | CAPA Type | String | 10 | 110px | left |
| 4 | source | Source | String | 12 | 110px | left |
| 5 | customerComplaintName | Customer Complaint | String | 58 | 300px | left |
| 6 | auditName | Audit | String | 0 | 80px | left |
| 7 | itemName | Item | String | 61 | 300px | left |
| 8 | customerName | Customer | String | 42 | 300px | left |
| 9 | openedAt | Opened At | Date/Datetime | 19 | 160px | center |
| 10 | openedBy | Opened By | String | 14 | 120px | left |
| 11 | d2ProblemDescription | D2 Problem Description | String | 63 | 300px | left |
| 12 | d4RootCauseOccurrence | D4 Root Cause Occurrence | String | 43 | 300px | left |
| 13 | d4RootCauseEscape | D4 Root Cause Escape | String | 100 | 300px | left |
| 14 | d4RootCauseMethod | D4 Root Cause Method | String | 0 | 180px | left |
| 15 | d7PreventionPfmeaName | D7 Prevention PFMEA | String | 78 | 300px | left |
| 16 | d7PreventionControlPlanName | D7 Prevention Control Plan | String | 28 | 230px | left |
| 17 | d7PreventionLessonsLearned | D7 Prevention Lessons Learned | String | 79 | 300px | left |
| 18 | d7PreventionHorizontalDeployment | D7 Prevention Horizontal Deployment | String | 48 | 300px | left |
| 19 | d8ClosureClosedBy | D8 Closure Closed By | String | 15 | 180px | left |
| 20 | d8ClosureClosedAt | D8 Closure Closed At | Date/Datetime | 19 | 180px | center |
| 21 | d8ClosureCustomerAccepted | D8 Closure Customer Accepted | Boolean | 3 | 240px | center |
| 22 | dueAt | Due At | Date/Datetime | 19 | 160px | center |
| 23 | currentDiscipline | Current Discipline | String | 2 | 170px | left |
| 24 | status | Status | String | 21 | 170px | left |
| 25 | createdBy | Created By | String | 14 | 120px | left |
| 26 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 27 | updatedBy | Updated By | String | 14 | 120px | left |
| 28 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerComplaintId (reference key, shown through customerComplaintName); auditId (reference key, shown through auditName); itemId (reference key, shown through itemName); customerId (reference key, shown through customerName); openedById (reference key, shown through openedBy); d7PreventionPfmeaId (reference key, shown through d7PreventionPfmeaName); d7PreventionControlPlanId (reference key, shown through d7PreventionControlPlanName); d8ClosureClosedById (reference key, shown through d8ClosureClosedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): auditName, d4RootCauseMethod

## u_mes_qual_capaContainmentAction - CAPA Containment Actions (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_capaContainmentAction.json | _id: mes_qual_capaContainmentActionStable | rel: CL20261018-23:51 | samples: 10 | columns: 10 | total width: 1720px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | capaName | CAPA | String | 41 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | description | Description | String | 69 | 300px | left |
| 5 | ownerUserName | Owner User | String | 14 | 120px | left |
| 6 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 7 | createdBy | Created By | String | 14 | 120px | left |
| 8 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 9 | updatedBy | Updated By | String | 14 | 120px | left |
| 10 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); capaId (reference key, shown through capaName); ownerUserId (reference key, shown through ownerUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_capaControlledDocument - CAPA Documents (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_capaControlledDocument.json | _id: mes_qual_capaControlledDocumentStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1440px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | capaName | CAPA | String | 45 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | controlledDocumentName | Controlled Document | String | 64 | 300px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); capaId (reference key, shown through capaName); controlledDocumentId (reference key, shown through controlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_capaCorrectiveAction - CAPA Corrective Actions (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_capaCorrectiveAction.json | _id: mes_qual_capaCorrectiveActionStable | rel: CL20261018-23:51 | samples: 10 | columns: 10 | total width: 1720px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | capaName | CAPA | String | 41 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | description | Description | String | 69 | 300px | left |
| 5 | ownerUserName | Owner User | String | 14 | 120px | left |
| 6 | dueAt | Due At | Date/Datetime | 19 | 160px | center |
| 7 | createdBy | Created By | String | 14 | 120px | left |
| 8 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 9 | updatedBy | Updated By | String | 14 | 120px | left |
| 10 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); capaId (reference key, shown through capaName); ownerUserId (reference key, shown through ownerUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_capaImplementationAction - CAPA Implementation Actions (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_capaImplementationAction.json | _id: mes_qual_capaImplementationActionStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1840px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | capaName | CAPA | String | 41 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | description | Description | String | 120 | 300px | left |
| 5 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 6 | verifiedBy | Verified By | String | 15 | 130px | left |
| 7 | effective | Effective | Boolean | 3 | 110px | center |
| 8 | createdBy | Created By | String | 14 | 120px | left |
| 9 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 10 | updatedBy | Updated By | String | 14 | 120px | left |
| 11 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); capaId (reference key, shown through capaName); verifiedById (reference key, shown through verifiedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_capaNonconformance - CAPA Nonconformances (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_capaNonconformance.json | _id: mes_qual_capaNonconformanceStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1430px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | capaName | CAPA | String | 45 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | nonconformanceName | Nonconformance | String | 55 | 300px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); capaId (reference key, shown through capaName); nonconformanceId (reference key, shown through nonconformanceName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_capaTeamMember - CAPA Team Members (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_capaTeamMember.json | _id: mes_qual_capaTeamMemberStable | rel: CL20261018-23:51 | samples: 10 | columns: 9 | total width: 1390px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | capaName | CAPA | String | 41 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | userName | User | String | 14 | 120px | left |
| 5 | roleInTeam | Role in Team | String | 8 | 130px | left |
| 6 | createdBy | Created By | String | 14 | 120px | left |
| 7 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 8 | updatedBy | Updated By | String | 14 | 120px | left |
| 9 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); capaId (reference key, shown through capaName); userId (reference key, shown through userName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_characteristic - Characteristics (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_characteristic.json | _id: mes_qual_characteristicStable | rel: CL20261018-23:51 | samples: 20 | columns: 24 | total width: 4340px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 11 | 110px | left |
| 2 | name | Name | String | 45 | 300px | left |
| 3 | itemName | Item | String | 61 | 300px | left |
| 4 | operationName | Operation | String | 31 | 240px | left |
| 5 | characteristicType | Characteristic Type | String | 7 | 180px | left |
| 6 | classification | Classification | String | 11 | 140px | left |
| 7 | drawingZone | Drawing Zone | String | 25 | 200px | left |
| 8 | balloonNo | Balloon No | String | 2 | 110px | left |
| 9 | dataType | Data Type | String | 8 | 110px | left |
| 10 | nominal | Nominal | Decimal128 | 6 | 90px | right |
| 11 | lowerSpecLimit | Lower Spec Limit | Decimal128 | 6 | 160px | right |
| 12 | upperSpecLimit | Upper Spec Limit | Decimal128 | 6 | 160px | right |
| 13 | unitOfMeasureName | Unit of Measure | String | 16 | 150px | left |
| 14 | toleranceType | Tolerance Type | String | 9 | 140px | left |
| 15 | measurementMethod | Measurement Method | String | 53 | 300px | left |
| 16 | gaugeName | Gauge | String | 39 | 300px | left |
| 17 | gaugeTypeName | Gauge Type | String | 28 | 220px | left |
| 18 | attributeAcceptance | Attribute Acceptance | String | 52 | 300px | left |
| 19 | isSpc | SPC | Boolean | 3 | 80px | center |
| 20 | targetCpk | Target Cpk | Decimal128 | 4 | 110px | right |
| 21 | reactionPlan | Reaction Plan | String | 81 | 300px | left |
| 22 | source | Source | String | 12 | 110px | left |
| 23 | positionCount | Position Count | Int32 | 1 | 140px | right |
| 24 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); operationId (reference key, shown through operationName); unitOfMeasureId (reference key, shown through unitOfMeasureName); gaugeId (reference key, shown through gaugeName); gaugeTypeId (reference key, shown through gaugeTypeName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_characteristicPosition - Characteristic Positions (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_characteristicPosition.json | _id: mes_qual_characteristicPositionStable | rel: CL20261018-23:51 | samples: 20 | columns: 9 | total width: 1500px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | characteristicName | Characteristic | String | 32 | 250px | left |
| 3 | positionNo | Position No | Int32 | 1 | 120px | right |
| 4 | positionName | Position Name | String | 45 | 300px | left |
| 5 | nominal | Nominal | Decimal128 | 6 | 90px | right |
| 6 | lowerSpecLimit | Lower Spec Limit | Decimal128 | 5 | 160px | right |
| 7 | upperSpecLimit | Upper Spec Limit | Decimal128 | 6 | 160px | right |
| 8 | unitOfMeasureName | Unit of Measure | String | 10 | 150px | left |
| 9 | curveEnvelopeName | Curve Envelope | String | 0 | 140px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); characteristicId (reference key, shown through characteristicName); unitOfMeasureId (reference key, shown through unitOfMeasureName); curveEnvelopeId (reference key, shown through curveEnvelopeName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): curveEnvelopeName

## u_mes_qual_checkSheet - Check Sheets (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_checkSheet.json | _id: mes_qual_checkSheetStable | rel: CL20261018-23:51 | samples: 20 | columns: 15 | total width: 2710px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | name | Name | String | 59 | 300px | left |
| 3 | checkSheetType | Check Sheet Type | String | 14 | 160px | left |
| 4 | workCenterName | Work Center | String | 37 | 280px | left |
| 5 | equipmentName | Equipment | String | 54 | 300px | left |
| 6 | operationName | Operation | String | 31 | 240px | left |
| 7 | itemName | Item | String | 61 | 300px | left |
| 8 | version | Version | Int32 | 1 | 90px | right |
| 9 | frequency | Frequency | String | 9 | 110px | left |
| 10 | masterSampleRequired | Master Sample Required | Boolean | 3 | 200px | center |
| 11 | estimatedMinutes | Estimated (min) | Int32 | 1 | 150px | right |
| 12 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 13 | approvedBy | Approved By | String | 0 | 120px | left |
| 14 | approvedAt | Approved At | Date/Datetime | 0 | 120px | center |
| 15 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); workCenterId (reference key, shown through workCenterName); equipmentId (reference key, shown through equipmentName); operationId (reference key, shown through operationName); itemId (reference key, shown through itemName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): approvedBy, approvedAt

## u_mes_qual_checkSheetItem - Check Sheet Items (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_checkSheetItem.json | _id: mes_qual_checkSheetItemStable | rel: CL20261018-23:51 | samples: 20 | columns: 11 | total width: 1830px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | checkSheetName | Check Sheet | String | 52 | 300px | left |
| 3 | itemNo | Item No | Int32 | 1 | 90px | right |
| 4 | question | Question | String | 97 | 300px | left |
| 5 | answerType | Answer Type | String | 6 | 120px | left |
| 6 | expectedAnswer | Expected Answer | String | 3 | 150px | left |
| 7 | lowerLimit | Lower Limit | Decimal128 | 6 | 120px | right |
| 8 | upperLimit | Upper Limit | Decimal128 | 6 | 120px | right |
| 9 | unitText | Unit Text | String | 3 | 110px | left |
| 10 | isCritical | Critical | Boolean | 3 | 100px | center |
| 11 | reactionOnFail | Reaction on Fail | String | 62 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); checkSheetId (reference key, shown through checkSheetName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_checkSheetResult - Check Sheet Results (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_checkSheetResult.json | _id: mes_qual_checkSheetResultStable | rel: CL20261018-23:51 | samples: 20 | columns: 22 | total width: 3690px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | checkSheetName | Check Sheet | String | 59 | 300px | left |
| 3 | checkSheetVersion | Check Sheet Version | Int32 | 1 | 180px | right |
| 4 | workCenterName | Work Center | String | 37 | 280px | left |
| 5 | equipmentName | Equipment | String | 54 | 300px | left |
| 6 | shiftName | Shift | String | 7 | 80px | left |
| 7 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 8 | productionOrderName | Production Order | String | 10 | 160px | left |
| 9 | performedBy | Performed By | String | 14 | 130px | left |
| 10 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 11 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 12 | overallResult | Overall Result | String | 4 | 140px | left |
| 13 | failedCount | Failed Count | Int32 | 1 | 130px | right |
| 14 | reactionTaken | Reaction Taken | String | 0 | 140px | left |
| 15 | verifiedBy | Verified By | String | 15 | 130px | left |
| 16 | verifiedAt | Verified At | Date/Datetime | 19 | 160px | center |
| 17 | nonconformanceName | Nonconformance | String | 52 | 300px | left |
| 18 | status | Status | String | 11 | 100px | left |
| 19 | createdBy | Created By | String | 14 | 120px | left |
| 20 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 21 | updatedBy | Updated By | String | 14 | 120px | left |
| 22 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); checkSheetId (reference key, shown through checkSheetName); workCenterId (reference key, shown through workCenterName); equipmentId (reference key, shown through equipmentName); shiftId (reference key, shown through shiftName); productionOrderId (reference key, shown through productionOrderName); performedById (reference key, shown through performedBy); verifiedById (reference key, shown through verifiedBy); nonconformanceId (reference key, shown through nonconformanceName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): reactionTaken

## u_mes_qual_checkSheetResultAnswer - Check Sheet Result Answers (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_checkSheetResultAnswer.json | _id: mes_qual_checkSheetResultAnswerStable | rel: CL20261018-23:51 | samples: 20 | columns: 11 | total width: 1630px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | checkSheetResultName | Check Sheet Result | String | 15 | 170px | left |
| 3 | itemNo | Item No | Int32 | 1 | 90px | right |
| 4 | answerText | Answer Text | String | 3 | 120px | left |
| 5 | answerNumber | Answer Number | Decimal128 | 0 | 140px | right |
| 6 | passed | Passed | Boolean | 3 | 90px | center |
| 7 | comment | Comment | String | 58 | 300px | left |
| 8 | createdBy | Created By | String | 14 | 120px | left |
| 9 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 10 | updatedBy | Updated By | String | 14 | 120px | left |
| 11 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); checkSheetResultId (reference key, shown through checkSheetResultName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): answerNumber

## u_mes_qual_complaintType - Complaint Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_complaintType.json | _id: mes_qual_complaintTypeStable | rel: CL20261018-23:51 | samples: 20 | columns: 5 | total width: 880px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 9 | 110px | left |
| 2 | name | Name | String | 33 | 260px | left |
| 3 | description | Description | String | 45 | 300px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_controlPlan - Control Plans (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_controlPlan.json | _id: mes_qual_controlPlanStable | rel: CL20261018-23:51 | samples: 20 | columns: 16 | total width: 2810px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 28 | 220px | left |
| 2 | itemName | Item | String | 61 | 300px | left |
| 3 | itemRevision | Item Revision | String | 1 | 140px | left |
| 4 | phase | Phase | String | 9 | 90px | left |
| 5 | version | Version | Int32 | 1 | 90px | right |
| 6 | routingName | Routing | String | 64 | 300px | left |
| 7 | pfmeaName | PFMEA | String | 78 | 300px | left |
| 8 | customerApprovalDate | Customer Approval Date | Date/Date | 0 | 200px | center |
| 9 | engineeringChangeName | Engineering Change | String | 57 | 300px | left |
| 10 | preparedBy | Prepared By | String | 14 | 120px | left |
| 11 | approvedBy | Approved By | String | 0 | 120px | left |
| 12 | approvedAt | Approved At | Date/Datetime | 0 | 120px | center |
| 13 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 14 | originalDate | Original Date | Date/Date | 10 | 140px | center |
| 15 | revisionDate | Revision Date | Date/Date | 10 | 140px | center |
| 16 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); routingId (reference key, shown through routingName); pfmeaId (reference key, shown through pfmeaName); engineeringChangeId (reference key, shown through engineeringChangeName); preparedById (reference key, shown through preparedBy); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): customerApprovalDate, approvedBy, approvedAt

## u_mes_qual_controlPlanCoreTeamUser - Control Plan Core Team (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_controlPlanCoreTeamUser.json | _id: mes_qual_controlPlanCoreTeamUserStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 740px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 34 | 260px | left |
| 2 | controlPlanName | Control Plan | String | 28 | 220px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | coreTeamUserName | Core Team User | String | 14 | 140px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); controlPlanId (reference key, shown through controlPlanName); coreTeamUserId (reference key, shown through coreTeamUserName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_controlPlanLine - Control Plan Lines (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_controlPlanLine.json | _id: mes_qual_controlPlanLineStable | rel: CL20261018-23:51 | samples: 20 | columns: 16 | total width: 3500px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 25 | 200px | left |
| 2 | controlPlanName | Control Plan | String | 21 | 170px | left |
| 3 | lineNo | Line No | Int32 | 3 | 90px | right |
| 4 | operationName | Operation | String | 31 | 240px | left |
| 5 | processName | Process Name | String | 65 | 300px | left |
| 6 | equipmentText | Equipment Text | String | 64 | 300px | left |
| 7 | characteristicName | Characteristic | String | 45 | 300px | left |
| 8 | classification | Classification | String | 11 | 140px | left |
| 9 | specification | Specification | String | 20 | 160px | left |
| 10 | gaugeName | Gauge | String | 39 | 300px | left |
| 11 | measurementTechnique | Measurement Technique | String | 53 | 300px | left |
| 12 | sampleSize | Sample Size | Int32 | 1 | 120px | right |
| 13 | sampleFrequency | Sample Frequency | String | 16 | 160px | left |
| 14 | controlMethod | Control Method | String | 54 | 300px | left |
| 15 | reactionPlan | Reaction Plan | String | 81 | 300px | left |
| 16 | responsible | Responsible | String | 8 | 120px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); controlPlanId (reference key, shown through controlPlanName); operationId (reference key, shown through operationName); characteristicId (reference key, shown through characteristicName); gaugeId (reference key, shown through gaugeName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_curveEnvelope - Curve Envelopes (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_curveEnvelope.json | _id: mes_qual_curveEnvelopeStable | rel: CL20261018-23:51 | samples: 20 | columns: 20 | total width: 3720px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 23 | 190px | left |
| 2 | name | Name | String | 76 | 300px | left |
| 3 | characteristicName | Characteristic | String | 29 | 230px | left |
| 4 | itemName | Item | String | 49 | 300px | left |
| 5 | productVariantName | Product Variant | String | 44 | 300px | left |
| 6 | operationName | Operation | String | 29 | 230px | left |
| 7 | recipeName | Recipe | String | 56 | 300px | left |
| 8 | curveType | Curve Type | String | 18 | 150px | left |
| 9 | xQuantity | X Quantity | String | 12 | 110px | left |
| 10 | xUnitText | X Unit Text | String | 3 | 120px | left |
| 11 | yQuantity | Y Quantity | String | 13 | 120px | left |
| 12 | yUnitText | Y Unit Text | String | 4 | 120px | left |
| 13 | version | Version | Int32 | 1 | 90px | right |
| 14 | goldenSampleSerialNo | Golden Sample Serial No | String | 16 | 210px | left |
| 15 | referenceControlledDocumentName | Reference Controlled Document | String | 44 | 300px | left |
| 16 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 17 | effectiveTo | Effective to | Date/Date | 10 | 130px | center |
| 18 | approvedBy | Approved By | String | 15 | 130px | left |
| 19 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 20 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); characteristicId (reference key, shown through characteristicName); itemId (reference key, shown through itemName); productVariantId (reference key, shown through productVariantName); operationId (reference key, shown through operationName); recipeId (reference key, shown through recipeName); referenceControlledDocumentId (reference key, shown through referenceControlledDocumentName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_curveEnvelopeWindow - Curve Envelope Windows (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_curveEnvelopeWindow.json | _id: mes_qual_curveEnvelopeWindowStable | rel: CL20261018-23:51 | samples: 20 | columns: 10 | total width: 1280px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 26 | 210px | left |
| 2 | curveEnvelopeName | Curve Envelope | String | 61 | 300px | left |
| 3 | windowNo | Window No | Int32 | 1 | 110px | right |
| 4 | windowType | Window Type | String | 11 | 120px | left |
| 5 | xMin | X Min | Decimal128 | 5 | 80px | right |
| 6 | xMax | X Max | Decimal128 | 5 | 80px | right |
| 7 | yMin | Y Min | Decimal128 | 4 | 80px | right |
| 8 | yMax | Y Max | Decimal128 | 4 | 80px | right |
| 9 | entrySide | Entry Side | String | 4 | 110px | left |
| 10 | exitSide | Exit Side | String | 5 | 110px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); curveEnvelopeId (reference key, shown through curveEnvelopeName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_customerComplaint - Customer Complaints (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_customerComplaint.json | _id: mes_qual_customerComplaintStable | rel: CL20261018-23:51 | samples: 20 | columns: 30 | total width: 5610px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | customerName | Customer | String | 42 | 300px | left |
| 3 | customerRefNo | Customer Ref No | String | 16 | 150px | left |
| 4 | complaintTypeName | Complaint Type | String | 33 | 260px | left |
| 5 | itemName | Item | String | 61 | 300px | left |
| 6 | description | Description | String | 63 | 300px | left |
| 7 | defectDescription | Defect Description | String | 63 | 300px | left |
| 8 | reportedAt | Reported At | Date/Datetime | 19 | 160px | center |
| 9 | receivedBy | Received By | String | 14 | 120px | left |
| 10 | occurredAt | Occurred At | Date/Datetime | 19 | 160px | center |
| 11 | customerLocation | Customer Location | String | 48 | 300px | left |
| 12 | quantityComplained | Quantity Complained | Int32 | 1 | 180px | right |
| 13 | quantityConfirmed | Quantity Confirmed | Int32 | 1 | 170px | right |
| 14 | vehicleModelName | Vehicle Model | String | 22 | 180px | left |
| 15 | mileageKm | Mileage Km | Decimal128 | 0 | 110px | right |
| 16 | severity | Severity | Int32 | 2 | 100px | right |
| 17 | isSafetyRelated | Safety Related | Boolean | 3 | 140px | center |
| 18 | containmentDueAt | Containment Due At | Date/Datetime | 19 | 170px | center |
| 19 | containmentSentAt | Containment Sent At | Date/Datetime | 19 | 180px | center |
| 20 | nonconformanceName | Nonconformance | String | 58 | 300px | left |
| 21 | capaName | CAPA | String | 47 | 300px | left |
| 22 | debitNoteInr | Debit Note (INR) | Decimal128 | 3 | 160px | right |
| 23 | ppmImpact | PPM Impact | Int32 | 2 | 110px | right |
| 24 | sortingCostInr | Sorting Cost (INR) | Decimal128 | 7 | 170px | right |
| 25 | customerClosedAt | Customer Closed At | Date/Datetime | 19 | 170px | center |
| 26 | status | Status | String | 16 | 140px | left |
| 27 | createdBy | Created By | String | 14 | 120px | left |
| 28 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 29 | updatedBy | Updated By | String | 14 | 120px | left |
| 30 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerId (reference key, shown through customerName); complaintTypeId (reference key, shown through complaintTypeName); itemId (reference key, shown through itemName); receivedById (reference key, shown through receivedBy); vehicleModelId (reference key, shown through vehicleModelName); nonconformanceId (reference key, shown through nonconformanceName); capaId (reference key, shown through capaName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): mileageKm

## u_mes_qual_customerComplaintCommunication - Customer Complaint Communications (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_customerComplaintCommunication.json | _id: mes_qual_customerComplaintCommunicationStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1810px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | customerComplaintName | Customer Complaint | String | 63 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | communicatedAt | Communicated At | Date/Datetime | 19 | 160px | center |
| 5 | direction | Direction | String | 8 | 110px | left |
| 6 | communicationSummary | Communication Summary | String | 59 | 300px | left |
| 7 | authorUserName | Author User | String | 14 | 120px | left |
| 8 | createdBy | Created By | String | 14 | 120px | left |
| 9 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 10 | updatedBy | Updated By | String | 14 | 120px | left |
| 11 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerComplaintId (reference key, shown through customerComplaintName); authorUserId (reference key, shown through authorUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_customerComplaintSerialNumber - Customer Complaint Serial Numbers (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_customerComplaintSerialNumber.json | _id: mes_qual_customerComplaintSerialNumberStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1270px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | customerComplaintName | Customer Complaint | String | 63 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | serialNumberName | Serial Number | String | 13 | 140px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerComplaintId (reference key, shown through customerComplaintName); serialNumberId (reference key, shown through serialNumberName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_customerComplaintShipment - Customer Complaint Shipments (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_customerComplaintShipment.json | _id: mes_qual_customerComplaintShipmentStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1250px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | customerComplaintName | Customer Complaint | String | 63 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | shipmentName | Shipment | String | 15 | 130px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerComplaintId (reference key, shown through customerComplaintName); shipmentId (reference key, shown through shipmentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_customerComplaintSuspectLot - Customer Complaint Suspect Lots (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_customerComplaintSuspectLot.json | _id: mes_qual_customerComplaintSuspectLotStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1260px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | customerComplaintName | Customer Complaint | String | 63 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | suspectLotName | Suspect Lot | String | 15 | 130px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerComplaintId (reference key, shown through customerComplaintName); suspectLotId (reference key, shown through suspectLotName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_defectCode - Defect Codes (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_defectCode.json | _id: mes_qual_defectCodeStable | rel: CL20261018-23:51 | samples: 20 | columns: 14 | total width: 2610px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 4 | 110px | left |
| 2 | name | Name | String | 36 | 280px | left |
| 3 | defectGroupName | Defect Group | String | 17 | 140px | left |
| 4 | description | Description | String | 63 | 300px | left |
| 5 | severity | Severity | Int32 | 2 | 100px | right |
| 6 | defaultDispositionTypeName | Default Disposition Type | String | 24 | 210px | left |
| 7 | dispositionRoutingName | Disposition Routing | String | 64 | 300px | left |
| 8 | isSafetyRelated | Safety Related | Boolean | 3 | 140px | center |
| 9 | requiresPhoto | Requires Photo | Boolean | 3 | 140px | center |
| 10 | requiresHold | Requires Hold | Boolean | 3 | 140px | center |
| 11 | scrapCostCategory | Scrap Cost Category | String | 19 | 180px | left |
| 12 | customerDefectCode | Customer Defect Code | String | 10 | 180px | left |
| 13 | pfmeaFailureMode | PFMEA Failure Mode | String | 40 | 300px | left |
| 14 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); defectGroupId (reference key, shown through defectGroupName); defaultDispositionTypeId (reference key, shown through defaultDispositionTypeName); dispositionRoutingId (reference key, shown through dispositionRoutingName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_defectCodeApplicableOperation - Defect Code Applicable Operations (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_defectCodeApplicableOperation.json | _id: mes_qual_defectCodeApplicableOperationStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 640px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 9 | 110px | left |
| 2 | defectCodeName | Defect Code | String | 28 | 220px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | applicableOperationName | Applicable Operation | String | 24 | 190px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); defectCodeId (reference key, shown through defectCodeName); applicableOperationId (reference key, shown through applicableOperationName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_defectGroup - Defect Groups (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_defectGroup.json | _id: mes_qual_defectGroupStable | rel: CL20261018-23:51 | samples: 20 | columns: 5 | total width: 650px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 5 | 110px | left |
| 2 | name | Name | String | 17 | 140px | left |
| 3 | description | Description | String | 24 | 190px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_defectRecord - Defect Records (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_defectRecord.json | _id: mes_qual_defectRecordStable | rel: CL20261018-23:51 | samples: 20 | columns: 34 | total width: 5980px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | defectCodeName | Defect Code | String | 36 | 280px | left |
| 3 | wipUnitName | WIP Unit | String | 20 | 160px | left |
| 4 | serialNumberName | Serial Number | String | 13 | 140px | left |
| 5 | lotName | Lot | String | 15 | 130px | left |
| 6 | itemName | Item | String | 61 | 300px | left |
| 7 | productVariantName | Product Variant | String | 44 | 300px | left |
| 8 | productionOrderName | Production Order | String | 10 | 160px | left |
| 9 | detectedAtOperationName | Detected At Operation | String | 31 | 240px | left |
| 10 | detectedAtWorkCenterName | Detected At Work Center | String | 37 | 280px | left |
| 11 | originOperationName | Origin Operation | String | 30 | 230px | left |
| 12 | isFirstFail | First Fail | Boolean | 3 | 110px | center |
| 13 | positionNo | Position No | Int32 | 1 | 120px | right |
| 14 | defectLocationText | Defect Location Text | String | 35 | 270px | left |
| 15 | quantity | Quantity | Int32 | 2 | 100px | right |
| 16 | fourMCategory | Four M Category | String | 8 | 150px | left |
| 17 | operatorUserName | Operator User | String | 14 | 140px | left |
| 18 | equipmentName | Equipment | String | 54 | 300px | left |
| 19 | componentLotName | Component Lot | String | 15 | 140px | left |
| 20 | operationExecutionName | Operation Execution | String | 15 | 180px | left |
| 21 | inspectionResultName | Inspection Result | String | 14 | 160px | left |
| 22 | shiftName | Shift | String | 7 | 80px | left |
| 23 | productionDate | Production Date | Date/Date | 10 | 150px | center |
| 24 | detectedAt | Detected At | Date/Datetime | 19 | 160px | center |
| 25 | detectedBy | Detected By | String | 14 | 120px | left |
| 26 | imageControlledDocumentName | Image Controlled Document | String | 0 | 220px | left |
| 27 | nonconformanceName | Nonconformance | String | 58 | 300px | left |
| 28 | reworkOrderName | Rework Order | String | 15 | 130px | left |
| 29 | scrapRecordName | Scrap Record | String | 15 | 130px | left |
| 30 | status | Status | String | 8 | 90px | left |
| 31 | createdBy | Created By | String | 14 | 120px | left |
| 32 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 33 | updatedBy | Updated By | String | 14 | 120px | left |
| 34 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); defectCodeId (reference key, shown through defectCodeName); wipUnitId (reference key, shown through wipUnitName); serialNumberId (reference key, shown through serialNumberName); lotId (reference key, shown through lotName); itemId (reference key, shown through itemName); productVariantId (reference key, shown through productVariantName); productionOrderId (reference key, shown through productionOrderName); detectedAtOperationId (reference key, shown through detectedAtOperationName); detectedAtWorkCenterId (reference key, shown through detectedAtWorkCenterName); originOperationId (reference key, shown through originOperationName); operatorUserId (reference key, shown through operatorUserName); equipmentId (reference key, shown through equipmentName); componentLotId (reference key, shown through componentLotName); operationExecutionId (reference key, shown through operationExecutionName); inspectionResultId (reference key, shown through inspectionResultName); shiftId (reference key, shown through shiftName); detectedById (reference key, shown through detectedBy); imageControlledDocumentId (reference key, shown through imageControlledDocumentName); nonconformanceId (reference key, shown through nonconformanceName); reworkOrderId (reference key, shown through reworkOrderName); scrapRecordId (reference key, shown through scrapRecordName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): imageControlledDocumentName

## u_mes_qual_deviationPermit - Deviation Permits (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_deviationPermit.json | _id: mes_qual_deviationPermitStable | rel: CL20261018-23:51 | samples: 20 | columns: 26 | total width: 4710px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | title | Title | String | 71 | 300px | left |
| 3 | itemName | Item | String | 61 | 300px | left |
| 4 | characteristicName | Characteristic | String | 45 | 300px | left |
| 5 | deviationType | Deviation Type | String | 7 | 140px | left |
| 6 | description | Description | String | 152 | 300px | left |
| 7 | requestedValue | Requested Value | Decimal128 | 5 | 150px | right |
| 8 | specifiedValue | Specified Value | Decimal128 | 6 | 150px | right |
| 9 | customerName | Customer | String | 42 | 300px | left |
| 10 | customerApprovalRef | Customer Approval Ref | String | 16 | 190px | left |
| 11 | nonconformanceName | Nonconformance | String | 58 | 300px | left |
| 12 | engineeringChangeName | Engineering Change | String | 0 | 170px | left |
| 13 | limitType | Limit Type | String | 8 | 110px | left |
| 14 | quantityLimit | Quantity Limit | Int32 | 4 | 140px | right |
| 15 | quantityUsed | Quantity Used | Int32 | 3 | 140px | right |
| 16 | validFrom | Valid From | Date/Date | 10 | 110px | center |
| 17 | validTo | Valid to | Date/Date | 10 | 100px | center |
| 18 | markingRequirement | Marking Requirement | String | 38 | 290px | left |
| 19 | requestedBy | Requested By | String | 14 | 130px | left |
| 20 | requestedAt | Requested At | Date/Datetime | 19 | 160px | center |
| 21 | closedAt | Closed At | Date/Datetime | 19 | 160px | center |
| 22 | status | Status | String | 9 | 90px | left |
| 23 | createdBy | Created By | String | 14 | 120px | left |
| 24 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 25 | updatedBy | Updated By | String | 14 | 120px | left |
| 26 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); characteristicId (reference key, shown through characteristicName); customerId (reference key, shown through customerName); nonconformanceId (reference key, shown through nonconformanceName); engineeringChangeId (reference key, shown through engineeringChangeName); requestedById (reference key, shown through requestedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): engineeringChangeName

## u_mes_qual_deviationPermitApproval - Deviation Permit Approvals (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_deviationPermitApproval.json | _id: mes_qual_deviationPermitApprovalStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1750px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | deviationPermitName | Deviation Permit | String | 52 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | businessFunction | Business Function | String | 7 | 160px | left |
| 5 | userName | User | String | 14 | 120px | left |
| 6 | decision | Decision | String | 24 | 190px | left |
| 7 | decidedAt | Decided At | Date/Datetime | 19 | 160px | center |
| 8 | createdBy | Created By | String | 14 | 120px | left |
| 9 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 10 | updatedBy | Updated By | String | 14 | 120px | left |
| 11 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); deviationPermitId (reference key, shown through deviationPermitName); userId (reference key, shown through userName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_dispositionType - Disposition Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_dispositionType.json | _id: mes_qual_dispositionTypeStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1320px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | name | Name | String | 24 | 190px | left |
| 3 | description | Description | String | 37 | 280px | left |
| 4 | requiresRework | Requires Rework | Boolean | 3 | 150px | center |
| 5 | requiresScrap | Requires Scrap | Boolean | 3 | 140px | center |
| 6 | requiresCustomerApproval | Requires Customer Approval | Boolean | 3 | 230px | center |
| 7 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 8 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_environmentalMonitoringPoint - Environmental Monitoring Points (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_environmentalMonitoringPoint.json | _id: mes_qual_environmentalMonitoringPointStable | rel: CL20261018-23:51 | samples: 10 | columns: 13 | total width: 2200px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | name | Name | String | 60 | 300px | left |
| 3 | areaName | Area | String | 29 | 230px | left |
| 4 | workCenterName | Work Center | String | 30 | 230px | left |
| 5 | monitoredParameter | Monitored Parameter | String | 25 | 200px | left |
| 6 | parameterUnitText | Parameter Unit Text | String | 16 | 180px | left |
| 7 | limitDirection | Limit Direction | String | 5 | 150px | left |
| 8 | alertLimit | Alert Limit | Decimal128 | 7 | 120px | right |
| 9 | actionLimit | Action Limit | Decimal128 | 7 | 130px | right |
| 10 | lowerActionLimit | Lower Action Limit | Decimal128 | 4 | 170px | right |
| 11 | samplingFrequency | Sampling Frequency | String | 11 | 170px | left |
| 12 | processTagName | Process Tag | String | 0 | 120px | left |
| 13 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); areaId (reference key, shown through areaName); workCenterId (reference key, shown through workCenterName); processTagId (reference key, shown through processTagName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): processTagName

## u_mes_qual_environmentalMonitoringResult - Environmental Monitoring Results (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_environmentalMonitoringResult.json | _id: mes_qual_environmentalMonitoringResultStable | rel: CL20261018-23:51 | samples: 10 | columns: 14 | total width: 2220px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | environmentalMonitoringPointName | Environmental Monitoring Point | String | 60 | 300px | left |
| 3 | sampledAt | Sampled At | Date/Datetime | 19 | 160px | center |
| 4 | measuredValue | Measured Value | Decimal128 | 7 | 140px | right |
| 5 | limitEvaluation | Limit Evaluation | String | 21 | 170px | left |
| 6 | sampledBy | Sampled By | String | 11 | 110px | left |
| 7 | gaugeName | Gauge | String | 0 | 80px | left |
| 8 | nonconformanceName | Nonconformance | String | 0 | 140px | left |
| 9 | productImpactText | Product Impact Text | String | 135 | 300px | left |
| 10 | status | Status | String | 16 | 140px | left |
| 11 | createdBy | Created By | String | 11 | 110px | left |
| 12 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 13 | updatedBy | Updated By | String | 11 | 110px | left |
| 14 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); environmentalMonitoringPointId (reference key, shown through environmentalMonitoringPointName); sampledById (reference key, shown through sampledBy); gaugeId (reference key, shown through gaugeName); nonconformanceId (reference key, shown through nonconformanceName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): gaugeName, nonconformanceName

## u_mes_qual_gauge - Gauges (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_gauge.json | _id: mes_qual_gaugeStable | rel: CL20261018-23:51 | samples: 20 | columns: 26 | total width: 4570px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 10 | 110px | left |
| 2 | name | Name | String | 39 | 300px | left |
| 3 | gaugeTypeName | Gauge Type | String | 28 | 220px | left |
| 4 | manufacturerName | Manufacturer | String | 14 | 130px | left |
| 5 | model | Model | String | 18 | 150px | left |
| 6 | serialNo | Serial No | String | 14 | 120px | left |
| 7 | rangeMin | Range Min | Decimal128 | 7 | 110px | right |
| 8 | rangeMax | Range Max | Decimal128 | 9 | 110px | right |
| 9 | rangeUnitOfMeasureName | Range Unit of Measure | String | 16 | 190px | left |
| 10 | resolution | Resolution | Decimal128 | 5 | 110px | right |
| 11 | accuracy | Accuracy | Decimal128 | 5 | 100px | right |
| 12 | storageLocationName | Storage Location | String | 33 | 260px | left |
| 13 | workCenterName | Work Center | String | 37 | 280px | left |
| 14 | ownerUserName | Owner User | String | 14 | 120px | left |
| 15 | calibrationIntervalDays | Calibration Interval (days) | Int32 | 3 | 230px | right |
| 16 | calibrationSource | Calibration Source | String | 8 | 170px | left |
| 17 | calibrationSupplierName | Calibration Supplier | String | 44 | 300px | left |
| 18 | lastCalibratedAt | Last Calibrated At | Date/Datetime | 19 | 170px | center |
| 19 | nextCalibrationDueAt | Next Calibration Due At | Date/Date | 10 | 210px | center |
| 20 | lastGaugeCalibrationName | Last Gauge Calibration | String | 23 | 200px | left |
| 21 | usageCount | Usage Count | Int32 | 4 | 120px | right |
| 22 | purchasedAt | Purchased At | Date/Datetime | 19 | 160px | center |
| 23 | isMasterGauge | Master Gauge | Boolean | 3 | 130px | center |
| 24 | blockedForUse | Blocked for Use | Boolean | 3 | 150px | center |
| 25 | equipmentName | Equipment | String | 33 | 260px | left |
| 26 | status | Status | String | 19 | 160px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); gaugeTypeId (reference key, shown through gaugeTypeName); manufacturerId (reference key, shown through manufacturerName); rangeUnitOfMeasureId (reference key, shown through rangeUnitOfMeasureName); storageLocationId (reference key, shown through storageLocationName); workCenterId (reference key, shown through workCenterName); ownerUserId (reference key, shown through ownerUserName); calibrationSupplierId (reference key, shown through calibrationSupplierName); lastGaugeCalibrationId (reference key, shown through lastGaugeCalibrationName); equipmentId (reference key, shown through equipmentName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_gaugeCalibration - Gauge Calibrations (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_gaugeCalibration.json | _id: mes_qual_gaugeCalibrationStable | rel: CL20261018-23:51 | samples: 20 | columns: 25 | total width: 4580px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 23 | 190px | left |
| 2 | gaugeName | Gauge | String | 39 | 300px | left |
| 3 | calibrationType | Calibration Type | String | 12 | 160px | left |
| 4 | calibratedAt | Calibrated At | Date/Datetime | 19 | 160px | center |
| 5 | calibratedBy | Calibrated By | String | 14 | 140px | left |
| 6 | calibrationSupplierName | Calibration Supplier | String | 44 | 300px | left |
| 7 | masterStandardRef | Master Standard Ref | String | 64 | 300px | left |
| 8 | traceability | Traceability | String | 50 | 300px | left |
| 9 | temperatureC | Temperature C | Decimal128 | 4 | 140px | right |
| 10 | humidityPct | Humidity (%) | Decimal128 | 4 | 130px | right |
| 11 | asFoundResult | As Found Result | String | 16 | 150px | left |
| 12 | asLeftResult | As Left Result | String | 16 | 140px | left |
| 13 | overallResult | Overall Result | String | 4 | 140px | left |
| 14 | uncertainty | Uncertainty | Decimal128 | 6 | 120px | right |
| 15 | adjustmentMade | Adjustment Made | Boolean | 3 | 150px | center |
| 16 | certificateNo | Certificate No | String | 19 | 160px | left |
| 17 | certificateControlledDocumentName | Certificate Controlled Document | String | 78 | 300px | left |
| 18 | nextDueAt | Next Due At | Date/Date | 10 | 120px | center |
| 19 | impactAssessmentRequired | Impact Assessment Required | Boolean | 3 | 230px | center |
| 20 | remarks | Remarks | String | 48 | 300px | left |
| 21 | status | Status | String | 9 | 90px | left |
| 22 | createdBy | Created By | String | 14 | 120px | left |
| 23 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 24 | updatedBy | Updated By | String | 14 | 120px | left |
| 25 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); gaugeId (reference key, shown through gaugeName); calibratedById (reference key, shown through calibratedBy); calibrationSupplierId (reference key, shown through calibrationSupplierName); certificateControlledDocumentId (reference key, shown through certificateControlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_gaugeCalibrationReading - Gauge Calibration Readings (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_gaugeCalibrationReading.json | _id: mes_qual_gaugeCalibrationReadingStable | rel: CL20261018-23:51 | samples: 20 | columns: 12 | total width: 1630px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 27 | 210px | left |
| 2 | gaugeCalibrationName | Gauge Calibration | String | 23 | 190px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | nominal | Nominal | Decimal128 | 6 | 90px | right |
| 5 | asFound | As Found | Decimal128 | 6 | 100px | right |
| 6 | asLeft | As Left | Decimal128 | 5 | 90px | right |
| 7 | tolerance | Tolerance | Decimal128 | 5 | 110px | right |
| 8 | withinTolerance | Within Tolerance | Boolean | 3 | 160px | center |
| 9 | createdBy | Created By | String | 14 | 120px | left |
| 10 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 11 | updatedBy | Updated By | String | 14 | 120px | left |
| 12 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); gaugeCalibrationId (reference key, shown through gaugeCalibrationName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_gaugeType - Gauge Types (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_gaugeType.json | _id: mes_qual_gaugeTypeStable | rel: CL20261018-23:51 | samples: 20 | columns: 5 | total width: 830px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | name | Name | String | 28 | 220px | left |
| 3 | description | Description | String | 37 | 280px | left |
| 4 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 5 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_inspectionPlan - Inspection Plans (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_inspectionPlan.json | _id: mes_qual_inspectionPlanStable | rel: CL20261018-23:51 | samples: 20 | columns: 17 | total width: 3000px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 9 | 110px | left |
| 2 | name | Name | String | 54 | 300px | left |
| 3 | controlPlanName | Control Plan | String | 28 | 220px | left |
| 4 | itemName | Item | String | 61 | 300px | left |
| 5 | operationName | Operation | String | 31 | 240px | left |
| 6 | workCenterName | Work Center | String | 37 | 280px | left |
| 7 | planType | Plan Type | String | 10 | 110px | left |
| 8 | version | Version | Int32 | 1 | 90px | right |
| 9 | collectionTrigger | Collection Trigger | String | 15 | 170px | left |
| 10 | samplingPlanName | Sampling Plan | String | 46 | 300px | left |
| 11 | blockOnFail | Block on Fail | Boolean | 3 | 140px | center |
| 12 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 13 | effectiveTo | Effective to | Date/Date | 10 | 130px | center |
| 14 | approvedBy | Approved By | String | 0 | 120px | left |
| 15 | approvedAt | Approved At | Date/Datetime | 0 | 120px | center |
| 16 | itemRevision | Item Revision | String | 1 | 140px | left |
| 17 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); controlPlanId (reference key, shown through controlPlanName); itemId (reference key, shown through itemName); operationId (reference key, shown through operationName); workCenterId (reference key, shown through workCenterName); samplingPlanId (reference key, shown through samplingPlanName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): approvedBy, approvedAt

## u_mes_qual_inspectionPlanLine - Inspection Plan Lines (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_inspectionPlanLine.json | _id: mes_qual_inspectionPlanLineStable | rel: CL20261018-23:51 | samples: 20 | columns: 12 | total width: 2230px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | inspectionPlanName | Inspection Plan | String | 54 | 300px | left |
| 3 | lineNo | Line No | Int32 | 2 | 90px | right |
| 4 | characteristicName | Characteristic | String | 45 | 300px | left |
| 5 | gaugeName | Gauge | String | 39 | 300px | left |
| 6 | sampleSize | Sample Size | Int32 | 1 | 120px | right |
| 7 | frequencyType | Frequency Type | String | 13 | 140px | left |
| 8 | frequencyValue | Frequency Value | Decimal128 | 2 | 150px | right |
| 9 | recordType | Record Type | String | 14 | 120px | left |
| 10 | autoNcOnFail | Auto Nc on Fail | Boolean | 3 | 150px | center |
| 11 | defectCodeName | Defect Code | String | 36 | 280px | left |
| 12 | overrideAllowed | Override Allowed | Boolean | 3 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); inspectionPlanId (reference key, shown through inspectionPlanName); characteristicId (reference key, shown through characteristicName); gaugeId (reference key, shown through gaugeName); defectCodeId (reference key, shown through defectCodeName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_inspectionPlanProductVariant - Inspection Plan Variants (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_inspectionPlanProductVariant.json | _id: mes_qual_inspectionPlanProductVariantStable | rel: CL20261018-23:51 | samples: 20 | columns: 4 | total width: 840px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | inspectionPlanName | Inspection Plan | String | 53 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | productVariantName | Product Variant | String | 49 | 300px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); inspectionPlanId (reference key, shown through inspectionPlanName); productVariantId (reference key, shown through productVariantName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_inspectionResult - Inspection Results (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_inspectionResult.json | _id: mes_qual_inspectionResultStable | rel: CL20261019-12:24 | samples: 20 | columns: 43 | total width: 7260px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 14 | 120px | left |
| 2 | inspectionPlanName | Inspection Plan | String | 54 | 300px | left |
| 3 | planLineNo | Plan Line No | Int32 | 2 | 130px | right |
| 4 | characteristicName | Characteristic | String | 45 | 300px | left |
| 5 | itemName | Item | String | 61 | 300px | left |
| 6 | wipUnitName | WIP Unit | String | 20 | 160px | left |
| 7 | lotName | Lot | String | 15 | 130px | left |
| 8 | goodsReceiptName | Goods Receipt | String | 15 | 140px | left |
| 9 | operationExecutionName | Operation Execution | String | 15 | 180px | left |
| 10 | operationName | Operation | String | 31 | 240px | left |
| 11 | workCenterName | Work Center | String | 37 | 280px | left |
| 12 | inspectionType | Inspection Type | String | 10 | 150px | left |
| 13 | sampleNo | Sample No | Int32 | 1 | 110px | right |
| 14 | measuredValue | Measured Value | Decimal128 | 7 | 140px | right |
| 15 | attributeResult | Attribute Result | String | 0 | 160px | left |
| 16 | nominal | Nominal | Decimal128 | 6 | 90px | right |
| 17 | lowerSpecLimit | Lower Spec Limit | Decimal128 | 6 | 160px | right |
| 18 | upperSpecLimit | Upper Spec Limit | Decimal128 | 6 | 160px | right |
| 19 | unitOfMeasureName | Unit of Measure | String | 16 | 150px | left |
| 20 | deviation | Deviation | Decimal128 | 5 | 110px | right |
| 21 | result | Result | String | 6 | 90px | left |
| 22 | gaugeName | Gauge | String | 39 | 300px | left |
| 23 | measuredBy | Measured By | String | 14 | 120px | left |
| 24 | measuredAt | Measured At | Date/Datetime | 19 | 160px | center |
| 25 | source | Source | String | 12 | 110px | left |
| 26 | defectCodeName | Defect Code | String | 22 | 180px | left |
| 27 | nonconformanceName | Nonconformance | String | 52 | 300px | left |
| 28 | overridden | Overridden | Boolean | 3 | 110px | center |
| 29 | remarks | Remarks | String | 48 | 300px | left |
| 30 | positionNo | Position No | Int32 | 1 | 120px | right |
| 31 | positionName | Position Name | String | 22 | 180px | left |
| 32 | imageControlledDocumentName | Image Controlled Document | String | 0 | 220px | left |
| 33 | measurementCurveName | Measurement Curve | String | 18 | 160px | left |
| 34 | analyticsModelName | Analytics Model | String | 0 | 150px | left |
| 35 | modelVersion | Model Version | String | 0 | 140px | left |
| 36 | modelClass | Model Class | String | 0 | 120px | left |
| 37 | modelConfidence | Model Confidence | Decimal128 | 0 | 160px | right |
| 38 | sourceMessageUuid | Source Message Uuid | String | 0 | 180px | left |
| 39 | status | Status | String | 8 | 90px | left |
| 40 | createdBy | Created By | String | 14 | 120px | left |
| 41 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 42 | updatedBy | Updated By | String | 14 | 120px | left |
| 43 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); inspectionPlanId (reference key, shown through inspectionPlanName); characteristicId (reference key, shown through characteristicName); itemId (reference key, shown through itemName); wipUnitId (reference key, shown through wipUnitName); lotId (reference key, shown through lotName); goodsReceiptId (reference key, shown through goodsReceiptName); operationExecutionId (reference key, shown through operationExecutionName); operationId (reference key, shown through operationName); workCenterId (reference key, shown through workCenterName); unitOfMeasureId (reference key, shown through unitOfMeasureName); gaugeId (reference key, shown through gaugeName); measuredById (reference key, shown through measuredBy); defectCodeId (reference key, shown through defectCodeName); nonconformanceId (reference key, shown through nonconformanceName); imageControlledDocumentId (reference key, shown through imageControlledDocumentName); measurementCurveId (reference key, shown through measurementCurveName); analyticsModelId (reference key, shown through analyticsModelName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): attributeResult, imageControlledDocumentName, analyticsModelName, modelVersion, modelClass, modelConfidence, sourceMessageUuid

## u_mes_qual_measurementCurve - Measurement Curves (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_measurementCurve.json | _id: mes_qual_measurementCurveStable | rel: CL20261019-12:24 | samples: 20 | columns: 25 | total width: 3960px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | curveEnvelopeName | Curve Envelope | String | 54 | 300px | left |
| 3 | characteristicName | Characteristic | String | 29 | 230px | left |
| 4 | positionNo | Position No | Int32 | 1 | 120px | right |
| 5 | wipUnitName | WIP Unit | String | 20 | 160px | left |
| 6 | serialNumberName | Serial Number | String | 13 | 140px | left |
| 7 | operationExecutionName | Operation Execution | String | 15 | 180px | left |
| 8 | equipmentName | Equipment | String | 33 | 260px | left |
| 9 | recipeVersion | Recipe Version | String | 1 | 140px | left |
| 10 | capturedAt | Captured At | Date/Datetime | 19 | 160px | center |
| 11 | pointCount | Point Count | Int32 | 3 | 120px | right |
| 12 | peakX | Peak X | Decimal128 | 5 | 90px | right |
| 13 | peakY | Peak Y | Decimal128 | 4 | 90px | right |
| 14 | finalX | Final X | Decimal128 | 5 | 90px | right |
| 15 | finalY | Final Y | Decimal128 | 4 | 90px | right |
| 16 | result | Result | String | 3 | 90px | left |
| 17 | failedWindowNo | Failed Window No | Int32 | 1 | 160px | right |
| 18 | rawControlledDocumentName | Raw Controlled Document | String | 44 | 300px | left |
| 19 | inspectionResultName | Inspection Result | String | 14 | 160px | left |
| 20 | sourceMessageUuid | Source Message Uuid | String | 36 | 280px | left |
| 21 | status | Status | String | 8 | 90px | left |
| 22 | createdBy | Created By | String | 14 | 120px | left |
| 23 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 24 | updatedBy | Updated By | String | 14 | 120px | left |
| 25 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); curveEnvelopeId (reference key, shown through curveEnvelopeName); characteristicId (reference key, shown through characteristicName); wipUnitId (reference key, shown through wipUnitName); serialNumberId (reference key, shown through serialNumberName); operationExecutionId (reference key, shown through operationExecutionName); equipmentId (reference key, shown through equipmentName); rawControlledDocumentId (reference key, shown through rawControlledDocumentName); inspectionResultId (reference key, shown through inspectionResultName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_measurementCurvePoint - Measurement Curve Points (Telemetry)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_measurementCurvePoint.json | _id: mes_qual_measurementCurvePointStable | rel: CL20261018-23:51 | samples: 10 | columns: 10 | total width: 1350px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 23 | 190px | left |
| 2 | measurementCurveName | Measurement Curve | String | 18 | 160px | left |
| 3 | pointNo | Point No | Int32 | 3 | 100px | right |
| 4 | sampledAt | Sampled At | Date/Datetime | 19 | 160px | center |
| 5 | xValue | X Value | Decimal128 | 4 | 90px | right |
| 6 | yValue | Y Value | Decimal128 | 4 | 90px | right |
| 7 | createdBy | Created By | String | 14 | 120px | left |
| 8 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 9 | updatedBy | Updated By | String | 14 | 120px | left |
| 10 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); measurementCurveId (reference key, shown through measurementCurveName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_msaStudy - MSA Studies (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_msaStudy.json | _id: mes_qual_msaStudyStable | rel: CL20261018-23:51 | samples: 10 | columns: 30 | total width: 5090px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 13 | 120px | left |
| 2 | gaugeName | Gauge | String | 37 | 280px | left |
| 3 | characteristicName | Characteristic | String | 32 | 250px | left |
| 4 | itemName | Item | String | 39 | 300px | left |
| 5 | studyType | Study Type | String | 19 | 160px | left |
| 6 | studyMethod | Study Method | String | 5 | 130px | left |
| 7 | studyDate | Study Date | Date/Date | 10 | 110px | center |
| 8 | partsCount | Parts Count | Int32 | 2 | 120px | right |
| 9 | trialsCount | Trials Count | Int32 | 1 | 130px | right |
| 10 | resultsEquipmentVariation | Results Equipment Variation | Decimal128 | 6 | 230px | right |
| 11 | resultsAppraiserVariation | Results Appraiser Variation | Decimal128 | 6 | 230px | right |
| 12 | resultsGrr | Results GRR | Decimal128 | 6 | 120px | right |
| 13 | resultsPartVariation | Results Part Variation | Decimal128 | 6 | 200px | right |
| 14 | resultsTotalVariation | Results Total Variation | Decimal128 | 6 | 210px | right |
| 15 | resultsGrrPctTolerance | Results GRR Pct Tolerance | Decimal128 | 3 | 220px | right |
| 16 | resultsGrrPctStudyVariation | Results GRR Pct Study Variation | Decimal128 | 3 | 260px | right |
| 17 | resultsNdc | Results Ndc | Decimal128 | 2 | 120px | right |
| 18 | resultsBiasValue | Results Bias Value | Decimal128 | 0 | 170px | right |
| 19 | resultsKappa | Results Kappa | Decimal128 | 0 | 140px | right |
| 20 | conclusion | Conclusion | String | 24 | 190px | left |
| 21 | actionRequired | Action Required | Boolean | 3 | 150px | center |
| 22 | conductedBy | Conducted By | String | 14 | 130px | left |
| 23 | approvedBy | Approved By | String | 15 | 130px | left |
| 24 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 25 | nextStudyDueAt | Next Study Due At | Date/Date | 10 | 160px | center |
| 26 | status | Status | String | 12 | 110px | left |
| 27 | createdBy | Created By | String | 14 | 120px | left |
| 28 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 29 | updatedBy | Updated By | String | 14 | 120px | left |
| 30 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); gaugeId (reference key, shown through gaugeName); characteristicId (reference key, shown through characteristicName); itemId (reference key, shown through itemName); conductedById (reference key, shown through conductedBy); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): resultsBiasValue, resultsKappa

## u_mes_qual_msaStudyAppraiserUser - MSA Study Appraisers (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_msaStudyAppraiserUser.json | _id: mes_qual_msaStudyAppraiserUserStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1090px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 18 | 150px | left |
| 2 | msaStudyName | MSA Study | String | 13 | 120px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | appraiserUserName | Appraiser User | String | 14 | 140px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); msaStudyId (reference key, shown through msaStudyName); appraiserUserId (reference key, shown through appraiserUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_msaStudyTrial - MSA Study Trials (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_msaStudyTrial.json | _id: mes_qual_msaStudyTrialStable | rel: CL20261018-23:51 | samples: 10 | columns: 10 | total width: 1290px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | msaStudyName | MSA Study | String | 13 | 120px | left |
| 3 | appraiserUserName | Appraiser User | String | 14 | 140px | left |
| 4 | partNo | Part No | Int32 | 1 | 90px | right |
| 5 | trialNo | Trial No | Int32 | 2 | 100px | right |
| 6 | measuredValue | Measured Value | Decimal128 | 4 | 140px | right |
| 7 | createdBy | Created By | String | 14 | 120px | left |
| 8 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 9 | updatedBy | Updated By | String | 14 | 120px | left |
| 10 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); msaStudyId (reference key, shown through msaStudyName); appraiserUserId (reference key, shown through appraiserUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_nonconformance - Nonconformances (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_nonconformance.json | _id: mes_qual_nonconformanceStable | rel: CL20261018-23:51 | samples: 20 | columns: 34 | total width: 6500px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | title | Title | String | 58 | 300px | left |
| 3 | description | Description | String | 132 | 300px | left |
| 4 | ncType | Nc Type | String | 8 | 90px | left |
| 5 | source | Source | String | 12 | 110px | left |
| 6 | detectedAt | Detected At | Date/Datetime | 19 | 160px | center |
| 7 | detectedBy | Detected By | String | 14 | 120px | left |
| 8 | detectedAtOperationName | Detected At Operation | String | 31 | 240px | left |
| 9 | detectedAtWorkCenterName | Detected At Work Center | String | 37 | 280px | left |
| 10 | originOperationName | Origin Operation | String | 31 | 240px | left |
| 11 | itemName | Item | String | 61 | 300px | left |
| 12 | defectCodeName | Defect Code | String | 36 | 280px | left |
| 13 | supplierName | Supplier | String | 36 | 280px | left |
| 14 | customerName | Customer | String | 24 | 190px | left |
| 15 | quantityAffected | Quantity Affected | Int32 | 3 | 160px | right |
| 16 | quantityRejected | Quantity Rejected | Int32 | 2 | 160px | right |
| 17 | qualityHoldName | Quality Hold | String | 15 | 130px | left |
| 18 | capaName | CAPA | String | 47 | 300px | left |
| 19 | rootCauseSummary | Root Cause Summary | String | 74 | 300px | left |
| 20 | severity | Severity | Int32 | 2 | 100px | right |
| 21 | costInr | Cost (INR) | Decimal128 | 7 | 110px | right |
| 22 | closedAt | Closed At | Date/Datetime | 19 | 160px | center |
| 23 | closedBy | Closed By | String | 15 | 130px | left |
| 24 | deviationClass | Deviation Class | String | 8 | 150px | left |
| 25 | productImpactText | Product Impact Text | String | 98 | 300px | left |
| 26 | investigationDueDate | Investigation Due Date | Date/Date | 10 | 200px | center |
| 27 | qaApprovedBy | Qa Approved By | String | 14 | 140px | left |
| 28 | qaApprovedAt | Qa Approved At | Date/Datetime | 19 | 160px | center |
| 29 | riskAssessmentName | Risk Assessment | String | 71 | 300px | left |
| 30 | status | Status | String | 13 | 120px | left |
| 31 | createdBy | Created By | String | 14 | 120px | left |
| 32 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 33 | updatedBy | Updated By | String | 14 | 120px | left |
| 34 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); detectedById (reference key, shown through detectedBy); detectedAtOperationId (reference key, shown through detectedAtOperationName); detectedAtWorkCenterId (reference key, shown through detectedAtWorkCenterName); originOperationId (reference key, shown through originOperationName); itemId (reference key, shown through itemName); defectCodeId (reference key, shown through defectCodeName); supplierId (reference key, shown through supplierName); customerId (reference key, shown through customerName); qualityHoldId (reference key, shown through qualityHoldName); capaId (reference key, shown through capaName); closedById (reference key, shown through closedBy); qaApprovedById (reference key, shown through qaApprovedBy); riskAssessmentId (reference key, shown through riskAssessmentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_nonconformanceAffectedObject - Nonconformance Affected Objects (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_nonconformanceAffectedObject.json | _id: mes_qual_nonconformanceAffectedObjectStable | rel: CL20261018-23:51 | samples: 10 | columns: 13 | total width: 2050px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | nonconformanceName | Nonconformance | String | 55 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | relatedCollectionName | Related Collection Name | String | 18 | 210px | left |
| 5 | relatedEntityName | Related Entity | String | 12 | 140px | left |
| 6 | quantity | Quantity | Int32 | 1 | 100px | right |
| 7 | dispositionTypeName | Disposition Type | String | 19 | 160px | left |
| 8 | dispositionBy | Disposition By | String | 14 | 140px | left |
| 9 | dispositionAt | Disposition At | Date/Datetime | 19 | 160px | center |
| 10 | createdBy | Created By | String | 14 | 120px | left |
| 11 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 12 | updatedBy | Updated By | String | 14 | 120px | left |
| 13 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); nonconformanceId (reference key, shown through nonconformanceName); relatedEntityId (reference key, shown through relatedEntityName); dispositionTypeId (reference key, shown through dispositionTypeName); dispositionById (reference key, shown through dispositionBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_nonconformanceContainmentAction - Nonconformance Containment Actions (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_nonconformanceContainmentAction.json | _id: mes_qual_nonconformanceContainmentActionStable | rel: CL20261018-23:51 | samples: 10 | columns: 10 | total width: 1710px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | nonconformanceName | Nonconformance | String | 55 | 300px | left |
| 3 | actionNo | Action No | Int32 | 1 | 110px | right |
| 4 | description | Description | String | 69 | 300px | left |
| 5 | ownerUserName | Owner User | String | 14 | 120px | left |
| 6 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 7 | createdBy | Created By | String | 14 | 120px | left |
| 8 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 9 | updatedBy | Updated By | String | 14 | 120px | left |
| 10 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); nonconformanceId (reference key, shown through nonconformanceName); ownerUserId (reference key, shown through ownerUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_nonconformanceInspectionResult - Nonconformance Inspection Results (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_nonconformanceInspectionResult.json | _id: mes_qual_nonconformanceInspectionResultStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1300px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | nonconformanceName | Nonconformance | String | 55 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | inspectionResultName | Inspection Result | String | 14 | 160px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); nonconformanceId (reference key, shown through nonconformanceName); inspectionResultId (reference key, shown through inspectionResultName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_nonconformanceMrbUser - Nonconformance MRB Members (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_nonconformanceMrbUser.json | _id: mes_qual_nonconformanceMrbUserStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1270px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | nonconformanceName | Nonconformance | String | 55 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | mrbUserName | Mrb User | String | 15 | 130px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); nonconformanceId (reference key, shown through nonconformanceName); mrbUserId (reference key, shown through mrbUserName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_nonconformancePhotoControlledDocument - Nonconformance Photos (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_nonconformancePhotoControlledDocument.json | _id: mes_qual_nonconformancePhotoControlledDocumentStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1450px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 21 | 170px | left |
| 2 | nonconformanceName | Nonconformance | String | 55 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | photoControlledDocumentName | Photo Controlled Document | String | 64 | 300px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); nonconformanceId (reference key, shown through nonconformanceName); photoControlledDocumentId (reference key, shown through photoControlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_nonconformanceReworkOrder - Nonconformance Rework Orders (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_nonconformanceReworkOrder.json | _id: mes_qual_nonconformanceReworkOrderStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1270px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | nonconformanceName | Nonconformance | String | 55 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | reworkOrderName | Rework Order | String | 15 | 130px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); nonconformanceId (reference key, shown through nonconformanceName); reworkOrderId (reference key, shown through reworkOrderName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_nonconformanceScrapRecord - Nonconformance Scrap Records (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_nonconformanceScrapRecord.json | _id: mes_qual_nonconformanceScrapRecordStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1270px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | nonconformanceName | Nonconformance | String | 55 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | scrapRecordName | Scrap Record | String | 15 | 130px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); nonconformanceId (reference key, shown through nonconformanceName); scrapRecordId (reference key, shown through scrapRecordName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_pfmea - Process FMEAs (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_pfmea.json | _id: mes_qual_pfmeaStable | rel: CL20261018-23:51 | samples: 20 | columns: 12 | total width: 1950px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 21 | 170px | left |
| 2 | title | Title | String | 78 | 300px | left |
| 3 | itemName | Item | String | 61 | 300px | left |
| 4 | itemRevision | Item Revision | String | 1 | 140px | left |
| 5 | version | Version | Int32 | 1 | 90px | right |
| 6 | methodology | Methodology | String | 8 | 120px | left |
| 7 | controlPlanName | Control Plan | String | 28 | 220px | left |
| 8 | originalDate | Original Date | Date/Date | 10 | 140px | center |
| 9 | revisionDate | Revision Date | Date/Date | 10 | 140px | center |
| 10 | approvedBy | Approved By | String | 0 | 120px | left |
| 11 | approvedAt | Approved At | Date/Datetime | 0 | 120px | center |
| 12 | status | Status | String | 8 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); controlPlanId (reference key, shown through controlPlanName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): approvedBy, approvedAt

## u_mes_qual_pfmeaCoreTeamUser - PFMEA Core Team (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_pfmeaCoreTeamUser.json | _id: mes_qual_pfmeaCoreTeamUserStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 760px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 25 | 200px | left |
| 2 | pfmeaName | PFMEA | String | 69 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | coreTeamUserName | Core Team User | String | 14 | 140px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); pfmeaId (reference key, shown through pfmeaName); coreTeamUserId (reference key, shown through coreTeamUserName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_pfmeaLine - PFMEA Lines (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_pfmeaLine.json | _id: mes_qual_pfmeaLineStable | rel: CL20261018-23:51 | samples: 10 | columns: 24 | total width: 4840px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 23 | 190px | left |
| 2 | pfmeaName | PFMEA | String | 52 | 300px | left |
| 3 | lineNo | Line No | Int32 | 3 | 90px | right |
| 4 | operationName | Operation | String | 24 | 190px | left |
| 5 | processFunction | Process Function | String | 50 | 300px | left |
| 6 | failureMode | Failure Mode | String | 40 | 300px | left |
| 7 | failureEffect | Failure Effect | String | 60 | 300px | left |
| 8 | severity | Severity | Int32 | 2 | 100px | right |
| 9 | characteristicName | Characteristic | String | 32 | 250px | left |
| 10 | classification | Classification | String | 11 | 140px | left |
| 11 | failureCause | Failure Cause | String | 42 | 300px | left |
| 12 | preventionControl | Prevention Control | String | 57 | 300px | left |
| 13 | occurrence | Occurrence | Int32 | 1 | 110px | right |
| 14 | detectionControl | Detection Control | String | 57 | 300px | left |
| 15 | detection | Detection | Int32 | 1 | 110px | right |
| 16 | rpn | RPN | Int32 | 3 | 80px | right |
| 17 | actionPriority | Action Priority | String | 6 | 150px | left |
| 18 | recommendedAction | Recommended Action | String | 44 | 300px | left |
| 19 | ownerUserName | Owner User | String | 14 | 120px | left |
| 20 | targetDate | Target Date | Date/Date | 10 | 120px | center |
| 21 | actionTaken | Action Taken | String | 69 | 300px | left |
| 22 | revisedSeverity | Revised Severity | Int32 | 2 | 160px | right |
| 23 | revisedOccurrence | Revised Occurrence | Int32 | 1 | 170px | right |
| 24 | revisedDetection | Revised Detection | Int32 | 1 | 160px | right |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); pfmeaId (reference key, shown through pfmeaName); operationId (reference key, shown through operationName); characteristicId (reference key, shown through characteristicName); ownerUserId (reference key, shown through ownerUserName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_ppapSubmission - PPAP Submissions (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_ppapSubmission.json | _id: mes_qual_ppapSubmissionStable | rel: CL20261018-23:51 | samples: 10 | columns: 23 | total width: 4300px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | itemName | Item | String | 39 | 300px | left |
| 3 | itemRevision | Item Revision | String | 1 | 140px | left |
| 4 | customerName | Customer | String | 23 | 190px | left |
| 5 | engineeringChangeName | Engineering Change | String | 57 | 300px | left |
| 6 | submissionLevel | Submission Level | Int32 | 1 | 160px | right |
| 7 | submissionReason | Submission Reason | String | 25 | 200px | left |
| 8 | controlPlanName | Control Plan | String | 27 | 210px | left |
| 9 | pfmeaName | PFMEA | String | 69 | 300px | left |
| 10 | sampleQuantity | Sample Quantity | Int32 | 1 | 150px | right |
| 11 | significantProductionRunQuantity | Significant Production Run Quantity | Int32 | 3 | 290px | right |
| 12 | pswSignedBy | Psw Signed By | String | 15 | 140px | left |
| 13 | pswSignedAt | Psw Signed At | Date/Datetime | 19 | 160px | center |
| 14 | submittedAt | Submitted At | Date/Datetime | 19 | 160px | center |
| 15 | customerDecision | Customer Decision | String | 0 | 160px | left |
| 16 | customerDecisionAt | Customer Decision At | Date/Datetime | 19 | 180px | center |
| 17 | customerRemarks | Customer Remarks | String | 0 | 160px | left |
| 18 | interimApprovalValidTo | Interim Approval Valid to | Date/Date | 0 | 220px | center |
| 19 | status | Status | String | 16 | 140px | left |
| 20 | createdBy | Created By | String | 14 | 120px | left |
| 21 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 22 | updatedBy | Updated By | String | 14 | 120px | left |
| 23 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); customerId (reference key, shown through customerName); engineeringChangeId (reference key, shown through engineeringChangeName); controlPlanId (reference key, shown through controlPlanName); pfmeaId (reference key, shown through pfmeaName); pswSignedById (reference key, shown through pswSignedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): customerDecision, customerRemarks, interimApprovalValidTo

## u_mes_qual_ppapSubmissionElement - PPAP Submission Elements (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_ppapSubmissionElement.json | _id: mes_qual_ppapSubmissionElementStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1860px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 26 | 210px | left |
| 2 | ppapSubmissionName | Ppap Submission | String | 22 | 180px | left |
| 3 | elementNo | Element No | Int32 | 2 | 110px | right |
| 4 | name | Name | String | 37 | 280px | left |
| 5 | required | Required | Boolean | 3 | 100px | center |
| 6 | status | Status | String | 14 | 120px | left |
| 7 | controlledDocumentName | Controlled Document | String | 64 | 300px | left |
| 8 | createdBy | Created By | String | 14 | 120px | left |
| 9 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 10 | updatedBy | Updated By | String | 14 | 120px | left |
| 11 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); ppapSubmissionId (reference key, shown through ppapSubmissionName); controlledDocumentId (reference key, shown through controlledDocumentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_ppapSubmissionMsaStudy - PPAP Submission MSA Studies (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_ppapSubmissionMsaStudy.json | _id: mes_qual_ppapSubmissionMsaStudyStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1190px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 27 | 210px | left |
| 2 | ppapSubmissionName | Ppap Submission | String | 22 | 180px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | msaStudyName | MSA Study | String | 13 | 120px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); ppapSubmissionId (reference key, shown through ppapSubmissionName); msaStudyId (reference key, shown through msaStudyName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_processValidation - Process Validations (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_processValidation.json | _id: mes_qual_processValidationStable | rel: CL20261018-23:51 | samples: 10 | columns: 22 | total width: 4300px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | title | Title | String | 78 | 300px | left |
| 3 | itemName | Item | String | 61 | 300px | left |
| 4 | lineName | Line | String | 22 | 180px | left |
| 5 | validationStage | Validation Stage | String | 38 | 290px | left |
| 6 | engineeringChangeName | Engineering Change | String | 57 | 300px | left |
| 7 | protocolControlledDocumentName | Protocol Controlled Document | String | 0 | 240px | left |
| 8 | reportControlledDocumentName | Report Controlled Document | String | 0 | 230px | left |
| 9 | plannedLotCount | Planned Lot Count | Int32 | 2 | 160px | right |
| 10 | executedLotCount | Executed Lot Count | Int32 | 2 | 170px | right |
| 11 | acceptanceCriteriaText | Acceptance Criteria Text | String | 150 | 300px | left |
| 12 | resultText | Result Text | String | 91 | 300px | left |
| 13 | plannedStartDate | Planned Start Date | Date/Date | 10 | 170px | center |
| 14 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 15 | approvedBy | Approved By | String | 11 | 120px | left |
| 16 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 17 | nextReviewDate | Next Review Date | Date/Date | 10 | 160px | center |
| 18 | status | Status | String | 12 | 110px | left |
| 19 | createdBy | Created By | String | 11 | 110px | left |
| 20 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 21 | updatedBy | Updated By | String | 11 | 110px | left |
| 22 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); lineId (reference key, shown through lineName); engineeringChangeId (reference key, shown through engineeringChangeName); protocolControlledDocumentId (reference key, shown through protocolControlledDocumentName); reportControlledDocumentId (reference key, shown through reportControlledDocumentName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): protocolControlledDocumentName, reportControlledDocumentName

## u_mes_qual_productQualityReview - Product Quality Reviews (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_productQualityReview.json | _id: mes_qual_productQualityReviewStable | rel: CL20261018-23:51 | samples: 10 | columns: 24 | total width: 4610px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 26 | 210px | left |
| 2 | itemName | Item | String | 61 | 300px | left |
| 3 | reviewPeriodFromDate | Review Period From Date | Date/Date | 10 | 210px | center |
| 4 | reviewPeriodToDate | Review Period to Date | Date/Date | 10 | 190px | center |
| 5 | lotsProducedCount | Lots Produced Count | Int32 | 2 | 180px | right |
| 6 | lotsReleasedCount | Lots Released Count | Int32 | 2 | 180px | right |
| 7 | lotsRejectedCount | Lots Rejected Count | Int32 | 1 | 180px | right |
| 8 | nonconformanceCount | Nonconformance Count | Int32 | 1 | 180px | right |
| 9 | deviationPermitCount | Deviation Permit Count | Int32 | 1 | 200px | right |
| 10 | customerComplaintCount | Customer Complaint Count | Int32 | 1 | 210px | right |
| 11 | capaCount | CAPA Count | Int32 | 1 | 110px | right |
| 12 | engineeringChangeCount | Engineering Change Count | Int32 | 1 | 210px | right |
| 13 | productRecallCount | Product Recall Count | Int32 | 1 | 180px | right |
| 14 | processCapabilityText | Process Capability Text | String | 76 | 300px | left |
| 15 | conclusionText | Conclusion Text | String | 96 | 300px | left |
| 16 | actionsText | Actions Text | String | 40 | 300px | left |
| 17 | reportControlledDocumentName | Report Controlled Document | String | 0 | 230px | left |
| 18 | approvedBy | Approved By | String | 12 | 120px | left |
| 19 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 20 | status | Status | String | 14 | 120px | left |
| 21 | createdBy | Created By | String | 11 | 110px | left |
| 22 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 23 | updatedBy | Updated By | String | 11 | 110px | left |
| 24 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); reportControlledDocumentId (reference key, shown through reportControlledDocumentName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): reportControlledDocumentName

## u_mes_qual_productRecall - Product Recalls (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_productRecall.json | _id: mes_qual_productRecallStable | rel: CL20261018-23:51 | samples: 10 | columns: 24 | total width: 4610px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | title | Title | String | 94 | 300px | left |
| 3 | recallClass | Recall Class | String | 9 | 130px | left |
| 4 | recallScope | Recall Scope | String | 11 | 130px | left |
| 5 | reasonText | Reason Text | String | 77 | 300px | left |
| 6 | customerName | Customer | String | 42 | 300px | left |
| 7 | customerComplaintName | Customer Complaint | String | 60 | 300px | left |
| 8 | nonconformanceName | Nonconformance | String | 57 | 300px | left |
| 9 | traceInvestigationName | Trace Investigation | String | 72 | 300px | left |
| 10 | capaName | CAPA | String | 40 | 300px | left |
| 11 | initiatedBy | Initiated By | String | 12 | 130px | left |
| 12 | initiatedAt | Initiated At | Date/Datetime | 19 | 160px | center |
| 13 | authorityNotified | Authority Notified | Boolean | 3 | 170px | center |
| 14 | authorityNotifiedAt | Authority Notified At | Date/Datetime | 19 | 190px | center |
| 15 | quantityShipped | Quantity Shipped | Int32 | 4 | 160px | right |
| 16 | quantityRecovered | Quantity Recovered | Int32 | 4 | 170px | right |
| 17 | effectivenessCheckCompleted | Effectiveness Check Completed | Boolean | 3 | 250px | center |
| 18 | closedBy | Closed By | String | 12 | 110px | left |
| 19 | closedAt | Closed At | Date/Datetime | 19 | 160px | center |
| 20 | status | Status | String | 11 | 100px | left |
| 21 | createdBy | Created By | String | 11 | 110px | left |
| 22 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 23 | updatedBy | Updated By | String | 11 | 110px | left |
| 24 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); customerId (reference key, shown through customerName); customerComplaintId (reference key, shown through customerComplaintName); nonconformanceId (reference key, shown through nonconformanceName); traceInvestigationId (reference key, shown through traceInvestigationName); capaId (reference key, shown through capaName); initiatedById (reference key, shown through initiatedBy); closedById (reference key, shown through closedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_productRecallLot - Recall Lots (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_productRecallLot.json | _id: mes_qual_productRecallLotStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1650px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | productRecallName | Product Recall | String | 94 | 300px | left |
| 3 | lineNo | Line No | Int32 | 2 | 90px | right |
| 4 | lotName | Lot | String | 13 | 120px | left |
| 5 | shipmentName | Shipment | String | 15 | 130px | left |
| 6 | quantityShipped | Quantity Shipped | Int32 | 4 | 160px | right |
| 7 | quantityRecovered | Quantity Recovered | Int32 | 4 | 170px | right |
| 8 | createdBy | Created By | String | 11 | 110px | left |
| 9 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 10 | updatedBy | Updated By | String | 11 | 110px | left |
| 11 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); productRecallId (reference key, shown through productRecallName); lotId (reference key, shown through lotName); shipmentId (reference key, shown through shipmentName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_qualityHold - Quality Holds (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_qualityHold.json | _id: mes_qual_qualityHoldStable | rel: CL20261018-23:51 | samples: 20 | columns: 23 | total width: 4300px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | holdType | Hold Type | String | 11 | 110px | left |
| 3 | reasonText | Reason Text | String | 102 | 300px | left |
| 4 | reasonCodeName | Reason Code | String | 27 | 210px | left |
| 5 | nonconformanceName | Nonconformance | String | 58 | 300px | left |
| 6 | itemName | Item | String | 61 | 300px | left |
| 7 | totalQuantity | Total Quantity | Int32 | 3 | 140px | right |
| 8 | quarantineLocationName | Quarantine Location | String | 36 | 280px | left |
| 9 | placedBy | Placed By | String | 14 | 120px | left |
| 10 | placedAt | Placed At | Date/Datetime | 19 | 160px | center |
| 11 | expectedReleaseAt | Expected Release At | Date/Datetime | 19 | 180px | center |
| 12 | releasedBy | Released By | String | 15 | 130px | left |
| 13 | releasedAt | Released At | Date/Datetime | 19 | 160px | center |
| 14 | releaseDecision | Release Decision | String | 8 | 160px | left |
| 15 | releaseComment | Release Comment | String | 62 | 300px | left |
| 16 | customerNotified | Customer Notified | Boolean | 3 | 160px | center |
| 17 | releaseReasonCodeName | Release Reason Code | String | 27 | 210px | left |
| 18 | releaseElectronicSignatureName | Release Electronic Signature | String | 0 | 240px | left |
| 19 | status | Status | String | 18 | 150px | left |
| 20 | createdBy | Created By | String | 14 | 120px | left |
| 21 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 22 | updatedBy | Updated By | String | 14 | 120px | left |
| 23 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); reasonCodeId (reference key, shown through reasonCodeName); nonconformanceId (reference key, shown through nonconformanceName); itemId (reference key, shown through itemName); quarantineLocationId (reference key, shown through quarantineLocationName); placedById (reference key, shown through placedBy); releasedById (reference key, shown through releasedBy); releaseReasonCodeId (reference key, shown through releaseReasonCodeName); releaseElectronicSignatureId (reference key, shown through releaseElectronicSignatureName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): releaseElectronicSignatureName

## u_mes_qual_qualityHoldHeldObject - Quality Hold Held Objects (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_qualityHoldHeldObject.json | _id: mes_qual_qualityHoldHeldObjectStable | rel: CL20261018-23:51 | samples: 10 | columns: 12 | total width: 1740px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | qualityHoldName | Quality Hold | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | relatedCollectionName | Related Collection Name | String | 14 | 210px | left |
| 5 | relatedEntityName | Related Entity | String | 15 | 140px | left |
| 6 | quantity | Quantity | Int32 | 1 | 100px | right |
| 7 | releasedAt | Released At | Date/Datetime | 19 | 160px | center |
| 8 | releaseDecision | Release Decision | String | 0 | 160px | left |
| 9 | createdBy | Created By | String | 14 | 120px | left |
| 10 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 11 | updatedBy | Updated By | String | 14 | 120px | left |
| 12 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); qualityHoldId (reference key, shown through qualityHoldName); relatedEntityId (reference key, shown through relatedEntityName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): releaseDecision

## u_mes_qual_retentionSample - Retention Samples (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_retentionSample.json | _id: mes_qual_retentionSampleStable | rel: CL20261018-23:51 | samples: 10 | columns: 20 | total width: 3470px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 22 | 180px | left |
| 2 | itemName | Item | String | 61 | 300px | left |
| 3 | lotName | Lot | String | 15 | 130px | left |
| 4 | productionOrderName | Production Order | String | 10 | 160px | left |
| 5 | serialNumberName | Serial Number | String | 13 | 140px | left |
| 6 | sampleType | Sample Type | String | 16 | 140px | left |
| 7 | sampleQuantity | Sample Quantity | Int32 | 3 | 150px | right |
| 8 | unitOfMeasureName | Unit of Measure | String | 8 | 150px | left |
| 9 | storageLocationName | Storage Location | String | 36 | 280px | left |
| 10 | collectedBy | Collected By | String | 11 | 130px | left |
| 11 | collectedAt | Collected At | Date/Datetime | 19 | 160px | center |
| 12 | retainUntilDate | Retain Until Date | Date/Date | 10 | 160px | center |
| 13 | withdrawnAt | Withdrawn At | Date/Datetime | 19 | 160px | center |
| 14 | withdrawalReason | Withdrawal Reason | String | 87 | 300px | left |
| 15 | customerComplaintName | Customer Complaint | String | 49 | 300px | left |
| 16 | status | Status | String | 9 | 90px | left |
| 17 | createdBy | Created By | String | 11 | 110px | left |
| 18 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 19 | updatedBy | Updated By | String | 11 | 110px | left |
| 20 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); itemId (reference key, shown through itemName); lotId (reference key, shown through lotName); productionOrderId (reference key, shown through productionOrderName); serialNumberId (reference key, shown through serialNumberName); unitOfMeasureId (reference key, shown through unitOfMeasureName); storageLocationId (reference key, shown through storageLocationName); collectedById (reference key, shown through collectedBy); customerComplaintId (reference key, shown through customerComplaintName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_reworkOrder - Rework Orders (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_reworkOrder.json | _id: mes_qual_reworkOrderStable | rel: CL20261018-23:51 | samples: 20 | columns: 29 | total width: 4980px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | nonconformanceName | Nonconformance | String | 57 | 300px | left |
| 3 | lotName | Lot | String | 0 | 80px | left |
| 4 | itemName | Item | String | 49 | 300px | left |
| 5 | quantity | Quantity | Int32 | 1 | 100px | right |
| 6 | reworkRoutingName | Rework Routing | String | 64 | 300px | left |
| 7 | reworkType | Rework Type | String | 17 | 140px | left |
| 8 | instruction | Instruction | String | 121 | 300px | left |
| 9 | workCenterName | Work Center | String | 37 | 280px | left |
| 10 | issuedBy | Issued By | String | 13 | 120px | left |
| 11 | issuedAt | Issued At | Date/Datetime | 19 | 160px | center |
| 12 | startedAt | Started At | Date/Datetime | 19 | 160px | center |
| 13 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 14 | reinspectionResult | Reinspection Result | String | 0 | 180px | left |
| 15 | reinspectedBy | Reinspected By | String | 14 | 140px | left |
| 16 | reinspectedAt | Reinspected At | Date/Datetime | 19 | 160px | center |
| 17 | quantityRecovered | Quantity Recovered | Int32 | 1 | 170px | right |
| 18 | quantityScrapped | Quantity Scrapped | Int32 | 1 | 160px | right |
| 19 | reworkAttemptNo | Rework Attempt No | Int32 | 1 | 160px | right |
| 20 | returnStepNo | Return Step No | Int32 | 3 | 140px | right |
| 21 | labourMinutes | Labour (min) | Int32 | 2 | 130px | right |
| 22 | reasonCodeName | Reason Code | String | 25 | 200px | left |
| 23 | releasedBy | Released By | String | 14 | 120px | left |
| 24 | releasedAt | Released At | Date/Datetime | 19 | 160px | center |
| 25 | status | Status | String | 21 | 170px | left |
| 26 | createdBy | Created By | String | 14 | 120px | left |
| 27 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 28 | updatedBy | Updated By | String | 14 | 120px | left |
| 29 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); nonconformanceId (reference key, shown through nonconformanceName); lotId (reference key, shown through lotName); itemId (reference key, shown through itemName); reworkRoutingId (reference key, shown through reworkRoutingName); workCenterId (reference key, shown through workCenterName); issuedById (reference key, shown through issuedBy); reinspectedById (reference key, shown through reinspectedBy); reasonCodeId (reference key, shown through reasonCodeName); releasedById (reference key, shown through releasedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): lotName, reinspectionResult

## u_mes_qual_reworkOrderStep - Rework Order Steps (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_reworkOrderStep.json | _id: mes_qual_reworkOrderStepStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1680px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | reworkOrderName | Rework Order | String | 15 | 130px | left |
| 3 | stepNo | Step No | Int32 | 2 | 90px | right |
| 4 | operationName | Operation | String | 18 | 150px | left |
| 5 | description | Description | String | 90 | 300px | left |
| 6 | completedAt | Completed At | Date/Datetime | 19 | 160px | center |
| 7 | completedBy | Completed By | String | 14 | 130px | left |
| 8 | createdBy | Created By | String | 14 | 120px | left |
| 9 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 10 | updatedBy | Updated By | String | 14 | 120px | left |
| 11 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); reworkOrderId (reference key, shown through reworkOrderName); operationId (reference key, shown through operationName); completedById (reference key, shown through completedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_reworkOrderWipUnit - Rework Order WIP Units (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_reworkOrderWipUnit.json | _id: mes_qual_reworkOrderWipUnitStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1080px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | reworkOrderName | Rework Order | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | wipUnitName | WIP Unit | String | 12 | 110px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); reworkOrderId (reference key, shown through reworkOrderName); wipUnitId (reference key, shown through wipUnitName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_riskAssessment - Quality Risk Assessments (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_riskAssessment.json | _id: mes_qual_riskAssessmentStable | rel: CL20261018-23:51 | samples: 10 | columns: 19 | total width: 3680px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | title | Title | String | 88 | 300px | left |
| 3 | relatedCollectionName | Related Collection Name | String | 29 | 230px | left |
| 4 | relatedEntityName | Related Entity | String | 58 | 300px | left |
| 5 | assessmentMethod | Assessment Method | String | 27 | 210px | left |
| 6 | scopeText | Scope Text | String | 122 | 300px | left |
| 7 | initialRiskLevel | Initial Risk Level | String | 6 | 170px | left |
| 8 | residualRiskLevel | Residual Risk Level | String | 3 | 180px | left |
| 9 | riskControlsText | Risk Controls Text | String | 151 | 300px | left |
| 10 | pfmeaName | PFMEA | String | 65 | 300px | left |
| 11 | acceptanceDecision | Acceptance Decision | String | 22 | 180px | left |
| 12 | approvedBy | Approved By | String | 12 | 120px | left |
| 13 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 14 | nextReviewDate | Next Review Date | Date/Date | 10 | 160px | center |
| 15 | status | Status | String | 14 | 120px | left |
| 16 | createdBy | Created By | String | 11 | 110px | left |
| 17 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 18 | updatedBy | Updated By | String | 11 | 110px | left |
| 19 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); relatedEntityId (reference key, shown through relatedEntityName); pfmeaId (reference key, shown through pfmeaName); approvedById (reference key, shown through approvedBy); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_samplingPlan - Sampling Plans (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_samplingPlan.json | _id: mes_qual_samplingPlanStable | rel: CL20261018-23:51 | samples: 20 | columns: 14 | total width: 2530px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | name | Name | String | 46 | 300px | left |
| 3 | samplingType | Sampling Type | String | 13 | 140px | left |
| 4 | standard | Standard | String | 15 | 130px | left |
| 5 | inspectionLevel | Inspection Level | String | 3 | 160px | left |
| 6 | aql | Aql | Decimal128 | 3 | 80px | right |
| 7 | frequencyType | Frequency Type | String | 13 | 140px | left |
| 8 | frequencyEveryNUnits | Frequency Every N Units | Int32 | 2 | 210px | right |
| 9 | frequencyEveryMinutes | Frequency Every (min) | Int32 | 3 | 190px | right |
| 10 | skipLotEnabled | Skip Lot Enabled | Boolean | 3 | 160px | center |
| 11 | skipLotConsecutiveAcceptedToSkip | Skip Lot Consecutive Accepted to Skip | Int32 | 2 | 300px | right |
| 12 | skipLotSkipFraction | Skip Lot Skip Fraction | Decimal128 | 3 | 200px | right |
| 13 | switchingRules | Switching Rules | String | 73 | 300px | left |
| 14 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_samplingPlanSizeRow - Sampling Plan Sample Size Table (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_samplingPlanSizeRow.json | _id: mes_qual_samplingPlanSizeRowStable | rel: CL20261018-23:51 | samples: 20 | columns: 8 | total width: 1240px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | samplingPlanName | Sampling Plan | String | 46 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 2 | 120px | right |
| 4 | lotSizeFrom | Lot Size From | Int32 | 4 | 140px | right |
| 5 | lotSizeTo | Lot Size to | Int32 | 4 | 120px | right |
| 6 | sampleSize | Sample Size | Int32 | 3 | 120px | right |
| 7 | acceptNumber | Accept Number | Int32 | 1 | 140px | right |
| 8 | rejectNumber | Reject Number | Int32 | 1 | 140px | right |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); samplingPlanId (reference key, shown through samplingPlanName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_scrapRecord - Scrap Records (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_scrapRecord.json | _id: mes_qual_scrapRecordStable | rel: CL20261018-23:51 | samples: 20 | columns: 29 | total width: 4760px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | nonconformanceName | Nonconformance | String | 58 | 300px | left |
| 3 | defectCodeName | Defect Code | String | 36 | 280px | left |
| 4 | wipUnitName | WIP Unit | String | 20 | 160px | left |
| 5 | lotName | Lot | String | 15 | 130px | left |
| 6 | itemName | Item | String | 61 | 300px | left |
| 7 | quantity | Quantity | Int32 | 1 | 100px | right |
| 8 | unitOfMeasureName | Unit of Measure | String | 4 | 150px | left |
| 9 | weightKg | Weight Kg | Decimal128 | 5 | 110px | right |
| 10 | originOperationName | Origin Operation | String | 31 | 240px | left |
| 11 | detectedAtOperationName | Detected At Operation | String | 31 | 240px | left |
| 12 | workCenterName | Work Center | String | 37 | 280px | left |
| 13 | shiftName | Shift | String | 7 | 80px | left |
| 14 | scrapType | Scrap Type | String | 16 | 140px | left |
| 15 | scrapCostInr | Scrap Cost (INR) | Decimal128 | 7 | 160px | right |
| 16 | declaredBy | Declared By | String | 14 | 120px | left |
| 17 | declaredAt | Declared At | Date/Datetime | 19 | 160px | center |
| 18 | approvedBy | Approved By | String | 15 | 130px | left |
| 19 | approvedAt | Approved At | Date/Datetime | 19 | 160px | center |
| 20 | scrapLocationName | Scrap Location | String | 22 | 180px | left |
| 21 | disposalMethod | Disposal Method | String | 12 | 150px | left |
| 22 | erpPosted | ERP Posted | Boolean | 3 | 110px | center |
| 23 | serialNumberName | Serial Number | String | 13 | 140px | left |
| 24 | dispositionTypeName | Disposition Type | String | 18 | 160px | left |
| 25 | status | Status | String | 8 | 90px | left |
| 26 | createdBy | Created By | String | 14 | 120px | left |
| 27 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 28 | updatedBy | Updated By | String | 14 | 120px | left |
| 29 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); nonconformanceId (reference key, shown through nonconformanceName); defectCodeId (reference key, shown through defectCodeName); wipUnitId (reference key, shown through wipUnitName); lotId (reference key, shown through lotName); itemId (reference key, shown through itemName); unitOfMeasureId (reference key, shown through unitOfMeasureName); originOperationId (reference key, shown through originOperationName); detectedAtOperationId (reference key, shown through detectedAtOperationName); workCenterId (reference key, shown through workCenterName); shiftId (reference key, shown through shiftName); declaredById (reference key, shown through declaredBy); approvedById (reference key, shown through approvedBy); scrapLocationId (reference key, shown through scrapLocationName); serialNumberId (reference key, shown through serialNumberName); dispositionTypeId (reference key, shown through dispositionTypeName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_spcChart - SPC Charts (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_spcChart.json | _id: mes_qual_spcChartStable | rel: CL20261018-23:51 | samples: 20 | columns: 20 | total width: 3820px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 12 | 110px | left |
| 2 | name | Name | String | 60 | 300px | left |
| 3 | characteristicName | Characteristic | String | 45 | 300px | left |
| 4 | itemName | Item | String | 61 | 300px | left |
| 5 | workCenterName | Work Center | String | 37 | 280px | left |
| 6 | equipmentName | Equipment | String | 54 | 300px | left |
| 7 | chartType | Chart Type | String | 7 | 110px | left |
| 8 | subgroupSize | Subgroup Size | Int32 | 1 | 140px | right |
| 9 | subgroupFrequency | Subgroup Frequency | String | 16 | 170px | left |
| 10 | lowerSpecLimit | Lower Spec Limit | Decimal128 | 6 | 160px | right |
| 11 | upperSpecLimit | Upper Spec Limit | Decimal128 | 6 | 160px | right |
| 12 | capabilityCp | Capability Cp | Decimal128 | 4 | 140px | right |
| 13 | capabilityCpk | Capability Cpk | Decimal128 | 4 | 140px | right |
| 14 | capabilityPp | Capability Pp | Decimal128 | 4 | 140px | right |
| 15 | capabilityPpk | Capability Ppk | Decimal128 | 4 | 140px | right |
| 16 | capabilityCalculatedAt | Capability Calculated At | Date/Datetime | 0 | 210px | center |
| 17 | capabilitySampleCount | Capability Sample Count | Int32 | 3 | 210px | right |
| 18 | ownerUserName | Owner User | String | 14 | 120px | left |
| 19 | reactionPlan | Reaction Plan | String | 81 | 300px | left |
| 20 | status | Status | String | 6 | 90px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); characteristicId (reference key, shown through characteristicName); itemId (reference key, shown through itemName); workCenterId (reference key, shown through workCenterName); equipmentId (reference key, shown through equipmentName); ownerUserId (reference key, shown through ownerUserName); schemaVersion (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): capabilityCalculatedAt

## u_mes_qual_spcChartControlLimit - SPC Chart Control Limits (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_spcChartControlLimit.json | _id: mes_qual_spcChartControlLimitStable | rel: CL20261018-23:51 | samples: 10 | columns: 11 | total width: 1530px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 17 | 140px | left |
| 2 | spcChartName | SPC Chart | String | 47 | 300px | left |
| 3 | revisionNo | Revision No | Int32 | 1 | 120px | right |
| 4 | effectiveFrom | Effective From | Date/Date | 10 | 140px | center |
| 5 | ucl | Ucl | Decimal128 | 6 | 80px | right |
| 6 | centerLine | Center Line | Decimal128 | 6 | 120px | right |
| 7 | lcl | Lcl | Decimal128 | 6 | 80px | right |
| 8 | uclRange | Ucl Range | Decimal128 | 5 | 110px | right |
| 9 | centerLineRange | Center Line Range | Decimal128 | 5 | 160px | right |
| 10 | lclRange | Lcl Range | Decimal128 | 3 | 110px | right |
| 11 | basedOnSubgroups | Based on Subgroups | Int32 | 2 | 170px | right |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); spcChartId (reference key, shown through spcChartName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_spcChartRule - SPC Chart Rules (Master)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_spcChartRule.json | _id: mes_qual_spcChartRuleStable | rel: CL20261018-23:51 | samples: 10 | columns: 4 | total width: 700px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 16 | 140px | left |
| 2 | spcChartName | SPC Chart | String | 47 | 300px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | rule | Rule | String | 17 | 140px | left |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); spcChartId (reference key, shown through spcChartName); schemaVersion (excluded key (identifier, site, app or schema))

## u_mes_qual_spcSample - SPC Samples (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_spcSample.json | _id: mes_qual_spcSampleStable | rel: CL20261018-23:51 | samples: 20 | columns: 27 | total width: 4480px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 15 | 130px | left |
| 2 | spcChartName | SPC Chart | String | 60 | 300px | left |
| 3 | characteristicName | Characteristic | String | 45 | 300px | left |
| 4 | workCenterName | Work Center | String | 37 | 280px | left |
| 5 | subgroupNo | Subgroup No | Int32 | 3 | 120px | right |
| 6 | sampledAt | Sampled At | Date/Datetime | 19 | 160px | center |
| 7 | sampledBy | Sampled By | String | 14 | 120px | left |
| 8 | shiftName | Shift | String | 7 | 80px | left |
| 9 | subgroupMean | Subgroup Mean | Decimal128 | 7 | 140px | right |
| 10 | subgroupRange | Subgroup Range | Decimal128 | 5 | 140px | right |
| 11 | stdDev | Std Dev | Decimal128 | 6 | 90px | right |
| 12 | ucl | Ucl | Decimal128 | 6 | 80px | right |
| 13 | lcl | Lcl | Decimal128 | 6 | 80px | right |
| 14 | centerLine | Center Line | Decimal128 | 6 | 120px | right |
| 15 | inControl | In Control | Boolean | 3 | 110px | center |
| 16 | assignableCause | Assignable Cause | String | 0 | 160px | left |
| 17 | correctiveAction | Corrective Action | String | 69 | 300px | left |
| 18 | nonconformanceName | Nonconformance | String | 52 | 300px | left |
| 19 | excludedFromLimits | Excluded From Limits | Boolean | 3 | 180px | center |
| 20 | reactionType | Reaction Type | String | 5 | 140px | left |
| 21 | qualityHoldName | Quality Hold | String | 0 | 130px | left |
| 22 | notificationName | Notification | String | 41 | 300px | left |
| 23 | status | Status | String | 19 | 160px | left |
| 24 | createdBy | Created By | String | 14 | 120px | left |
| 25 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 26 | updatedBy | Updated By | String | 14 | 120px | left |
| 27 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); spcChartId (reference key, shown through spcChartName); characteristicId (reference key, shown through characteristicName); workCenterId (reference key, shown through workCenterName); sampledById (reference key, shown through sampledBy); shiftId (reference key, shown through shiftName); nonconformanceId (reference key, shown through nonconformanceName); qualityHoldId (reference key, shown through qualityHoldName); notificationId (reference key, shown through notificationName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

No non-null sample value (width from title only): assignableCause, qualityHoldName

## u_mes_qual_spcSampleInspectionResult - SPC Sample Inspection Results (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_spcSampleInspectionResult.json | _id: mes_qual_spcSampleInspectionResultStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1130px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 20 | 160px | left |
| 2 | spcSampleName | SPC Sample | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | inspectionResultName | Inspection Result | String | 14 | 160px | left |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); spcSampleId (reference key, shown through spcSampleName); inspectionResultId (reference key, shown through inspectionResultName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_spcSampleReading - SPC Sample Readings (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_spcSampleReading.json | _id: mes_qual_spcSampleReadingStable | rel: CL20261018-23:51 | samples: 10 | columns: 8 | total width: 1060px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | spcSampleName | SPC Sample | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | reading | Reading | Decimal128 | 6 | 90px | right |
| 5 | createdBy | Created By | String | 14 | 120px | left |
| 6 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 7 | updatedBy | Updated By | String | 14 | 120px | left |
| 8 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); spcSampleId (reference key, shown through spcSampleName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))

## u_mes_qual_spcSampleViolation - SPC Sample Violations (Transaction)

File: 04_reference_data/ui_controls/table/PageConfigs/u_mes_qual_spcSampleViolation.json | _id: mes_qual_spcSampleViolationStable | rel: CL20261018-23:51 | samples: 10 | columns: 9 | total width: 1410px

| # | data_index | title | type | longest sample | width | align |
|---|---|---|---|---|---|---|
| 1 | recordNo | Record No | String | 19 | 160px | left |
| 2 | spcSampleName | SPC Sample | String | 15 | 130px | left |
| 3 | sequenceNo | Sequence No | Int32 | 1 | 120px | right |
| 4 | rule | Rule | String | 17 | 140px | left |
| 5 | description | Description | String | 46 | 300px | left |
| 6 | createdBy | Created By | String | 14 | 120px | left |
| 7 | createdAt | Created At | Date/Datetime | 19 | 160px | center |
| 8 | updatedBy | Updated By | String | 14 | 120px | left |
| 9 | updatedAt | Updated At | Date/Datetime | 19 | 160px | center |

Left out: _id (excluded key (identifier, site, app or schema)); app (excluded key (identifier, site, app or schema)); siteId (excluded key (identifier, site, app or schema)); siteName (excluded key (identifier, site, app or schema)); spcSampleId (reference key, shown through spcSampleName); schemaVersion (excluded key (identifier, site, app or schema)); createdById (excluded key (identifier, site, app or schema)); updatedById (excluded key (identifier, site, app or schema))
