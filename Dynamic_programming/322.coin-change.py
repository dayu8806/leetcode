# https://leetcode.com/problems/coin-change/description/

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.



# 每次调用 dp(n) 都要去展开所有可能的子问题，时间复杂度是指数级 => time limit
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins, reverse=True)

        def dp(n):
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1:
                    continue
                res = min(res, 1 + subproblem)
            return res if res != float('INF') else -1

        return dp(amount)



# Bottom-Up 動態規劃（更簡潔也更快）
# 思路：先算小的金额，最后直接读 dp[amount]
# 时间复杂度：𝑂(amount × ∣coins∣ )
# 空间复杂度：𝑂(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[a] = 组成金额 a 所需的最少硬币数
        # 初始：dp[0] = 0，dp[1..amount] = ∞
        dp = [0] + [float('inf')] * amount     # 初始化一个长度为 amount+1 的列表 dp  ex:amount = 5 then dp = [0, inf, inf, inf, inf, inf]

        # 从 1 到 amount 依次计算
        for a in range(1, amount + 1):
            for coin in coins:     # 「用每一種硬幣」去更新 dp[a]，無論 coins 是什么顺序，最终都能找到最小值。
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)   # 狀態轉移   含義是：用一枚面额為 coin 的硬幣，再加上凑出 a - coin 所需的最优解，取所有面额的最小值。

        return dp[amount] if dp[amount] != float('inf') else -1