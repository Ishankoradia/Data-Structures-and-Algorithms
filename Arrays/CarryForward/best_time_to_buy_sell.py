"""
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Return the maximum possible profit.
"""
def maxProfit(self, A):
    buy_idx = None
    profit = 0
    for i in range(len(A)):
        # Buy
        if(buy_idx is None or A[i] < A[buy_idx]):
            buy_idx = i

        # Sell
        if(A[i] > A[buy_idx] and A[i] - A[buy_idx] > profit):
            profit = A[i] - A[buy_idx]

    return profit