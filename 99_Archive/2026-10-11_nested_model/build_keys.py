import re
from catalogue import C
from keys import K
names=[c[0] for c in C]
assert set(K)==set(names),(set(names)-set(K),set(K)-set(names))
def sing(n):
    parts=n.split("_"); w=parts[-1]
    w={"enterprises":"enterprise","boms":"bom","pfmeas":"pfmea","capas":"capa","process":"process","equipment":"equipment","data":"data","units":"unit","certifications":"certification","processes":"process","bills":"bill"}.get(w, w[:-3]+"y" if w.endswith("ies") else w[:-1] if w.endswith("s") else w)
    parts[-1]=w
    return parts[0]+"".join(p.title() for p in parts[1:])
stem={sing(n).lower():n for n in names}
stem.update({"uom":"units_of_measure","hold":"quality_holds","location":"storage_locations","user":"users","app":"operator_apps","customerschedule":"customer_schedules","schedule":"customer_schedules","calibration":"gauge_calibrations","movement":"material_movements","spcchart":"spc_charts"})
SKIP={"refId","badgeId","controllerResultId","nodeId"}
unres=set(); rows=[]; nref=0
for c in C:
    ks=["_id",c[3],"siteId"]+[k.strip() for k in K[c[0]].split(",")]+["status","schemaVersion","createdAt","createdBy","updatedAt","updatedBy"]
    assert len(ks)==len(set(ks)),(c[0],[k for k in ks if ks.count(k)>1])
    for k in ks:
        leaf=k.split(".")[-1].replace("[]","")
        m=re.fullmatch(r"(.*?)Ids?",leaf)
        if m and leaf not in SKIP and leaf!="_id":
            s=m.group(1).lower(); hit=[t for t in stem if s.endswith(t)]
            if hit: nref+=1
            else: unres.add((c[0],k))
    rows.append((c[1].split(" ",1)[1],c[0],ks))
print("collections",len(rows),"keys",sum(len(r[2]) for r in rows),"refs",nref,"unresolved",sorted(unres))
out="# MES data model - key list per collection\n\nRegister version 1.1 draft | 11 October 2026 | %d collections, %d keys\n\nNotation: a.b is a field of an embedded document; a[].b is a field of each element of an embedded array; x[] is an array of scalar values. Fields ending in Id or Ids hold the _id of a document in another collection; refCollection + refId is a polymorphic reference. createdBy, updatedBy and other fields ending in By hold users._id.\n\n| Module | Collection | List of keys |\n|---|---|---|\n"%(len(rows),sum(len(r[2]) for r in rows))
for m,n,ks in rows: out+="| %s | %s | %s |\n"%(m,n,", ".join(ks))
open("/mnt/user-data/outputs/collection_keys.md","w").write(out)
open("collection_keys.md","w").write(out)
