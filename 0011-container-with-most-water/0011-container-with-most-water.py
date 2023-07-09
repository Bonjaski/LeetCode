class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        area = 0

        left, right = 0, len(height) - 1
        height_left, height_right = height[left], height[right]

        curr_width = right - left
        curr_height = min(height_left, height_right)

        curr_area = curr_width * curr_height

        while left < right:

            height_left = max(height[left], height_left)
            height_right = max(height[right], height_right)

            curr_width = right - left
            curr_height = min(height_left, height_right)
            curr_area = curr_width * curr_height

        # 오른쪽 왼쪽 포인터를 최대 기둥 높이로 이동시키기 위한 목적
            if height_left <= height_right:
                area = max(area, curr_area)
                left += 1

            else:
                area = max(area, curr_area)
                right -= 1
        
        return area