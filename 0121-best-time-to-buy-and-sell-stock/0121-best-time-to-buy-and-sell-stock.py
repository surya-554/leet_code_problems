class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price to infinity and max profit to 0
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the lowest purchase price seen so far
            if price < min_price:
                min_price = price
            # Calculate potential profit if sold today and update max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit