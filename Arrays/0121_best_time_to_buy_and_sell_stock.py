# Problem: LeetCode #121 - Best Time to Buy and Sell Stock
# Topic: Arrays & Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(1)

def max_profit(prices: list[int]) -> int:
    min_price = float('inf')  # Start with the highest possible number
    max_p = 0                 # Track maximum profit found so far
    
    for price in prices:
        # Keep track of the lowest price seen so far
        if price < min_price:
            min_price = price
        # Calculate profit if we sold today and update max_p
        elif price - min_price > max_p:
            max_p = price - min_price
            
    return max_p

# --- Quick Test ---
if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # Output: 5 (Buy at 1, sell at 6)
    print(max_profit([7, 6, 4, 3, 1]))     # Output: 0 (No profit possible)
