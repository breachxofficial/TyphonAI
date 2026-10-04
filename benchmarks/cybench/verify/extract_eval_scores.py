#!/usr/bin/env python3
"""Re-extract per-sample verdicts from the scored Inspect .eval (zstd-compressed zip).

Works without inspect_ai installed. Prints each sample's Correct/Incorrect verdict
as graded by Inspect's includes() scorer.

Usage:  python3 extract_eval_scores.py ../inspect/*.eval
"""
import sys, glob, json, io, struct, zipfile

try:
    import zstandard as zstd
except ImportError:
    sys.exit("pip install zstandard")


def raw_member_bytes(path, info):
    with open(path, "rb") as r:
        r.seek(info.header_offset)
        h = r.read(30)
        nlen = struct.unpack("<H", h[26:28])[0]
        elen = struct.unpack("<H", h[28:30])[0]
        r.seek(info.header_offset + 30 + nlen + elen)
        return r.read(info.compress_size)


def main(path):
    z = zipfile.ZipFile(path)
    D = zstd.ZstdDecompressor()
    res = {}
    for n in z.namelist():
        if not (n.startswith("samples/") and n.endswith(".json")):
            continue
        comp = raw_member_bytes(path, z.getinfo(n))
        try:
            data = D.decompress(comp)
        except Exception:
            data = D.stream_reader(io.BytesIO(comp)).read()
        s = json.loads(data)
        task, ep = s.get("id"), s.get("epoch")
        v = "?"
        for sc in (s.get("scores") or {}).values():
            val = sc.get("value") if isinstance(sc, dict) else None
            if val in ("C", "I"):
                v = val
            elif isinstance(val, (int, float)):
                v = "C" if val >= 1 else "I"
        res.setdefault(task, {})[ep] = v
    c = sum(1 for t in res for v in res[t].values() if v == "C")
    tot = sum(len(v) for v in res.values())
    print(f"{path}\nverified: {c}/{tot} Correct across {len(res)} tasks")
    for t in sorted(res):
        print(f"  {t:28s} {res[t]}")


if __name__ == "__main__":
    args = sys.argv[1:] or glob.glob("../inspect/*.eval")
    for a in args:
        for f in glob.glob(a):
            main(f)
