# System and Integration (syst) - module summary

| # | Collection | Kind | Data class | Keys | Required (non-null) keys | Keys with allowed values | Indexes |
|---|---|---|---|---|---|---|---|
| 1 | u_mes_syst_erpMessage | Entity | transaction | 40 | 25 | 4 | 9 |
| 2 | u_mes_syst_integrationConnector | Entity | master | 22 | 18 | 6 | 3 |
| 3 | u_mes_syst_integrationConnectorFunction | Child | master | 13 | 12 | 2 | 1 |
| 4 | u_mes_syst_iotDevice | Entity | master | 31 | 23 | 3 | 7 |
| 5 | u_mes_syst_operatorApp | Entity | master | 17 | 9 | 2 | 3 |
| 6 | u_mes_syst_operatorAppWorkCenter | Relationship | master | 10 | 10 | 0 | 2 |
| 7 | u_mes_syst_operatorAppOperation | Relationship | master | 10 | 10 | 0 | 2 |
| 8 | u_mes_syst_operatorAppStep | Child | master | 15 | 12 | 1 | 3 |
| 9 | u_mes_syst_operatorAppStepTrigger | Child | master | 11 | 10 | 2 | 1 |
| 10 | u_mes_syst_operatorAppDeviceBinding | Child | master | 11 | 11 | 1 | 2 |
| 11 | u_mes_syst_operatorAppLanguage | Relationship | master | 10 | 10 | 0 | 2 |
| 12 | u_mes_syst_businessEvent | Entity | transaction | 32 | 19 | 3 | 8 |
| 13 | u_mes_syst_auditTrail | Entity | transaction | 27 | 24 | 1 | 5 |
| 14 | u_mes_syst_auditTrailChange | Child | transaction | 17 | 15 | 0 | 1 |
| 15 | u_mes_syst_electronicSignature | Entity | transaction | 29 | 26 | 1 | 7 |
| 16 | u_mes_syst_notification | Entity | transaction | 42 | 20 | 1 | 9 |
| 17 | u_mes_syst_notificationRecipient | Child | transaction | 22 | 17 | 1 | 3 |
| 18 | u_mes_syst_controlledDocument | Entity | transaction | 38 | 30 | 2 | 8 |
| 19 | u_mes_syst_controlledDocumentTag | Value list | transaction | 15 | 15 | 0 | 1 |
| 20 | u_mes_syst_numberRange | Entity | master | 24 | 19 | 4 | 3 |
| 21 | u_mes_syst_systemConfiguration | Entity | master | 18 | 14 | 4 | 2 |
| 22 | u_mes_syst_documentType | Entity | master | 11 | 11 | 1 | 2 |
| 23 | u_mes_syst_deviceType | Entity | master | 9 | 9 | 1 | 2 |
| 24 | u_mes_syst_notificationType | Entity | master | 9 | 9 | 1 | 2 |
| 25 | u_mes_syst_statusDefinition | Entity | master | 15 | 14 | 1 | 3 |
| 26 | u_mes_syst_enumerationValue | Entity | master | 13 | 13 | 1 | 2 |
| 27 | u_mes_syst_statusTransition | Entity | master | 15 | 15 | 1 | 4 |
| 28 | u_mes_syst_interlockRule | Entity | master | 28 | 15 | 4 | 7 |
| 29 | u_mes_syst_statusTransitionRole | Relationship | master | 10 | 10 | 0 | 2 |
| 30 | u_mes_syst_escalationRule | Entity | master | 17 | 12 | 3 | 5 |
| 31 | u_mes_syst_escalationRuleLevel | Child | master | 15 | 15 | 2 | 3 |
| 32 | u_mes_syst_alertRule | Entity | master | 29 | 16 | 5 | 7 |
| 33 | u_mes_syst_analyticsModel | Entity | master | 22 | 13 | 2 | 4 |
| 34 | u_mes_syst_modelPrediction | Entity | transaction | 39 | 21 | 3 | 9 |
| 35 | u_mes_syst_simulationStudy | Entity | transaction | 33 | 16 | 3 | 7 |
| 36 | u_mes_syst_recordPolicy | Entity | master | 17 | 12 | 2 | 4 |
| 37 | u_mes_syst_savedView | Entity | master | 16 | 13 | 2 | 4 |
| 38 | u_mes_syst_backupRun | Entity | transaction | 23 | 17 | 2 | 4 |
