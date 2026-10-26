class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num , 0) +1
        if any(value >1 for value in freq.values()):
            return True
        else : 
            return False