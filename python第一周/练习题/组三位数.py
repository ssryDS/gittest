print("有 1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？")
l1=[1,2,3,4]
count=0
for i in l1:
    for j in l1:
        for k in l1:
            if(i!=j and j!=k and k!=i):
                if(count%4==0):
                    print()
                print("%d%d%d,   " % (i,j,k) ,end='')
                count+=1

print("共有%d个" %count)


            
    
