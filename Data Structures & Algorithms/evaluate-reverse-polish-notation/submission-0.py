class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        st = []
        
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                st.append(int(i))
            else:
                # Pop the right operand first, then the left operand
                b = st.pop()
                a = st.pop()
                
                match i:
                    case "+":
                        st.append(a + b)
                    case "-":
                        st.append(a - b)
                    case "*":
                        st.append(a * b)
                    case "/":
                        # int() handles truncation toward zero for both positive and negative results
                        st.append(int(a / b))
                        
        return st[0]