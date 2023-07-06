def pow_sum():
    n=int(input("enter the valu n:"))
    res=0
    for i in range(1,n+1):
        res=res+i**i

    print(res)

pow_sum()