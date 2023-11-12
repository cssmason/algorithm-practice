class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirX, dirY = 0, 1
        x, y = 0, 0
        for step in instructions:
            if step == "G":
                x, y = x + dirX, y + dirY
            elif step == "L":
                dirX, dirY = -1*dirY, dirX
            else:
                dirX, dirY = dirY, -1*dirX
        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)


if __name__ == '__main__':
    instructions = "GGLLGG"
    print(Solution().isRobotBounded(instructions))
