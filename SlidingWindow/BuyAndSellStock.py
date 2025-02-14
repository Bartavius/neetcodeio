'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
'''
def maxProfit(prices) -> int:

    max_profit = 0
    min_price = prices[0]

    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    
    return max_profit