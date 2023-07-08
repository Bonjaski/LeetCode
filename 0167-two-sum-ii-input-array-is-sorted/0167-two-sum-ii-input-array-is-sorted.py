class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        ans = []

        for idx, num in enumerate(nums):

            seen[num] = idx

        for idx, num in enumerate(nums):

            look_value = target - num

            if look_value in seen and idx != seen[look_value]:
                index1, index2 = min(seen[look_value] + 1,idx + 1), max(seen[look_value] + 1,idx + 1)
                return [index1, index2]
        