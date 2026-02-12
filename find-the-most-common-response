from collections import defaultdict
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        c_res = defaultdict(int)
        for lis in responses:
            setlis = set(lis)
            for res in setlis:
                c_res[res] += 1
        maxv= 0
        maxk = 0
        for k, v in c_res.items():
            if v >= maxv:
                if v == maxv:
                    if  k[0] < maxk[0]:
                        maxv = v
                        maxk = k
                    elif k[0] == maxk[0] and k < maxk:
                        maxv = v
                        maxk = k
                    elif k[0] == maxk[0] and len(k) == len(maxk) and k < maxk:
                        maxv = v
                        maxk = k
                else:
                    maxv = v
                    maxk = k
        return maxk
