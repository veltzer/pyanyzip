from typing import List


dev_requires: List[str] = [
    "pymultigit",
    "pypitools",
    "black",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "pypipegzip",
    "pylzma",
    "typing",
]
make_requires: List[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
requires: List[str] = config_requires + install_requires + make_requires + test_requires
