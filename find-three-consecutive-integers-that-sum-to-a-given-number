class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        divthr = num//3
        total = 0
        for i in range(3):
            if divthr + divthr +1 + divthr+2 == num:
                return[divthr, divthr+1, divthr+2]
            elif divthr + divthr -1 + divthr + 1 == num:
                return[divthr - 1, divthr, divthr+1]
            elif divthr + divthr -1 + divthr-2 == num:
                return[divthr-2, divthr -1, divthr]
        return []

            

