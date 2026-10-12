"""Builds the sample-data universe: exactly 10 flat documents per collection, one consistent set of IDs and names.
Usage: python gen_samples.py <project root>   (run from 05_generator). Import build() to get the documents."""
import re,os,sys,json,collections,datetime
import spec_rules as R
from sample_universe import PROC,MASTER,TITLES,KEYPOOL
from sample_rules import *
cols=R.cols; byent=R.byent; bycol=R.bycol; cat=R.cat
N=10
COLNO={c["collection"]:1001+i for i,c in enumerate(cols)}
def oid(c,i): return "%04d%012d"%(COLNO[c["collection"]],i+1)
def D(dt): return ("date",dt)
def code(s): return s.split("|")[0]
def name(s): return s.split("|")[1]
PROCMAP={"operation":"op","workCenter":"wc","equipment":"eq","equipmentType":"eqt","manufacturer":"mfr","recipe":"rcp","tool":"tool","toolType":"tlt","iotDevice":"dev","deviceType":"dvt","skill":"skill","gauge":"gauge","gaugeType":"gty","processTag":"tag","defectCode":"defect","defectGroup":"dgroup","reasonCode":"reason"}
ALIGNED=set(PROCMAP)|{"workInstruction","characteristic","checkSheet","inspectionPlan","spcChart","maintenancePlan","operatorApp"}
IST=datetime.timedelta(0)  # D035: times are stored as local plant time (IST) with a +0000 suffix, no conversion
DAYS=[15,15,16,17,18,19,21,22,23,24]
SHIFTSTART=[6,14,22]
def basetime(i): return datetime.datetime(2026,9,DAYS[i],SHIFTSTART[i%3],0)-IST+datetime.timedelta(minutes=17*i)
def istmidnight(dt):
    l=dt+IST; return datetime.datetime(l.year,l.month,l.day)-IST
# ------------------------------------------------------------------ parents and contexts
def policy(c):
    e=c["entity"]
    if e in PARENTIDX: return None
    if c["kind"]=="relationship": return "rel"
    return "single" if e in SINGLE else "pair"
