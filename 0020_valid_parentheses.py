# Problem: LeetCode #20 - Valid Parentheses
# Topic: Stack & Strings
# Time Complexity: O(n)
# Space Complexity: O(n)

def is_valid(s: str) -> bool:
    stack = []
    close_to_open = {")": "(", "}": "{", "]": "["}

    for char in s:
        # If it's a closing bracket
        if char in close_to_open:
            # Check if stack has matching open bracket at the top
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()  # Match found, remove it!
            else:
                return False  # Mismatch or empty stack
        else:
            # It's an opening bracket, add it to stack
            stack.append(char)

    # Return True if all brackets were matched and popped
    return len(stack) == 0

# --- Quick Test ---
if __name__ == "__main__":
    print(is_valid("()[]{}"))  # Output: True
    print(is_valid("(]"))      # Output: False
