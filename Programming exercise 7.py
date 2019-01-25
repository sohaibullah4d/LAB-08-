print("MUHAMMAD SOHAIB - 18B-054-CS")
print("SECTION A")
print("LAB NO-08")
print("28-12-2018\n")

def cheer(n):
    x = n.upper()
    lst = list(x)
    string = " ".join(lst)
    print("How do you spell winners?")

    print("I know!, I know!")
    print(string,"!")
    print("And that is how you spell winners!")
    print("Go",n.title(),'!....')
user = input("Enter your team name: ")
cheer(user)

