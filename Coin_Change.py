class Solution:    
    def coinChange(self, coins, amount):
        dp = [None] * (amount + 1)
        if amount < 1:
            return 0
        left_coins = []
        for coin in coins:
            if coin <= amount:
                left_coins.append(coin)

        if not coins:
            return -1
        return self.coinChangeUtil(left_coins, amount, dp)


    def coinChangeUtil(self, coins, amount, dp):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if dp[amount]:
            return dp[amount]

        if amount == 0:
            return 0
        if amount < 0:
            return - 1

        minimum = sys.maxsize

        for coin in coins:
            changeresult = self.coinChangeUtil(coins, amount - coin, dp)
            if 0 <= changeresult < minimum:
                minimum = 1 + changeresult


        if minimum == sys.maxsize:
            dp[amount] = -1

        else:
            dp[amount] = minimum
        return dp[amount]
