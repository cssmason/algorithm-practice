class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = collections.Counter(ransomNote)
        magazine_count = collections.Counter(magazine)
        
        for key in ransom_count:
            if ransom_count[key] > magazine_count[key]:
                return False
        return True