# Problem: LeetCode #1 - Two Sum
# Topic: Arrays & Hash Maps
# Time Complexity: O(n)
# Space Complexity: O(n)

def two_sum(nums, target):
    """
    Finds two numbers in 'nums' that add up to 'target'
    and returns their indices.
    """
    seen = {}  # Stores number -> index mapping
    
    for index, num in enumerate(nums):
        complement = target - num
        
        # If the complement exists in our map, we found the pair
        if complement in seen:
            return [seen[complement], index]
        
        # Otherwise, record the current number's index
        seen[num] = index
        
    return []

# --- Quick Test ---
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices: {result}")  # Expected Output: [0, 1]
