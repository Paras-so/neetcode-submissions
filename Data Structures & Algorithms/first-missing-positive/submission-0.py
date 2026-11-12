class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set()
        ans = 1
        for num in nums:
            s.add(num)
        for i in range(len(s)):
            if ans not in s:
                break
            else :
                ans+=1
        
        return ans