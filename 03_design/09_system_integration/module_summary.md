# System and Integration (syst) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_syst_erpMessage | Entity | transaction | 41 | 26 | 5 | 9 |
| 2 | u_mes_syst_integrationConnector | Entity | master | 23 | 19 | 7 | 3 |
| 3 | u_mes_syst_integrationConnectorFunction | Child | master | 14 | 13 | 3 | 1 |
| 4 | u_mes_syst_iotDevice | Entity | master | 32 | 24 | 4 | 7 |
| 5 | u_mes_syst_operatorApp | Entity | master | 18 | 10 | 3 | 3 |
| 6 | u_mes_syst_operatorAppWorkCenter | Relationship | master | 11 | 11 | 1 | 2 |
| 7 | u_mes_syst_operatorAppOperation | Relationship | master | 11 | 11 | 1 | 2 |
| 8 | u_mes_syst_operatorAppStep | Child | master | 16 | 13 | 2 | 3 |
| 9 | u_mes_syst_operatorAppStepTrigger | Child | master | 12 | 11 | 3 | 1 |
| 10 | u_mes_syst_operatorAppDeviceBinding | Child | master | 12 | 12 | 2 | 2 |
| 11 | u_mes_syst_operatorAppLanguage | Relationship | master | 11 | 11 | 1 | 2 |
| 12 | u_mes_syst_businessEvent | Entity | transaction | 33 | 20 | 4 | 8 |
| 13 | u_mes_syst_auditTrail | Entity | transaction | 31 | 26 | 2 | 6 |
| 14 | u_mes_syst_auditTrailChange | Child | transaction | 18 | 16 | 1 | 1 |
| 15 | u_mes_syst_electronicSignature | Entity | transaction | 33 | 29 | 2 | 7 |
| 16 | u_mes_syst_notification | Entity | transaction | 43 | 21 | 2 | 9 |
| 17 | u_mes_syst_notificationRecipient | Child | transaction | 23 | 18 | 2 | 3 |
| 18 | u_mes_syst_controlledDocument | Entity | transaction | 39 | 31 | 3 | 8 |
| 19 | u_mes_syst_controlledDocumentTag | Value list | transaction | 16 | 16 | 1 | 1 |
| 20 | u_mes_syst_numberRange | Entity | master | 25 | 20 | 5 | 3 |
| 21 | u_mes_syst_systemConfiguration | Entity | master | 19 | 15 | 5 | 2 |
| 22 | u_mes_syst_documentType | Entity | master | 12 | 12 | 2 | 2 |
| 23 | u_mes_syst_deviceType | Entity | master | 10 | 10 | 2 | 2 |
| 24 | u_mes_syst_notificationType | Entity | master | 10 | 10 | 2 | 2 |
| 25 | u_mes_syst_statusDefinition | Entity | master | 16 | 15 | 2 | 3 |
| 26 | u_mes_syst_enumerationValue | Entity | master | 14 | 14 | 2 | 2 |
| 27 | u_mes_syst_statusTransition | Entity | master | 16 | 16 | 2 | 4 |
| 28 | u_mes_syst_interlockRule | Entity | master | 29 | 16 | 5 | 7 |
| 29 | u_mes_syst_statusTransitionRole | Relationship | master | 11 | 11 | 1 | 2 |
| 30 | u_mes_syst_escalationRule | Entity | master | 18 | 13 | 4 | 5 |
| 31 | u_mes_syst_escalationRuleLevel | Child | master | 16 | 16 | 3 | 3 |
| 32 | u_mes_syst_alertRule | Entity | master | 30 | 17 | 6 | 7 |
| 33 | u_mes_syst_analyticsModel | Entity | master | 23 | 14 | 3 | 4 |
| 34 | u_mes_syst_modelPrediction | Entity | transaction | 40 | 22 | 4 | 9 |
| 35 | u_mes_syst_simulationStudy | Entity | transaction | 34 | 17 | 4 | 7 |
| 36 | u_mes_syst_recordPolicy | Entity | master | 19 | 14 | 3 | 4 |
| 37 | u_mes_syst_savedView | Entity | master | 17 | 14 | 3 | 4 |
| 38 | u_mes_syst_backupRun | Entity | transaction | 24 | 18 | 3 | 4 |
| 39 | u_mes_syst_computerisedSystem | Entity | master | 28 | 22 | 7 | 6 |
| 40 | u_mes_syst_systemValidation | Entity | transaction | 39 | 23 | 4 | 8 |
| 41 | u_mes_syst_systemPeriodicReview | Entity | transaction | 32 | 26 | 2 | 4 |
| 42 | u_mes_syst_auditTrailReview | Entity | transaction | 32 | 23 | 4 | 7 |
| 43 | u_mes_syst_userAccessReview | Entity | transaction | 26 | 22 | 2 | 4 |
| 44 | u_mes_syst_userAccessReviewLine | Child | transaction | 23 | 21 | 2 | 3 |
