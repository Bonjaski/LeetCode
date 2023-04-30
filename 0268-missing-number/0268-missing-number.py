class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        min_num = 0
        max_num = len(nums) + 1
        
        for i in range(max_num):
            if i not in nums:
                return i
        