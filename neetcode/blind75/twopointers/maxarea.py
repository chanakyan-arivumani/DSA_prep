class Solution:
    def maxArea_bruteforce(self, heights: list[int]) -> int:
        max_area = 0
        for i in range(0, len(heights)-1):
            for j in range(i+1, len(heights)):
                diff = (i-j) if i > j else (j-i)
                area = min(heights[i], heights[j]) * diff
                max_area = max(area, max_area)
        return max_area

    def max_area(self, heights):
        l = 0
        r = len(heights)-1
        max_area = 0
        while True:
            print(f"l: {l}, r: {r}")
            print(f"left: {heights[l]}, right: {heights[r]}")
            if l == r:
                break
            diff = (l-r) if l > r else (r-l)
            area = min(heights[l], heights[r]) * diff
            max_area = max(area, max_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            print(max_area)
        return max_area
