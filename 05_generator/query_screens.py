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
}
