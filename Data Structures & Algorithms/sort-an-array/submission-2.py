class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            min_indx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_indx]:
                    min_indx = j
            nums[i], nums[min_indx] = nums[min_indx], nums[i]
        return nums