def f(x):
    if(x>5):
            return x
l=list(range(10))
print(list(filter(f,l)))
