class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        ans = 0
        for num in nums:
          freq[num] = freq.get(num , 0) +1
          if freq[num] > len(nums) //2 :
            ans  = num

        return ans

             