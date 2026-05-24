class Solution:
    def passwordStrength(self, password: str) -> int:
        res = 0
        seen = set()
        for c in password:
            if c not in seen:
                seen.add(c)
                if c.isalpha():
                    
                    if c.islower():
                        res += 1
                    else:
                        res += 2
                elif c.isnumeric():
                    
                    res += 3
                else:
                    
                    res += 5
            
        return res

