# kadane's algorithm
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# ans 6
cursum = [-2, -1, -4, 0, -1, 1, 2, -3, 1]

class Solution:
    def max_sum(self, nums: list[int]):
        bestEndingHere = maxsum = 0
        for i in nums:
            bestEndingHere = max(i, bestEndingHere+i)
            maxsum = max(maxsum, bestEndingHere)
            print(f"bestEndingHere: {bestEndingHere}, maxsum: {maxsum}")
        return maxsum

    def min_sum(self, nums: list[int]):
        leastEndingHere = minsum = nums[0]
        for i in nums[1:]:
            leastEndingHere = min(i, leastEndingHere+i)
            minsum = min(minsum, leastEndingHere)
            print(f"leastEndingHere: {leastEndingHere}, minsum: {minsum}")
        return minsum
