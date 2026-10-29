from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

       # Sort the words to get their 'key' and then add them to the hasmhmap 
        map = defaultdict(list)

        for i in strs:
            key = "".join(sorted(i))
            map[key].append(i)

        return list(map.values())