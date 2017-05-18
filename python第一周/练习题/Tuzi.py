def Tuzi(n):
    if(n==1 or n==2):
        return 1
    else:
        return Tuzi(n-1)+Tuzi(n-2)

number=int(input('请输入月数:'))
result=Tuzi(number)
print('%d月后的兔子总数为%d' %(number,result))
