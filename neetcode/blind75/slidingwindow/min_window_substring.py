class Solution():
    def minWindow(self, s: str, t: str):
        left = 0
        tmap = {}
        smap = {}
        ans = ""
        formed = 0
        for _ in t:
            tmap[_] = tmap.get(_, 0) + 1
        required = len(tmap)

        for right in range(len(s)):
            smap[s[right]] = smap.get(s[right], 0) + 1
            if tmap.get(s[right]) and smap[s[right]] == tmap[s[right]]:
                formed += 1
            while formed == required:
                window_len = right - left + 1
                if ans == "" or window_len < len(ans):
                    ans = s[left:right+1]
                smap[s[left]] -= 1
                if smap[s[left]] < tmap.get(s[left], 0):
                    formed -= 1
                left += 1
        return ans
