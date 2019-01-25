print("MUHAMMAD SOHAIB - 18B-054-CS")
print("SECTION-A")
print("LAB NO-08")
print("28-12-2018\n")

def month(n):
    months = "'JAN' 'FEB' 'MAR' 'APR' 'MAY' 'JUN' 'JUL' 'AUG' 'SEP' 'OCT' 'NOV' 'DEC'"
    months_lst = months.split()
    print(months_lst[n-1])
user = int(input("Enter the month number: "))
month(user)

