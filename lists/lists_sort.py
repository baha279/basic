# chapter 3: lists sort
cars = ['tesla', 'lexus', 'moskvich', 'bmw']
print('Pernament sorting - sort().')
print('List before sorting :', cars)
cars.sort()
print('List after sorting: ', cars)

names = ['john', 'jane', 'mark']
print('list before sorting:', names)
names.sort(reverse=True)
# sorting in desc order
print ('list after sorting: ', names)
print(' sorting temporary -sorted()')
car_models = [ 'corolla', 'camry', 'model x', '550 xi']
print('car models after sorting: ', car_models)
sorted_car_models_asc = sorted(car_models)
sorted_car_models_desc = sorted(car_models, reverse=True)
print('Car models after sorting: ', car_models)
print('sorted car models after sorting in asc order: ', sorted_car_models_asc)
print('sorted car models after sorting in desc order: ', sorted_car_models_desc)

print('reversing the list without sorting: ')
nums = [6, 3, 9, 7, 10]
print('list before reversing: ', nums)
nums.reverse()
print('list after reversing: ', nums)

