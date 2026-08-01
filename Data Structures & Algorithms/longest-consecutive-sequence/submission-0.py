class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        mySet = set(nums)
        longest = 0 

        for n in nums: 
            # check to see if it's a start 
            if (n - 1) not in mySet: 
                length = 0
                while (length + n) in mySet: 
                    length += 1 
                longest = max(longest, length)

        return longest