class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        for ch in s:
            if ch =='['or ch=='(' or ch=='{':
                stack.append(ch)
                top=top+1
                print("Stack",stack)
                print("Top",top)
            else: 
                if top==-1:
                    return False
                print("Stack1",stack)
                print("Top1",top)
                if ch=="]" and stack[top]!='[' or ch=="}" and stack[top]!='{' or ch==")" and stack[top]!='(':
                    return False
                else:
                    stack.pop()
                    top=top-1
        return top==-1
            
