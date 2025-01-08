class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x *= sign

        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10

        res *= sign

        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0

        return res

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    x = 123
    print(f"Input: {x}, Reversed: {solution.reverse(x)}")  # Output: 321

    # Test case 2
    x = -123
    print(f"Input: {x}, Reversed: {solution.reverse(x)}")  # Output: -321

    # Test case 3
    x = 120
    print(f"Input: {x}, Reversed: {solution.reverse(x)}")  # Output: 21

    # Test case 4
    x = 0
    print(f"Input: {x}, Reversed: {solution.reverse(x)}")  # Output: 0
