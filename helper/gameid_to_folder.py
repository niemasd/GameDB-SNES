#! /usr/bin/env python3
'''
Convert the GameID output of an SNES game to its GameDB-SNES folder name
'''
from sys import argv, stderr
if len(argv) == 1:
    from sys import stdin as f
elif len(argv) == 2:
    f = open(argv[1], 'rt')
else:
    print("USAGE: %s [GameID_output.txt]" % argv[0], file=stderr); exit(1)
data = dict()
for line in f:
    k, v = [x.strip() for x in line.strip().split('\t')]
    data[k] = v
print('.....'.join(data[k] for k in ['developer_ID', 'internal_title', 'rom_version', 'checksum']))
