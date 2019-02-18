#!/usr/bin/env python3
def main(): 
    m1_size=input().split();
    m1_rows=int(m1_size[0]);
    m1_cols=int(m1_size[1]);

    m1=[]
    for i in range(m1_rows):
        row=input();
        row=[float(j) for j in row.split()]
        m1.append(row)

    m2_size=input().split();
    m2_rows=int(m2_size[0]);
    m2_cols=int(m2_size[1]);

    m2=[]
    for i in range(m2_rows):
        row=input();
        row=[float(j) for j in row.split()]
        m2.append(row)

    if m1_cols!=m2_rows:
        print("invalid input")
        raise SystemExit(0)

    res=[]
    for i in range(m1_rows):
        res_row=[]
        for j in range(m2_cols):
            new_val=0
            for k in range(m2_rows):
                new_val+=m1[i][k]*m2[k][j]
            res_row.append(new_val)
        res.append(res_row)

    for i in range(len(res)):
        s=""
        for j in range(len(res[i])):
            s+=str(res[i][j])
            if j != (len(res[i])-1):
                s+=" "
        print(s)

if __name__=="__main__":
    main()
