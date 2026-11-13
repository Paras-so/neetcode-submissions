class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i, ops in enumerate(operations) :   
            if ops.lstrip("-").isdigit():
                stack.append(int(ops))
            elif ops == "+":
                stack.append(stack[-1]+stack[-2])
            elif ops == "C":
                stack.pop()
            elif ops == "D":
                stack.append(stack[-1]*2)
        return sum(stack)