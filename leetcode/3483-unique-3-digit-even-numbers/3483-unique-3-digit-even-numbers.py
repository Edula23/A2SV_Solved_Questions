class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        all = set()
        used = [False] * len(digits)
        def rec(num):
            temp = "".join(num)
            if len(temp) >= 3:                
                if int(temp) % 2 == 0 and int(temp) >= 100 :
                    all.add(int(temp))
                return 
            for i in range(len(digits)):
                if used[i]:
                    continue
                used[i] = True
                num.append(str(digits[i]))
                rec(num)
                num.pop()
                used[i] = False
            return

        rec([])
        return(len(all))
        