from typing import List  # Import List for type hinting

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)  # Get the number of days (length of the array)
        min_price = float('inf')  # Initialize min_price to a very high value (infinity)
        max_profit = 0  # Initialize max_profit as 0 (no transaction yet)

        # Iterate through the price list
        for price in prices:  
            # Update the minimum price if a lower price is found
            if price < min_price:  
                min_price = price  
            
            # Calculate the potential profit if selling at the current price
            profit = price - min_price  

            # Update max_profit if this profit is greater than the previous max profit
            if profit > max_profit:  
                max_profit = profit  

        return max_profit  # Return the maximum profit that can be achieved