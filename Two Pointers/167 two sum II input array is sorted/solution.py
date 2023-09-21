class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # O(1) space complexity
        # O(n) runtime
        l,r = 0,len(numbers)-1

        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r-=1
            if numbers[l] + numbers[r] < target:
                l+=1
        
        return [l+1,r+1]
    
s = Solution()

print(s.twoSum([2,7,11,15],9))
print(s.twoSum([2,3,4],6))
print(s.twoSum([-1,0],-1))

