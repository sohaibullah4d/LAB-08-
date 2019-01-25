print("MUHAMMAD SOHAIB - 18B-054-CS")
print("SECTION-A")
print("LAB NO-08")
print("28-12-2018\n")

print("PART(a)")
message = 'The secret of this message is that is secret.'
print('message =',message,'\n')

print("PART(b)")
length = len(message)
print("The length of the string message is:",length,'\n')

print("PART(c)")
count = message.count('secret')
print("In string message the word 'secret' appears", count,'times.\n')

print("PART(d)")
censored = message.replace('secret','xxxxxx')
print(censored)
      
