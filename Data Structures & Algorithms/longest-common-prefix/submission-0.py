class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        match = True
        for j in range(len(strs[0])):
            for i in range(len(strs)):
                if j <len(strs[i]) and strs[i][j] == strs[0][j] :
                    pass
                else :
                    match = False
                    break
            if match:
                ans +=strs[0][j]
        return ans