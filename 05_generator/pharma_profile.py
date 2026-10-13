"""Switches the shared sample-generation tables between the Auto universe (caliper, sample_universe.py + sample_rules.py)
and the Gamp universe (pharma, pharma_universe.py + pharma_rules.py). D060-D064.
All tables are changed in place, so every function that already holds a reference to them sees the active universe."""
import copy
import sample_universe as U
import sample_rules as S
import spec_rules as R
import pharma_universe as PU
import pharma_rules as PR

_RULE_DICTS = ["VAL", "REFIDX", "STATUSOF", "RECFMT", "PARENTIDX", "CTXOF", "POST", "NULLWHEN", "SPECIALIDENT", "GEN", "BOOLRULE", "ENUMRULE", "PKEY"]
_SAVED = {}

def _save():
    if _SAVED: return
    _SAVED["PROC"] = [dict(r) for r in U.PROC]
    _SAVED["MASTER"] = {k: list(v) for k, v in U.MASTER.items()}
    _SAVED["TITLES"] = {k: list(v) for k, v in U.TITLES.items()}
    _SAVED["KEYPOOL"] = {k: list(v) for k, v in U.KEYPOOL.items()}
    _SAVED["PERSONS"] = list(S.PERSONS)
    for n in _RULE_DICTS:
        if hasattr(S, n): _SAVED[n] = dict(getattr(S, n))
    _SAVED["TD"] = dict(R.TD); _SAVED["ND"] = dict(R.ND)

def _put_lists(dst, src):
    for k, v in src.items():
        if k in dst and isinstance(dst[k], list): dst[k][:] = v
        else: dst[k] = list(v)

def activate(profile, G):
    _save()
    G.PROFILE[0] = profile
    G.APPCOMMON.clear(); G.APPCOMMON.update(PU.COMMONAPP)
    # restore Auto first
    U.PROC[:] = [dict(r) for r in _SAVED["PROC"]]
    _put_lists(U.MASTER, _SAVED["MASTER"]); _put_lists(U.TITLES, _SAVED["TITLES"]); _put_lists(U.KEYPOOL, _SAVED["KEYPOOL"])
    S.PERSONS[:] = _SAVED["PERSONS"]
    for n in _RULE_DICTS:
        if n in _SAVED:
            d = getattr(S, n); d.clear(); d.update(_SAVED[n])
    R.TD.clear(); R.TD.update(_SAVED["TD"]); R.ND.clear(); R.ND.update(_SAVED["ND"])
    G.RUNOFF.clear()
    cols = {c["collection"] for c in G.cols}
    if profile == "Auto":
        G.AVAIL[0] = cols - set(PU.GMPONLY)
        return
    # Gamp
    G.AVAIL[0] = set(PU.DUAL) | set(PU.GMPONLY) | set(PU.COMMONAPP)
    for n in PU.DUAL: G.RUNOFF[n] = 10
    U.PROC[:] = [dict(r) for r in PU.PROC]
    _put_lists(U.MASTER, PU.MASTER); _put_lists(U.MASTER, PR.MASTER_ADD)
    _put_lists(U.TITLES, PU.TITLES); _put_lists(U.TITLES, PR.TITLES_ADD)
    _put_lists(U.KEYPOOL, PU.KEYPOOL)
    S.PERSONS[:] = PR.PERSONS
    for n in _RULE_DICTS:
        if hasattr(S, n) and hasattr(PR, n):
            d = getattr(S, n)
            for k in getattr(PR, "DROP_" + n, []): d.pop(k, None)
            d.update(getattr(PR, n))
    for k, ex in PR.TD_EXAMPLE.items():
        if k in R.TD:
            flag, lst = R.TD[k]
            R.TD[k] = (flag, [ex] + list(lst[1:]))
    for k, ex in PR.ND_EXAMPLE.items():
        if k in R.ND:
            flag, lst = R.ND[k]
            R.ND[k] = (flag, [ex] + list(lst[1:]))
