class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        comstr = ""
        for i in range(len(strs[0])):
            comstr = strs[0][0:i+1]
            for j in range(1, len(strs)):
                if strs[j][0:i+1] != comstr and i == 0:
                    return ""
                elif strs[j][0:i+1] != comstr:
                    return comstr[0:i]
        return comstr



                

