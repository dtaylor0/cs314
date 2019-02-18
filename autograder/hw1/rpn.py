#!/usr/bin/env python3
class Stack:
    def __init__(self):
        self.operands = []
    def push(self, operand):
        self.operands.append(operand)
    def pop(self):
        return self.operands.pop()

def is_num(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def main():
    stack=Stack()
    while True:
        try:
            s=input();
        except EOFError:
            raise SystemExit(0)
        if is_num(s):
            stack.push(float(s))
            print(s)
        else:
            if not stack.operands:
                print("stack is empty")
                continue
            if s=="~":
                a=stack.pop()
                res=-1*a
                stack.push(res)
                print(str(res))
                continue
            if len(stack.operands)<2:
                print("only one number on stack")
                continue
            else:
                b=stack.pop()
                a=stack.pop()
                if s=="+":
                    res=a+b
                    stack.push(res)
                    print(str(res))
                    continue
                elif s=="-":
                    res=a-b
                    stack.push(res)
                    print(str(res))
                    continue
                elif s=="*":
                    res=a*b
                    stack.push(res)
                    print(str(res))
                    continue
                elif s=="/":
                    if b==0:
                        print("error: division by zero")
                        stack.push(a)
                        stack.push(b)
                        continue
                    res=float(a)/float(b)
                    stack.push(res)
                    print(str(res))
                    continue
                else:
                    print("invalid input")
                    stack.push(a)
                    stack.push(b)
                    continue

if __name__=="__main__":
    main()
