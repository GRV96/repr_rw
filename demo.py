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
	Point(10.2, 83)
]

demo_path = Path("objects.txt")

print("Objects to write:")
for obj in objs:
	print(obj)

write_reprs(demo_path, objs)

# A None value works in this case because
# demo_package is in the same directory as repr_rw.
objs = read_reprs(demo_path, {"from demo_package import Ajxo, Point": None})

# Delete the file where the representations are written.
demo_path.unlink()

print("\nRead objects:")
for obj in objs:
	print(obj)

print()
