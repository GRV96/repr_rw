from pathlib import Path
import sys
from syspathmodif import\
	sp_append,\
	sp_remove

_LOCAL_DIR = Path(__file__).parent.resolve()
_REPO_ROOT = _LOCAL_DIR.parent

sp_append(_REPO_ROOT)
from repr_rw import\
	read_reprs
sp_remove(_REPO_ROOT)


obj_path = _LOCAL_DIR/"objects.txt"

if not obj_path.exists():
	print("Run demos/demo_write.py to generate the file that this script needs.\n")
	sys.exit(1)

importations = [
	"from demo_package import Ajxo",
	"from point import Point",
	"from pathlib import PosixPath, WindowsPath"
]
paths = [_REPO_ROOT, _REPO_ROOT/"demo_package"]
obj_generator = read_reprs(obj_path, importations, paths)

print("Objects read:")
for obj in obj_generator:
	print(f"{obj} {type(obj)}")
