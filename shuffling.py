import random
myList = [2,3,45,64,2,2,1,7,6]
#To take random number 
num = random.choice(myList)
 
my_list = [1, 2, 3, 4, 5]
shuffled_list =  sorted(my_list, key=lambda x: random.random())

# #How sorted works 
# Time Complexity: O(n), where n is the length of the list
# Space Complexity: O(n), where n is the length of the list
my_list = [1, 2, 3, 4, 5]
key=lambda x: random.random()
decorated = [(key(item), item) for item in my_list]
#decorated.sort()

# using random.sample()to shuffle a list
res = random.sample(my_list, len(my_list)-2)
print(res)