class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = strs[0]
        res_len = len(res)
        for s in strs[1:]:
            while res != s[0:res_len]:
                res_len-=1
                if res_len == 0:
                    return ""
                res = res[0:res_len]


        return res