from __future__ import division

def jia(x,y):
    return x+y

def jian(x,y):
    return x-y

def cheng(x,y):
    return x*y

def chu(x,y):
    return x/y

operator= {"+":jia,"-":jian,"*":cheng,"/":chu}

def f(x,o,y):
    print (operator.get(o)(x,y))

f(3,"+",2)
