from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orgColor = image[sr][sc]
        if color != orgColor:
            image = self.dfs(image, sr, sc, orgColor, color)
        return image

    def dfs(self, image: List[List[int]], sr: int, sc: int, orgColor: int, newColor: int) -> List[List[int]]:
        if 0 <= sr < len(image) and 0 <= sc < len(image[0]) and image[sr][sc] == orgColor:
            image[sr][sc] = newColor
            image = self.dfs(image, sr - 1, sc, orgColor, newColor)
            image = self.dfs(image, sr + 1, sc, orgColor, newColor)
            image = self.dfs(image, sr, sc - 1, orgColor, newColor)
            image = self.dfs(image, sr, sc + 1, orgColor, newColor)
        return image
