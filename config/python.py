""" python deps for this project """

config_requires: list[str] = [
    "pyclassifiers",
]
install_requires: list[str] = [
    "pypipegzip",
    "typing",
]
build_requires: list[str] = [
    "hatch",
    "pymakehelper",
    "pycmdtools",
    "pydmt",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "mypy",
    "ruff",
]
requires: list[str] = config_requires + install_requires + build_requires + test_requires
