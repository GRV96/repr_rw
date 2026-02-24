import setuptools


_ENCODING_UTF8: str = "utf-8"
_MODE_R: str = "r"

_NEW_LINE: str = "\n"


def _make_descriptions() -> tuple[str, str]:
	with open("README.md", _MODE_R, encoding=_ENCODING_UTF8) as readme_file:
		readme_content = readme_file.read()

	title_fr = "## FRANÇAIS"
	title_en = "## ENGLISH"

	index_fr = readme_content.index(title_fr)
	index_end_fr = readme_content.index("### Importation")

	index_en = readme_content.index(title_en)
	index_desc_en = index_en + len(title_en)
	index_desc_end_en = readme_content.index("### Content", index_desc_en)
	index_end_en = readme_content.index("### Importing", index_desc_end_en)

	short_description = readme_content[index_desc_en: index_desc_end_en]
	short_description = short_description.replace(_NEW_LINE, " ")
	short_description = short_description.replace("`", "")
	short_description = short_description.strip()

	long_description = readme_content[index_fr: index_end_fr]\
		+ readme_content[index_en:index_end_en].rstrip()

	return short_description, long_description


def _make_requirement_list() -> list[str]:
	with open("requirements.txt",
			_MODE_R, encoding=_ENCODING_UTF8) as req_file:
		req_str = req_file.read()

	raw_requirements = req_str.split(_NEW_LINE)

	requirements: list[str] = list()
	for requirement in raw_requirements:
		if len(requirement) > 0:
			requirements.append(requirement)

	return requirements


if __name__ == "__main__":
	short_desc, long_desc = _make_descriptions()

	setuptools.setup(
		name = "repr_rw",
		version = "3.0.4",
		author = "Guyllaume Rousseau",
		description = short_desc,
		long_description = long_desc,
		long_description_content_type = "text/markdown",
		url = "https://github.com/GRV96/repr_rw",
		classifiers = [
			"Development Status :: 5 - Production/Stable",
			"Intended Audience :: Developers",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
			"Programming Language :: Python :: 3.10",
			"Topic :: Software Development :: Libraries :: Python Modules",
			"Topic :: Utilities"
		],
		install_requires = _make_requirement_list(),
		packages = setuptools.find_packages(
			exclude=(".github", "demo_package", "demos")),
		license = "MIT",
		license_files = ("LICENSE",))
