config_requires = []
dev_requires = [
    "pypitools",
]
install_requires = [
    "pypipegzip",
    "pylzma",
    "typing",
]
make_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires = [
    "pyclassifiers",
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
