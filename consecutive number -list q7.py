
a=7
l=[]
for i in range(a):
    n=int(input('jknh'))
    l.append(n)
j=0
p=len(l)
while j<int(p):
    if l[j]+1==l[j+1]:
        k='ture'
        j+=1
    else:
        print('not') 
        break
if 'ture'==k:
    print('consecutive') 