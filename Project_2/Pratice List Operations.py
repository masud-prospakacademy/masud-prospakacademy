
my_shopping_list = []
print(f"Initial list: {my_shopping_list}")

my_shopping_list.append("Apples")
my_shopping_list.append("Bread")
my_shopping_list.append("Milk")
print(f"After appends: {my_shopping_list}")

my_shopping_list.insert(1, "Eggs")
print(f"After inserting Eggs at index 1: {my_shopping_list}")

print(f"First item (index 0): {my_shopping_list[0]}")
print(f"Last item (index -1): {my_shopping_list[-1]}")
print(f"Item at index 2: {my_shopping_list[2]}")


print(f"First two items: {my_shopping_list[:2]}")
print(f"From index 2 to end: {my_shopping_list[2:]}")
print(f"Reversed list: {my_shopping_list[::-1]}")

my_shopping_list.remove("Bread")
print(f"After removing Bread: {my_shopping_list}")

popped_item = my_shopping_list.pop(0)
print(f"Popped item: {popped_item}")
print(f"List after pop: {my_shopping_list}")

my_shopping_list.append("Bananas")
my_shopping_list.append("Cheese")
my_shopping_list.append("Avocado")

my_shopping_list.sort()
print(f"Sorted list: {my_shopping_list}")

print(f"Final list length: {len(my_shopping_list)}")