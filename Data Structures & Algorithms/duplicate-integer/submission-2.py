class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen :
                seen.add(nums[i])
        if len(seen) != len(nums):
            return True
        else :
            return False
            
       