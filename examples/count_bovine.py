#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from search_rcsb import findSimilarSequence

seq = """
MNGTEGPNFYVPFSNKTGVVRSPFEAPQYYLAEPWQFSMLAAYMFLLIMLGFPINFLTLYVTVQHKKLRTPLNYILLNLAVADLFMVFGGFTTTLYTSLHGYFVFGPTGCNLEGFFATLGGEIALWSLVVLAIERYVVVCKPMSNFRFGENHAIMGVAFTWVMALACAAPPLVGWSRYIPEGMQCSCGIDYYTPHEETNNESFVIYMFVVHFIIPLIVIFFCYGQLVFTVKEAAAQQQESATTQKAEKEVTRMVIIMVIAFLICWLPYAGVAFYIFTHQGSDFGPIFMTIPAFFAKTSAVYNPVIYIMMNKQFRNCMVTTLCCGKNPLGDDEASTTVSKTETSQVAPA
""".strip()

counts = []
for i in range(0,100,5):
    r = findSimilarSequence(seq, i)
    c = r.json()["total_count"]

    counts.append([i, c])

py_bs = os.path.basename(__file__)[:-3]
fl_dat = f"{py_bs}.dat"
with open(fl_dat,'w') as fh:
    for i, c in counts:
        fh.write(f"{i:3d}    {c:6d}\n")
