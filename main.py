class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # n^2 complexity. Goes through every permutation and assumes that there is exactly one solution and no more or less
        # for i in range(len(nums)):
        #     for j in range(1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # O(n) complexity:
        # Make a hash map that maps the value to the index.

        prevMap = {} # Val : Index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i] # if you find the value
            prevMap[n] = i
