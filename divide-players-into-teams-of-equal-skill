class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) == 2:
            return skill[0] * skill[1]
        skill.sort()
        i = 0
        j = len(skill)-1
        curr = skill[i] + skill[j]
        res = skill[i] * skill[j]
        i+=1
        j-=1
        while i!=j and i<j:
            print(skill[i],  skill[j])
            if skill[i] + skill[j] == curr:
                res += skill[i] * skill[j]
            else:
                return -1
            i+=1
            j-=1
        return res

