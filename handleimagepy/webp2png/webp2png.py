from os import listdir
from os.path import isfile, join
import sys
import os

path = sys.argv[1]
dwebppath = "./dwebp"

files = [f for f in listdir(path) if isfile(join(path, f))]

for f in files:
	if f[-4:].lower() == 'webp':
		os.system(dwebppath + ' -o \"' + path + f[:-5] + '.png\" \"' + path + f + '\"')

print("Done")
