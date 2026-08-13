# Problem: LeetCode #217 - Contains Duplicate
# Topic: Arrays & Hash Sets
# Time Complexity: O(n)
# Space Complexity: O(n)

def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    
    for num in nums:
        # If the number is already in our set, we found a duplicate
        if num in seen:
            return True
        seen.add(num)
        
    return False

# --- Quick Test ---
if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))  # Output: True
    print(contains_duplicate([1, 2, 3, 4]))  # Output: False
