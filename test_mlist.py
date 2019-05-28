import unittest

from mlist import *

class Test(unittest.TestCase):

    def test_construct_object(self):
        lista=MLista(20)

        self.assertEqual(lista.capacity,20)



