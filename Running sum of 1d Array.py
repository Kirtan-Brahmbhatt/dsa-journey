arr = [2,7,11,15]
prefix=0
pre_sum=[]
for i in arr:
    prefix=prefix+i
    pre_sum.append(prefix)
print(pre_sum)