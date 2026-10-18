"""
query_screens.py - control decisions of the MES list screens, read by gen_query.py.

One SCREENS entry per collection, controls in display order. Draft new entries with
  python3 05_generator/gen_query.py --propose <module>
review the printed draft, then paste or adjust it here and run gen_query.py <module>.
Readings of the skill applied here: D067 (decision_log.md). Rules: skill mes-query-control.
"""
# Registry ids of the shared sources (profile section 2.1)
USER = ("u_mes_mast_user", "fullName")
TOOL = ("u_mes_maint_tool", "name")
STORAGE = ("u_mes_matl_storageLocation", "name")
PO = ("u_mes_plan_productionOrder", "recordNo")
LOT = ("u_mes_plan_lot", "recordNo")
WIP = ("u_mes_plan_wipUnit", "recordNo")
OPEX = ("u_mes_plan_operationExecution", "recordNo")
CHANGEOVER = ("u_mes_plan_changeover", "recordNo")
HANDOVER = ("u_mes_plan_shiftHandover", "recordNo")

# Display text of data maps whose stored values are not readable words
DATA_TEXT = {
    ("u_mes_plan_documentAcknowledgement", "relatedCollectionName"): {
        "u_mes_prod_workInstruction": "Work Instruction",
        "u_mes_prod_recipe": "Recipe",
        "u_mes_syst_controlledDocument": "Controlled Document",
    },
}

# Label overrides (default: key without Id / ById, camelCase split, Title Case)
LABELS = {
    "currentWorkCenterId": "Current Work Center",
    "ownerCustomerId": "Owner Customer",
    "ownerUserId": "Owner",
    "toUserId": "Escalated To",
    "performedByUserId": "Performed By",
    "userId": "User",
    "rule": "Sequencing Rule",
    "internalExternal": "Internal or External",
    "isReturnable": "Returnable",
    "isPaid": "Paid",
    "relatedCollectionName": "Document Source",
    "closed": "Closed",
    "passed": "Passed",
    "frozen": "Frozen",
    "supplierInvoiceDate": "Invoice Date Range",       # range label within 25 characters
    "plannedDispatchAt": "Planned Dispatch Range",
    "masterManufacturingRecordId": "Master Mfg Record",
    "productionReviewedAt": "Review Date Range",
    "registeredAddressCountryId": "Registered Country",
    "billOfMaterialComponentId": "BOM Component",
    "readAcknowledgementRequired": "Read Ack Required",
    "arContentControlledDocumentId": "AR Content Document",
    "environmentalMonitoringPointId": "Monitoring Point",
    "reviewPeriodFromDate": "Review Period Range",
    "usesElectronicSignatures": "Uses E-Signatures",
    "createdInSourceAt": "Created Date Range",
    "overrideRequiresSignature": "Override Needs Signature",
    "requiresSignatureForEdit": "Edit Needs Signature",
}
ACRONYMS = {"Wip": "WIP", "Erp": "ERP", "Plc": "PLC"}


# ---------------------------------------------------------------------------
# Control decisions per collection (display order = modalElements order)
# R  = range picker on the time key (defaultFrom, defaultTo)
# MD = dropdown from /mdict (dictName)
# SH = Shift dropdown from cropdown "Shift"
# D  = hard-coded data dropdown (status, enumeration or Boolean)
# DD = /dd dynamic dropdown (coln, val); DS = /dd search dropdown (coln, val)
# ---------------------------------------------------------------------------
def R(key, frm, to):
    return {"kind": "range", "key": key, "from": frm, "to": to}


def MD(key, dict_name):
    return {"kind": "mdict", "key": key, "dict": dict_name}


def SH():
    return {"kind": "shift", "key": "shiftId"}


def D(key, multi=False):
    return {"kind": "data", "key": key, "multi": multi}


def DD(key, source):
    return {"kind": "dd", "key": key, "coln": source[0], "val": source[1], "search": False}


def DS(key, source):
    return {"kind": "dd", "key": key, "coln": source[0], "val": source[1], "search": True}


