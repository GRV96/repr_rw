from pathlib import Path

from ajxo import\
	Ajxo
from repr_rw import\
	read_reprs,\
	write_reprs


objs = [
	Ajxo(7, "abc"),
	Ajxo("def", 3.14159),
	Ajxo(False, (19, 23))
]

demo_path = Path("objects.txt")

print("Objects to write:")
for obj in objs:
	print(obj)

write_reprs(demo_path, objs)

objs = read_reprs(demo_path, statements=["from ajxo import Ajxo"])

print("\nRead objects:")
for obj in objs:
	print(obj)

print()
