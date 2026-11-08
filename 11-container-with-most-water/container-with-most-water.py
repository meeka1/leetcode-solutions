class Solution:
    def maxArea(self, height: list[int]) -> int:
        ind1, ind2 = 0, len(height)-1
        max_area = 0

        while ind1 < ind2:
            w = ind2 - ind1
            if height[ind1] < height[ind2]:
                h = height[ind1]
                ind1 += 1
            else:
                h = height[ind2]
                ind2 -= 1
            
            area = w * h
            max_area = max(area, max_area)
        
        return max_area
