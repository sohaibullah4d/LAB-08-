import time
print("MUHAMMAD SOHAIB - 18B-054-CS")
print("SECTION-A")
print("LAB NO-08")
print("28-12-2018\n")

def even(x,y):
    for i in range(x,y+1):
        if (i%2==0) and (i%3==0):
            print(i,'is divisible by 2 and 3 both')
        elif (i%2==0):
            print(i,'is divisible by 2')
        elif (i%3==0):
            print(i,'is divisible by 3')
        else:
            print(i,'is not divisible by 2 nor 3')

even(2,16)            
            
