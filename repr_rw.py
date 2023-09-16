from pathlib import\
	Path


_ENCODING_UTF8 = "utf-8"
_MODE_R = "r"
_MODE_W = "w"
_NEW_LINE = "\n"


def _ensure_is_path(obj):
	if isinstance(obj, Path):
		return obj

	elif isinstance(obj, str):
		return Path(obj)

	else:
		raise TypeError(
			"An argument of type string or pathlib.Path is expected.")


def read_reprs(file_path, ignore_except=False, statements=None):
	"""
	If a text file contains the representation of Python objects, this function
	can read it to recreate those objects. Each line must contain a string
	returned by function repr. Empty lines are ignored.

	Args:
		file_path (str or pathlib.Path): the path to a text file that contains
			object representations
		ignore_except (bool): If it is True, exceptions raised upon the parsing
			of object representations will be ignored. Defaults to False.
		statements (container): code in str objects to be executed with
			function exec before the parsing of object representations. They
			should be the importation of the type of the objects to recreate.
			Defaults to None.

	Returns:
		list: the objects recreated from their representation

	Raises:
		Exception: any exception raised upon the parsing of an object
			representation if ignore_except is False.
	"""
	if statements is not None:
		for statement in statements:
			exec(statement)

	file_path = _ensure_is_path(file_path)

	with file_path.open(mode=_MODE_R, encoding=_ENCODING_UTF8) as file:
		text = file.read()

	raw_lines = text.split(_NEW_LINE)

	objs = list()

	for line in raw_lines:

		if len(line) >= 1:

			try:
				objs.append(eval(line))

			except Exception as e:
				if not ignore_except:
					raise e

	return objs


def write_reprs(file_path, objs):
	"""
	Writes the representation of Python objects in a text file. Each line
	contains a string returned by function repr. If the file already exists,
	this function will overwrite it.

	Args:
		file_path (str or pathlib.Path): the path to the text file that will
			contains the object representations
		objs (container): the objects whose representation will be written
	"""
	file_path = _ensure_is_path(file_path)

	with file_path.open(mode=_MODE_W, encoding=_ENCODING_UTF8) as file:

		for obj in objs:
			file.write(repr(obj) + _NEW_LINE)
