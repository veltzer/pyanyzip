from typing import List


config_requires: List[str] = []
dev_requires: List[str] = [
    "pypitools",
]
install_requires: List[str] = [
    "pypipegzip",
    "pylzma",
    "typing",
]
make_requires: List[str] = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires: List[str] = [
    "pyclassifiers",
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
requires: List[str] = config_requires + install_requires + make_requires + test_requires
