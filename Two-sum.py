#Problem Statement:

'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

#My Solution:
#Solution 1: Traversing on the array given and finding out the complement.
#This solution has high time complexity and it is not much scalable. 
#We only check the complement on the indexes greater than the current index.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            new_target = target - nums[i]
            if new_target in nums[i+1:]:
                new_index = (nums[i+1:]).index(new_target)
                return [i, new_index+i+1]

#Solution 2: We could use a hash to store the index and the element and reduce the time complexity
#as finding something in a hash has near to constant time complexity.
