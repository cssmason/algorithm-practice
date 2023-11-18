from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def gen(S: str):
            if not S or (len(S) > 1 and S[0] == S[-1] == '0'):
                return []
            if S[-1] == '0':
                return [S]
            if S[0] == '0':
                return [S[0] + '.' + S[1:]]
            return [S] + [S[:i] + '.' + S[i:] for i in range(1, len(S))]

        s = s[1:-1]
        return ['(%s, %s)' % (a, b) for i in range(len(s)) for a, b in itertools.product(gen(s[:i]), gen(s[i:]))]
