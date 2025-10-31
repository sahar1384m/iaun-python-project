number=int(input("enter your numbre:"))
if(10<=number<=99):
 ten=abs(number)//10
 one=abs(number)%10
 power1=ten**one
 power2=one**ten
 print("the first digit to the power of the second digit:",power1)
 print("the second digit to the power of the first digit:",power2)
else:
 print("error(your number is false)") 