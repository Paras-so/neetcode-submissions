class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids :
            survives = True
            while stack and stack[-1]>0 and ast <0:
                if abs(ast)>stack[-1]:
                    stack.pop()
                elif abs(ast) == stack[-1]:
                    stack.pop()
                    survives = False
                    break
                else :
                    survives = False
                    break
            if survives:
                stack.append(ast)

        return stack
