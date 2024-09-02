from pathlib import Path
import sys

LOCAL_DIR = Path(__file__).parent
PARENT_DIR = LOCAL_DIR.parent

sys.path.append(str(PARENT_DIR))
from repr_rw import\
	read_reprs
sys.path.remove(str(PARENT_DIR))


obj_path = LOCAL_DIR/"objects.txt"

if not obj_path.exists():
	print("Run demos/demo_write.py to generate the file that this script needs.\n")
	sys.exit(1)

importations = {
	# The importation of Ajxo and Point requires the path to
	# the repository's root, which is not included in sys.path.
	"from demo_package import Ajxo, Point": PARENT_DIR,
	# Since pathlib is a built-in module, its importation
	# does not require a path.
	"from pathlib import PosixPath, WindowsPath": None
}
objs = read_reprs(obj_path, importations)

print("Read objects:")
for obj in objs:
	print(obj)
