# Problem: LeetCode #242 - Valid Anagram
# Topic: Strings & Hash Maps
# Time Complexity: O(n)
# Space Complexity: O(1) -- At most 26 lowercase English letters

def is_anagram(s: str, t: str) -> bool:
    # Quick check: If the lengths are different, they cannot be anagrams
    if len(s) != len(t):
        return False

    # Count character frequencies for both strings
    count_s = {}
    count_t = {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    # Compare both dictionary counts
    return count_s == count_t

# --- Quick Test ---
if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # Output: True
    print(is_anagram("rat", "car"))          # Output: False
