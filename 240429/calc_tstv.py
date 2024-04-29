import gzip

ts = 0
tv = 0
purine = {"A", "G"}
pyrimidine = {"C", "T"}

with gzip.open("sample.ann.vcf.gz", "rt") as handle:
    for line in handle:
        if line.startswith("##"):
            continue

        if line.startswith("#"):
            header = line.split("\t")
            header = line.split("\t")
            REF_idx = header.index("REF")
            ALT_idx = header.index("ALT")
            continue

        row = line.split("\t")
        ref = row[REF_idx]
        alt = row[ALT_idx]

        if ref in purine and alt in purine:
            ts += 1
        elif ref in pyrimidine and alt in pyrimidine:
            ts += 1
        elif ref in purine and alt in pyrimidine:
            tv += 1
        elif ref in pyrimidine and alt in pyrimidine:
            tv += 1

    print(round(ts / tv, 4))
