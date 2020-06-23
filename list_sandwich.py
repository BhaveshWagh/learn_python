sandwich_orders = ['tuna', 'corn & peas', 'veg shammi', 'chopped cheese']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am working on your order that is {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)

print("\n")
for finished_sandwiches in finished_sandwiches:
    print(f" I made your {finished_sandwiches} sandwich ")
