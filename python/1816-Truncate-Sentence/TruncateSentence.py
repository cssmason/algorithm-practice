class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(' ')
        return ' '.join([s[i] for i in range(k)])
        print(s)
        
if __name__ == '__main__':
    s = "Hello how are you Contestant"
    k = 4
    print(Solution().truncateSentence(s, k))