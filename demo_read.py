from pathlib import Path

from repr_rw import\
	read_reprs


obj_path = Path("objects.txt")

# The first importation works with None because the
# first entry in sys.path is the current directory.
# To ensure that the function works with any
# package, copy demo_package in another directory
# and replace None with the new path.
importations = {
	"from demo_package import Ajxo, Point": None,
	"from pathlib import PosixPath, WindowsPath": None}
objs = read_reprs(obj_path, importations)

print("Read objects:")
for obj in objs:
	print(obj)

print()
