class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        seqlist = []
        seqlen = []
        curlen = 0
        while i+1 < len(nums):
            if nums[i+1] == nums[i] + 1:
                start = nums[i]
                curlen += 2
            elif nums[i+1] == nums[i]:
                i += 1
                continue
            else:
                start = nums[i+1]
                seqlen.append(curlen)
                curlen = 1
            i+=1
        seqlen.append(curlen)
        return max(seqlen)

    def longCon(self, nums):
        numd = {i: i for i in nums}
        start = []
        for i in nums:
            if i-1 not in numd:
                start.append(i)
        seqlens = []
        print(f"start: {start}")
        while start:
            num = start.pop()
            seq = [num]
            for i in range(num, len(nums)):
                print(f"i:{i}, i+1:{i+1}")
                if numd.get(i+1) is not None:
                    seq.append(i+1)
            print(f"seq: {seq}")
            seqlens.append(len(seq))
        return max(seqlens)
