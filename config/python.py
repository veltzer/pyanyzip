""" python deps for this project """

import config.shared

install_requires: list[str] = [
    "pypipegzip",
]
build_requires: list[str] = config.shared.PBUILD
test_requires: list[str] = config.shared.PTEST
requires: list[str] = install_requires + build_requires + test_requires
