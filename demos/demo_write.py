from pathlib import Path

LOCAL_DIR = Path(__file__).parent

# Required to import from the repository's root
import sys
sys.path.append(str(LOCAL_DIR.parent))

from demo_package import\
	Ajxo,\
	Point
from repr_rw import\
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

obj_path = LOCAL_DIR/"objects.txt"

print("Objects to write:")
for obj in objs:
	print(obj)

write_reprs(obj_path, objs)
