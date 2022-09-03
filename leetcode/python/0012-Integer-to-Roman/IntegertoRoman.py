class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        bases = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ""
        for symbol, base in zip(symbols, bases):
            if num // base:
                count = num // base
                res += symbol * count
                num = num % base
        return res