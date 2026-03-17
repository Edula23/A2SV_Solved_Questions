class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        count = Counter(answers)
        res = k = c = 0
        for i in range(len(answers)):
            if answers[i] == 0:
                res += 1
            elif i != 0 and answers[i] != answers[i-1]:
                res+=answers[i] + 1
                k = answers[i] + 1
                c = 1
            elif i != 0 and answers[i] == answers[i-1] and c < k:
                c+=1
            elif i != 0 and answers[i] == answers[i-1] and c >= k:
                res+=answers[i] + 1
                k = answers[i] + 1
                c = 1    
            elif i==0:
                res+=answers[i] + 1
                k = answers[i] + 1
                c = 1 

        return res