#cars = ["audi","ferrari", "ford focus", "toyta sienna hybrid"]
#groceries = ['grapes', 'oranges', 'bananas']

#def car_adder(thing_to_add, target_list):
#    if thing_to_add[0].lower() in 'abcdefj':
#        print("This thing starts with A-G")
#        target_list.append(thing_to_add)
#    else:
 #       print("This thing starts with H-Z and we are not allowing it in our club")
    
#car_adder("BMW",cars)
#car_adder("Honda", cars)
#car_adder("cinnamon", groceries)
#car_adder("apples", groceries)

#print(cars)
#print(groceries)

#def addTwo(num):
#    return num + 2
#def addThree(num):
#    return num + 3
#print(addThree(addTwo(5)))

#def namePrinter(first, last, middle):
#    return f"The name's {last}, {first},{middle}, {last}"
 
#print(namePrinter("James", "Bond", " Freedy"))

def giveMeMySports(name_to_add):
    sports_dic = {'soccer': ['Manchester city', 'Liverpool', 'Bayern Muich'],
                    'basketball': 'cavaliers', 
                    'baseball': 'Marlins'}
    sports_dic['wrestling']= name_to_add
    return sports_dic

print(giveMeMySports('Dan Gable'))

