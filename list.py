cities = ["mumbai","pune","delhi"]
print(cities)

cities.append('bengaluru')
print(cities)

cities.append('dhule')
print(cities)

cities.remove('pune')
print(cities)

print("city:",cities[2])
cities.remove('dhule')

print("last item",cities[-1])

for city in cities:
   print(city)

for index, city in enumerate(cities):
    print(cities[index])