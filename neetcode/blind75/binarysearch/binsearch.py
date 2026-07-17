class Solution():
    def __bin_search(self, key, nums, left, right):
        if left > right:
            return -1
        mid = left + (right - left)//2
        if key == nums[mid]:
            return mid
        elif key < nums[mid]:
            right = mid-1
            return self.__bin_search(key, nums, left, right)
        else:
            left = mid + 1
            return self.__bin_search(key, nums, left, right)

    def findKey(self, key: int, nums: list) -> int:
        left = 0
        right = len(nums) - 1
        return self.__bin_search(key, nums, left, right)

