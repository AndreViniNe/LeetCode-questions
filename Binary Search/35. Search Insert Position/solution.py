class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        small = 0
        big = len(nums) - 1

        while small <= big:
            middle = (small + big)//2

            if nums[middle] == target:
                return middle
            
            elif nums[middle] > target:
                big = middle - 1
            
            else:
                small = middle + 1

        return small
    
sol = Solution()
print(sol.searchInsert([1,3,5,6], 4))