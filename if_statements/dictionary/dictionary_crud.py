# chapter 6: Dictionary - data structure( key- value pair)
# creating the empty dictionary
person1 = {}
person2 = dict()
person1 = {'name': 'john doe', 'age': 25, 'location': 'ny'}

print('# 2 accessing the value (R)')
print(f"getting name of person1 '{person1['name']}' ...")
print(f"getting name of person1 {person1['age']} ...")

print('#### 3.  adding/updating key value pair to the dictionary (U)')
person1['phone'] = '(123)-456-7891' # phone does not exist in keys in person1 dictionary,
# so it adds new key-value pair(element)
print('updated with new key dictionary: ', person1)
print("updating the value of 'age' in person1 dictionary.")
person1['age'] = 30
print('updated age in person1 dictionary: ', person1)

print('updating the list value inside the dictionary')
cars[0] = 'merc'
person1['cars'][0] = 'merc'
print('updating list (audi to merc) in person1 dictionary: ', person1)

# languages_list = ['eng', 'ru', 'esp', 'marsian']
# person1['languages'] = languages_list
# print(person1)
print( 'updating the list languages_list(marsian to ger)... ')
languages_list[3] = 'ger'
print('updated list: ', language_list)
print('dictionary: ', person1)
person1['language'][2] = 'french'
print('updated list: ', languages_list)
print('dictionary: ', person1)
#delete


odds = list(range(1, 20, 2))
print(odds)
[1, 3, 5, 7, 9, 11, 13, 17, 19]


b = {'num1': 45, 'num2': 55, 'num3': 22}
print(b['num2'])
