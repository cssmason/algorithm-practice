class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


if __name__ == '__main__':
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    print(Solution().checkIfPangram(sentence))
