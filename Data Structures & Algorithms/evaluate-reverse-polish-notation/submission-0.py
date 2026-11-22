class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        temp =0
        for val in tokens:
            ans = 0
            if val.lstrip("-").isdigit():
                stack.append(int(val))
            
            elif val == "+" and  stack:
                    
                    temp = stack.pop()
                    ans = stack.pop() + temp
                    stack.append(ans)

            elif val == "-" and  stack:
                    
                    temp = stack.pop()
                    ans = stack.pop() - temp
                    stack.append(ans)

            elif val == "*" and stack:
                    
                    temp = stack.pop()
                    ans = stack.pop()*temp
                    stack.append(ans)

            elif val == "/" and stack:
                    
                    temp = stack.pop()
                    ans = int(stack.pop()/temp)
                    stack.append(ans)

        return stack[-1]

        