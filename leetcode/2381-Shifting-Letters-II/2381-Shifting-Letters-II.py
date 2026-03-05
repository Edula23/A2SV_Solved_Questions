class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s= list(s)
        nums = [0] * (len(s) + 1)
        for l, r, k in shifts:
            nums[l] += 1 if k == 1 else -1
            if r + 1 < len(nums):
                nums[r+1] -= k if k==1 else -1
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        for i in range(len(s)):
            s[i] = chr((ord(s[i]) - ord('a') + nums[i]) % 26 + ord('a'))
        return "".join(s)