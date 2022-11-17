# Chapter 3: Data structure - saves / store storage to hold multiple values, manage( create, add, uptade, remove)
# Python Data structure : Lists, Dictionary,(Set , Tuple)
# [4,10,6] ['john', 'mark', 'jane'] [True,False]
nums = [4, 5, 6]
nums = []
friends = [] # empty list
players = list() # creates empty list
names = ['john', 'mark', 'jane']
bool_values = [True, False, True]
print(names)
print(nums)
# list is considered mutable object ( we can change in the list)
print('Hi, ', names[1].title())
print('Hi, ', names[0].title())
print('Hi, ', names[-1].title())
print('Hi, ', names[-2].title())
print('Hi, ', names[-3].title())
# listname.append(newvalue)- adds newvalue to the end of the list
names.append("Alex")
print(names)
names.insert(2,"araz")    # put the 'value' to the 'index
print(names)
names[-1] = 'benny'    # updating the last element of the list 'alex'->'benny'
print(names)
del names[3]
print(names)

print(names)
deleted_name=names.pop()
print(names)
names.pop(0)
print(names)
print('we deleted following names: ', deleted_name)
print(names)


msg = "Hello world"
print(msg)
first_name = 'albert'
last_name = 'lee'
full_name = 'first_name +', '+ last_name'
print(full_name)
full_name = 'albert +', '+ lee'
print(full_name)
guests = ['akmal', 'said', 'lenur']
print(guests[0].title(), 'I am inviting you to the party')
print(guests[1], 'I am inviting you to the party')
print(guests[2], 'I am inviting you to the party')

## Hello Akmal, I am inviting you to the dinner.



print(f'Hello {guests[0].title()}, I am inviting you to the party')
print(f'Hello {guests[1].title()}, I am inviting you to the party')
a = guests.pop(1)
# a = 'said' this is the same as line 51

# chapter 3 : lists sort
cars = ['bmw','lexus','moskvich','tesla']
print('List before sorting: ',cars)
cars.sort()
print('List after sorting: ', cars)
names = ['john', 'jane', 'mark']
print('List after sorting: ', cars)
names.sort(reverse=True)
print('List after sorting: ', names)
cars_models = ['corolla', 'camry', 'model x', '550 xi']
print(guests)
guests.append('max')
print(guests)
print(f'Hello {guests[0].title()}, I am inviting you to the party')
print(f'Hello {guests[1].title()}, I am inviting you to the party')
print(f'Hello {guests[2].title()}, I am inviting you to the party')
 