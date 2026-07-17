class Solution:
    def longsub(self, s: str) -> int:
        last_seen = {}
        left = 0
        maxlen = 0
        for right, ch in enumerate(s):
            if ch in last_seen and left <= last_seen[ch]:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            maxlen = max(right-left+1, maxlen)
        return maxlen
