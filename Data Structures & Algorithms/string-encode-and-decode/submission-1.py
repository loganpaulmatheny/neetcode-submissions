class Solution:

    # Goal is to create an encode function and decode function 
    # e.g. ["Logan", "Matheny"] > encode that as "5#Logan8#Matheny" and the decode function should be able to read it accordingly
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs: 
            res += str(len(i)) + "#" + i
        return res

    def decode(self, s: str) -> List[str]:

        # read 5
        # go until you hit # 
        # add the word to res array 
        # move i and or j
        res, i = [], 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return res
            