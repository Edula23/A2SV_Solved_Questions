"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {e.id: e for e in employees}
        summ = 0
        def dfs(eid):
            nonlocal summ
            employee= emp[eid]
            summ += employee.importance
            for empl in employee.subordinates:
                dfs(empl)
        dfs(id)
        return summ