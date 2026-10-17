class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # SELECTION SORT 
        for i in range(len(nums) -1) :
            min = i
            for j in range(i+1 , len(nums)):
                if nums[j] < nums[min] :
                    min = j
            nums[i], nums[min] = nums[min] , nums[i]
        return nums
