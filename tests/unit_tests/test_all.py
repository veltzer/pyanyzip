""" basic tests """

import os
import unittest

import pytest

import pyanyzip.core


class TestAll(unittest.TestCase):

    def test_pass(self):
        pass

    def test_open_not_exists(self):
        with pytest.raises(FileNotFoundError):
            pyanyzip.core.openzip(name="data/doesnt_exist.txt", mode="rt")

    def test_open_text_file(self):
        print(os.getcwd())
        with pyanyzip.core.openzip(name="data/text.txt", mode="rt") as stream:
            assert stream.read()
