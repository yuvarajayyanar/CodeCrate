class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        pre_value=0
        for char in reversed(s):
            value=roman_values[char]
            if value<pre_value:
                total-=value
            else:
                total+=value
            pre_value=value

        return total