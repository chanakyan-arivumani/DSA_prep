class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxFreq = 0
        char_count = {}
        max_len = 0
        for right in range(len(s)):
            print(f"left: {left}, right: {right}")
            char_count.setdefault(s[right], 0)
            char_count[s[right]] += 1
            maxFreq = max(maxFreq, char_count[s[right]])

            while (right-left+1) - maxFreq > k: # invalid substring window
                char_count[s[left]] -= 1
                left += 1
            max_len = max(max_len, (right-left+1))

        return max_len
