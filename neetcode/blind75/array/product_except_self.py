class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prev = None
        ans = None
        for i in range(len(nums)):
            v = nums.pop(0)
            if prev == 0:
                ans = 0
            elif not ans:
                ans = math.prod(nums)
            else:
                ans = math.prod([(ans//v), prev])
            prev = v
            res.append(ans)
            nums.append(v)
        return res
