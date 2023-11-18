from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = {value: index for index, value in enumerate(order)}
        def char2index(word): return [dict[char] for char in word]
        return all(char2index(words[i]) <= char2index(words[i+1]) for i in range(len(words) - 1))


if __name__ == '__main__':
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(Solution().isAlienSorted(words, order))
