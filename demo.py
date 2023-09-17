from pathlib import Path

from demo_package import\
	Ajxo,\
	Point
from repr_rw import\
	read_reprs,\
	write_reprs


objs = [
	Ajxo(7, "abc"),
	Ajxo("def", 3.14159),
	Ajxo(False, (19, 23)),
	Point(29, 7),
	Point(461.28, 37.59),
	Point(10.2, 83),
	Path("some/directory/file.txt")
]

demo_path = Path("objects.txt")

print("Objects to write:")
for obj in objs:
	print(obj)

write_reprs(demo_path, objs)

# The first importation works with None because the
# first entry in sys.path is the current directory.
# To ensure that the function works with any
# package, copy demo_package in another directory
# and replace None with the new path.
importations = {
	"from demo_package import Ajxo, Point": None,
	"from pathlib import PosixPath, WindowsPath": None}
objs = read_reprs(demo_path, importations)

# Delete the file where the representations are written.
demo_path.unlink()

print("\nRead objects:")
for obj in objs:
	print(obj)

print()
