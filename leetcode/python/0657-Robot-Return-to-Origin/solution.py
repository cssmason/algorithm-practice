class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for step in moves:
            if step == 'L':
                x -= 1
            elif step == 'R':
                x += 1
            elif step == 'U':
                y += 1
            elif step == 'D':
                y -= 1
        return (x, y) == (0, 0)


if __name__ == '__main__':
    moves = "UD"
    print(Solution().judgeCircle(moves))
