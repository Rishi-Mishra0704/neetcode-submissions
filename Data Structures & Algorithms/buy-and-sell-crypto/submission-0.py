class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0                      # buy day
        best = 0

        for right in range(len(prices)):      # sell day
            # window = buy on left, sell on right

            if prices[right] < prices[left]:
                # cheaper buy day found, window is useless now
                left = right          # the "shrink" step, as a jump
            else:
                profit = prices[right] - prices[left]
                best = max(best, profit)

        return best