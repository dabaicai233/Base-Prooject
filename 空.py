class Solution:
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        b = len(nums)
        for i in range(b):
            for j in range(i + 1, b):
                if nums[i] + nums[j] == target:
                    a.append(i)
                    a.append(j)
                    b = 0
                    break
        return a


