# u_mes_syst_numberRange

| Property | Value |
|---|---|
| Module | System and Integration (syst) |
| Purpose | Counters and format masks for serials, lots, orders, labels, NCRs |
| Kind | Entity |
| Data class | Master |
| Parent collection | none |
| _id pattern | 16-digit numeric string, unique across the database |
| Display value used by references | name |
| Keys | 24 (19 required, 5 may be null) |
| Estimated volume per year | 30-100 |
| Storage | standard |

## Structure

Flat entity collection: one document per number range, all keys top-level and scalar.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null. Date tag: Date = calendar date stored as 00:00:00 local plant time; Datetime = local plant time stored with the +0000 suffix (no UTC conversion).

| # | Key | BSON type | Date tag | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|---|
| 1 | _id | String | - | Yes | Unique identifier of the document. Pattern: 16-digit numeric string, unique across the database | `"1248000000000001"` |  |
| 2 | recordNo | String | - | Yes | Business identifier of the document, readable by people and unique within the site | `"SERIAL-FBC-LH"` |  |
| 3 | siteId | String | - | Yes | Reference to u_mes_mast_site._id: the site the document belongs to | `"1003000000000001"` | Reference: u_mes_mast_site._id |
| 4 | siteName | String | - | Yes | Display value of the site, copied from u_mes_mast_site.name | `"Chakan Plant, Pune"` |  |
| 5 | name | String | - | Yes | Name of the number range; used as its display value in other collections | `"Serial numbers, front caliper LH"` |  |
| 6 | rangeType | String | - | Yes | Range type | `"Serial Number"` | Serial Number; Lot Number; Order Number; Label Number; Document Number |
| 7 | itemId | String | - | No (null allowed) | Reference to u_mes_prod_item._id | `"1043000000000004"` | Reference: u_mes_prod_item._id |
| 8 | itemName | String | - | No (null allowed) | Display value of itemId, copied from u_mes_prod_item.description | `"Caliper Body Casting, LH, T6"` |  |
| 9 | prefix | String | - | Yes | Prefix of the number range | `"VB"` |  |
| 10 | formatMask | String | - | Yes | Format mask | `"VB{YY}{DDD}{SHIFT}{NNNNN}"` |  |
| 11 | currentValue | Int64 | - | Yes | Current value | `NumberLong("184")` |  |
| 12 | minValue | Int64 | - | Yes | Minimum value | `NumberLong("1")` |  |
| 13 | maxValue | Int64 | - | Yes | Maximum value | `NumberLong("99999")` |  |
| 14 | incrementById | String | - | Yes | Reference to u_mes_mast_user._id: user recorded for 'increment' | `"1029000000000001"` | Reference: u_mes_mast_user._id |
| 15 | incrementBy | String | - | Yes | Display name of the user in incrementById, copied from u_mes_mast_user.fullName | `"Sunil Jadhav"` |  |
| 16 | resetPolicy | String | - | Yes | Reset policy | `"Never"` | Never; Daily; Monthly; Yearly |
| 17 | lastResetAt | Date | Datetime | No (null allowed) | Last reset date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 18 | checkDigitMethod | String | - | No (null allowed) | Check digit method | `null` | None; Modulo 10; Modulo 43 |
| 19 | warnAtPct | Decimal128 | - | Yes | Warn at (percent) | `NumberDecimal("90.0")` |  |
| 20 | lastIssuedValue | Int64 | - | Yes | Last issued value | `NumberLong("184")` |  |
| 21 | lastIssuedAt | Date | Datetime | No (null allowed) | Last issued date and time. Datetime field: local plant time (IST) stored with the +0000 suffix | `null` |  |
| 22 | exampleValue | String | - | Yes | Example value | `"VB26272A00184"` |  |
| 23 | status | String | - | Yes | Primary lifecycle state of the document | `"Active"` | Active; Inactive |
| 24 | schemaVersion | Int32 | - | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Status values

Active, Inactive. Initial state: Active. The values are maintained in u_mes_syst_statusDefinition.

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ siteId: 1, recordNo: 1 }` | Yes | Business identifier is unique within the site |
| 2 | `{ siteId: 1, status: 1 }` | No | Work lists filtered by lifecycle state |
| 3 | `{ itemId: 1 }` | No | Look-up of documents by item |

## Referenced by

u_mes_prod_item, u_mes_trac_serialNumber.

## Files

- Validator: 03_design/09_system_integration/validators/u_mes_syst_numberRange.json
- Indexes: 03_design/09_system_integration/indexes/u_mes_syst_numberRange.js
- Sample documents (10): 03_design/09_system_integration/samples/u_mes_syst_numberRange.js
