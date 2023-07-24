#grocery_list = ["apple", "banana", "organge", "spinach", "kale", "curry", "potatoes", "quiche", "qunioa"]
#my_enumeration_station = list(enumerate(grocery_list))
#print(my_enumeration_station)

#[(0, "apple"), (1, "banana"), (2, "organge"), (3, "spinach"), (4, "kale"), (5, "curry"), (6, "potatoes"),(7, "quiche"), (8,"qunioa")]
#print(type(my_enumeration_station[4]))

#my_tup = ('cat, 5')
#print(my_tup)

nums_one = [1,2,3]
nums_two = [3,4,5]
prompt = "Find all the unique numbers between two list"
new_list = set(nums_one + nums_two)
for i in new_list:
    print(i)