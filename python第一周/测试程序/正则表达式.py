import re

print("正则表达式")
res=r"t[^io]p"
re2=r"t[io]p"
st="aa top   ttititp teroptrprtrprtrptrtopoprtoptorptopr"
print("正向选择用[]")
print(re.findall(re2,st))
print("取反选择,用[^]")
print(re.findall(res,st))
