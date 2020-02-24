#!/usr/bin/env python3
import sys
import os
import os.path
import struct

OUTDIR = 'extract'

try:
	os.mkdir(OUTDIR)
except:
	pass

f = open(sys.argv[1], 'rb')
assert f.read(4) == b'\xA5UPG'
f.seek(32)
while True:
	assert f.read(4)[:2] == b'GW'
	file_size, section_size = struct.unpack('<LL', f.read(8))
	# print(file_size, section_size)
	file_name = f.read(20)[1:15].strip(b'\x00').decode('utf8')
	print(file_name, file_size)
	open(os.path.join(OUTDIR, file_name), 'wb').write(f.read(file_size))
	if section_size != 0xffffffff:
		f.seek(section_size - file_size, os.SEEK_CUR)
	else:
		break

print("All files extracted into the "+ OUTDIR+"/ directory")