def parent_idx(c,i):
    e=c["entity"]
    if e in PARENTIDX: return PARENTIDX[e][i]
    return {"rel":i,"single":0,"pair":i//2}[policy(c)]
def line_no(c,i):
    e=c["entity"]
    if e in PARENTIDX:
        p=PARENTIDX[e]; return sum(1 for k in range(i+1) if p[k]==p[i])
    return {"rel":1,"single":i+1,"pair":i%2+1}[policy(c)]
def ctx_of(c,i):
    e=c["entity"]
    if e in CTXOF: return CTXOF[e][i]
    if c["parent"]:
        if policy(c)=="single" and e not in NOCTXSTEP: return i
        return ctx_of(bycol[c["parent"]],parent_idx(c,i))
    return i
# ------------------------------------------------------------------ identities
IDENT={}
def trans_rec(c,i):
    e=c["entity"]
    if e in RECFMT: return RECFMT[e](i,ctx_of(c,i))
    pre=c["prefix"]; b=basetime(i)+IST
    return "%s-2026-%06d"%(pre,101+((sum(map(ord,e))*7)%400)+i*3)
def derived_identity(e,i):
    p=PROC[i]
    return {"workInstruction":("WI-%s-001"%code(p["op"]),p["wi"]),"characteristic":("CH-%s-01"%code(p["op"]),p["char"]),
     "checkSheet":("SOS-%s"%code(p["wc"]),"Start of shift check, %s"%name(p["wc"])),"inspectionPlan":("INP-%s"%code(p["op"]),"In-process inspection, %s"%name(p["op"]).lower()),
     "spcChart":("SPC-%s-01"%code(p["op"]),"%s, X-bar R chart"%p["char"]),"maintenancePlan":("PM-%s"%code(p["eq"]),"Preventive maintenance, %s"%name(p["eq"])),
     "operatorApp":("APP-%s"%code(p["wc"]),"Operator app, %s"%name(p["wc"]))}[e]
def identity(c,i):
    e=c["entity"]; key=(e,i)
    if key in IDENT: return IDENT[key]
    if c["parent"]:
        pc=bycol[c["parent"]]; prec=identity(pc,parent_idx(c,i))[1]
        rec="%s-%s%02d"%(prec,c["tag"],line_no(c,i)); nm=rec
    elif e in PROCMAP: rec,nm=code(PROC[i][PROCMAP[e]]),name(PROC[i][PROCMAP[e]])
    elif e in MASTER: rec,nm=code(MASTER[e][i]),name(MASTER[e][i])
    elif e in("workInstruction","characteristic","checkSheet","inspectionPlan","spcChart","maintenancePlan","operatorApp"): rec,nm=derived_identity(e,i)
    elif e in SPECIALIDENT: rec,nm=SPECIALIDENT[e](i)
    else:
        rec=trans_rec(c,i); nm=TITLES[e][i] if e in TITLES else rec
    if c["displayField"]=="recordNo": nm=rec
    IDENT[key]=(oid(c,i),rec,nm); return IDENT[key]
# ------------------------------------------------------------------ generation
DOCS={}; META={}; BUILDING=set()
ANCHORS=["operationExecution","wipUnit","productionOrder","lot","goodsReceipt","nonconformance","downtimeEvent","maintenanceWorkOrder","shipment","customerSchedule"]
NOCOPY={"siteId","createdById","updatedById","unitOfMeasureId","storageLocationId","supplierId","customerId","qualityHoldId","capaId","defectCodeId"}
def docs_of(entity):
    c=byent[entity]
    if c["collection"] not in DOCS and c["collection"] not in BUILDING: build_collection(c)
    return DOCS.get(c["collection"])
def role_user(key,c,i):
    r=R.userrole(key,dict(c,sourceEntity=c["rootEntity"]))
    return {"operator":[0,1,2][i%3],"quality":3,"supervisor":4,"maintenance":5,"manager":6,"stores":7,"system":9}[r]
doc_item=[None]
def pick_index(c,key,target,i,j,nul):
    e=c["entity"]
    if (e,key) in REFIDX: return REFIDX[(e,key)][i]
    stem=key[:-2]
    if target=="user":
        if nul and re.search(r"^(replaced|injured|witness)",key): return None
        return role_user(key,c,i)
    if target=="site": return 0
    if target==e or re.match(r"(parent|previous|supersedes|reversal|replaced|alternate)",key):
        return None if nul else (i+9)%N
    if target in ALIGNED:
        if re.match(r"(next|to[A-Z])",key) and target in("operation","workCenter"): return min(j+1,9)
        if re.match(r"from",key): return max(j-1,0)
        if target=="recipe" and j in(5,9): return None if nul else j
        return j
    if target=="line": return PROC[j]["line"]
    if target=="area": return PROC[j]["area"]
    if target=="costCenter": return PROC[j]["area"]
    if target=="item":
        if re.match(r"(component|child|suppliedItem)",key): return PROC[j]["comp"]
        if re.match(r"from",key): return 1
        return PROC[j]["item"]
    if target in("routing","billOfMaterial","billOfProcess") and doc_item[0] is not None and doc_item[0]<=3: return doc_item[0]
    if target=="unitOfMeasure":
        if c["rootEntity"] in QUALROOT: return PROC[j]["uom"]
        if c["rootEntity"] in TAGROOT: return PROC[j]["tuom"]
        if c["rootEntity"]=="energyReading": return 9
        return 0
    if target=="shift": return i%3
    if target=="workCalendar": return 0
    if target=="customer": return [0,0,0,1,0,0,2,0,7,0][i]
    if target=="supplier": return {4:0,5:1,6:1,7:2,8:4,9:3}.get(PROC[j]["comp"],[0,1,2,3,4,5,6,7,8,9][i])
    if target=="enterprise": return 0
    if target=="storageLocation":
        if re.match(r"from",key): return [0,1,2,1,2,1,1,7,7,7][i]
        if re.search(r"quarantine",key): return 6
        if re.search(r"scrap",key): return 9
        if re.search(r"dock",key): return 8
        return [3,3,4,4,4,5,5,5,5,7][j]
    if target=="stockStatus": return 1 if re.match(r"from",key) else 0
    if target=="currency" or target=="country" or target=="language": return 0
    if target=="department": return {"maint":2,"qual":1,"matl":3}.get(c["module"],0)
    if target=="reasonCategory": return PROC[j]["rcat"]
    if target=="productVariant": return 0 if PROC[j]["item"]==0 else None if nul else 0
    tc=byent[target]
    if tc["dataClass"]=="transaction" and tc["parent"] is None:
        cand=[k for k in range(N) if ctx_of(tc,k)==j]
        return cand[i%len(cand)] if cand else (None if nul else i)
    return i%N
def status_blocks(stem,status):
    """True = must be null in this status, False = must be filled, None = no rule."""
    if status is None: return None
    if stem in STATUSDATE: return status not in STATUSDATE[stem]
    if stem in STATUSDATE_NOT: return status in STATUSDATE_NOT[stem]
    return None
def later_null(k,status):
    return status in OPENISH and bool(R.LATE.match(k)) and not FUT.search(k)
def numval(t,v):
    if v is None: return None
    if t=="Int32": return ("int",int(round(float(v))))
    if t=="Int64": return ("long",int(round(float(v))))
    if t=="Double": return ("dbl",float(v))
    if t=="Decimal128": return ("dec",str(v))
    return v
def build_collection(c):
    name_=c["collection"]; BUILDING.add(name_); e=c["entity"]; root=c["rootEntity"]
    out=[]; metas=[]
    fields=c["fields"]; keys=[f["key"] for f in fields]; fmap={f["key"]:f for f in fields}
    master=c["dataClass"]=="master"
    for i in range(N):
        j=ctx_of(c,i); doc=collections.OrderedDict((k,UNSET) for k in keys); meta=dict(ctx=j,i=i); doc_item[0]=None
        _id,rec,disp=identity(c,i)
        base=basetime(i)
        pdoc=None
        if c["parent"]:
            pc=bycol[c["parent"]]; pi=parent_idx(c,i); pdocs=docs_of(pc["entity"]); pdoc=pdocs[pi] if pdocs else None
            pid=identity(pc,pi); pe=pc["entity"]
            if pe!="site": doc[pe+"Id"]=pid[0]; doc[pe+"Name"]=pid[2]
            else: doc["siteId"]=pid[0]; doc["siteName"]=pid[2]
            if pdoc is not None: base=META[pc["collection"]][pi]["base"]+datetime.timedelta(minutes=3*line_no(c,i))
        # status first (drives null rules)
        status=None
        if "status" in keys and c["statusValues"]:
            sv=c["statusValues"]
            if e in STATUSOF: status=STATUSOF[e][i]
            elif master or c["parent"]: status=next((p for p in PREF if p in sv),sv[0]) if not c["parent"] else sv[i%len(sv)]
            else: status=sv[i%len(sv)]
            assert status in sv,(e,status)
        # anchors
        def setref(k,target,idx):
            if idx is None: doc[k]=None; pair=k[:-2]+"Name" if not k.endswith("ById") else k[:-2]
            else:
                tid=identity(byent[target],idx); doc[k]=tid[0]; pair=k[:-2]+"Name" if not k.endswith("ById") else k[:-2]
            if pair in doc: doc[pair]=None if idx is None else tid[2]
        anchored=False
        for a in ANCHORS:
            k=a+"Id"
            if k in keys and doc[k] is UNSET and fmap[k]["ref"]==a and a!=e:
                nul=R.nullable(c,fmap[k]); idx=pick_index(c,k,a,i,j,nul)
                if nul and (e,k) in NULLWHEN and NULLWHEN[(e,k)](i,j,status): idx=None
                setref(k,a,idx)
                if idx is None: continue
                adocs=docs_of(a)
                if adocs is None: continue
                ad=adocs[idx]; am=META[byent[a]["collection"]][idx]
                if not anchored and e not in CTXOF and not c["parent"]:
                    j=am["ctx"]; meta["ctx"]=j
                if not anchored and e not in OWNTIME: base=am["base"]+datetime.timedelta(seconds=40+7*i)
                anchored=True
                for k2 in keys:
                    if k2.endswith("Id") and k2!="_id" and k2 not in NOCOPY and doc[k2] is UNSET and k2 in ad and ad[k2] is not None and fmap[k2]["ref"] and (e,k2) not in REFIDX and (e,k2) not in VAL and not k2.endswith("ById"):
                        doc[k2]=ad[k2]; p2=k2[:-2]+"Name"
                        if p2 in doc and p2 in ad: doc[p2]=ad[p2]
        meta["base"]=base; meta["status"]=status
        seq=[base+datetime.timedelta(seconds=30)]
        step=datetime.timedelta(seconds=25) if root in R_SHORT else datetime.timedelta(minutes=70)
        ctxp=PROC[j]; dates=[]
        env=dict(i=i,j=j,p=ctxp,doc=doc,status=status,c=c,e=e,root=root,pdoc=pdoc,base=base,line=line_no(c,i) if c["parent"] else None,rec=rec,disp=disp,meta=meta,docs_of=docs_of,identity=identity,byent=byent,pidx=parent_idx(c,i) if c["parent"] else None)
        for f in fields:
            k=f["key"]; t=f["type"]
            if doc[k] is not UNSET: continue
            nul=R.nullable(c,f); v=UNSET
            if k=="_id": v=_id
            elif k=="recordNo": v=rec
            elif k=="siteId": v=identity(byent["site"],0)[0]
            elif k=="siteName": v=identity(byent["site"],0)[2]
            elif k=="schemaVersion": v=("int",1)
            elif k=="status": v=status
            elif k in("createdAt","updatedAt"): continue
            elif (e,k) in VAL:
                x=VAL[(e,k)]; v=x(env) if callable(x) else x[i]
                v=numval(t,v) if t in("Int32","Int64","Double","Decimal128") else (D(v) if isinstance(v,datetime.datetime) else v)
            elif k=="sequenceNo": v=("int",line_no(c,i) if c["parent"] else i+1)
            elif k=="relatedCollectionName":
                te=RELATED.get(root,"wipUnit"); v=byent[te]["collection"]
            elif k=="relatedEntityId":
                te=RELATED.get(root,"wipUnit"); ti=identity(byent[te],i); v=ti[0]; doc["relatedEntityName"]=ti[2]
            elif f["ref"]:
                idx=pick_index(c,k,f["ref"],i,j,nul)
                if nul and (e,k) in NULLWHEN and NULLWHEN[(e,k)](i,j,status): idx=None
                if idx is not None and nul and k.endswith("ById") and (later_null(k,status) or status_blocks(k[:-4],status)): idx=None
                if idx is not None and nul and "onHold" in keys and re.search(r"(qualityHold)",k) and not (doc.get("onHold") is True or status in("On Hold",)): idx=None
                if idx is None and not nul: idx=i
                setref(k,f["ref"],idx)
                if k=="itemId": doc_item[0]=idx
                continue
            elif k in LINEKEYS_STEP and c["parent"] and (e,k) not in VAL: v=("int",(line_no(c,i) if c["parent"] else i+1)*LINEKEYS_STEP[k])
            elif k in GEN:
                v=GEN[k](env)
                v=numval(t,v) if t in("Int32","Int64","Double","Decimal128") else v
            elif k==c["displayField"] and not c["parent"]: v=disp
            elif t=="Boolean":
                v=BOOLRULE[k](env) if k in BOOLRULE else (not bool(FALSEB.search(k)))
            elif t=="Date":
                if nul and status_blocks(k[:-2],status)==False and status is not None:
                    if k.startswith("actualEnd"): v=D(base+datetime.timedelta(hours=7,minutes=40)); seq[0]=max(seq[0],v[1]+datetime.timedelta(minutes=25))
                    else: v=D(seq[0]); seq[0]=seq[0]+step
                elif nul and (later_null(k,status) or status_blocks(k[:-2],status) or re.search(r"(void|revok|removed|scrapp|cancel|nextRetry|lastFailure|interimApproval)",k)): v=None
                elif FUT.search(k): v=D(datetime.datetime(2027,3,31,18,29,59) if re.search(r"validTo|effectiveTo|expir",k) else datetime.datetime(2026,10,5+2*i,18,30))
                elif EARLY.search(k): v=D(datetime.datetime(2019+(i*3)%6,1+(i*5)%12,3+2*i,18,30))
                elif PAST.search(k) or master: v=D(datetime.datetime(2026,4+(i%5),1+(i*7)%27,18,30))
                elif re.search(r"Date$",k): v=D(istmidnight(base))
                elif k=="horizonFrom": v=D(istmidnight(base))
                elif k=="horizonTo": v=D(istmidnight(base)+datetime.timedelta(days=28))
                elif re.match(r"(plannedStart|plannedDispatch|hourStart|periodStart|intervalStart|clockOn|startedAt|raisedAt|occurredAt|timestamp|queueSince|detectedAt|reportedAt|receivedAt)",k): v=D(base)
                elif re.match(r"(plannedEnd|periodEnd|clockOff)",k): v=D(base+datetime.timedelta(hours=8))
                elif re.match(r"(actualEnd)",k): v=D(base+datetime.timedelta(hours=7,minutes=40)); seq[0]=max(seq[0],v[1]+datetime.timedelta(minutes=25))
                elif k=="hourEndAt": v=D(base+datetime.timedelta(hours=1))
                elif k=="intervalEndAt": v=D(base+datetime.timedelta(minutes=15))
                elif re.match(r"(due|required|expectedRelease|containmentDue|targetDate)",k): v=D(base+datetime.timedelta(days=2))
                else:
                    v=D(seq[0]); seq[0]=seq[0]+step
            else:
                en=R.enum(c,f)
                if en:
                    if nul and k in NULLENUM: v=None
                    elif k in ENUMRULE: v=ENUMRULE[k](env,en)
                    elif k in FIRSTONLY: v=en[0]
                    else: v=en[(i+len(k))%len(en)]
                elif k in PKEY and (PKEY[k][1] is None or root in PKEY[k][1]): v=ctxp[PKEY[k][0]]
                elif k in KEYPOOL: v=KEYPOOL[k][i]
                elif k in("name","title","description") and c["parent"]: v=CHILDNAME(env,k)
                elif k in R.TD:
                    ex=R.TD[k][1][0]
                    v=(disp if ex=="(entity)" else (ex if ex!="" else None))
                    if isinstance(v,str) and ex!="(entity)" and AUTOVARY.search(k) and k not in NOVARY: v=bump(v,i)
                elif k in R.ND:
                    ex=R.ND[k][1][0]
                    if ex=="": v=None
                    else:
                        x=float(ex)
                        if re.search(r"(Quantity$|^quantity|Count$|Output|^cumulative|^output)",k) and k not in NOSCALE: x=(max(1.0,round(x*SCALE[i])) if x>=1 else x)
                        elif re.search(r"Inr$",k): x=round(x*SCALE[i],2)
                        elif re.search(r"Pct$",k): x=round(min(100.0,x+PCTJ[i]),1)
                        v=numval(t,("%.*f"%(len(ex.split(".")[1]) if "." in ex else 0,x)) if t=="Decimal128" else x)
                else: v=None
            if v is None and not nul:
                v=FALLBACK(t,k,env)
            if v is not None and nul and t!="Boolean" and not f["ref"] and k not in("status",) and (later_null(k,status)) and t!="Date": v=None if R.LATE.match(k) else v
            doc[k]=v
            if isinstance(v,tuple) and v[0]=="date" and datetime.datetime(2026,9,14)<=v[1]<datetime.datetime(2026,10,1): dates.append(v[1])
        if "createdAt" in keys:
            ev=[d for d in dates if d>=base-datetime.timedelta(days=1)]
            doc["createdAt"]=D(min(ev+[base])); doc["updatedAt"]=D(max(ev+[base]))
        for k in keys:
            if doc[k] is UNSET: doc[k]=None
        GENERIC_POST(env)
        for f in fields:
            v=doc[f["key"]]
            if f["type"]=="Date" and isinstance(v,tuple):
                t=v[1]
                if (t.hour,t.minute)==(18,30) or (t.hour,t.minute,t.second)==(18,29,59): t=t.replace(second=0)+datetime.timedelta(hours=5,minutes=30)
                if f.get("dateKind")=="Date": t=datetime.datetime(t.year,t.month,t.day)
                doc[f["key"]]=("date",t)
        if "createdAt" in doc and doc["createdAt"] and doc["updatedAt"] and doc["updatedAt"][1]<doc["createdAt"][1]: doc["updatedAt"]=doc["createdAt"]
        if e in POST: POST[e](env)
        out.append(doc); metas.append(meta)
    DOCS[name_]=out; META[name_]=metas; BUILDING.discard(name_)
def build():
    for c in cols:
        if c["collection"] not in DOCS: build_collection(c)
    return DOCS
# ------------------------------------------------------------------ validation and output
ORDERPAIRS=[("startedAt","completedAt"),("startedAt","endedAt"),("plannedStartAt","plannedEndAt"),("actualStartAt","actualEndAt"),("raisedAt","acknowledgedAt"),("acknowledgedAt","resolvedAt"),("raisedAt","clearedAt"),("clockOnAt","clockOffAt"),("validFrom","validTo"),("effectiveFrom","effectiveTo"),("periodStartAt","periodEndAt"),("hourStartAt","hourEndAt"),("intervalStartAt","intervalEndAt"),("horizonFrom","horizonTo"),("createdAt","updatedAt"),("lastCalibratedAt","nextCalibrationDueAt"),("pickStartedAt","pickCompletedAt"),("issuedAt","markedAt"),("reportedAt","startedAt"),("detectedAt","closedAt"),("openedAt","d8ClosureClosedAt"),("placedAt","releasedAt")]
TYPETAG={"Date":"date","Int32":"int","Int64":"long","Decimal128":"dec","Double":"dbl"}
CHECKS=["Exactly 10 documents","Every document has a unique _id","_id is a 16-digit numeric string","No ObjectId","No nested documents or arrays","All schema keys present, no extra keys, same order","Data types match the schema","Required keys are not null","Values are in the allowed list","Status values are approved","ID and display pairs are complete","Every reference points to an existing document","Display value equals the referenced document's display value","Business numbers (recordNo) unique in the collection","Parent and line number unique in child collections","Audit keys valid (transaction collections only)","Dates in logical order","Dates inside 2018-2027","Quantities not negative"]
def validate(docs):
    fails=collections.defaultdict(list); byid={}
    for c in cols:
        for d in docs[c["collection"]]: byid.setdefault(d["_id"],[]).append((c,d))
    for c in cols:
        n=c["collection"]; ds=docs[n]; keys=[f["key"] for f in c["fields"]]; fmap={f["key"]:f for f in c["fields"]}
        def F(chk,msg): fails[chk].append((n,msg))
        if len(ds)!=10: F(CHECKS[0],"count %d"%len(ds))
        if len({d["_id"] for d in ds})!=len(ds): F(CHECKS[1],"duplicate _id inside collection")
        if len({d["recordNo"] for d in ds})!=len(ds): F(CHECKS[13],"duplicate recordNo")
        if c["parent"]:
            pe=bycol[c["parent"]]["entity"]; pk=pe+"Id" if pe!="site" else "siteId"
            lk=next((x for x in R_LINEKEYS if x in keys),None) or ("sequenceNo" if "sequenceNo" in keys else None)
            if c["kind"]=="relationship":
                tk=[f["key"] for f in c["fields"] if f["ref"] and f["key"] not in("siteId",pk,"createdById","updatedById")][0]
                sig=[(d[pk],d[tk]) for d in ds]
            elif c["entity"]=="msaStudyTrial": sig=[(d[pk],d["appraiserUserId"],d["partNo"],d["trialNo"]) for d in ds]
            else: sig=[(d[pk],d[lk]) for d in ds] if lk else list(range(10))
            if len(set(sig))!=len(sig): F(CHECKS[14],"duplicate parent/line")
        for x,d in enumerate(ds):
            if len(byid[d["_id"]])>1: F(CHECKS[1],"_id %s used in more than one document"%d["_id"])
            if not re.fullmatch(r"\d{16}",str(d["_id"])): F(CHECKS[2],d["_id"])
            if list(d.keys())!=keys: F(CHECKS[5],"doc %d keys differ"%x)
            for k in keys:
                f=fmap[k]; v=d.get(k); t=f["type"]; nul=R.nullable(c,f)
                if isinstance(v,(dict,list)): F(CHECKS[4],"%s doc %d"%(k,x))
                if isinstance(v,str) and "ObjectId" in v: F(CHECKS[3],k)
                if v is None:
                    if not nul: F(CHECKS[7],"%s doc %d"%(k,x))
                    continue
                ok=isinstance(v,str) if t=="String" else isinstance(v,bool) if t=="Boolean" else (isinstance(v,tuple) and v[0]==TYPETAG[t])
                if not ok: F(CHECKS[6],"%s doc %d (%r)"%(k,x,v))
                en=R.enum(c,f)
                if en and v not in en: F(CHECKS[9] if k=="status" else CHECKS[8],"%s doc %d: %s"%(k,x,v))
                if t=="Date" and not (datetime.datetime(2018,1,1)<=v[1]<=datetime.datetime(2027,12,31)): F(CHECKS[17],"%s doc %d"%(k,x))
                if t in("Int32","Int64","Decimal128") and re.search(r"(Quantity|Count|Minutes)$",k) and float(v[1])<0: F(CHECKS[18],"%s doc %d"%(k,x))
                if k.endswith("Id") and k!="_id":
                    pair=k[:-2] if k.endswith("ById") else k[:-2]+"Name"
                    if k=="relatedEntityId":
                        tc=bycol.get(d.get("relatedCollectionName")); hit=[y for cc,y in byid.get(v,[]) if tc and cc["collection"]==tc["collection"]]
                    else:
                        tc=byent[f["ref"]]; hit=[y for cc,y in byid.get(v,[]) if cc["collection"]==tc["collection"]]
                    if not hit: F(CHECKS[11],"%s doc %d -> %s"%(k,x,v))
                    elif pair in d:
                        if d[pair] is None: F(CHECKS[10],"%s doc %d has ID but no display value"%(k,x))
                        elif d[pair]!=hit[0][tc["displayField"]]: F(CHECKS[12],"%s doc %d: '%s' vs '%s'"%(k,x,d[pair],hit[0][tc["displayField"]]))
                if (k.endswith("Name") and k[:-4]+"Id" in d and d[k[:-4]+"Id"] is None) or (k+"Id" in d and d[k+"Id"] is None): F(CHECKS[10],"%s doc %d has display value but no ID"%(k,x))
            for a,b in ORDERPAIRS:
                if a in d and b in d and d[a] and d[b] and d[a][1]>d[b][1]: F(CHECKS[16],"%s after %s, doc %d"%(a,b,x))
            if "createdAt" in d and (d["createdAt"] is None or d["createdById"] is None or d["createdBy"] is None or d["updatedById"] is None): F(CHECKS[15],"doc %d"%x)
            if c["dataClass"]=="master" and "createdAt" in d: F(CHECKS[15],"audit keys on a master collection")
    return fails
R_LINEKEYS=["lineNo","stepNo","itemNo","taskNo","actionNo","findingNo","elementNo","levelNo","stageNo","releaseNo","revisionNo","rank","level","lotSizeFrom","subgroupNo"]
def write(root):
    docs=build(); fails=validate(docs)
    def w(p,t):
        p=os.path.join(root,p); os.makedirs(os.path.dirname(p),exist_ok=True); open(p,"w",encoding="utf-8").write(t)
    for c in cols:
        n=c["collection"]
        s="// Sample documents for %s: exactly 10, flat, one consistent sample-data universe\n// Generated by 05_generator/gen_samples.py - do not edit by hand\ndb.getCollection(\"%s\").insertMany([\n"%(n,n)
        s+=",\n".join("  {\n"+",\n".join("    %s: %s"%(k,R.sh(v)) for k,v in d.items())+"\n  }" for d in docs[n])+"\n]);\n"
        w("03_design/%s/samples/%s.js"%(R.DOMF[c["module"]],n),s)
    # registry
    s="# Sample data registry\n\nOne consistent sample-data universe: every _id, business number and display value used in the sample documents. A reference in any sample document uses exactly these IDs and names. Generated by 05_generator/gen_samples.py.\n\nCollections: %d | Documents: %d | Sample period: April to September 2026; production fortnight 15 to 26 September 2026 (IST, stored as UTC)\n"%(len(cols),sum(len(v) for v in docs.values()))
    for m in R.order:
        s+="\n## %s (%s)\n"%(R.MODN[m],m)
        for c in cols:
            if c["module"]!=m or c["kind"]!="entity": continue
            df=c["displayField"]
            s+="\n### %s\n\n| # | _id | recordNo | %s | status |\n|---|---|---|---|---|\n"%(c["collection"],df if df!="recordNo" else "display value")
            for x,d in enumerate(docs[c["collection"]],1): s+="| %d | %s | %s | %s | %s |\n"%(x,d["_id"],d["recordNo"],str(d[df]).replace("|","/"),d.get("status") or "-")
    s+="\n## Child, relationship and value-list collections\n\nTheir documents are identified by the parent's recordNo plus a line tag; see the sample file of each collection.\n\n| Collection | Parent collection | First _id | Last _id |\n|---|---|---|---|\n"
    for c in cols:
        if c["kind"]!="entity": s+="| %s | %s | %s | %s |\n"%(c["collection"],c["parent"],docs[c["collection"]][0]["_id"],docs[c["collection"]][-1]["_id"])
    w("04_reference_data/sample_data_registry.md",s)
    # validation report
    tot=sum(len(v) for v in fails.values())
    s="# Sample data validation\n\nRun: 12 October 2026 | Tool: 05_generator/gen_samples.py | Collections: %d | Documents: %d\n\n| # | Check | Scope | Result | Findings |\n|---|---|---|---|---|\n"%(len(cols),sum(len(v) for v in docs.values()))
    for x,ch in enumerate(CHECKS,1): s+="| %d | %s | all collections | %s | %d |\n"%(x,ch,"Pass" if not fails.get(ch) else "Fail",len(fails.get(ch,[])))
    s+="\nShell format: every Int32 is written with NumberInt(), Int64 with NumberLong(), Decimal128 with NumberDecimal(), Double with Double(), dates with ISODate(); this is done by one formatting function for all files.\n"
    if tot:
        s+="\n## Findings\n\n| Check | Collection | Detail |\n|---|---|---|\n"
        for ch,v in fails.items():
            for n,msg in v: s+="| %s | %s | %s |\n"%(ch,n,str(msg).replace("|","/"))
    s+=OBSERVATIONS
    w("08_validation/reports/sample_data_validation.md",s)
    return docs,fails
OBSERVATIONS=OBS
if __name__=="__main__":
    d,f=write(sys.argv[1]); print("collections",len(d),"documents",sum(len(v) for v in d.values()),"findings",sum(len(v) for v in f.values()))
    for ch,v in f.items(): print(len(v),ch,v[:3])
