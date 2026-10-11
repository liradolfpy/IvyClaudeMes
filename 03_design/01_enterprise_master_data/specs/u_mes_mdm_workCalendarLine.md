# u_mes_mdm_workCalendarLine

| Property | Value |
|---|---|
| Module | Master data (mdm) |
| Purpose | Links one work calendar to one line; one document per link |
| Kind | Relationship |
| Data class | Master |
| Parent collection | u_mes_mdm_workCalendar |
| _id pattern | <workCalendarId>-L<nnn> |
| Display value used by references | recordNo |
| Keys | 10 (10 required, 0 may be null) |

## Structure

Relationship collection. A work calendar can be linked to several documents of another collection, and DATA-001 does not allow an array of IDs, so each link is its own document carrying one singular reference pair. workCalendarId and workCalendarName point to the parent.
Data class (master) and site are inherited from the parent. Documents are created, changed and removed together with the parent's lifecycle.

## Field dictionary

Every key is present in every document. "Required" means the value may not be null.

| # | Key | BSON type | Required | Description | Example (shell) | Allowed values / reference |
|---|---|---|---|---|---|---|
| 1 | _id | String | Yes | Unique identifier of the document. Pattern: <workCalendarId>-L<nnn> | `"CAL-PN1-2026-L001"` |  |
| 2 | recordNo | String | Yes | Business identifier of the document, readable by people and unique within the site | `"PN1-2026-L001"` |  |
| 3 | siteId | String | Yes | Reference to u_mes_mdm_site._id: the site the document belongs to | `"SITE-PN1"` | Reference: u_mes_mdm_site._id |
| 4 | siteName | String | Yes | Display value of the site, copied from u_mes_mdm_site.name | `"Chakan Plant, Pune"` |  |
| 5 | workCalendarId | String | Yes | Reference to u_mes_mdm_workCalendar._id: the parent document this one belongs to | `"CAL-PN1-2026"` | Reference: u_mes_mdm_workCalendar._id |
| 6 | workCalendarName | String | Yes | Display value of workCalendarId, copied from u_mes_mdm_workCalendar.name | `"Chakan Plant Calendar 2026"` |  |
| 7 | sequenceNo | Int32 | Yes | Position of this document in its list (within the same parent for child collections), starting at 1 | `NumberInt(1)` |  |
| 8 | lineId | String | Yes | Reference to u_mes_mdm_line._id | `"LN-ASY-01"` | Reference: u_mes_mdm_line._id |
| 9 | lineName | String | Yes | Display value of lineId, copied from u_mes_mdm_line.name | `"Caliper Assembly Line 1"` |  |
| 10 | schemaVersion | Int32 | Yes | Version of this collection's document structure, starting at 1 | `NumberInt(1)` |  |

## Indexes

| # | Keys | Unique | Purpose |
|---|---|---|---|
| 1 | `{ workCalendarId: 1, lineId: 1 }` | Yes | One link per pair |
| 2 | `{ lineId: 1, workCalendarId: 1 }` | No | Look-up from the other side of the relationship |

## Referenced by

No other collection refers to this one.

## Files

- Validator: 03_design/01_enterprise_master_data/validators/u_mes_mdm_workCalendarLine.json
- Indexes: 03_design/01_enterprise_master_data/indexes/u_mes_mdm_workCalendarLine.js
- Sample document: 03_design/01_enterprise_master_data/samples/u_mes_mdm_workCalendarLine.js
