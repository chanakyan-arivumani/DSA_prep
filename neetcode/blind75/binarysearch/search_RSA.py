class Solution():
    def search(self, nums: list[int], target: int) -> int:
        # [3,5,6,0,1,2], 1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]: # left side is sorted
                if nums[left] <= target < nums[mid]: # target is in left sorted subarray
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

