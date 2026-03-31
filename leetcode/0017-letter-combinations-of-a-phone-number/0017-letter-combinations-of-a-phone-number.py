class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z'],}
        nums = []
        res = []
        for d in digits:
            nums.append(phone[int(d)])
        def backTrack(curr, comb):
            if len(comb) == len(digits):
                res.append("".join(comb))
                return
            for c in nums[curr]:                
                comb.append(c)
                backTrack(curr+1, comb)
                comb.pop()
        backTrack(0, [])
        return(res)
        

            


