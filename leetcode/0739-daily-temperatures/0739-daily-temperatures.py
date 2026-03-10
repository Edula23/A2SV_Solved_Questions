class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        mp = defaultdict(int)
        for i in range(len(temperatures)):
            mp[i] = 0
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                mp[stack[-1][0]] = i
                stack.pop()
            stack.append((i, t))
        res = list(mp.keys())
        res.sort()
        ans = []
        for n in res:
            if mp[n] - n > 0:
                ans.append(mp[n]-n)  
            else:
                ans.append(0)   
        return ans

