class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # O(1) space complexity
        # O(nlogn) + O(n^2) time complexity or O(n^2)
        nums.sort()

        res = []
        for i,a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue

            l,r = i+1,len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l-1] == nums[l] and l < r:
                        l+=1
        return res
    

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))
