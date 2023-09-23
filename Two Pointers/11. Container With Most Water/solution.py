class Solution:
    def maxArea(self, height: list[int]) -> int:
        l,r = 0,len(height)-1

        area = 0
        while l < r:
            diff = r - l
            if height[l] > height[r]:
                area = max(area,height[r]*diff)
                r-=1
            elif height[r] > height[l]:
                area = max(area,height[l]*diff)
                l+=1
            else:
                area = max(area,height[r]*diff)
                r-=1

        return area
    

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))