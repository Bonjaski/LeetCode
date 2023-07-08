class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtrack(i, cur_arr):

            if i == len(nums):
                res.append(cur_arr.copy())
                return

            cur_arr.append(nums[i])
            backtrack(i+1, cur_arr)
            cur_arr.pop()
            backtrack(i+1, cur_arr)

        backtrack(0, [])
        return res

            