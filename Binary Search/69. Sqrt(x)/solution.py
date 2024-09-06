class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            middle = (left + right)//2

            if middle*middle < x:
                left = middle + 1
            elif middle*middle > x:
                right = middle - 1
            else:
                return middle
            
        return right

sol = Solution()
print(sol.mySqrt(10))