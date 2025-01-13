class Solution:
    def summaryRanges(self, nums):
        out = []
        i = 0
        while i < len(nums):
            start = nums[i]
            end = nums[i]
            i +=1
            while i < len(nums) and nums[i] == end + 1 :
                end = nums[i]
                i +=1
            if start < end:
                out.append(f"{start}->{end}")
            else:
                out.append(f"{start}")
                
        return out