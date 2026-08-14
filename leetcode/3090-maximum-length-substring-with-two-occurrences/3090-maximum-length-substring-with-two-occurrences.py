class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        setS = set(s)
        count = defaultdict(int)
        maxLen = 0
        left = 0
        for i in range(len(s)):
            
            while count[s[i]] >= 2:
                count[s[left]]-=1
                left+=1
            count[s[i]] += 1
            maxLen = max(maxLen, i-left+1)
            
        return maxLen

