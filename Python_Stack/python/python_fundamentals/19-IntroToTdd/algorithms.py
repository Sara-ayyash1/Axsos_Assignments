import unittest

# ============================================================
# 1. reverseList
# ============================================================
# Reverses a list in place without creating a temporary array
# Uses two pointers — one from the start, one from the end
# Swaps values until both pointers meet in the middle

def reverseList(arr):
    """Reverses the values in the list in-place."""
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    return arr


# ============================================================
# 2. isPalindrome
# ============================================================
# Checks if a word reads the same forwards and backwards
# Example: "racecar" reversed is still "racecar" ✅
# word[::-1] reverses the string using slicing

def isPalindrome(word):
    return word == word[::-1]


# ============================================================
# 3. coins
# ============================================================
# Calculates the minimum number of coins needed for a given amount
# Order: quarters(25) -> dimes(10) -> nickels(5) -> pennies(1)
# Use // to get how many coins, % to get the remainder

def coins(cents):
    quarters = cents // 25      # how many quarters
    cents %= 25                 # remainder after quarters

    dimes = cents // 10         # how many dimes
    cents %= 10                 # remainder after dimes

    nickels = cents // 5        # how many nickels
    cents %= 5                  # remainder after nickels

    pennies = cents             # everything left is pennies

    return [quarters, dimes, nickels, pennies]


# ============================================================
# 4. BONUS - factorial (recursive)
# ============================================================
# Returns the factorial of a number: n! = n * (n-1) * ... * 1
# Example: 4! = 4 * 3 * 2 * 1 = 24
# Base case: factorial(0) = 1
# Recursive case: n * factorial(n-1)

def factorial(n):
    if n == 0:                    # base case - stop here
        return 1
    return n * factorial(n - 1)  # call itself with n-1


# ============================================================
# 5. BONUS - fibonacci (recursive)
# ============================================================
# Returns the nth Fibonacci number: 0, 1, 1, 2, 3, 5, 8, 13...
# Each number = sum of the two numbers before it
# Base cases: fib(0) = 0, fib(1) = 1
# Recursive case: fib(n) = fib(n-1) + fib(n-2)

def fibonacci(n):
    if n == 0:                                    # base case
        return 0
    if n == 1:                                    # base case
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)   # call itself twice


# ============================================================
# Tests
# ============================================================

class TestAlgorithms(unittest.TestCase):

    # --- reverseList tests ---
    def test_reverseList(self):
        self.assertEqual(reverseList([1, 3, 5]), [5, 3, 1])
        self.assertEqual(reverseList([1, 2]), [2, 1])
        self.assertEqual(reverseList([1]), [1])
        self.assertEqual(reverseList([]), [])

    # --- isPalindrome tests ---
    def test_isPalindrome(self):
        self.assertTrue(isPalindrome("racecar"))
        self.assertFalse(isPalindrome("rabcr"))
        self.assertTrue(isPalindrome("madam"))
        self.assertTrue(isPalindrome("a"))
        self.assertTrue(isPalindrome(""))
        self.assertFalse(isPalindrome("leveal"))

    
    # --- coins tests ---
    def test_coins(self):
        self.assertEqual(coins(87), [3, 1, 0, 2])
        self.assertEqual(coins(41), [1, 1, 1, 1])
        self.assertEqual(coins(10), [0, 1, 0, 0])
        self.assertEqual(coins(5), [0, 0, 1, 0])
        self.assertEqual(coins(0), [0, 0, 0, 0])

    # --- factorial tests ---
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(4), 24)

    # --- fibonacci tests ---
    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(6), 8)


if __name__ == '__main__':
    unittest.main()