class Solution(object):
    def twoSum(self, nums, target):
        for i in range (len(nums) - 1):
            j = i + 1
            for j in range (j,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
            

        