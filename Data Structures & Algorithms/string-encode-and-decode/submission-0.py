class Solution:

    # Goal is to use delimiters to encode/decode the list/string properly
    # e.g. ["Logan", "Matheny"] >> "5#Logan8#Matheny" 
    # This should work because it tracks where we need to slice up strings despite 
    # if there are letters or symbols within them. All we care about are the lengths


    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs: 
            res += str(len(i)) + "#" + i
        
        return res


    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res