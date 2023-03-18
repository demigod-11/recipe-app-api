
"""
Sample Tests
"""


from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """
    Test the calc module
    """

    def test_add_numbers(self):
        """
        test adding numbers together
        """
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """
        test subracting numbers together
        """
        res = calc.subtract(15, 10)

        self.assertEqual(res, 5)
