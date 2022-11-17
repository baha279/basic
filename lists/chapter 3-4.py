# 4-8 cubes :
cubes = []
for num in range(1, 11):
    print(num ** 3)
    cubes.append(num ** 3)
    print(f'This is our new list:{cubes}')
    for letter in

# 4-9 list comprehension- short syntax, short form

cubes = [num ** 3 for num in range(1, 11)]
print(cubes)

the same thing

cubes = []
for num in range(1, 11):
    cubes.append(num **3)

   # print  4.1 and 4.2
   pizzas = ['margarita, 'capriciosa', 'funghi']
    for pizza in pizzas:
print(pizza.title())
