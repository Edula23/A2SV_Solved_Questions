from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        n_count = Counter(s)
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                print(s[i], s[i+1])
                if n_count[s[i]] == int(s[i]) and n_count[s[i+1]] == int(s[i+1]):
                    return s[i:i+2]
        return ""

