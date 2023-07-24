grocey_list = ['apple', 'bananas', 'oranges','spinch','kale', 'potatoes']

#items_to_check = input("what would you like to check?" )

#for items in grocey_list:
#    if items[0] == items_to_check:
#        print(items)
#     else:
#        print("nothing with that letter here")
       
urgent_grocey_list = []

for item in grocey_list:
    if item [0] in ['a', 'b', 'c']:
        urgent_grocey_list.append(item)
    else:
        continue
my_grocey_list = [item for item in grocey_list if item [0] in ['a', 'b', 'c']]


print(my_grocey_list)
print(urgent_grocey_list)