import os
import unittest

import pyanyzip


class TestAll(unittest.TestCase):

    def testPass(self):
        pass

    def testOpenNotExists(self):
        self.assertRaises(FileNotFoundError, pyanyzip.open, name="data/doesnt_exist.txt", mode="rt")

    def testOpenTextFile(self):
        print(os.getcwd())
        pyanyzip.open(name="data/text.txt", mode="rt")
