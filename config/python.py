import config.project

package_name = config.project.project_name

console_scripts = [
    'pymakehelper=pymakehelper.endpoints.main:main',
]

setup_requires = [
]

run_requires = [
    'pypipegzip',  # for opening zipped files
    'pylzma',  # for working with .xz files
    'typing',  # for types
]

test_requires = [
    'pylint',  # to check for lint errors
    'pytest',  # for testing
    'pyflakes',  # for testing
]

dev_requires = [
    'pyclassifiers',  # for programmatic classifiers
    'pypitools',  # for upload etc
    'pydmt',  # for building
    'Sphinx',  # for the sphinx builder
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.6"

extras_require={
#    ':python_version == "2.7"': ['futures'],  # for python2.7 backport of concurrent.futures
}
