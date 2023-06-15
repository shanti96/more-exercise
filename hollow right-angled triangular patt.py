n=5
for i in range(n):
    for j in range(n):
        if j==n-1 or i==n-1 :
            print('*',end=' ')
        elif j==2 and i==2:
            print('*',end=' ') 
        elif i==1 and j==3 or i==3 and j==1 :
            print('*',end=' ')  
        else:
            print(' ',end=' ') 
    print()           
