password=input("enter your strong password ") 
lenght=len(password)
if lenght>=6 and lenght<=16:
    a=True
    if "$" in password:
        b=True
    else:
        b=False 
else:
    a=False       
for i in password:
    if i>="2" and i<="8":
        c=True   
        break 
    else:
        c=False
for j in password:    
    if j>="A" and i<="Z":
        d=True 
        break
    else: 
        d=False
if a==True and b==True and c==True and d==True: 
    print("strong password") 
else:
    print("weak password")                                
   