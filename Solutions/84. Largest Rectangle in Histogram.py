class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append(-1)
        heights.append(0)
        max_rect = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                j = stack[-1]
                width = i - j - 1
                if height*width > max_rect:
                    max_rect = height*width
                
                
            stack.append(i)
        return max_rect
        
        