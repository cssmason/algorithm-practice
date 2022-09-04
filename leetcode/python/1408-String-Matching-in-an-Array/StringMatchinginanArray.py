class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for sub in words:
            for word in words:
                if sub != word and sub in word:
                    ans.append(sub)
                    break
        return ans