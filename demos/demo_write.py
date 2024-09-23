from pathlib import Path
from syspathmodif import\
	sp_append,\
	sp_remove

_LOCAL_DIR = Path(__file__).parent
_REPO_ROOT = _LOCAL_DIR.parent

sp_append(_REPO_ROOT)
from demo_package import\
	Ajxo,\
	Point
from repr_rw import\
	write_reprs
sp_remove(_REPO_ROOT)


objs = [
	Ajxo(7, "abc"),
	Ajxo("def", 3.14159),
	Ajxo(False, (19, 23)),
	Point(29, 7),
	Point(461.28, 37.59),
	Point(10.2, 83),
	Path("some/directory/file.txt")
]

obj_path = _LOCAL_DIR/"objects.txt"

print("Objects to write:")
for obj in objs:
	print(obj)

write_reprs(obj_path, objs)
