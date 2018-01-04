import unittest
from scripts.es_adapter import add_test


class TestEsAdapter(unittest.TestCase):
    def test_add_test(self):
        add_test()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
