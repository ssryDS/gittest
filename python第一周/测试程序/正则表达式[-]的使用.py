import re
print ("[]的特殊使用数字可以用1-10的‘-’来表示一连串的数字")
r=r"t[1-9]p"
s="sakdjfkjsadtt0tptti0rttptpttpt9t0pt4t4pt4pt43wp243pt2pt54ptp4p4tptp4ptp4t 5p023352"
print(re.findall(r,s))
print()
print("*任意次+一次或更多？一次或零次（表示某个字符可有可无）,《对单字符的特殊定义》")
rx=r"abcd8*"
sx="abcd8s8"
print(re.findall(rx,sx))
rj=r"abcd8+"
sj="abcd8s88888sdfsdf"
print(re.findall(rj,sj))
rw=r"010-?\d{8}"
print(re.findall(rw,"01012345678"))
print(re.findall(rw,"010-12345678"))
