class Solution:
    def maxCoins(self, nums):
        # Add 1 on both sides to handle boundary cases easily
        nums = [1] + nums + [1]
        n = len(nums)

        # dp[left][right] means max coins from balloons between left and right
        dp = [[0] * n for _ in range(n)]

        # length is the gap between left and right
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length

                # Try each balloon as the last balloon burst in this range
                for i in range(left + 1, right):
                    coins = nums[left] * nums[i] * nums[right]
                    coins += dp[left][i] + dp[i][right]

                    dp[left][right] = max(dp[left][right], coins)

        return dp[0][n - 1]