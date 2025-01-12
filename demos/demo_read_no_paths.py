from pathlib import Path
import sys
from syspathmodif import\
	SysPathBundle

_LOCAL_DIR = Path(__file__).parent.resolve()
_REPO_ROOT = _LOCAL_DIR.parent

paths = (
	# For Ajxo's package
	_REPO_ROOT,
	# For Point's module
	_REPO_ROOT/"demo_package"
)

with SysPathBundle(paths):
	from repr_rw import\
		read_reprs

	# Classes Ajxo and Point are not required in this script.
	# Importing them ensures their presence in sys.modules.
	# Thus, the same import statements will work in read_reprs
	# even though that function will not modify sys.path.
	from demo_package import\
		Ajxo
	from point import\
		Point

del paths


obj_path = _LOCAL_DIR/"objects.txt"

if not obj_path.exists():
	print("Run demos/demo_write.py to generate the file that this script needs.\n")
	sys.exit(1)

importations = [
	"from demo_package import Ajxo",
	"from point import Point",
	"from pathlib import PosixPath, WindowsPath"
]

obj_generator = read_reprs(obj_path, importations)

print("Objects read:")
for obj in obj_generator:
	print(f"{obj} {type(obj)}")
