from collections import deque
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        og_color=image[sr][sc]
        if og_color==color:
            return image
        
        m, n=len(image), len(image[0])
        queue = deque([(sr, sc)])
        image[sr][sc]=color
        
        while queue:
            r,c=queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and image[nr][nc]==og_color:
                    image[nr][nc]=color
                    queue.append((nr, nc))
                    
        return image