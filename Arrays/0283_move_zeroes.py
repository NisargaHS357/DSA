# Problem: LeetCode #283 - Move Zeroes
# Topic: Arrays & Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

def move_zeroes(nums: list[int]) -> None:
    # 'left' keeps track of the position to swap the next non-zero element
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            # Swap non-zero element to the left position
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

# --- Quick Test ---
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    print(nums)  # Output: [1, 3, 12, 0, 0]
