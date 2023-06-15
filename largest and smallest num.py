l=0
s=0
for i in range(10):
    a=int(input('enter'))
    if l<a:
        l=a
    elif s>a:
        s=a 
print(l,s)            