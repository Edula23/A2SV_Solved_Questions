class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)
        for b in bills:
            if b == 5:
                count[b] += 1
            elif b == 10:
                if count[5] < 1:
                    return False
                count[5] -= 1
                count[b] += 1
            elif b == 20:
                if count[5] < 1 or (count[5] <= 2 and count[10] < 1):
                    return False
                elif count[5] >= 1 and count[10] >= 1:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] >= 3:
                    count[5] -= 3                
                count[20] += 1
        return True
                

                    
            