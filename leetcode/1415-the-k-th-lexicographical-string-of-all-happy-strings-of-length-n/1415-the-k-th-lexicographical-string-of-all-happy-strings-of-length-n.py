class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy = ['a', 'b', 'c']
        res = []
        def backTrack(string):
            if len(res) == k:
                return 
            if len(string) == n:
                res.append("".join(string))
                return

            for i in range(3):
                if not string or string[-1] != happy[i]:
                    string.append(happy[i])
                    backTrack(string)
                    string.pop()

        backTrack([])
        if k <= len(res):
            return res[k-1]
        return ""
        
        
            
