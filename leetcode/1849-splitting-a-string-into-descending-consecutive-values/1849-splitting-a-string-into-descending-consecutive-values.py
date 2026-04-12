class Solution:
    def splitString(self, s: str) -> bool:
        def backTrack(i, prev):
            if i == len(s):
                return True

            for j in range(i, len(s)):
                val = int(s[i:j+1])
                if val + 1 == prev and backTrack(j+1, val):
                    return True

            return False 


        for i in range(len(s)-1):
            prev = int(s[:i+1])
            if backTrack(i+1, prev):
                return True
        return False