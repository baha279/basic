# chapter 4 : looping through the list
places = [ 'hawaii', 'paris', 'bahamas', 'iceland']
print('looping through entire list: ')
print(f' I want to visit {places[0]} nest summer')
#for var_each_element in list_name:
print('this is the code to repeat')


for a in places:
    print(a)


 # range(5) -> 0,1,2,3,4
 #range(2,6) -> 2, 3, 4, 5(6-1)
 #range(4,16,3) -> 4,7,10,13
print(range(5))
print(list(range(5)))
for num in range(5):
     print(f'Each number : {num}')

nums = list(range(5))

print(f"Each number : {num}")


# list all numbers between 21 and 35 that can be devided by 4
for num in range(24, 37, 4):
    print(f'each number: {num}')
 # create a list the squares of numbers between 25 to 30
num_squares = []
for num in range (25, 31):
    print(f"num= {num} and square is : {num**2}")
    num_squares.append(num**2)

print("final list of squares", num_squares)

nums = [4, 2, 9, 10]
print(f'sum of the nums: {sum(nums)}')
sum = 0

for num in nums:
    sum= sum + num
print(sum)

