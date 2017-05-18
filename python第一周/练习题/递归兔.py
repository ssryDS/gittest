def fab(n):
    if(n<1):
        print('输入有错')
        return -1
    if(n==1 or n==2):
        return 1
    else:
        return fab(n-1)+fab(n-2)
number=int(input('请输入经过的月份(超过40会卡):'))
result=fab(number)
print('一对兔子经过%d个月后有兔子%d对' %(number,result))
