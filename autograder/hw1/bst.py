#!/usr/bin/env python3
class Node:
    def __init__(self,new_data):
        self.data=new_data
        self.left=None
        self.right=None

def insert(value,root):
    new_node=Node(value);
    ptr=root
    if ptr is None:
        return new_node
    while ptr is not None:
        if ptr.data==value:
            return root
        elif ptr.data<value:
            if ptr.right is None:
                ptr.right=new_node
                return root
            else:
                ptr=ptr.right
                continue
        elif ptr.data>value:
            if ptr.left is None:
                ptr.left=new_node
                return root
            else:
                ptr=ptr.left
                continue
    return root

def query(value,root):
    ptr=root
    path="found:"
    if ptr is None:
        print("not found")
        return
    while ptr is not None:
        if ptr.data==value:
            if ptr==root:
                print("found: root")
            else:
                print(path)
            return
        elif ptr.data<value:
            path+=" r"
            ptr=ptr.right
            continue
        elif ptr.data>value:
            path+=" l"
            ptr=ptr.left
            continue
    print("not found")
    return

def main():
    root=None
    while True:
        try:
            instruction=input().split();
        except EOFError:
            raise SystemExit(0)
        if len(instruction)!=2:
            print("invalid input")
            continue
        command=instruction[0]
        value=int(instruction[1])
        if command=="i":
            root=insert(value,root)
        elif command=="q":
            query(value,root)
        else:
            print("invalid input")
            continue


if __name__=="__main__":
    main()
