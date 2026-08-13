# Problem: LeetCode #704 - Binary Search
# Topic: Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)

def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Find center position

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # Target is in right half
        else:
            right = mid - 1  # Target is in left half

    return -1

# --- Quick Test ---
if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))  # Output: 4
    print(search([-1, 0, 3, 5, 9, 12], 2))  # Output: -1
