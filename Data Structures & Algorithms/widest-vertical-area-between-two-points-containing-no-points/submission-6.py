class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        max_width = 0
        points.sort()
        for i in range(len(points)-1):
            max_width = max(points[i+1][0] - points[i][0], max_width)
        return max_width
