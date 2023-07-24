#def greet_user(): 
#    "Display a simple greeting."
#    print("Hello")
#greet_user()

#def greet_user(username):
#    """Display a simple greeting."""
#    print("Hello, " + username.title() + "!")

    ##Postitional Arguments
#def describe_pet(animal_type, pet_name):
#"""Display information about a pet."""
#    print("\nI have a " + animal_type + ".")
#    print("My " +animal_type + "'s name is " + pet_name.title() + ".")

#describe_pet('hamester', 'harry')
#describe_pet('dog', 'willie')

    #Keyword Arguments format
#describe_pet(animal_type='hamster', pet_name= 'harry')

    #Default Values format
#def describe_pet(pet_name, animal_type='dog'):
#    """Display information about a pet."""
#    print("\nI have a " + animal_type + ".")
#    print("My " +animal_type + "'s name is " + pet_name.title() + ".")

#describe_pet(pet_name='willie')

    #Equivalent Function Calls 

#def describe_pet(pet_name, animal_type='dog'):
#    print("\nI have a " + animal_type + ".")
#    print("My " +animal_type + "'s name is " + pet_name.title() + ".")
#    """A dog named Willie"""
#describe_pet('willie')

#"""A hamster named Harry."""
#describe_pet('harry', 'hamster')

    # Returnn Values
#def get_formatted_name(first_name, last_name):
#    """Return a full name, neatly formatted."""
#    full_name= first_name + ' '  + last_name
#    return full_name.title()

#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)
    
    #Opthinal Arguments
#def get_formatted_name(first_name, last_name, middle_name= ''):
#    """Return a full name, neatly formatted."""
#    if middle_name:
#        full_name= first_name + ' '  + middle_name + ' '  + last_name
#    else:
#        full_name = first_name + ' ' + last_name
#    return full_name.title()

#musician = get_formatted_name('john', 'lee' , 'hooker')
#print(musician)

#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)

    #Reuturning a Dictionary 
#def build_person(first_name, last_name, age='', race= ''):
#    """Return a dictionary of information about a person"""
#    person={'first': first_name, 'last': last_name}
#    if age: 
#        person['age'] = age
#    if race:
#        person['race']=race
#    return person
    
#musician = build_person('jimi', 'hendrix', age= 27,race= 'black')
#print(musician)

    #Using a Function with a while Loop
#ef get_formatted_name(first_name, last_name):
#    """Return a full name, neatly formatted."""
#    full_name = first_name+ ' ' + last_name
#    return full_name.title()
#while True:
#    print("\nPlease tell me your name:")
#    print("(enter 'q' at any time to quite)")
#    f_name= input("First name: ")
#    if f_name == 'q':
#        break
#    l_name= input("Last name: ")
#    if l_name == 'q':
#        break

#    formatted_name = get_formatted_name(f_name , l_name)
#    print("\nHello, " + formatted_name + "!")

    #Passing a list
#def greet_users(names):
#    """Print a simmple greeting to each user in the lsit"""
#    for name in names:
#        msg = "Hello, " + name.title() + "!"
#        print(msg)

#usernames = ['hannah', 'ty', 'margot']
#greet_users(usernames)

    #Modifying a List in a Function 
## Start with some designs that need to be printed
#unprinted_designs = ['iphone case','robot thing', 'dodecahedron']
#completed_models = []

##simulate printing each design, until none are left 
## Move each design to completed_models after printed 
#while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    # Simulate creating 3D print from design
#    print("Printing model: " + current_design)
#    completed_models.append(current_design)
#print("\nThe following models have been printed:")
#for completed_model in completed_models:
#    print(completed_model)

#def print_models(unprinted_designs, completed_models):

#    """
#    Simulated printing each design, until none are left.
#    Move each design to completed_models once printed
#    """

#    while unprinted_designs:
#        current_design = unprinted_designs.pop()

#        #simulate creating a 3D print from the design.
#        print("Printing model: "+ current_design)
#        completed_models.append(current_design)
    
#def show_completed_models(completed_models): 
#    """ Show all the models that were printed."""
#    print("\nThe following models have been printed:")
#    for completed_model in completed_models:
#            print(completed_model)
#unprinted_designs = ['iphone case', 'robot pendant', 'dodecaheadron']
#completed_models = []

#print_models(unprinted_designs, completed_models)
#show_completed_models(completed_models)


    #Preventing a function from Modifying alist
#def print_models(unprinted_designs, completed_models):

#    """
#    Simulated printing each design, until none are left.
#    Move each design to completed_models once printed
#    """

#    while unprinted_designs:
#        current_design = unprinted_designs.pop()

#        #simulate creating a 3D print from the design.
#        print("Printing model: "+ current_design)
#        completed_models.append(current_design)
    
#def show_completed_models(completed_models): 
#    """ Show all the models that were printed."""
#    print("\nThe following models have been printed:")
#    for completed_model in completed_models:
#            print(completed_model)
#unprinted_designs = ['iphone case', 'robot pendant', 'dodecaheadron']
#completed_models = []

#print_models(unprinted_designs[:], completed_models)
#show_completed_models(completed_models)
    # Passing an arbitrary number of arg
#def make_pizza(*toppings):
#    """Print the list of toppings that have been requested"""
#    print(*toppings)
#make_pizza('pepperoni')
#make_pizza('mushroom','green peppers', 'extra cheese')

#def make_pizza(*toppings):
#    """Summarize the pizza we are about to make"""
#    print("\nMaking a pizza with the following toppings:")
#    for topping in toppings:
#        print("-" + topping)
#make_pizza('pepperoni')
#make_pizza('mushroom','green peppers', 'extra cheese')

    #Mixing positional and arbitrary arguments
#def make_pizza(size, *toppings):
#    """Summarize the pizza we are about to make"""
#    print("\nMaking a " +str(size) +
#          "-inch pizza with the follwing toppings: ")
#    for topping in toppings:
#        print("-" + topping)
#make_pizza(16, 'pepperoni')
#make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')
    #Using Arbitrart Keyword Aruguments
#def build_profile(first, last, **user_info):
#    """Build a dictionary contraing everything we know about a user."""
#    profile = {}
#    profile['first_name']= first
#    profile['last_name'] = last
#    for key, value in user_info.items():
#        profile[key] = value
#    return profile
#user_profile = build_profile('albert', 'einstein', 
#                             location= 'princeton',
#                             field='physics')
#print(user_profile)

    #Importing an Entire Module
