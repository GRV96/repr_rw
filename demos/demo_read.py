from pathlib import Path
import sys
from syspathmodif import\
	sp_append,\
	sp_remove

_LOCAL_DIR = Path(__file__).parent
_REPO_ROOT = _LOCAL_DIR.parent

sp_append(_REPO_ROOT)
from repr_rw import\
	read_reprs
sp_remove(_REPO_ROOT)


obj_path = _LOCAL_DIR/"objects.txt"

if not obj_path.exists():
	print("Run demos/demo_write.py to generate the file that this script needs.\n")
	sys.exit(1)

importations = {
	# Importing Ajxo from demo_package requires the path to
	# the repository's root, which is not included in sys.path.
	"from demo_package import Ajxo": _REPO_ROOT,
	# Importing Point from its module requires the path to
	# directory demo_package, which is not included in sys.path.
	"from point import Point": _REPO_ROOT/"demo_package",
	# Since pathlib is a built-in module, its importation
	# does not require a path.
	"from pathlib import PosixPath, WindowsPath": None
}
obj_generator = read_reprs(obj_path, importations)

print("Objects read:")
for obj in obj_generator:
	print(f"{obj} {type(obj)}")
