import unittest
from main import karatsuba


class TestKaratsuba(unittest.TestCase):
    def test_multiplicacao(self):
        test_cases = [
            (12345678901234567890, 98765432109876543210),
            (111111111111111111111111, 222222222222222222222222),
            (99999999999999999999, 88888888888888888888),
            (123456789123456789123456789, 987654321987654321987654321),
            (1000000000000000000000000001, 1000000000000000000000000001),
            (314159265358979323846264338327950288419716939937510, 
             271828182845904523536028747135266249775724709369995)

            # #   (2, 4),
            # (15555, 166666555555)
            # # (25, 40),
            # # (10, 2),
            # # (2, 8),
            # # (7, 
            # #  9)
        ]

        for x, y in test_cases:
            with self.subTest(x=x, y=y):
                self.assertEqual(karatsuba(x, y), x * y)
                print(karatsuba(x, y))
                print(x * y)
                print("")

if __name__ == "__main__":
    unittest.main()
