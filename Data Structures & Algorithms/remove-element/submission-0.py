class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val :
                k += 1
            else:
                pass
        i = 0
        j = len(nums) - 1
        while (j > i) :
            if nums[i] != val:
                 i+=1
            elif nums[j] == val:
                j-=1
            else :
                nums[i],nums[j] = nums[j], nums[i]
                i+=1
                j-=1
        return k