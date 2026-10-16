# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         freq = {}
#         ans = 0
#         for num in nums:
#           freq[num] = freq.get(num , 0) +1
#           if freq[num] > len(nums) //2 :
#             ans  = num

#         return ans

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
            if nums[i] == candidate:
                count +=1   
            else :
                count -=1
            
        return candidate