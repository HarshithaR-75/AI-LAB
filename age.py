age=int(input("Enter your age:"))
if age<0:
    print("Age cannot be negative")
elif age>=0 and age <=12:
    print("You are a child")
elif age>=13 and age<=19:
    print("You are a teenager")
elif age>19 and age<65:
    print("You are an adult")
else:
    print("You are a senior citizen")