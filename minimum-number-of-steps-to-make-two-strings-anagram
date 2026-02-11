from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        op = 0
        for k, v in t_count.items():
            if t_count[k] > s_count[k]:
                op += t_count[k] - s_count[k]
        return op
