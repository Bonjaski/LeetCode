class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []

        def backtrack(c_sum, index, path):

            if c_sum == 0:
                res.append(path.copy())
            
            if c_sum <= 0:
                return

            prev =- 1

            for i in range(index, len(candidates)):
                if candidates[i] == prev:
                    continue
                
                path.append(candidates[i])
                backtrack(c_sum - candidates[i], i + 1, path) #index로 두면 틀림
                path.pop()
                
                prev = candidates[i]

        backtrack(target, 0, [])
        return res

            





