class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rec(i, j):
            nonlocal s
            if i >= j:
                return s
            s[i], s[j] = s[j], s[i]
            rec(i+1, j-1)

        return rec(0, len(s)-1)
        