# Problem: LeetCode #125 - Valid Palindrome
# Topic: Strings & Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1
            
        # Compare characters (ignore case)
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True

# --- Quick Test ---
if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
    print(is_palindrome("race a car"))                      # Output: False
