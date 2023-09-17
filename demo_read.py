from pathlib import Path
from sys import exit

from repr_rw import\
	read_reprs


obj_path = Path("objects.txt")

if not obj_path.exists():
	print("Run demo_write.py to generate the file that this script needs.\n")
	exit(1)

# The first importation works with None because the first
# entry in sys.path is the current working directory.
# To ensure that the function works with any
# package, move demo_package to another directory
# and replace None with the path to that directory.
importations = {
	"from demo_package import Ajxo, Point": None,
	"from pathlib import PosixPath, WindowsPath": None}
objs = read_reprs(obj_path, importations)

print("Read objects:")
for obj in objs:
	print(obj)

print()
