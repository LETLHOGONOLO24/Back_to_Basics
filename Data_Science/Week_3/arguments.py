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