SCREENS = {
    # Plan and schedule screens: range -30 / 0 (skill 0.19, Q10)
    "u_mes_plan_customerSchedule": [
        R("horizonFrom", -30, 0), D("status"), MD("customerId", "Customer"), D("scheduleType")],
    "u_mes_plan_customerScheduleLine": [
        DS("customerScheduleId", ("u_mes_plan_customerSchedule", "recordNo")), MD("itemId", "Item"),
        D("firmness")],
    "u_mes_plan_productionOrder": [
        R("plannedStartAt", -30, 0), MD("lineId", "Line"), D("status"),
        MD("productVariantId", "ProductVariant"), D("orderType"), D("priority"), D("onHold")],
    "u_mes_plan_productionOrderRelease": [
        DS("productionOrderId", PO), DS("releasedById", USER)],
    "u_mes_plan_productionOrderLot": [
        DS("productionOrderId", PO), DS("lotId", LOT)],
    "u_mes_plan_productionSchedule": [
        R("productionDate", -30, 0), MD("lineId", "Line"), SH(), D("status"), D("frozen")],
    "u_mes_plan_productionScheduleSlot": [
        DS("productionScheduleId", ("u_mes_plan_productionSchedule", "recordNo")),
        DS("productionOrderId", PO), MD("itemId", "Item")],
    # Operational screens: range -7 / 0
    "u_mes_plan_dispatchList": [
        R("productionDate", -7, 0), MD("workCenterId", "WorkCenter"), SH(), D("status"), D("rule")],
    "u_mes_plan_dispatchListEntry": [
        DS("dispatchListId", ("u_mes_plan_dispatchList", "recordNo")), DS("productionOrderId", PO),
        D("status"), MD("itemId", "Item"), D("priority"), D("materialAvailable"), D("toolAvailable")],
    "u_mes_plan_operationExecution": [
        R("startedAt", -7, 0), DS("productionOrderId", PO), MD("workCenterId", "WorkCenter"),
        MD("equipmentId", "Equipment"), SH(), D("status"), MD("operationId", "Operation"), D("result")],
    "u_mes_plan_operationExecutionDefectCode": [
        DS("operationExecutionId", OPEX), MD("defectCodeId", "DefectCode")],
    "u_mes_plan_operationExecutionTool": [
        DS("operationExecutionId", OPEX), DS("toolId", TOOL)],
    "u_mes_plan_stepCompletion": [
        R("startedAt", -7, 0), DS("wipUnitId", WIP), MD("workCenterId", "WorkCenter"), D("status"),
        DD("workInstructionId", ("u_mes_prod_workInstruction", "title")), D("withinLimits"),
        D("overridden")],
    "u_mes_plan_wipUnit": [
        R("startedAt", -7, 0), DS("productionOrderId", PO), MD("currentWorkCenterId", "WorkCenter"),
        D("status"), MD("productVariantId", "ProductVariant"), D("qualityStatus"), D("onHold")],
    "u_mes_plan_wipUnitCompletedStep": [
        DS("wipUnitId", WIP)],
    "u_mes_plan_lot": [
        R("manufacturedAt", -7, 0), DS("productionOrderId", PO), DS("storageLocationId", STORAGE),
        D("status"), D("lotType"), MD("itemId", "Item"), D("qualityStatus"), D("onHold")],
    "u_mes_plan_lotParentLot": [
        DS("lotId", LOT), DS("parentLotId", LOT)],
    "u_mes_plan_lotAttributesCavityNo": [
        DS("lotId", LOT)],
    "u_mes_plan_container": [
        R("packedAt", -7, 0), DS("storageLocationId", STORAGE), D("status"),
        MD("containerTypeId", "ContainerType"), MD("ownerCustomerId", "Customer"), D("isReturnable"),
        D("onHold")],
    "u_mes_plan_containerLot": [
        DS("containerId", ("u_mes_plan_container", "recordNo")), DS("lotId", LOT)],
    "u_mes_plan_labourBooking": [
        R("productionDate", -7, 0), DS("productionOrderId", PO), MD("workCenterId", "WorkCenter"), SH(),
        D("status"), DS("userId", USER), D("bookingType"), MD("indirectActivityId", "IndirectActivity")],
    "u_mes_plan_changeover": [
        R("startedAt", -7, 0), MD("lineId", "Line"), MD("workCenterId", "WorkCenter"), D("status"),
        D("changeoverType")],
    "u_mes_plan_changeoverStep": [
        DS("changeoverId", CHANGEOVER), D("internalExternal"), DS("completedById", USER)],
    "u_mes_plan_changeoverRemovedTool": [
        DS("changeoverId", CHANGEOVER), DS("removedToolId", TOOL)],
    "u_mes_plan_changeoverInstalledTool": [
        DS("changeoverId", CHANGEOVER), DS("installedToolId", TOOL)],
    "u_mes_plan_changeoverPerformedByUser": [
        DS("changeoverId", CHANGEOVER), DS("performedByUserId", USER)],
    "u_mes_plan_shiftHandover": [
        R("productionDate", -7, 0), MD("lineId", "Line"), SH(), D("status")],
    "u_mes_plan_shiftHandoverProductionOrder": [
        DS("shiftHandoverId", HANDOVER), DS("productionOrderId", PO)],
    "u_mes_plan_shiftHandoverDowntimeEvent": [
        DS("shiftHandoverId", HANDOVER), DS("downtimeEventId", ("u_mes_perf_downtimeEvent", "recordNo"))],
    "u_mes_plan_shiftHandoverNonconformance": [
        DS("shiftHandoverId", HANDOVER), DS("nonconformanceId", ("u_mes_qual_nonconformance", "title"))],
    "u_mes_plan_shiftHandoverOpenItem": [
        DS("shiftHandoverId", HANDOVER), DS("ownerUserId", USER), D("closed")],
    # Worked example of the skill (section 12): multi-select status, compelling reason:
    # the open-calls board must show Raised and Acknowledged together
    "u_mes_plan_andonEvent": [
        R("raisedAt", -7, 0), MD("lineId", "Line"), MD("workCenterId", "WorkCenter"), SH(),
        D("status", multi=True), MD("andonTypeId", "AndonType"), D("lineStopped")],
    "u_mes_plan_andonEventEscalation": [
        DS("andonEventId", ("u_mes_plan_andonEvent", "description")), DS("toUserId", USER), D("channel")],
    # Master screens: no period control
    "u_mes_plan_indirectActivity": [
        D("status"), DD("costCenterId", ("u_mes_mast_costCenter", "name")), D("isPaid")],
    "u_mes_plan_containerType": [
        D("status"), D("isReturnable")],
    "u_mes_plan_andonType": [
        D("status"), DD("responsibleDepartmentId", ("u_mes_mast_department", "name"))],
    # Station evidence (D036 - D041)
    "u_mes_plan_operatorSession": [
        R("loginAt", -7, 0), MD("workCenterId", "WorkCenter"), MD("equipmentId", "Equipment"), SH(),
        D("status"), DS("userId", USER), D("authenticationMethod")],
    "u_mes_plan_documentAcknowledgement": [
        R("acknowledgedAt", -7, 0), MD("workCenterId", "WorkCenter"), SH(), D("status"),
        D("relatedCollectionName"), D("acknowledgementType"), DS("userId", USER)],
    "u_mes_plan_interlockEvent": [
        R("raisedAt", -7, 0), DS("productionOrderId", PO), MD("workCenterId", "WorkCenter"),
        MD("equipmentId", "Equipment"), SH(), D("status"),
        DD("interlockRuleId", ("u_mes_syst_interlockRule", "name"))],
    "u_mes_plan_recipeDownload": [
        R("downloadedAt", -7, 0), MD("workCenterId", "WorkCenter"), MD("equipmentId", "Equipment"),
        D("status"), DD("recipeId", ("u_mes_prod_recipe", "name")), D("verificationResult"), D("trigger")],
    "u_mes_plan_setupVerification": [
        R("verifiedAt", -7, 0), DS("productionOrderId", PO), MD("workCenterId", "WorkCenter"),
        MD("equipmentId", "Equipment"), D("status"), MD("productVariantId", "ProductVariant"),
        D("trigger")],
    "u_mes_plan_setupVerificationItem": [
        DS("setupVerificationId", ("u_mes_plan_setupVerification", "recordNo")), D("checkType"),
        D("passed")],
    "u_mes_plan_lineClearance": [
        R("startedAt", -7, 0), DS("productionOrderId", PO), MD("lineId", "Line"),
        MD("workCenterId", "WorkCenter"), D("status"), D("clearanceType")],
    # MaterialManagement, Traceability, EnvironmentHealthAndSafety (18 Oct 2026, D074): drafted with --propose, reviewed
    "u_mes_matl_storageLocation": [D("status"), MD("areaId", "Area"), MD("workCenterId", "WorkCenter"), D("locationType"), D("isQuarantine"), D("isLineSide")],
    "u_mes_matl_inventoryBalance": [R("firstReceivedAt", -7, 0), DS("lotId", ("u_mes_plan_lot", "recordNo")), DS("storageLocationId", ("u_mes_matl_storageLocation", "name")), D("status"), MD("itemId", "Item"), MD("stockStatusId", "StockStatus")],
    "u_mes_matl_materialMovement": [R("movedAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), D("status"), MD("movementTypeId", "MovementType"), MD("itemId", "Item"), D("scanSource")],
    "u_mes_matl_goodsReceipt": [R("supplierInvoiceDate", -7, 0), D("status"), MD("supplierId", "Supplier")],
    "u_mes_matl_goodsReceiptLine": [DS("goodsReceiptId", ("u_mes_matl_goodsReceipt", "recordNo")), MD("itemId", "Item"), DS("lotId", ("u_mes_plan_lot", "recordNo")), D("inspectionStatus"), D("certificateReceived")],
    "u_mes_matl_goodsReceiptLineInspectionResult": [DS("goodsReceiptLineId", ("u_mes_matl_goodsReceiptLine", "recordNo")), DS("inspectionResultId", ("u_mes_qual_inspectionResult", "recordNo"))],
    "u_mes_matl_kit": [R("requiredAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), MD("workCenterId", "WorkCenter"), D("status"), D("kitType")],
    "u_mes_matl_kitLine": [DS("kitId", ("u_mes_matl_kit", "recordNo")), MD("itemId", "Item"), DS("lotId", ("u_mes_plan_lot", "recordNo")), DS("fromLocationId", ("u_mes_matl_storageLocation", "name")), D("verificationResult"), D("isMandatory")],
    "u_mes_matl_materialRequest": [R("requestedAt", -7, 0), MD("workCenterId", "WorkCenter"), D("status"), MD("itemId", "Item"), DD("replenishmentRuleId", ("u_mes_matl_replenishmentRule", "recordNo")), D("requestType"), D("priority")],
    "u_mes_matl_materialConsumption": [R("consumedAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), MD("workCenterId", "WorkCenter"), D("status"), MD("componentItemId", "Item"), D("consumptionType")],
    "u_mes_matl_packagingSpecification": [D("status"), MD("itemId", "Item"), MD("customerId", "Customer"), D("vciRequired"), D("approvedByCustomer")],
    "u_mes_matl_packagingSpecificationLevel": [DD("packagingSpecificationId", ("u_mes_matl_packagingSpecification", "recordNo")), DD("packTypeId", ("u_mes_matl_packType", "name"))],
    "u_mes_matl_labelTemplate": [D("status"), MD("customerId", "Customer"), D("labelType"), D("printerLanguage")],
    "u_mes_matl_labelTemplateField": [DD("labelTemplateId", ("u_mes_matl_labelTemplate", "name")), D("source"), D("isBarcode")],
    "u_mes_matl_label": [R("printedAt", -7, 0), DS("wipUnitId", ("u_mes_plan_wipUnit", "recordNo")), D("status"), DD("labelTemplateId", ("u_mes_matl_labelTemplate", "name")), DD("printerIotDeviceId", ("u_mes_syst_iotDevice", "name")), D("labelType")],
    "u_mes_matl_shipment": [R("plannedDispatchAt", -7, 0), D("status"), MD("customerId", "Customer"), DD("transporterId", ("u_mes_mast_transporter", "name"))],
    "u_mes_matl_shipmentLine": [DS("shipmentId", ("u_mes_matl_shipment", "recordNo")), MD("itemId", "Item")],
    "u_mes_matl_shipmentLineContainer": [DS("shipmentLineId", ("u_mes_matl_shipmentLine", "recordNo")), DS("containerId", ("u_mes_plan_container", "recordNo"))],
    "u_mes_matl_shipmentLineLot": [DS("shipmentLineId", ("u_mes_matl_shipmentLine", "recordNo")), DS("lotId", ("u_mes_plan_lot", "recordNo"))],
    "u_mes_matl_movementType": [D("status"), D("stockEffect"), D("requiresReason")],
    "u_mes_matl_stockStatus": [D("status"), D("isUsable")],
    "u_mes_matl_packType": [D("status")],
    "u_mes_matl_exposureTimer": [R("startedAt", -7, 0), DS("lotId", ("u_mes_plan_lot", "recordNo")), DS("storageLocationId", ("u_mes_matl_storageLocation", "name")), D("status"), MD("itemId", "Item"), MD("resetReasonCodeId", "ReasonCode"), D("timerType")],
    "u_mes_matl_replenishmentRule": [D("status"), MD("itemId", "Item"), MD("workCenterId", "WorkCenter"), D("triggerType")],
    "u_mes_matl_materialDemandForecast": [R("productionDate", -10, 0), MD("lineId", "Line"), D("status"), MD("itemId", "Item"), DD("analyticsModelId", ("u_mes_syst_analyticsModel", "name")), D("method")],
    "u_mes_matl_storageLocationAllowedItem": [DS("storageLocationId", ("u_mes_matl_storageLocation", "name")), MD("itemId", "Item"), DD("itemGroupId", ("u_mes_prod_itemGroup", "name"))],
    "u_mes_matl_dispenseRecord": [R("dispensedAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), DS("storageLocationId", ("u_mes_matl_storageLocation", "name")), D("status"), MD("itemId", "Item"), D("dispenseMethod"), D("verificationMethod")],
    "u_mes_trac_serialNumber": [R("issuedAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), D("status"), MD("productVariantId", "ProductVariant"), MD("customerId", "Customer"), D("markGrade")],
    "u_mes_trac_genealogyLink": [R("linkedAt", -7, 0), DS("parentSerialNumberId", ("u_mes_trac_serialNumber", "recordNo")), D("status"), MD("childItemId", "Item"), D("linkType")],
    "u_mes_trac_componentLotLink": [R("linkedAt", -7, 0), DS("parentLotId", ("u_mes_plan_lot", "recordNo")), D("status"), MD("childItemId", "Item"), D("linkType")],
    "u_mes_trac_asBuiltRecord": [R("builtAt", -10, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), D("status"), MD("productVariantId", "ProductVariant"), MD("customerId", "Customer"), D("leakTestVerdict")],
    "u_mes_trac_asBuiltRecordComponent": [DS("asBuiltRecordId", ("u_mes_trac_asBuiltRecord", "recordNo")), MD("itemId", "Item"), DS("lotId", ("u_mes_plan_lot", "recordNo"))],
    "u_mes_trac_asBuiltRecordOperation": [DS("asBuiltRecordId", ("u_mes_trac_asBuiltRecord", "recordNo")), MD("operationId", "Operation"), DS("operatorUserId", ("u_mes_mast_user", "fullName")), DD("recipeId", ("u_mes_prod_recipe", "name")), D("result")],
    "u_mes_trac_asBuiltRecordInspectionResult": [DS("asBuiltRecordId", ("u_mes_trac_asBuiltRecord", "recordNo")), DS("inspectionResultId", ("u_mes_qual_inspectionResult", "recordNo"))],
    "u_mes_trac_traceInvestigation": [R("requestedAt", -7, 0), D("status"), D("direction")],
    "u_mes_trac_traceInvestigationResult": [DS("traceInvestigationId", ("u_mes_trac_traceInvestigation", "title")), MD("itemId", "Item"), DS("shipmentId", ("u_mes_matl_shipment", "recordNo")), MD("customerId", "Customer")],
    "u_mes_ehs_safetyIncident": [R("occurredAt", -7, 0), MD("areaId", "Area"), MD("workCenterId", "WorkCenter"), D("status"), MD("incidentTypeId", "IncidentType"), DD("bodyPartId", ("u_mes_ehs_bodyPart", "name")), D("reportableToAuthority")],
    "u_mes_ehs_safetyIncidentWitnessUser": [DS("safetyIncidentId", ("u_mes_ehs_safetyIncident", "title")), DS("witnessUserId", ("u_mes_mast_user", "fullName"))],
    "u_mes_ehs_safetyIncidentAction": [DS("safetyIncidentId", ("u_mes_ehs_safetyIncident", "title")), DS("ownerUserId", ("u_mes_mast_user", "fullName"))],
    "u_mes_ehs_incidentType": [D("status"), D("isInjury"), D("reportableToAuthority")],
    "u_mes_ehs_bodyPart": [D("status")],
    "u_mes_ehs_injuryType": [D("status")],
    # MasterDataManagement, ProductDefinition, QualityManagement, PerformanceManagement (remaining 18), SystemAndIntegration,
    # BatchManufacturingRecord, MasterManufacturingRecord (18 Oct 2026, D078): drafted with --propose, reviewed
    "u_mes_mast_enterprise": [D("status"), DD("parentEnterpriseId", ("u_mes_mast_enterprise", "name")), DD("registeredAddressCountryId", ("u_mes_mast_country", "name")), D("scope")],
    "u_mes_mast_enterpriseContact": [DD("enterpriseId", ("u_mes_mast_enterprise", "name"))],
    "u_mes_mast_site": [D("status"), DD("enterpriseId", ("u_mes_mast_enterprise", "name")), DD("addressCountryId", ("u_mes_mast_country", "name")), D("siteType")],
    "u_mes_mast_siteCertificate": [DS("issuedById", ("u_mes_mast_user", "fullName"))],
    "u_mes_mast_area": [D("status"), MD("parentAreaId", "Area"), DD("costCenterId", ("u_mes_mast_costCenter", "name")), D("areaType"), D("isProductionArea"), D("environmentallyMonitored")],
    "u_mes_mast_line": [D("status"), MD("areaId", "Area"), DD("itemFamilyId", ("u_mes_prod_itemFamily", "name"))],
    "u_mes_mast_lineDefaultShift": [MD("lineId", "Line")],
    "u_mes_mast_lineIdealRate": [MD("lineId", "Line"), MD("itemId", "Item")],
    "u_mes_mast_workCenter": [D("status"), MD("areaId", "Area"), MD("lineId", "Line"), D("workCenterType"), D("andonEnabled")],
    "u_mes_mast_workCenterEquipment": [MD("workCenterId", "WorkCenter"), MD("equipmentId", "Equipment")],
    "u_mes_mast_workCenterOperation": [MD("workCenterId", "WorkCenter"), MD("operationId", "Operation")],
    "u_mes_mast_workCenterRequiresSkill": [MD("workCenterId", "WorkCenter"), DD("requiresSkillId", ("u_mes_mast_skill", "name"))],
    "u_mes_mast_equipment": [D("status"), DD("equipmentTypeId", ("u_mes_mast_equipmentType", "name")), MD("lineId", "Line"), D("equipmentClass"), D("calibrationRequired"), D("isProductionReady")],
    "u_mes_mast_equipmentIotDevice": [MD("equipmentId", "Equipment"), DD("iotDeviceId", ("u_mes_syst_iotDevice", "name"))],
    "u_mes_mast_shift": [D("status"), D("crossesMidnight")],
    "u_mes_mast_shiftBreak": [DD("shiftId", ("u_mes_mast_shift", "name")), D("paid")],
    "u_mes_mast_shiftWorkingDay": [DD("shiftId", ("u_mes_mast_shift", "name")), D("workingDay")],
    "u_mes_mast_workCalendar": [D("status")],
    "u_mes_mast_workCalendarLine": [DD("workCalendarId", ("u_mes_mast_workCalendar", "name")), MD("lineId", "Line")],
    "u_mes_mast_workCalendarShift": [DD("workCalendarId", ("u_mes_mast_workCalendar", "name")), SH()],
    "u_mes_mast_workCalendarWeeklyOffDay": [DD("workCalendarId", ("u_mes_mast_workCalendar", "name")), D("weeklyOffDay")],
    "u_mes_mast_workCalendarException": [DD("workCalendarId", ("u_mes_mast_workCalendar", "name")), D("exceptionType"), D("isWorking")],
    "u_mes_mast_workCalendarExceptionShift": [DD("workCalendarExceptionId", ("u_mes_mast_workCalendarException", "recordNo")), SH()],
    "u_mes_mast_shiftRoster": [R("productionDate", -7, 0), MD("lineId", "Line"), SH(), D("status")],
    "u_mes_mast_shiftRosterAssignment": [DS("shiftRosterId", ("u_mes_mast_shiftRoster", "recordNo")), DS("userId", ("u_mes_mast_user", "fullName")), DS("replacedUserId", ("u_mes_mast_user", "fullName")), D("roleInCrew"), D("attendance"), D("assignmentSource")],
    "u_mes_mast_role": [D("status"), D("scope"), D("canSign"), D("isSystemRole")],
    "u_mes_mast_rolePermission": [DD("roleId", ("u_mes_mast_role", "name")), DD("permissionId", ("u_mes_mast_permission", "name"))],
    "u_mes_mast_roleSignatureMeaning": [DD("roleId", ("u_mes_mast_role", "name")), DD("signatureMeaningId", ("u_mes_mast_signatureMeaning", "name"))],
    "u_mes_mast_user": [D("status"), DD("departmentId", ("u_mes_mast_department", "name")), DD("designationId", ("u_mes_mast_designation", "name")), D("userType"), D("isLocked")],
    "u_mes_mast_userRole": [DS("userId", ("u_mes_mast_user", "fullName")), DD("roleId", ("u_mes_mast_role", "name"))],
    "u_mes_mast_skill": [D("status"), DD("skillCategoryId", ("u_mes_mast_skillCategory", "name")), D("assessmentMethod"), D("isSafetyCritical")],
    "u_mes_mast_skillOperation": [DD("skillId", ("u_mes_mast_skill", "name")), MD("operationId", "Operation")],
    "u_mes_mast_skillLevelScale": [DD("skillId", ("u_mes_mast_skill", "name"))],
    "u_mes_mast_skillCertification": [R("awardedAt", -30, 0), D("status"), DS("userId", ("u_mes_mast_user", "fullName")), DD("skillId", ("u_mes_mast_skill", "name")), D("assessmentMethod")],
    "u_mes_mast_customer": [D("status"), DD("billingAddressCountryId", ("u_mes_mast_country", "name")), DD("labelTemplateId", ("u_mes_matl_labelTemplate", "name")), D("customerType"), D("asnRequired")],
    "u_mes_mast_customerShipTo": [MD("customerId", "Customer")],
    "u_mes_mast_customerContact": [MD("customerId", "Customer"), D("businessFunction")],
    "u_mes_mast_supplier": [D("status"), DD("commodityId", ("u_mes_mast_commodity", "name")), DD("addressCountryId", ("u_mes_mast_country", "name")), D("supplierType"), D("isDirectedSource")],
    "u_mes_mast_supplierContact": [MD("supplierId", "Supplier"), D("businessFunction")],
    "u_mes_mast_supplierCertificate": [MD("supplierId", "Supplier")],
    "u_mes_mast_supplierSuppliedItem": [MD("supplierId", "Supplier"), MD("suppliedItemId", "Item"), D("qualificationStatus")],
    "u_mes_mast_unitOfMeasure": [D("status"), DD("baseUnitOfMeasureId", ("u_mes_mast_unitOfMeasure", "name")), D("scope"), D("isBaseUnit")],
    "u_mes_mast_department": [D("status"), DD("parentDepartmentId", ("u_mes_mast_department", "name")), DD("costCenterId", ("u_mes_mast_costCenter", "name"))],
    "u_mes_mast_designation": [D("status"), DD("departmentId", ("u_mes_mast_department", "name")), D("isSupervisory")],
    "u_mes_mast_employmentType": [D("status"), D("isContract")],
    "u_mes_mast_costCenter": [D("status")],
    "u_mes_mast_manufacturer": [D("status"), DD("countryId", ("u_mes_mast_country", "name"))],
    "u_mes_mast_equipmentType": [D("status")],
    "u_mes_mast_skillCategory": [D("status")],
    "u_mes_mast_permission": [D("status")],
    "u_mes_mast_signatureMeaning": [D("status")],
    "u_mes_mast_currency": [D("status")],
    "u_mes_mast_country": [D("status")],
    "u_mes_mast_language": [D("status")],
    "u_mes_mast_transporter": [D("status")],
    "u_mes_mast_commodity": [D("status")],
    "u_mes_mast_roleRequiredSkill": [DD("roleId", ("u_mes_mast_role", "name")), DD("requiredSkillId", ("u_mes_mast_skill", "name"))],
    "u_mes_prod_item": [D("status"), DD("itemGroupId", ("u_mes_prod_itemGroup", "name")), DD("baseUnitOfMeasureId", ("u_mes_mast_unitOfMeasure", "name")), D("itemType"), D("isSerialised"), D("isLotControlled")],
    "u_mes_prod_itemRevision": [MD("itemId", "Item"), DS("engineeringChangeId", ("u_mes_prod_engineeringChange", "title"))],
    "u_mes_prod_itemCustomerPart": [MD("itemId", "Item"), MD("customerId", "Customer")],
    "u_mes_prod_productVariant": [D("status"), MD("baseItemId", "Item"), MD("variantItemId", "Item"), D("optionsHand")],
    "u_mes_prod_billOfMaterial": [D("status"), MD("itemId", "Item"), DD("baseUnitOfMeasureId", ("u_mes_mast_unitOfMeasure", "name")), D("bomType")],
    "u_mes_prod_billOfMaterialComponent": [DD("billOfMaterialId", ("u_mes_prod_billOfMaterial", "recordNo")), MD("componentItemId", "Item"), MD("operationId", "Operation"), D("traceLevel"), D("isTraceable"), D("backflush")],
    "u_mes_prod_billOfMaterialComponentProductVariant": [DD("billOfMaterialComponentId", ("u_mes_prod_billOfMaterialComponent", "recordNo")), MD("productVariantId", "ProductVariant")],
    "u_mes_prod_billOfMaterialComponentAlternateItem": [DD("billOfMaterialComponentId", ("u_mes_prod_billOfMaterialComponent", "recordNo")), MD("alternateItemId", "Item")],
    "u_mes_prod_operation": [D("status"), MD("defaultWorkCenterId", "WorkCenter"), D("trackingGrain"), D("isInspection"), D("isSpecialProcess")],
    "u_mes_prod_operationRequiredSkill": [MD("operationId", "Operation"), DD("requiredSkillId", ("u_mes_mast_skill", "name"))],
    "u_mes_prod_routing": [D("status"), MD("itemId", "Item"), DD("parentRoutingId", ("u_mes_prod_routing", "description")), D("routingType")],
    "u_mes_prod_routingStep": [DD("routingId", ("u_mes_prod_routing", "description")), MD("operationId", "Operation"), MD("workCenterId", "WorkCenter"), D("isMilestone"), D("isOptional")],
    "u_mes_prod_routingStepAlternateWorkCenter": [DD("routingStepId", ("u_mes_prod_routingStep", "recordNo")), MD("alternateWorkCenterId", "WorkCenter")],
    "u_mes_prod_routingStepNextStep": [DD("routingStepId", ("u_mes_prod_routingStep", "recordNo")), D("nextStepCondition")],
    "u_mes_prod_billOfProcess": [D("status"), MD("itemId", "Item")],
    "u_mes_prod_billOfProcessStep": [DD("billOfProcessId", ("u_mes_prod_billOfProcess", "recordNo")), MD("operationId", "Operation"), DD("recipeId", ("u_mes_prod_recipe", "name")), DD("workInstructionId", ("u_mes_prod_workInstruction", "title")), DD("inspectionPlanId", ("u_mes_qual_inspectionPlan", "name"))],
    "u_mes_prod_billOfProcessStepEquipment": [DD("billOfProcessStepId", ("u_mes_prod_billOfProcessStep", "recordNo")), MD("equipmentId", "Equipment")],
    "u_mes_prod_billOfProcessStepTool": [DD("billOfProcessStepId", ("u_mes_prod_billOfProcessStep", "recordNo")), DS("toolId", ("u_mes_maint_tool", "name"))],
    "u_mes_prod_billOfProcessStepRequiredSkill": [DD("billOfProcessStepId", ("u_mes_prod_billOfProcessStep", "recordNo")), DD("requiredSkillId", ("u_mes_mast_skill", "name"))],
    "u_mes_prod_billOfProcessStepConsumedComponent": [DD("billOfProcessStepId", ("u_mes_prod_billOfProcessStep", "recordNo")), MD("itemId", "Item"), D("verifyByScan")],
    "u_mes_prod_billOfProcessStepInterlock": [DD("billOfProcessStepId", ("u_mes_prod_billOfProcessStep", "recordNo")), D("interlockType"), D("enforced")],
    "u_mes_prod_billOfProcessStepProcessParameter": [DD("billOfProcessStepId", ("u_mes_prod_billOfProcessStep", "recordNo"))],
    "u_mes_prod_workInstruction": [D("status"), MD("itemId", "Item"), MD("operationId", "Operation"), D("generationSource"), D("readAcknowledgementRequired"), D("reacknowledgeOnRevision")],
    "u_mes_prod_workInstructionStep": [DD("workInstructionId", ("u_mes_prod_workInstruction", "title")), DS("arContentControlledDocumentId", ("u_mes_syst_controlledDocument", "title")), D("inputType"), D("isMandatory"), D("requiresScan")],
    "u_mes_prod_workInstructionStepMediaControlledDocument": [DD("workInstructionStepId", ("u_mes_prod_workInstructionStep", "recordNo")), DS("mediaControlledDocumentId", ("u_mes_syst_controlledDocument", "title"))],
    "u_mes_prod_workInstructionStepProductVariant": [DD("workInstructionStepId", ("u_mes_prod_workInstructionStep", "recordNo")), MD("productVariantId", "ProductVariant")],
    "u_mes_prod_workInstructionStepTool": [DD("workInstructionStepId", ("u_mes_prod_workInstructionStep", "recordNo")), DS("toolId", ("u_mes_maint_tool", "name"))],
    "u_mes_prod_workInstructionStepCharacteristic": [DD("workInstructionStepId", ("u_mes_prod_workInstructionStep", "recordNo")), DS("characteristicId", ("u_mes_qual_characteristic", "name"))],
    "u_mes_prod_workInstructionPpeItem": [DD("workInstructionId", ("u_mes_prod_workInstruction", "title")), DD("ppeItemId", ("u_mes_prod_ppeItem", "name"))],
    "u_mes_prod_workInstructionKeyPoint": [DD("workInstructionId", ("u_mes_prod_workInstruction", "title"))],
    "u_mes_prod_recipe": [D("status"), MD("equipmentId", "Equipment"), MD("itemId", "Item"), D("origin"), D("isGoldenRecipe")],
    "u_mes_prod_recipeParameter": [DD("recipeId", ("u_mes_prod_recipe", "name")), DS("processTagId", ("u_mes_perf_processTag", "description")), D("isCritical"), D("downloadToController")],
    "u_mes_prod_recipeStage": [DD("recipeId", ("u_mes_prod_recipe", "name"))],
    "u_mes_prod_engineeringChange": [R("raisedAt", -30, 0), D("status"), MD("customerId", "Customer"), MD("stockDispositionTypeId", "DispositionType"), D("changeType")],
    "u_mes_prod_engineeringChangeAffectedItem": [DS("engineeringChangeId", ("u_mes_prod_engineeringChange", "title")), MD("itemId", "Item")],
    "u_mes_prod_engineeringChangeAffectedObject": [DS("engineeringChangeId", ("u_mes_prod_engineeringChange", "title")), D("changeAction")],
    "u_mes_prod_engineeringChangeApproval": [DS("engineeringChangeId", ("u_mes_prod_engineeringChange", "title")), DS("userId", ("u_mes_mast_user", "fullName")), D("businessFunction"), D("decision")],
    "u_mes_prod_engineeringChangeControlledDocument": [DS("engineeringChangeId", ("u_mes_prod_engineeringChange", "title")), DS("controlledDocumentId", ("u_mes_syst_controlledDocument", "title"))],
    "u_mes_prod_itemGroup": [D("status")],
    "u_mes_prod_itemFamily": [D("status")],
    "u_mes_prod_ppeItem": [D("status")],
    "u_mes_prod_market": [D("status")],
    "u_mes_prod_padCompound": [D("status")],
    "u_mes_prod_surfaceFinish": [D("status")],
    "u_mes_prod_vehicleModel": [D("status"), MD("customerId", "Customer")],
    "u_mes_prod_recipeProductVariant": [DD("recipeId", ("u_mes_prod_recipe", "name")), MD("productVariantId", "ProductVariant")],
    "u_mes_prod_recipeControlledDocument": [DD("recipeId", ("u_mes_prod_recipe", "name")), DS("controlledDocumentId", ("u_mes_syst_controlledDocument", "title")), D("fileRole")],
    "u_mes_prod_workInstructionWorkCenter": [DD("workInstructionId", ("u_mes_prod_workInstruction", "title")), MD("workCenterId", "WorkCenter")],
    "u_mes_prod_workInstructionProductVariant": [DD("workInstructionId", ("u_mes_prod_workInstruction", "title")), MD("productVariantId", "ProductVariant")],
    "u_mes_qual_characteristic": [D("status"), MD("itemId", "Item"), MD("operationId", "Operation"), D("characteristicType"), D("isSpc")],
    "u_mes_qual_controlPlan": [D("status"), MD("itemId", "Item"), DD("pfmeaId", ("u_mes_qual_pfmea", "title")), D("phase")],
    "u_mes_qual_controlPlanCoreTeamUser": [DD("controlPlanId", ("u_mes_qual_controlPlan", "recordNo")), DS("coreTeamUserId", ("u_mes_mast_user", "fullName"))],
    "u_mes_qual_controlPlanLine": [DD("controlPlanId", ("u_mes_qual_controlPlan", "recordNo")), MD("operationId", "Operation"), DS("characteristicId", ("u_mes_qual_characteristic", "name")), DS("gaugeId", ("u_mes_qual_gauge", "name")), D("classification")],
    "u_mes_qual_inspectionPlan": [D("status"), DD("controlPlanId", ("u_mes_qual_controlPlan", "recordNo")), MD("itemId", "Item"), D("planType"), D("blockOnFail")],
    "u_mes_qual_inspectionPlanLine": [DD("inspectionPlanId", ("u_mes_qual_inspectionPlan", "name")), DS("characteristicId", ("u_mes_qual_characteristic", "name")), DS("gaugeId", ("u_mes_qual_gauge", "name")), MD("defectCodeId", "DefectCode"), D("frequencyType"), D("recordType"), D("autoNcOnFail"), D("overrideAllowed")],
    "u_mes_qual_samplingPlan": [D("status"), D("samplingType"), D("inspectionLevel"), D("frequencyType"), D("skipLotEnabled")],
    "u_mes_qual_samplingPlanSizeRow": [DD("samplingPlanId", ("u_mes_qual_samplingPlan", "name"))],
    "u_mes_qual_checkSheet": [D("status"), MD("workCenterId", "WorkCenter"), MD("equipmentId", "Equipment"), D("checkSheetType"), D("masterSampleRequired")],
    "u_mes_qual_checkSheetItem": [DD("checkSheetId", ("u_mes_qual_checkSheet", "name")), D("answerType"), D("isCritical")],
    "u_mes_qual_checkSheetResult": [R("startedAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), MD("workCenterId", "WorkCenter"), MD("equipmentId", "Equipment"), SH(), D("status"), DD("checkSheetId", ("u_mes_qual_checkSheet", "name")), D("overallResult")],
    "u_mes_qual_checkSheetResultAnswer": [DS("checkSheetResultId", ("u_mes_qual_checkSheetResult", "recordNo")), D("passed")],
    "u_mes_qual_inspectionResult": [R("measuredAt", -7, 0), DS("wipUnitId", ("u_mes_plan_wipUnit", "recordNo")), MD("workCenterId", "WorkCenter"), D("status"), DD("inspectionPlanId", ("u_mes_qual_inspectionPlan", "name")), MD("itemId", "Item"), D("inspectionType"), D("overridden")],
    "u_mes_qual_spcChart": [D("status"), MD("itemId", "Item"), MD("workCenterId", "WorkCenter"), D("chartType")],
    "u_mes_qual_spcChartControlLimit": [DD("spcChartId", ("u_mes_qual_spcChart", "name"))],
    "u_mes_qual_spcChartRule": [DD("spcChartId", ("u_mes_qual_spcChart", "name")), D("rule")],
    "u_mes_qual_spcSample": [R("sampledAt", -7, 0), MD("workCenterId", "WorkCenter"), SH(), D("status"), DD("spcChartId", ("u_mes_qual_spcChart", "name")), D("reactionType")],
    "u_mes_qual_spcSampleReading": [DS("spcSampleId", ("u_mes_qual_spcSample", "recordNo"))],
    "u_mes_qual_spcSampleInspectionResult": [DS("spcSampleId", ("u_mes_qual_spcSample", "recordNo")), DS("inspectionResultId", ("u_mes_qual_inspectionResult", "recordNo"))],
    "u_mes_qual_spcSampleViolation": [DS("spcSampleId", ("u_mes_qual_spcSample", "recordNo")), D("rule")],
    "u_mes_qual_defectCode": [D("status"), DD("defectGroupId", ("u_mes_qual_defectGroup", "name")), MD("defaultDispositionTypeId", "DispositionType"), D("scrapCostCategory"), D("isSafetyRelated"), D("requiresPhoto")],
    "u_mes_qual_defectCodeApplicableOperation": [MD("defectCodeId", "DefectCode"), MD("applicableOperationId", "Operation")],
    "u_mes_qual_nonconformance": [R("detectedAt", -7, 0), D("status"), MD("detectedAtOperationId", "Operation"), MD("detectedAtWorkCenterId", "WorkCenter"), D("ncType")],
    "u_mes_qual_nonconformanceAffectedObject": [DS("nonconformanceId", ("u_mes_qual_nonconformance", "title")), MD("dispositionTypeId", "DispositionType"), DS("dispositionById", ("u_mes_mast_user", "fullName"))],
    "u_mes_qual_nonconformanceContainmentAction": [DS("nonconformanceId", ("u_mes_qual_nonconformance", "title")), DS("ownerUserId", ("u_mes_mast_user", "fullName"))],
    "u_mes_qual_nonconformanceInspectionResult": [DS("nonconformanceId", ("u_mes_qual_nonconformance", "title")), DS("inspectionResultId", ("u_mes_qual_inspectionResult", "recordNo"))],
    "u_mes_qual_nonconformanceReworkOrder": [DS("nonconformanceId", ("u_mes_qual_nonconformance", "title")), DS("reworkOrderId", ("u_mes_qual_reworkOrder", "recordNo"))],
    "u_mes_qual_nonconformanceScrapRecord": [DS("nonconformanceId", ("u_mes_qual_nonconformance", "title")), DS("scrapRecordId", ("u_mes_qual_scrapRecord", "recordNo"))],
    "u_mes_qual_nonconformancePhotoControlledDocument": [DS("nonconformanceId", ("u_mes_qual_nonconformance", "title")), DS("photoControlledDocumentId", ("u_mes_syst_controlledDocument", "title"))],
    "u_mes_qual_nonconformanceMrbUser": [DS("nonconformanceId", ("u_mes_qual_nonconformance", "title")), DS("mrbUserId", ("u_mes_mast_user", "fullName"))],
    "u_mes_qual_reworkOrder": [R("startedAt", -7, 0), DS("lotId", ("u_mes_plan_lot", "recordNo")), MD("workCenterId", "WorkCenter"), D("status"), MD("itemId", "Item"), DD("reworkRoutingId", ("u_mes_prod_routing", "description")), D("reworkType")],
    "u_mes_qual_reworkOrderWipUnit": [DS("reworkOrderId", ("u_mes_qual_reworkOrder", "recordNo")), DS("wipUnitId", ("u_mes_plan_wipUnit", "recordNo"))],
    "u_mes_qual_reworkOrderStep": [DS("reworkOrderId", ("u_mes_qual_reworkOrder", "recordNo")), MD("operationId", "Operation"), DS("completedById", ("u_mes_mast_user", "fullName"))],
    "u_mes_qual_scrapRecord": [R("declaredAt", -7, 0), DS("wipUnitId", ("u_mes_plan_wipUnit", "recordNo")), MD("workCenterId", "WorkCenter"), SH(), D("status"), MD("defectCodeId", "DefectCode"), MD("itemId", "Item")],
    "u_mes_qual_qualityHold": [R("placedAt", -7, 0), D("status"), MD("reasonCodeId", "ReasonCode"), MD("itemId", "Item"), D("holdType")],
    "u_mes_qual_qualityHoldHeldObject": [DS("qualityHoldId", ("u_mes_qual_qualityHold", "recordNo")), D("releaseDecision")],
    "u_mes_qual_deviationPermit": [R("requestedAt", -7, 0), D("status"), MD("itemId", "Item"), MD("customerId", "Customer"), D("deviationType")],
    "u_mes_qual_deviationPermitApproval": [DS("deviationPermitId", ("u_mes_qual_deviationPermit", "title")), DS("userId", ("u_mes_mast_user", "fullName")), D("businessFunction"), D("decision")],
    "u_mes_qual_capa": [R("openedAt", -7, 0), D("status"), MD("itemId", "Item"), MD("customerId", "Customer"), D("capaType")],
    "u_mes_qual_capaNonconformance": [DS("capaId", ("u_mes_qual_capa", "title")), DS("nonconformanceId", ("u_mes_qual_nonconformance", "title"))],
    "u_mes_qual_capaTeamMember": [DS("capaId", ("u_mes_qual_capa", "title")), DS("userId", ("u_mes_mast_user", "fullName")), D("roleInTeam")],
    "u_mes_qual_capaContainmentAction": [DS("capaId", ("u_mes_qual_capa", "title")), DS("ownerUserId", ("u_mes_mast_user", "fullName"))],
    "u_mes_qual_capaCorrectiveAction": [DS("capaId", ("u_mes_qual_capa", "title")), DS("ownerUserId", ("u_mes_mast_user", "fullName"))],
    "u_mes_qual_capaImplementationAction": [DS("capaId", ("u_mes_qual_capa", "title")), DS("verifiedById", ("u_mes_mast_user", "fullName")), D("effective")],
    "u_mes_qual_capaControlledDocument": [DS("capaId", ("u_mes_qual_capa", "title")), DS("controlledDocumentId", ("u_mes_syst_controlledDocument", "title"))],
    "u_mes_qual_pfmea": [D("status"), MD("itemId", "Item"), DD("controlPlanId", ("u_mes_qual_controlPlan", "recordNo")), D("methodology")],
    "u_mes_qual_pfmeaCoreTeamUser": [DD("pfmeaId", ("u_mes_qual_pfmea", "title")), DS("coreTeamUserId", ("u_mes_mast_user", "fullName"))],
    "u_mes_qual_pfmeaLine": [DD("pfmeaId", ("u_mes_qual_pfmea", "title")), MD("operationId", "Operation"), DS("characteristicId", ("u_mes_qual_characteristic", "name")), DS("ownerUserId", ("u_mes_mast_user", "fullName")), D("classification"), D("actionPriority")],
    "u_mes_qual_ppapSubmission": [R("pswSignedAt", -30, 0), D("status"), MD("itemId", "Item"), MD("customerId", "Customer"), D("submissionReason")], # F6: no required date key
    "u_mes_qual_ppapSubmissionElement": [DS("ppapSubmissionId", ("u_mes_qual_ppapSubmission", "recordNo")), D("status"), DS("controlledDocumentId", ("u_mes_syst_controlledDocument", "title")), D("required")],
    "u_mes_qual_ppapSubmissionMsaStudy": [DS("ppapSubmissionId", ("u_mes_qual_ppapSubmission", "recordNo")), DS("msaStudyId", ("u_mes_qual_msaStudy", "recordNo"))],
    "u_mes_qual_gauge": [D("status"), DD("gaugeTypeId", ("u_mes_qual_gaugeType", "name")), DD("manufacturerId", ("u_mes_mast_manufacturer", "name")), D("calibrationSource"), D("isMasterGauge"), D("blockedForUse")],
    "u_mes_qual_gaugeCalibration": [R("calibratedAt", -30, 0), D("status"), MD("calibrationSupplierId", "Supplier"), D("calibrationType"), D("asFoundResult")],
    "u_mes_qual_gaugeCalibrationReading": [DS("gaugeCalibrationId", ("u_mes_qual_gaugeCalibration", "recordNo")), D("withinTolerance")],
    "u_mes_qual_msaStudy": [R("nextStudyDueAt", -30, 0), D("status"), MD("itemId", "Item"), D("studyType"), D("studyMethod")],
    "u_mes_qual_msaStudyAppraiserUser": [DS("msaStudyId", ("u_mes_qual_msaStudy", "recordNo")), DS("appraiserUserId", ("u_mes_mast_user", "fullName"))],
    "u_mes_qual_msaStudyTrial": [DS("msaStudyId", ("u_mes_qual_msaStudy", "recordNo")), DS("appraiserUserId", ("u_mes_mast_user", "fullName"))],
    "u_mes_qual_audit": [R("startedAt", -7, 0), MD("areaId", "Area"), MD("lineId", "Line"), D("status"), MD("customerId", "Customer"), DD("checkSheetId", ("u_mes_qual_checkSheet", "name")), D("auditType")],
    "u_mes_qual_auditAuditorUser": [DS("auditId", ("u_mes_qual_audit", "title")), DS("auditorUserId", ("u_mes_mast_user", "fullName"))],
    "u_mes_qual_auditFinding": [DS("auditId", ("u_mes_qual_audit", "title")), DS("ownerUserId", ("u_mes_mast_user", "fullName")), DS("capaId", ("u_mes_qual_capa", "title")), D("grade")],
    "u_mes_qual_customerComplaint": [R("reportedAt", -7, 0), D("status"), MD("customerId", "Customer"), MD("complaintTypeId", "ComplaintType")],
    "u_mes_qual_customerComplaintSerialNumber": [DS("customerComplaintId", ("u_mes_qual_customerComplaint", "description")), DS("serialNumberId", ("u_mes_trac_serialNumber", "recordNo"))],
    "u_mes_qual_customerComplaintShipment": [DS("customerComplaintId", ("u_mes_qual_customerComplaint", "description")), DS("shipmentId", ("u_mes_matl_shipment", "recordNo"))],
    "u_mes_qual_customerComplaintSuspectLot": [DS("customerComplaintId", ("u_mes_qual_customerComplaint", "description")), DS("suspectLotId", ("u_mes_plan_lot", "recordNo"))],
    "u_mes_qual_customerComplaintCommunication": [DS("customerComplaintId", ("u_mes_qual_customerComplaint", "description")), DS("authorUserId", ("u_mes_mast_user", "fullName")), D("direction")],
    "u_mes_qual_defectGroup": [D("status")],
    "u_mes_qual_gaugeType": [D("status")],
    "u_mes_qual_dispositionType": [D("status"), D("requiresRework"), D("requiresScrap")],
    "u_mes_qual_complaintType": [D("status")],
    "u_mes_qual_characteristicPosition": [DS("characteristicId", ("u_mes_qual_characteristic", "name")), DD("curveEnvelopeId", ("u_mes_qual_curveEnvelope", "name"))],
    "u_mes_qual_curveEnvelope": [D("status"), MD("productVariantId", "ProductVariant"), MD("operationId", "Operation"), D("curveType")],
    "u_mes_qual_curveEnvelopeWindow": [DD("curveEnvelopeId", ("u_mes_qual_curveEnvelope", "name")), D("windowType"), D("entrySide"), D("exitSide")],
    "u_mes_qual_measurementCurve": [R("capturedAt", -7, 0), DS("wipUnitId", ("u_mes_plan_wipUnit", "recordNo")), MD("equipmentId", "Equipment"), D("status"), DD("curveEnvelopeId", ("u_mes_qual_curveEnvelope", "name")), D("result")],
    "u_mes_qual_measurementCurvePoint": [R("sampledAt", -7, 0), DS("measurementCurveId", ("u_mes_qual_measurementCurve", "recordNo"))],
    "u_mes_qual_defectRecord": [R("detectedAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), MD("equipmentId", "Equipment"), SH(), D("status"), MD("defectCodeId", "DefectCode"), MD("productVariantId", "ProductVariant")],
    "u_mes_qual_auditSchedule": [D("status"), MD("areaId", "Area"), MD("lineId", "Line"), D("auditType")],
    "u_mes_qual_inspectionPlanProductVariant": [DD("inspectionPlanId", ("u_mes_qual_inspectionPlan", "name")), MD("productVariantId", "ProductVariant")],
    "u_mes_qual_environmentalMonitoringPoint": [D("status"), MD("areaId", "Area"), MD("workCenterId", "WorkCenter"), D("monitoredParameter")],
    "u_mes_qual_environmentalMonitoringResult": [R("sampledAt", -7, 0), D("status"), DD("environmentalMonitoringPointId", ("u_mes_qual_environmentalMonitoringPoint", "name")), D("limitEvaluation")],
    "u_mes_qual_retentionSample": [R("collectedAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), DS("storageLocationId", ("u_mes_matl_storageLocation", "name")), D("status"), MD("itemId", "Item"), D("sampleType")],
    "u_mes_qual_riskAssessment": [R("approvedAt", -30, 0), D("status"), DD("pfmeaId", ("u_mes_qual_pfmea", "title")), D("assessmentMethod"), D("initialRiskLevel")], # F6: no required date key
    "u_mes_qual_productQualityReview": [R("reviewPeriodFromDate", -30, 0), D("status"), MD("itemId", "Item")],
    "u_mes_qual_productRecall": [R("initiatedAt", -30, 0), D("status"), MD("customerId", "Customer"), D("recallClass"), D("recallScope")],
    "u_mes_qual_productRecallLot": [DS("productRecallId", ("u_mes_qual_productRecall", "title")), DS("lotId", ("u_mes_plan_lot", "recordNo"))],
    "u_mes_qual_processValidation": [R("plannedStartDate", -30, 0), MD("lineId", "Line"), D("status"), MD("itemId", "Item"), D("validationStage")],
    "u_mes_perf_reasonCode": [D("status"), MD("parentReasonCodeId", "ReasonCode"), DD("reasonCategoryId", ("u_mes_perf_reasonCategory", "name")), D("oeeImpact"), D("isPlanned"), D("requiresComment")],
    "u_mes_perf_equipmentState": [R("startedAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), MD("workCenterId", "WorkCenter"), MD("equipmentId", "Equipment"), SH(), D("status"), D("stateCode"), D("source")],
    "u_mes_perf_downtimeEventComment": [DS("downtimeEventId", ("u_mes_perf_downtimeEvent", "recordNo")), DS("authorUserId", ("u_mes_mast_user", "fullName"))],
    "u_mes_perf_productionCount": [R("productionDate", -10, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), MD("lineId", "Line"), MD("workCenterId", "WorkCenter"), SH(), D("status"), MD("itemId", "Item"), D("source")],
    "u_mes_perf_oeeRecord": [R("periodStartAt", -10, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), MD("lineId", "Line"), MD("equipmentId", "Equipment"), SH(), D("status"), MD("itemId", "Item")],
    "u_mes_perf_oeeRecordLoss": [DS("oeeRecordId", ("u_mes_perf_oeeRecord", "recordNo")), MD("lossCategoryId", "LossCategory"), MD("reasonCodeId", "ReasonCode")],
    "u_mes_perf_processTag": [D("status"), MD("equipmentId", "Equipment"), DD("iotDeviceId", ("u_mes_syst_iotDevice", "name")), D("dataType"), D("isCritical"), D("historise")],
    "u_mes_perf_processReading": [R("timestamp", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), MD("areaId", "Area"), MD("equipmentId", "Equipment"), SH(), D("signalQuality")],
    "u_mes_perf_torqueResult": [R("tightenedAt", -7, 0), DS("wipUnitId", ("u_mes_plan_wipUnit", "recordNo")), MD("equipmentId", "Equipment"), D("status"), DD("recipeId", ("u_mes_prod_recipe", "name")), DD("controllerIotDeviceId", ("u_mes_syst_iotDevice", "name")), D("strategy")],
    "u_mes_perf_leakTestResult": [R("testedAt", -7, 0), DS("wipUnitId", ("u_mes_plan_wipUnit", "recordNo")), MD("equipmentId", "Equipment"), D("status"), DD("recipeId", ("u_mes_prod_recipe", "name")), DD("testerIotDeviceId", ("u_mes_syst_iotDevice", "name")), D("testMedium")],
    "u_mes_perf_leakTestResultStage": [DS("leakTestResultId", ("u_mes_perf_leakTestResult", "recordNo")), D("stageName"), D("stageResult")],
    "u_mes_perf_energyReading": [R("intervalStartAt", -7, 0), MD("lineId", "Line"), MD("equipmentId", "Equipment"), SH(), DD("meterIotDeviceId", ("u_mes_syst_iotDevice", "name")), MD("energyTypeId", "EnergyType"), D("signalQuality")],
    "u_mes_perf_lossCategory": [D("status"), D("oeeImpact")],
    "u_mes_perf_reasonCategory": [D("status")],
    "u_mes_perf_energyType": [D("status")],
    "u_mes_perf_alarmDefinition": [D("status"), DD("equipmentTypeId", ("u_mes_mast_equipmentType", "name")), DD("authorizingRoleId", ("u_mes_mast_role", "name")), D("alarmClass"), D("blocksRestart"), D("createsDowntime")],
    "u_mes_perf_lossSummary": [R("productionDate", -10, 0), MD("lineId", "Line"), MD("workCenterId", "WorkCenter"), SH(), D("status"), MD("lossCategoryId", "LossCategory"), MD("reasonCodeId", "ReasonCode")],
    "u_mes_perf_operatorPerformance": [R("productionDate", -10, 0), MD("workCenterId", "WorkCenter"), SH(), D("status"), DS("userId", ("u_mes_mast_user", "fullName")), MD("productVariantId", "ProductVariant")],
    "u_mes_syst_erpMessage": [R("createdInSourceAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), D("status"), DD("integrationConnectorId", ("u_mes_syst_integrationConnector", "name")), D("direction"), D("messageType")],
    "u_mes_syst_integrationConnector": [D("status"), D("protocol"), D("environment"), D("authMethod")],
    "u_mes_syst_integrationConnectorFunction": [DD("integrationConnectorId", ("u_mes_syst_integrationConnector", "name")), D("direction"), D("messageType")],
    "u_mes_syst_iotDevice": [D("status"), DD("deviceTypeId", ("u_mes_syst_deviceType", "name")), DD("manufacturerId", ("u_mes_mast_manufacturer", "name")), D("protocol")],
    "u_mes_syst_operatorApp": [D("status"), D("appType")],
    "u_mes_syst_operatorAppWorkCenter": [DD("operatorAppId", ("u_mes_syst_operatorApp", "name")), MD("workCenterId", "WorkCenter")],
    "u_mes_syst_operatorAppOperation": [DD("operatorAppId", ("u_mes_syst_operatorApp", "name")), MD("operationId", "Operation")],
    "u_mes_syst_operatorAppStep": [DD("operatorAppId", ("u_mes_syst_operatorApp", "name")), DD("workInstructionId", ("u_mes_prod_workInstruction", "title")), DD("inspectionPlanId", ("u_mes_qual_inspectionPlan", "name")), D("widgetType")],
    "u_mes_syst_operatorAppStepTrigger": [DD("operatorAppStepId", ("u_mes_syst_operatorAppStep", "recordNo")), D("triggerEvent"), D("triggerAction")],
    "u_mes_syst_operatorAppDeviceBinding": [DD("operatorAppId", ("u_mes_syst_operatorApp", "name")), DD("iotDeviceId", ("u_mes_syst_iotDevice", "name")), D("purpose")],
    "u_mes_syst_operatorAppLanguage": [DD("operatorAppId", ("u_mes_syst_operatorApp", "name")), DD("languageId", ("u_mes_mast_language", "name"))],
    "u_mes_syst_businessEvent": [R("occurredAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), MD("workCenterId", "WorkCenter"), MD("equipmentId", "Equipment"), DS("userId", ("u_mes_mast_user", "fullName")), DD("iotDeviceId", ("u_mes_syst_iotDevice", "name")), D("eventType")],
    "u_mes_syst_auditTrail": [R("changedAt", -7, 0), D("changeAction")],
    "u_mes_syst_auditTrailChange": [DS("auditTrailId", ("u_mes_syst_auditTrail", "recordNo"))],
    "u_mes_syst_electronicSignature": [R("signedAt", -7, 0), DS("userId", ("u_mes_mast_user", "fullName")), DD("roleId", ("u_mes_mast_role", "name")), D("authenticationMethod")],
    "u_mes_syst_notification": [R("raisedAt", -7, 0), D("status"), MD("notificationTypeId", "NotificationType"), DD("alertRuleId", ("u_mes_syst_alertRule", "name"))],
    "u_mes_syst_notificationRecipient": [DS("notificationId", ("u_mes_syst_notification", "title")), DS("userId", ("u_mes_mast_user", "fullName")), DD("roleId", ("u_mes_mast_role", "name")), D("channel")],
    "u_mes_syst_controlledDocument": [R("effectiveFrom", -30, 0), D("status"), MD("documentTypeId", "DocumentType"), MD("itemId", "Item"), D("storageProvider")],
    "u_mes_syst_controlledDocumentTag": [DS("controlledDocumentId", ("u_mes_syst_controlledDocument", "title"))],
    "u_mes_syst_numberRange": [D("status"), MD("itemId", "Item"), D("rangeType"), D("resetPolicy")],
    "u_mes_syst_systemConfiguration": [D("status"), D("module"), D("valueType"), D("scope"), D("configValueFlag"), D("isEditable")],
    "u_mes_syst_documentType": [D("status"), D("isControlled")],
    "u_mes_syst_deviceType": [D("status")],
    "u_mes_syst_notificationType": [D("status")],
    "u_mes_syst_statusDefinition": [D("status"), D("isInitial"), D("isFinal")],
    "u_mes_syst_enumerationValue": [D("status"), D("isDefault")],
    "u_mes_syst_statusTransition": [D("status"), D("requiresSignature"), D("requiresReason")],
    "u_mes_syst_interlockRule": [D("status"), MD("lineId", "Line"), MD("workCenterId", "WorkCenter"), D("transactionPoint"), D("overrideAllowed"), D("overrideRequiresSignature")],
    "u_mes_syst_statusTransitionRole": [DD("statusTransitionId", ("u_mes_syst_statusTransition", "transitionName")), DD("roleId", ("u_mes_mast_role", "name"))],
    "u_mes_syst_escalationRule": [D("status"), MD("lineId", "Line"), DD("firstResponderRoleId", ("u_mes_mast_role", "name")), D("sourceType")],
    "u_mes_syst_escalationRuleLevel": [DD("escalationRuleId", ("u_mes_syst_escalationRule", "name")), DD("roleId", ("u_mes_mast_role", "name")), MD("notificationTypeId", "NotificationType"), D("basis"), D("channel")],
    "u_mes_syst_alertRule": [D("status"), MD("lineId", "Line"), MD("workCenterId", "WorkCenter"), D("metric")],
    "u_mes_syst_analyticsModel": [D("status"), MD("equipmentId", "Equipment"), D("modelType")],
    "u_mes_syst_modelPrediction": [R("predictedAt", -7, 0), MD("workCenterId", "WorkCenter"), SH(), D("status"), DD("analyticsModelId", ("u_mes_syst_analyticsModel", "name")), MD("productVariantId", "ProductVariant"), D("predictionType")],
    "u_mes_syst_simulationStudy": [R("inputSnapshotAt", -7, 0), D("status"), DD("recommendedRecipeId", ("u_mes_prod_recipe", "name")), D("studyType"), D("comparisonResult")],
    "u_mes_syst_recordPolicy": [D("status"), DD("lockOnStatusDefinitionId", ("u_mes_syst_statusDefinition", "statusName")), DD("editRoleId", ("u_mes_mast_role", "name")), D("editPolicy"), D("requiresReasonForEdit"), D("requiresSignatureForEdit")],
    "u_mes_syst_savedView": [D("status"), DD("roleId", ("u_mes_mast_role", "name")), D("viewType"), D("isShared")],
    "u_mes_syst_backupRun": [R("startedAt", -7, 0), D("status"), D("runType")],
    "u_mes_syst_computerisedSystem": [D("status"), MD("supplierId", "Supplier"), MD("equipmentId", "Equipment"), D("systemCategory"), D("holdsElectronicRecords"), D("usesElectronicSignatures")],
    "u_mes_syst_systemValidation": [R("plannedStartDate", -30, 0), D("status"), DD("computerisedSystemId", ("u_mes_syst_computerisedSystem", "name")), D("validationType"), D("assuranceApproach")],
    "u_mes_syst_systemPeriodicReview": [R("reviewPeriodFromDate", -30, 0), D("status"), DD("computerisedSystemId", ("u_mes_syst_computerisedSystem", "name"))],
    "u_mes_syst_auditTrailReview": [R("reviewFromAt", -30, 0), D("status"), DD("computerisedSystemId", ("u_mes_syst_computerisedSystem", "name")), D("reviewType")],
    "u_mes_syst_userAccessReview": [R("reviewPeriodFromDate", -30, 0), D("status"), DD("computerisedSystemId", ("u_mes_syst_computerisedSystem", "name"))],
    "u_mes_syst_userAccessReviewLine": [DS("userAccessReviewId", ("u_mes_syst_userAccessReview", "recordNo")), DS("userId", ("u_mes_mast_user", "fullName")), DD("roleId", ("u_mes_mast_role", "name")), D("reviewAction"), D("accessStillRequired")],
    "u_mes_bmr_batchRecordReview": [R("productionReviewedAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), D("status"), MD("itemId", "Item"), D("reviewScope")], # F6: no required date key
    "u_mes_bmr_batchRecordReviewException": [DS("batchRecordReviewId", ("u_mes_bmr_batchRecordReview", "recordNo")), DS("assessedById", ("u_mes_mast_user", "fullName")), D("exceptionType"), D("assessment")],
    "u_mes_bmr_batchRelease": [R("releasedAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), D("status"), MD("itemId", "Item")], # F6: no required date key
    "u_mes_bmr_yieldReconciliation": [R("calculatedAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), D("status"), MD("itemId", "Item"), D("reconciliationType"), D("withinLimits")],
    "u_mes_bmr_batchManufacturingRecord": [R("openedAt", -7, 0), DS("productionOrderId", ("u_mes_plan_productionOrder", "recordNo")), D("status"), MD("itemId", "Item"), DD("masterManufacturingRecordId", ("u_mes_mmr_masterManufacturingRecord", "title"))],
    "u_mes_mmr_masterManufacturingRecord": [D("status"), DD("itemRevisionId", ("u_mes_prod_itemRevision", "recordNo")), MD("productVariantId", "ProductVariant")],
    "u_mes_mmr_masterManufacturingRecordRecipe": [DD("masterManufacturingRecordId", ("u_mes_mmr_masterManufacturingRecord", "title")), DD("recipeId", ("u_mes_prod_recipe", "name"))],
}
