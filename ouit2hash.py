#!/usr/bin/env python3
# to include this in your script, add the following line to your imports:
# from ouilookup import ouilookup_vals

import sys
import os

filename = sys.argv[1]

with open(filename, "r") as fh:
    with open('oui_hashtable.txt', "w") as wfh:
        
        for line in fh:
            if("base 16" in line):
                line = line.strip('\n')
                linelist = line.split('\t')
                oui = linelist[0].strip().replace('     (base 16)','')
                vendor = linelist[2]
                wfh.write(f'"{oui}":"{vendor}",\n')
        wfh.write('"":None\n')
    wfh.close()
fh.close()

os.system("sort -t':' -n -k1 oui_hashtable.txt > oui_hashtable_sorted.txt")

with open('oui_hashtable_sorted.txt', "r") as rfh:
    with open('ouilookup.py', "w") as finalfh:
        finalfh.write('#!/usr/bin/env python3\n')
        finalfh.write('\n')
        finalfh.write('# OUI hashtable\n')
        finalfh.write('ouilookup_vals = {\n')
        for line in rfh:
            finalfh.write(line)
        finalfh.write('}')
    finalfh.close()
rfh.close()

os.remove('oui_hashtable.txt')
os.remove('oui_hashtable_sorted.txt')