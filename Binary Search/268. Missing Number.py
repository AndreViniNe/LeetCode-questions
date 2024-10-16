class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sum_expected = (n*(n+1)) // 2
        sum_actual = sum(nums)
        return sum_expected - sum_actual

         
if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([0,1,3]))
