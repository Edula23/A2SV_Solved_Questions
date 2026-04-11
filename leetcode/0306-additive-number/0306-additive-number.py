class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        def is_valid(a, b, start):
            while start < n:
                c = a + b
                c_str = str(c)
                
                if not num.startswith(c_str, start):
                    return False
                
                start += len(c_str)
                a, b = b, c
            
            return True
        
        for i in range(1, n):
            for j in range(i + 1, n):
                
                a = num[:i]
                b = num[i:j]
                
                if (a[0] == '0' and len(a) > 1) or (b[0] == '0' and len(b) > 1):
                    continue
                
                if is_valid(int(a), int(b), j):
                    return True
        
        return False