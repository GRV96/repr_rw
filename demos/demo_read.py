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
	# The importation of Ajxo and Point requires the path to
	# the repository's root, which is not included in sys.path.
	"from demo_package import Ajxo, Point": _REPO_ROOT,
	# Since pathlib is a built-in module, its importation
	# does not require a path.
	"from pathlib import PosixPath, WindowsPath": None
}
object_generator = read_reprs(obj_path, importations)

print("Objects read:")
for object in object_generator:
	print(f"{object} {type(object)}")
