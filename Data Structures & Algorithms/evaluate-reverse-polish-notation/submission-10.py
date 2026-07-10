import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        result=0
        for ch in tokens:
            print("Character",ch)
            if ch == "+":
                b=stack.pop()
                a=stack.pop()
                result=math.ceil(a+b)
                stack.append(result)
                print("A",a)
                print("A",b)
                print("A",result)
                print("A",stack)
            elif ch=="-":
                b=stack.pop()
                a=stack.pop()
                result=math.ceil(a-b)
                stack.append(result)
                print("S",a)
                print("S",b)
                print("S",result)
                print("S",stack)
            elif ch=="*":
                b=stack.pop()
                a=stack.pop()
                result=math.ceil(a*b)
                stack.append(result)
                print("M",a)
                print("M",b)
                print("M",result)
                print("M",stack)
            elif ch=="/":
                b=stack.pop()
                a=stack.pop()
                result=int(a/b)
                stack.append(result)
                print("D",a)
                print("D",b)
                print("D",result)
                print("D",stack)
            else:
                stack.append(int(ch))
                print("Stack",stack)
        if result==0:
            return stack[0]
        return result

