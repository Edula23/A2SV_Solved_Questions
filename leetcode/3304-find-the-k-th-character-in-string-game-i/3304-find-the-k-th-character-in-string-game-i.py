class Solution:
    def kthCharacter(self, k: int) -> str:
        def rec(word):
            if len(word) > k:
                return word[k-1]
            temp = ''
            for i in range(len(word)):
                temp += chr((ord(word[i])-97+1)%26 + 97)
            return rec(word+temp)
        return rec('a')

        