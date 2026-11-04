class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #BRUTE FORCE :- SORT AND ANSWER
        #BETTER :- SET
        arr = set()
        for num in nums:
            arr.add(num)
        max_len = 0
        for num in arr :
            ans = 1
            i=0
            if num-1 not in arr:
                start = num
                while start+1+i in arr:
                    ans+=1
                    i+=1
                max_len = max(max_len , ans)
        return max_len

