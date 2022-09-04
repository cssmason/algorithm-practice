class Solution:
    def decodeString(self, s: str) -> str:
        curr_num, curr_str, stack = 0, '', []
        for c in s:
            if c.isdigit():
                curr_num = 10 * curr_num + int(c)
            elif c == '[':
                stack.append((curr_num, curr_str))
                curr_num, curr_str = 0, ''
            elif c == ']':
                prev_num, prev_str = stack.pop()
                curr_str = prev_str+ prev_num * curr_str
            else: curr_str += c
        return curr_str

if __name__ == '__main__':
    s = "2[abc]3[cd]ef"
    print(Solution().decodeString(s))