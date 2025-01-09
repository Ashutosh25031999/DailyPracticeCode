class Solution:
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
        sign = 1 if ((dividend < 0) ^ (divisor < 0)) else 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            k = 0
            while dividend >= divisor << (k + 1):
                k += 1
            dividend -= (divisor << k)
            res += 1 << k
        MAX_INT = (1 << 31) - 1
        return -res if sign else (res if res <= MAX_INT else MAX_INT)

# Testing the divide method
test_cases = [
    (10, 3),
    (7, -3),
    (0, 1),
    (1, 1),
    (-1, 1),
    (1, -1),
    (123456789, 1),
    (-2147483648, -1),  # Edge case for MAX_INT overflow
    (2147483647, 1)    # Edge case for MAX_INT
]

solution = Solution()
for dividend, divisor in test_cases:
    result = solution.divide(dividend, divisor)
    print(f"divide({dividend}, {divisor}) = {result}")
