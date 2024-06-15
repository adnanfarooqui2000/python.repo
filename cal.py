def add(x=0,y=0):
    z=x+y
    return z
def sub(x=0,y=0):
    z=x-y
    return z
def multi(x=0,y=0):
    z=x*y
    return z
def div(x=0,y=0):
    z=x/y
    return z
print("Please select operator =>\n","+\n","-\n","*\n","/\n")
while True:
  select = int(input("Select operations form 1, 2, 3, 4, :"))
  p=int(input("Enter First Digit :"))
  q=int(input("Enter Secand Digit :"))
  if select == 1:
         print(p+q)
         add(p,q)   
  elif select == 2:
        print(p-q)
        sub(p,q)
  elif select == 3:
         print(p*q)
         multi(p,q)
  elif select == 4:
         print(p/q)
