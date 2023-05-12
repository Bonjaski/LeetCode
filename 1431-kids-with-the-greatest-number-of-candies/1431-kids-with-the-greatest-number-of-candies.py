class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        ans = []
        max_candy = max(candies)
        
        for candy in candies:
             ans.append(candy + extraCandies >= max_candy)
                
        return ans
            