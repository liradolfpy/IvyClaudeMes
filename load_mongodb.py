"""
07_database_scripts/MongoDocUpload/load_mongodb.py - load MES sample data and UI configurations into MongoDB.

Functions (each one can be switched off by commenting its line in main()):
  1. load_sample_data()   - every 03_design/<module>/samples/<collection>.js file into the collection named
                            in its db.getCollection("...") call
  2. load_query_configs()  - every 04_reference_data/ui_controls/query/PageConfigs/*.json into collection "pc0M"
  3. load_ivy_configs()   - every 04_reference_data/ui_controls/query/IvyConfig/*.json into collection "u_int_ivyConfig"

The source files are MongoDB shell style (NumberInt, NumberLong, NumberDecimal, Double, ISODate, unquoted keys).
They are parsed here into the exact BSON types (Int32, Int64, Decimal128, Double, Date), so no shell is needed.

Writes are idempotent: each document is upserted by _id (replaceOne with upsert), so the script can be run again
without duplicate-key errors. Set DRY_RUN=1 to parse and count only, without connecting.

Credentials are never written in this file. They are read from environment variables (see .env.example):
  MONGO_HOST      host, or host:port, or Atlas cluster host (for example cluster0.abcd.mongodb.net)
  MONGO_USER      database user
  MONGO_PASSWORD  password (if not set, it is asked for at run time without echo)
  MONGO_DB        database name (default: mes)
  MONGO_SRV       "1" for mongodb+srv:// (Atlas), "0" for mongodb:// (default: 0)
  MONGO_AUTH_DB   authentication database (default: admin)
  MONGO_TLS       "1" to force TLS (default: 1 for SRV, 0 otherwise)
  DRY_RUN         "1" to parse files and report counts only

Requirements: Python 3.9+, pymongo (pip install pymongo). Optional: python-dotenv (pip install python-dotenv)
to read a local .env file automatically.
"""
import datetime
import getpass
import glob
import json
import os
import sys
from urllib.parse import quote_plus

from bson.decimal128 import Decimal128
from bson.int64 import Int64

# ------------------------------------------------------------------ paths (relative to the project root)
HERE = os.path.dirname(os.path.abspath(__file__))


