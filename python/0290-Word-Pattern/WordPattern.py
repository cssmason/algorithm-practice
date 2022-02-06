class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        return len(pattern) == len(s) and len(set(pattern)) == len(set(s)) == len(set(zip(pattern,s)))

if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    print(Solution().wordPattern(pattern, s))