number=int(input("enter your numbre:"))
if(10<=abs(number)<=99):
 ten=abs(number)//10
 one=abs(number)%10
 reverse=one*10+ten
 if(number<0):
  reverse=-reverse
 print("defeated:",reverse)  
else:
 print("error(your number is false)") 
 