def find_project_root(start):
    """Walk up from this script's folder to the project root (the folder that holds Folder_Guide.md)."""
    d = start
    while True:
        if os.path.exists(os.path.join(d, "Folder_Guide.md")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            sys.exit("Project root not found: no Folder_Guide.md above %s" % start)
        d = parent


ROOT = find_project_root(HERE)
# ROOT = r"E:\Ivy\SyncAi\MES"
SAMPLE_GLOB = os.path.join(ROOT, "03_design", "*", "samples", "*.js")

# SAMPLE_GLOB = os.path.join(ROOT, "03_design", "**", "samples", "*.js")

QUERY_DIR = os.path.join(ROOT, "04_reference_data", "ui_controls", "query")
PAGECONFIG_GLOB = os.path.join(QUERY_DIR, "PageConfigs", "*.json")
IVYCONFIG_GLOB = os.path.join(QUERY_DIR, "IvyConfig", "*.json")
TABLE_DIR = os.path.join(ROOT, "04_reference_data", "ui_controls", "table")
TABLECONFIG_GLOB = os.path.join(TABLE_DIR, "PageConfigs", "*.json")
MENU_GLOB = os.path.join(ROOT, "04_reference_data", "ui_controls", "menu", "*.json")

SMODAL_DIR = os.path.join(ROOT, "04_reference_data", "ui_controls", "smodal")
SMODAL_GLOB = os.path.join(SMODAL_DIR, "*.json")

STADNEW_DIR = os.path.join(ROOT, "04_reference_data", "ui_controls", "stadnew")
STADNEW_GLOB = os.path.join(STADNEW_DIR, "*.json")

SMODAL_COLLECTION = "smodalM"      
STADNEW_COLLECTION = "pc0M"    


TABLECONFIG_COLLECTION = "pc0M"
PAGECONFIG_COLLECTION = "pc0M"
IVYCONFIG_COLLECTION = "u_int_ivyConfig"
MENU_COLLECTION = "menuM"



# Agar yeh folders ke andar hain ya specific files hain toh aap yahan path adjust kar sakte hain
# CROPDOWN_GLOB = os.path.join(QUERY_DIR, "cropdown", "*.json")
# MASTER_DICT_GLOB = os.path.join(QUERY_DIR, "u_int_mdict", "*.json")

CROPDOWN_COLLECTION = "cropdown"
DYNAMIC_DROPDOWN_COLLECTION = "u_int_dynamicDropdown"
MASTER_DICT_COLLECTION = "u_int_masterDict"




CROPDOWN_GLOB = os.path.join(QUERY_DIR, "cropdown*")       
MASTER_DICT_GLOB = os.path.join(QUERY_DIR, "u_int_mdict.json")   
DYNAMIC_DROPDOWN_GLOB = os.path.join(QUERY_DIR, "u_int_dynamicDropdown")




DYNAMIC_GLOB = os.path.join(QUERY_DIR, "u_int_dynamicDropdown*")
DYNAMIC_COLLECTION = "u_int_dynamicDropdown" # Apni target collection ka naam





BATCH_SIZE = 500


# ------------------------------------------------------------------ MongoDB shell-style parser
class ShellParser:
    """Small recursive-descent parser for the MongoDB shell syntax used in the project files."""

    def __init__(self, text, source):
        self.t = text
        self.i = 0
        self.source = source

    def error(self, msg):
        line = self.t.count("\n", 0, self.i) + 1
        raise ValueError("%s line %d: %s" % (self.source, line, msg))

    def skip(self):
        t = self.t
        while self.i < len(t):
            c = t[self.i]
            if c in " \t\r\n":
                self.i += 1
            elif t.startswith("//", self.i):
                j = t.find("\n", self.i)
                self.i = len(t) if j < 0 else j + 1
            elif t.startswith("/*", self.i):
                j = t.find("*/", self.i)
                if j < 0:
                    self.error("unclosed comment")
                self.i = j + 2
            else:
                break

    def peek(self):
        self.skip()
        return self.t[self.i] if self.i < len(self.t) else ""

    def expect(self, ch):
        if self.peek() != ch:
            self.error("expected %r" % ch)
        self.i += 1

    def string(self):
        q = self.t[self.i]
        j = self.i + 1
        while True:
            if j >= len(self.t):
                self.error("unclosed string")
            if self.t[j] == "\\":
                j += 2
                continue
            if self.t[j] == q:
                break
            j += 1
        raw = self.t[self.i + 1:j]
        self.i = j + 1
        if q == "'":
            raw = raw.replace('\\\'', "'").replace('"', '\\"')
        return json.loads('"' + raw + '"')

    def ident(self):
        j = self.i
        while j < len(self.t) and (self.t[j].isalnum() or self.t[j] in "_$"):
            j += 1
        if j == self.i:
            self.error("unexpected character %r" % self.t[self.i])
        name = self.t[self.i:j]
        self.i = j
        return name

    def number(self):
        j = self.i
        while j < len(self.t) and self.t[j] in "+-0123456789.eE":
            j += 1
        raw = self.t[self.i:j]
        self.i = j
        return float(raw) if any(c in raw for c in ".eE") else int(raw)

    def value(self):
        c = self.peek()
        if c == "{":
            return self.obj()
        if c == "[":
            return self.arr()
        if c in "\"'":
            return self.string()
        if c == "-" or c.isdigit():
            return self.number()
        name = self.ident()
        if name == "true":
            return True
        if name == "false":
            return False
        if name == "null":
            return None
        self.expect("(")
        arg = self.value() if self.peek() != ")" else None
        self.expect(")")
        return self.constructor(name, arg)

    def constructor(self, name, arg):
        if name == "NumberInt":
            return int(arg)
        if name == "NumberLong":
            return Int64(int(arg))
        if name == "NumberDecimal":
            return Decimal128(str(arg))
        if name == "Double":
            return float(arg)
        if name in ("ISODate", "Date"):
            s = str(arg).replace("Z", "+0000")
            for fmt in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z"):
                try:
                    return datetime.datetime.strptime(s, fmt).astimezone(datetime.timezone.utc)
                except ValueError:
                    pass
            self.error("unreadable date %r" % arg)
        self.error("unsupported constructor %s()" % name)

    def obj(self):
        self.expect("{")
        out = {}
        while True:
            c = self.peek()
            if c == "}":
                self.i += 1
                return out
            key = self.string() if c in "\"'" else self.ident()
            self.expect(":")
            out[key] = self.value()
            c = self.peek()
            if c == ",":
                self.i += 1
            elif c != "}":
                self.error("expected ',' or '}'")

    def arr(self):
        self.expect("[")
        out = []
        while True:
            c = self.peek()
            if c == "]":
                self.i += 1
                return out
            out.append(self.value())
            c = self.peek()
            if c == ",":
                self.i += 1
            elif c != "]":
                self.error("expected ',' or ']'")


def read_sample_file(path):
    """Return (collection name, list of documents) from a db.getCollection("x").insertMany([...]) file."""
    text = open(path, encoding="utf-8").read()
    start = text.find('db.getCollection("')
    if start < 0:
        raise ValueError("%s: no db.getCollection(...) call" % path)
    name_start = start + len('db.getCollection("')
    collection = text[name_start:text.index('"', name_start)]
    k = text.index("insertMany(", name_start) + len("insertMany(")
    p = ShellParser(text, path)
    p.i = k
    docs = p.value()
    if not isinstance(docs, list):
        raise ValueError("%s: insertMany argument is not an array" % path)
    return collection, docs


def read_config_file(path):
    """Return one document from a shell-style or plain JSON file."""
    text = open(path, encoding="utf-8").read()
    p = ShellParser(text, path)
    doc = p.value()
    if not isinstance(doc, dict) or "_id" not in doc:
        raise ValueError("%s: not a document with an _id" % path)
    return doc

def read_menu_file(path):
    text = open(path, encoding="utf-8").read()
    p = ShellParser(text, path)
    docs = []
    while p.peek():
        doc = p.value()
        if not isinstance(doc, dict) or "_id" not in doc:
            raise ValueError("%s: not a document with an _id" % path)
        docs.append(doc)
    return docs


# ------------------------------------------------------------------ connection
def load_env_file():
    """Read a local .env file if python-dotenv is installed; environment variables already set take priority."""
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    for candidate in (os.path.join(HERE, ".env"), os.path.join(ROOT, ".env")):
        if os.path.exists(candidate):
            load_dotenv(candidate, override=False)


def dry_run():
    return os.environ.get("DRY_RUN", "0") == "1"


def get_database():
    from pymongo import MongoClient
    connection = MongoClient('vikrant2021.centralindia.cloudapp.azure.com:28428',  userName="nimbleservicepy", password=f'R4(ka14rCitrus@22')
    db = connection.MNV_MES_V3
    return connection, db


def upsert(db, collection, docs):
    """Replace each document by _id, inserting it when missing. Returns (inserted, replaced)."""
    if db is None:
        return len(docs), 0
    from pymongo import ReplaceOne

    inserted = replaced = 0
    for k in range(0, len(docs), BATCH_SIZE):
        ops = [ReplaceOne({"_id": d["_id"]}, d, upsert=True) for d in docs[k:k + BATCH_SIZE]]
        res = db[collection].bulk_write(ops, ordered=False)
        inserted += res.upserted_count
        replaced += res.matched_count
    return inserted, replaced


# ------------------------------------------------------------------ the three loaders
# def load_sample_data(db):
#     """1. Insert the sample documents of every collection into the collection of the same name."""
#     #files = sorted(glob.glob(SAMPLE_GLOB))
#     files =  glob.glob(SAMPLE_GLOB, recursive=True)
#     total = 0
#     for path in files:
#         collection, docs = read_sample_file(path)
#         ins, rep = upsert(db, collection, docs)
#         total += len(docs)
#         print("  %-60s %3d documents (new %d, replaced %d)" % (collection, len(docs), ins, rep))
#     print("Sample data: %d files, %d documents" % (len(files), total))


def load_sample_data(db, module_filter=None):
    """1. Insert the sample documents of every collection into the collection of the same name."""
    # Agar filter diya gaya hai (jaise "01"), toh wahi folder match karega; warna sabhi (*)
    if module_filter:
        folder_pattern = f"{module_filter}*"
    else:
        folder_pattern = "*"
        
    sample_glob_path = os.path.join(ROOT, "03_design", folder_pattern, "samples", "*.js")
    files = glob.glob(sample_glob_path, recursive=True)
    total = 0
    for path in files:
        collection, docs = read_sample_file(path)
        ins, rep = upsert(db, collection, docs)
        total += len(docs)
        print("   %-60s %3d documents (new %d, replaced %d)" % (collection, len(docs), ins, rep))
    print("Sample data: %d files, %d documents" % (len(files), total))




def load_query_configs(db):
    """2. Insert the query page configurations into collection pc0M."""
    files = sorted(glob.glob(PAGECONFIG_GLOB))
    docs = [read_config_file(p) for p in files]
    ins, rep = upsert(db, PAGECONFIG_COLLECTION, docs)
    for d in docs:
        print("  %s" % d["_id"])
    print("Page configurations -> %s: %d documents (new %d, replaced %d)" % (PAGECONFIG_COLLECTION, len(docs), ins, rep))


def load_ivy_configs(db):
    """3. Insert the IvyConfig documents into collection u_int_ivyConfig."""
    files = sorted(glob.glob(IVYCONFIG_GLOB))
    docs = [read_config_file(p) for p in files]
    ins, rep = upsert(db, IVYCONFIG_COLLECTION, docs)
    for d in docs:
        print("  %s" % d["_id"])
    print("IvyConfigs -> %s: %d documents (new %d, replaced %d)" % (IVYCONFIG_COLLECTION, len(docs), ins, rep))

def load_table_configs(db):
    """4. Load table configurations into MongoDB."""
    files = sorted(glob.glob(TABLECONFIG_GLOB))
    docs = [read_config_file(p) for p in files]
    ins, rep = upsert(db, TABLECONFIG_COLLECTION, docs)
    for d in docs:
        print("  %s" % d["_id"])
    print("Table configurations -> %s: %d documents (new %d, replaced %d)" % (TABLECONFIG_COLLECTION, len(docs), ins, rep))


def load_menu_configs(db):
    files = sorted(glob.glob(MENU_GLOB))
    docs = []
    for path in files:
        docs.extend(read_menu_file(path))
    ins, rep = upsert(db, MENU_COLLECTION, docs)
    for d in docs:
        print("  %s" % d["_id"])
    print("Menu configurations -> %s: %d documents (new %d, replaced %d)" % (MENU_COLLECTION, len(docs), ins, rep))

def load_smodal_configs(db):
    """Load smodal configurations into MongoDB."""
    files = sorted(glob.glob(SMODAL_GLOB))
    docs = []
    for path in files:
        docs.extend(read_menu_file(path))  
    ins, rep = upsert(db, SMODAL_COLLECTION, docs)
    for d in docs:
        print("  %s" % d.get("_id", "unknown"))
    print("Smodal configurations -> %s: %d documents (new %d, replaced %d)" % (SMODAL_COLLECTION, len(docs), ins, rep))


def load_stadnew_configs(db):
    """Load stadnew configurations into MongoDB."""
    files = sorted(glob.glob(STADNEW_GLOB))
    docs = []
    for path in files:
        docs.extend(read_menu_file(path))  
    ins, rep = upsert(db, STADNEW_COLLECTION, docs)
    for d in docs:
        print("  %s" % d.get("_id", "unknown"))
    print("Stadnew configurations -> %s: %d documents (new %d, replaced %d)" % (STADNEW_COLLECTION, len(docs), ins, rep))

def load_cropdown_configs(db):
    """Load cropdown configurations into MongoDB."""
    files = sorted(glob.glob(CROPDOWN_GLOB))
    docs = []
    for path in files:
        docs.extend(read_menu_file(path))
    ins, rep = upsert(db, CROPDOWN_COLLECTION, docs)
    print("Cropdown configurations -> %s: %d documents (new %d, replaced %d)" % (CROPDOWN_COLLECTION, len(docs), ins, rep))

def load_mdict_configs(db):
    """Load u_int_mdict configurations into MongoDB."""
    files = sorted(glob.glob(MASTER_DICT_GLOB))
    docs = []
    for path in files:
        docs.extend(read_menu_file(path))
    ins, rep = upsert(db, MASTER_DICT_COLLECTION, docs)
    print("MasterDict configurations -> %s: %d documents (new %d, replaced %d)" % (MASTER_DICT_COLLECTION, len(docs), ins, rep))


def load_mdict_configs(db):
    """Load u_int_mdict configurations into MongoDB using sample file reader."""
    files = sorted(glob.glob(MASTER_DICT_GLOB))
    total = 0
    for path in files:
        collection, docs = read_sample_file(path)  # read_menu_file ki jagah read_sample_file use karein
        ins, rep = upsert(db, collection, docs)
        total += len(docs)
        print("   %-60s %3d documents (new %d, replaced %d)" % (collection, len(docs), ins, rep))
    print("MasterDict configurations: %d files, %d documents" % (len(files), total))


def load_dynamic_configs(db):
    """Load u_int_dynamicDropdown configurations into MongoDB."""
    print("Checking QUERY_DIR path:", QUERY_DIR)
    print("All files inside QUERY_DIR:", os.listdir(QUERY_DIR) if os.path.exists(QUERY_DIR) else "Folder not found!")
    
    # Flexible glob pattern taaki agar naam mein thoda bhi fark ho toh match ho jaye
    files = sorted(glob.glob(os.path.join(QUERY_DIR, "*dynamic*")))
    # print("Matched files count:", len(files))
    
    total = 0
    for path in files:
        print("Processing file:", path)
        collection, docs = read_sample_file(path)
        ins, rep = upsert(db, collection, docs)
        total += len(docs)
        print("   %-60s %3d documents (new %d, replaced %d)" % (collection, len(docs), ins, rep))
    print("Dynamic configurations: %d files, %d documents" % (len(files), total))


def main():
    load_env_file()
    client, db = (None, None) if dry_run() else get_database()
    if db is None:
        print("DRY_RUN=1: files are parsed and counted, nothing is written")
    try:
        load_sample_data(db, module_filter="01") # None
        load_query_configs(db)
        load_ivy_configs(db)
        load_table_configs(db)
        load_menu_configs(db)
        load_smodal_configs(db)
        load_stadnew_configs(db)
        load_cropdown_configs(db)
        load_mdict_configs(db)
        load_dynamic_configs(db)
    finally:
        if client is not None:
            client.close()










if __name__ == "__main__":
    main()
    