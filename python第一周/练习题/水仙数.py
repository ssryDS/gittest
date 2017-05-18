for i in range(100,1000):
    a=int(i/100)
    b=int((i-100*a)/10)
    c = i-100*a-10*b
    if(a*a*a+b*b*b+c*c*c==i):
        print("%d," %i)
