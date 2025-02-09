from typing import List  # Import List for type hinting

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)  # Get the length of the prices array
        profit = 0  # Initialize total profit to 0
        lmin = prices[0]  # Initialize local minimum (buy price)
        lmax = prices[0]  # Initialize local maximum (sell price)
        i = 0  # Pointer to traverse the array

        while i < n - 1:  # Loop until the second last element
            # Find local minima (buying point)
            while i < n - 1 and prices[i] >= prices[i + 1]:  
                i += 1  # Move forward if the price is decreasing (skip downward trend)
            lmin = prices[i]  # Found a local minimum (potential buy price)

            # Find local maxima (selling point)
            while i < n - 1 and prices[i] <= prices[i + 1]:  
                i += 1  # Move forward if the price is increasing (ride upward trend)
            lmax = prices[i]  # Found a local maximum (sell price)

            # Add the profit from this transaction
            profit += (lmax - lmin)

        return profit  # Return the total accumulated profit