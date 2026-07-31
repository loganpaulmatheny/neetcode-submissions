class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # the way you do this in O(n) and with O(1) memory is that you should use the resultant array for where you put the prefix and postfix values 
        # fill the result array with 1s
        # fill prefix values, then go through the postfix values

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # start at the end
            res[i] *= postfix
            postfix *= nums[i]

        return res