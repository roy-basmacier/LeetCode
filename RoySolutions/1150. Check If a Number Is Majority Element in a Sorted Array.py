class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        cnt = 0
        for num in nums:
            if num == target:
                cnt += 1
                if cnt > len(nums)/2:
                    return True
        return False
        