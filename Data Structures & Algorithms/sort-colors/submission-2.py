class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #SELECTION SORT
        for i in range(len(nums)):
            min_indx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_indx]:
                    min_indx = j
            nums[i], nums[min_indx] = nums[min_indx], nums[i]