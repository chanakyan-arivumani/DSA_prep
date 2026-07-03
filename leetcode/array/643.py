class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # cursum = [0] * len(num)
        # nums =   [1, 12,-5,-6, 50, 3]
        # cursum = [1, 13, 8, 2, 52, 55]
        # for i in range(len(num)):
        #     cursum[i] = cursum[i] + cursum[i+1]

        if k == 1:
            return max(nums)
        cursum = 0
        maxnum = 0
        for i in range(k):
            cursum += nums[i]

        j = 0
        while j+k < len(nums):
            tempsum = cursum - nums[j] + nums[j+k]
            tempavg = tempsum/k
            if tempavg > maxnum:
                maxnum = tempavg
            cursum = tempsum
            j += 1
        return maxnum
    