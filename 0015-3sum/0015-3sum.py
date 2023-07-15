class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
    
        for i in range(len(nums)-2):

            left, right = i+1, len(nums) -1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                
                sum_2 = nums[left] + nums[right]
                sum_3 = sum_2 + nums[i]

                if sum_3 < 0:
                    left += 1

                elif sum_3 > 0:
                    right -= 1

                elif sum_3 == 0:
                    
                    if len(ans) > 0 and ans[-1] == [nums[i], nums[left], nums[right]]:
                        
                        left += 1
                        right -=1
                                                    
                    else:
                        
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
    
        return ans