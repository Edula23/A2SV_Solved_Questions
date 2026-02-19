class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_str = [str(n) for n in nums]
        count = Counter(num_str)
        def comparePairs(self, a: str, b:str) -> str:
            temp = a + b
            temp2 = b + a
            if int(temp) > int(temp2):
                return a
            elif int(temp2) > int(temp):
                return b
            else:
                return a
        res = []        
        for n in num_str:
            maxval = "0"
            for n2 in num_str:
                intn2 = int(n2[0])
                print(maxval)
                intmaxval = int(maxval[0])            
                if count[n2] > 0 and intn2 > intmaxval:
                    maxval = n2
                elif count[n2] > 0 and intn2 == intmaxval:
                    maxval = comparePairs(self, n2, maxval)
            for i in range(count[maxval]):
                res.append(maxval)
                count[maxval] -= 1
        if res[0] == "0":
            return "0"
        else:
            return "".join(res)



        

            


                 
