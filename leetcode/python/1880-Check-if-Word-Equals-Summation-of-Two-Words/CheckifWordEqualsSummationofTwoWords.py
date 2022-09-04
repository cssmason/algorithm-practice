class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def converter(s: str) -> int:
            num = 0
            for char in s:
                num = num * 10 + ord(char) - ord('a')
            return num

        return converter(firstWord) + converter(secondWord) == converter(targetWord)
        

if __name__ == '__main__':
    firstWord = "acb"
    secondWord = "cba"
    targetWord = "cdb"
    print(Solution().isSumEqual(firstWord, secondWord, targetWord))