import unittest
from es_1 import somma


class TestSomma(unittest.TestCase):
    def test_somma(self):
        risultato = somma(2, 4)
        self.assertEqual(risultato, 6, "Should be 6")


if __name__ == "__main__":
    unittest.main()
