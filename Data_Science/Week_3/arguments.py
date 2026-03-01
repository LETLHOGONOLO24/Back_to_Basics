def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emily", "Tobias", "Linus")
print(my_function)

def my_func(*args):
    print("\nType:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

my_func("Emily", "Tobias", "Linus")

def my_func_2(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

def my_func_3(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_func_3(1,2,3))
print(my_func_3(10,20,30,40))
print(my_func_3(5))

def my_func_4(**kid):
    print("His last name is " + kid["lname"])

my_func_4(fname = "Tobias", lname = "Refnes")

# Using kwargs with regular arguments

def my_func_5(username, **details):
    print("Username:", username)
    print("Additional details:")
    
    for key, value in details.items():
        print(" ", key + ":", value)
        
my_func_5("emil123", age = 25, city = "Oslo", hobby = "coding")

# Combining *args and **kwargs

def my_func_6(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_func_6("User Info", "Emil", "Tobias", age=25, city="Oslo")

# Unpacking arguments

def my_func_7(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = my_func_7(*numbers) # Same as my_func_7(1, 2, 3)
print(result)

# Unpacking dictionaries with **

def my_func_7(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refnes"}
my_func_7(**person)