a =[]

for i in range(100,301):
    if (i%100)%2==0 and (i//10)%2==0 and (i//100)%2==0:
        a.append(i)

print(','.join(map(str,a)))