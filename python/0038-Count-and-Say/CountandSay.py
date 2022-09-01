class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        
        for _ in range(1, n):
            prev, count = "#", 0
            currStr = ""
            for char in s:
                if char == prev or prev == "#":
                    count += 1
                else:
                    currStr += str(count) + prev
                    count = 1
                prev = char
            
            currStr += str(count) + prev
            s = currStr
        
        return s