class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        res = 0
        while i < j:
            temp = (j - i) * min(height[i], height[j])
            if temp > res:
                res = temp
            
            #iterate the smaller height (comparing i, j)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res