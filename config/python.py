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
build_requires: List[str] = [
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
requires: List[str] = config_requires + install_requires + build_requires + test_requires
