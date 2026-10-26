class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        st = []

        for char in s:
            if char not in paren:
                st.append(char)
            elif st and st[-1] == paren[char]:
                st.pop()
            else:
                return False

        return not st