class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr_element = []

        num_count = {n:0 for n in nums}
        for n in nums:
            num_count[n] += 1

        def dfs():

            if len(curr_element) == len(nums):
                res.append(curr_element.copy())
                return

            for n in num_count:
                if num_count[n] > 0:
                    num_count[n] -= 1
                    curr_element.append(n)

                    dfs()

                    num_count[n] += 1
                    curr_element.pop()

        dfs()
        return res




            
