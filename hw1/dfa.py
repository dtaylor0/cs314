#!/usr/bin/env python3
class State:
    def __init__(self,name):
        self.name=name
        self.rules={}
        self.is_final=False

def get_state(name,states):
    for state in states:
        if state.name==name:
            return state
    return None

def main():
    states=[]
    symbols=[]
    line=input().split()
    for i in range(1,len(line)):
        states.append(State(line[i]))
    line=input().split()
    for i in range(1,len(line)):
        symbols.append(line[i])
    line=input()
    line=input()
    while line!="end_rules":
        line=line.split()
        current_state=line[0]
        dest_state=line[2]
        symbol=line[4]
        for state in states:
            if state.name==current_state:
                state.rules[symbol]=dest_state
                break
        line=input()
    line=input().split()
    start=line[1]
    line=input().split()
    final_states=[]
    for i in range(1,len(line)):
        final_states.append(line[i])
    for state in states:
        for name in final_states:
            if state.name==name:
                state.is_final=True
    while True:
        current_state=start
        try:
            line=input()
        except EOFError:
            raise SystemExit(0)
        is_rejected=False
        for letter in line:
            current_state=get_state(current_state,states)
            if current_state==None:
                print("rejected")
                is_rejected=True
                break
            current_state=current_state.rules.get(letter)
        if(is_rejected):
            continue
        current_state=get_state(current_state,states)
        if current_state is None:
            print("rejected")
            continue
        if not current_state.is_final:
            print("rejected")
        else:
            print("accepted")

if __name__=="__main__":
    main()
