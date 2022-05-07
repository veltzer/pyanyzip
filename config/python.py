import config.project

package_name = config.project.project_name

install_requires = [
    "pypipegzip",
    "pylzma",
    "typing",
]

test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "pymakehelper",
]

dev_requires = [
    "pyclassifiers",
    "pypitools",
    "pydmt",
    "Sphinx",
]

python_requires = ">=3.10"

test_os = ["ubuntu-22.04"]
test_python = ["3.10"]
