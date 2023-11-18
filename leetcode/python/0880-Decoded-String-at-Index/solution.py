class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(s):
            k %= size
            if k == 0 and c.isalpha():
                return c
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1

# class Solution:
#     def decodeAtIndex(self, s: str, k: int) -> str:
#         size, index = 0, 0
#         while size < k:
#             if s[index].isdigit():
#                 size *= int(s[index])
#             else:
#                 size += 1
#             index += 1

#         for c in reversed(s[:index]):
#             k %= size
#             if c.isdigit():
#                 size /= int(c)
#             elif k == 0:
#                 return c
#             else:
#                 size -= 1
