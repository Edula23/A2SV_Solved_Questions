class Solution:
    def findEvenNumbers(self, digits):
        result = set()

        def backtrack(path, used):

            if len(path) == 3:
                num = int("".join(path))
                if num % 2 == 0:
                    result.add(num)

                return

            for i in range(len(digits)):
                if used[i]:
                    continue
                    
                if len(path) == 0 and digits[i] == 0:
                    continue

                used[i] = True
                path.append(str(digits[i]))

                backtrack(path, used)

                path.pop()
                used[i] = False

        backtrack([], [False] * len(digits))

        return sorted(result)