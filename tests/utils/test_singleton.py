from utils import Singleton
import unittest

class TestSingleton(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     pass

    # @classmethod
    # def tearDownClass(cls):
    #     pass

    # def setUp(self):
    #     pass

    # def tearDown(self):
    #     pass

    def test_same_id(self):
        s1 = Singleton()
        s2 = Singleton()

        self.assertEqual(id(s1), id(s2))

