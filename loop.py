'''
for i in range(2,20,2):
    if i<=18:
        print(i)
'''
# Difference between break & return
# break keyword particular block se bhar nikal deta hai
#return keyword 
def f(n):
    for i in range(1,n+1):
        yield i
        i 
data=f(10)
for i in data :
    print(next(data))