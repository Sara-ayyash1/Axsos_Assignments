import unittest

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self


# ============================================================
# Tests
# ============================================================
# The Unit Test class using setUp()
class TestMathDojo(unittest.TestCase):
    
    def setUp(self):
        # setUp() runs before EVERY test
        self.md = MathDojo()

    def test_add(self):
        self.md.add(2).add(2, 5, 1)
        self.assertEqual(self.md.result, 10)

    def test_subtract(self):
        self.md.subtract(5, 2).subtract(3)
        self.assertEqual(self.md.result, -10)

    def test_complex_chaining(self):
        self.md.add(2).add(2, 5, 1).add(4, 8, 6, 7).subtract(9, 1, 3).subtract(3, 2)
        self.assertEqual(self.md.result, 18)

if __name__ == '__main__':
    unittest.main()