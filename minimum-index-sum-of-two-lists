class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp = {}
        result = []
        for i in list1:
            if i in list2:
                mp[i] = list1.index(i) + list2.index(i)
        indexs = list(mp.values())
        minin = min(indexs)
        for k, v in mp.items():
            if v == minin:
                result.append(k)
        return result
        
