import os
import unittest

import pyanyzip.core


class TestAll(unittest.TestCase):

    def testPass(self):
        pass

    def testOpenNotExists(self):
        self.assertRaises(FileNotFoundError, pyanyzip.core.openzip, name="data/doesnt_exist.txt", mode="rt")

    def testOpenTextFile(self):
        print(os.getcwd())
        pyanyzip.core.openzip(name="data/text.txt", mode="rt")
