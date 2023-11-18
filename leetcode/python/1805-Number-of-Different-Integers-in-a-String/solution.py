class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = ''.join(char if char.isdigit() else ' ' for char in word)
        return len(set(num.lstrip('0') for num in word.split()))


if __name__ == '__main__':
    word = "a123bc34d8ef34"
    print(Solution().numDifferentIntegers(word))
