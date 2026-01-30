
global_data = "I am data from the global scope!"

def access_global():
    print(f"Inside access_global(): {global_data}")

access_global()
print("-" * 30)


def create_and_destroy_local():
    local_variable = "I am local to this function!"
    print(f"Inside create_and_destroy_local(): {local_variable}")

create_and_destroy_local()

print("-" * 30)

my_name = "Global User"

def greet_user():
    my_name = "Local User" 
    print(f"Inside greet_user() - my_name: {my_name}")

print(f"Before calling greet_user() - my_name: {my_name}")
greet_user()
print(f"After calling greet_user() - my_name: {my_name}")
print("-" * 30)

counter = 0

def increment_counter():
    global counter
    counter += 1
    print(f"Inside increment_counter() - counter: {counter}")

print(f"Global counter before calls: {counter}")
increment_counter()
increment_counter()
print(f"Global counter after calls: {counter}")