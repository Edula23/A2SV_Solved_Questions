from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        paths = "@".join(paths)
        i = 0
        filen = ""
        result = []
        while i<len(paths):
            if paths[i] == '(' and paths[i+1] != ')':
                i+=1
                index = i
                while(paths[i] != ')'):
                    filen += paths[i]
                    i+=1
                mp[filen].append(index)
                filen = ""
            i+=1
        for index in mp.values():
            res = []
            dire = ""
            for j in index:
                a = j - 2
                dire = ""
                anoD = False
                while(a >= 0):
                    if paths[a] == ')':
                        anoD = True
                        a-=1                      
                    elif paths[a] == '@':
                        break
                    elif paths[a] == " " and not anoD:
                        dire+='/'
                        a-=1
                    elif not anoD:                        
                        dire += paths[a]
                        a-=1
                    elif anoD and paths[a] == " ":
                        anoD = False
                        # dire += paths[a]
                        a-=1
                    else:
                        a-=1
                res.append(dire[::-1])
            if len(res) != 1:   
                result.append(res)
        return result
                
                
            

