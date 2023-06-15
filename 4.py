# input ka use kar ke 3 alag variables mein 3 integers ka input lein.
#  Input lene ke baad inn 3 mein se sabse bade number ko print karo.

a=int(input("take first number "))
b=int(input("take second number "))
c=int(input("take third number "))
if a>b and a>c:
    print("a sabse bade number hain")  
elif b>c and b>a:
    print("b sabse bade number hain") 
elif c>a and c>b:
    print("c sabse bade number hain")   
else:
    print("bade number nahi hain")        