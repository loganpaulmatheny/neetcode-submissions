class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # CACTC

        # Using k to return the most occuring values
        # if k is 2, what two values show up most - if 3, three values etc... 

        # hash or set...
        # if we use a hash then we can then get the top values and return keys

        hash = {}

        for num in nums: 
            if num not in hash: 
                hash[num] = 1
            else: 
                hash[num] += 1
        
        result = []

        # how do we get the largest values in hash 
        # sort the hash to an array based on values 

        for i in range(k): 
            max_key = max(hash, key=hash.get)
            result.append(max_key)
            del hash[max_key]

        return result