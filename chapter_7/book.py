#message = input("Tell me something and ill repeat it back to you: " )
#print(message)

#name = input("Please enter your name: ")
#print("Hello, " + name + "!")

#prompt = "If you tell us who you are, we can personalize the message you see"
#prompt += "\nWhat is your first name? "
#name = input(prompt)
#print("\nHoello, " + name + "!")
    
    ##using numbers 
#age = input("How old are you? ")
#age = int(age)
#age >= 18

#height = input("How tall are you, in inches? ")
#height = int(height)
#if height > 36: 
#    print ("\nYou're tall enough to ride!")
#else: 
#    print("\n You'll be able to ride when you're a little older.")

    ##The Modulo Operator 
#4 % 3
#5 % 3
#6 % 3

#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)
#if number % 2 == 0:
#    print ("\nThe number " + str(number) + " is even")
#else: 
#    print("\nThe number "  + str(number) + " is odd.") 
    
    ## While Loops
#current_number =1
#while current_number <=5:
#    print(current_number)
#    current_number+=1
#prompt = "\nTell me something, and ill repeat it back "
#prompt += "\nEnter 'quit' to end the program "
#message = ""
#while message != 'quit':
#    message = input(prompt)
#    if message != 'quit':
#        print(message)

    ## Flags
#active = True 
#while active: 
#    message = input(prompt)
#    if message == 'quit':
#        active = False
#    else: 
#        print(message)
#prompt = "\nPlease enter the name of a city you visited"
#prompt += "\n(Enter 'quit' when you are finished.)  "
#while True:
#    city = input(prompt)
#    if city == 'quit':
#         break
#    else: 
#         print("I'd love to go to " + city.title() + "!")

    ## Continue loop
#current_number = 0 
#while current_number < 10:
#    current_number += 1
#    if current_number %2 == 0:
#       continue

#    print(current_number)

#x = 1
#while x <=5:
#    print(x)
#    x += 1
    ## Moving items from one list to another 
#unconfirmed_users = ['alice', 'brain', 'candace']
#confirmed_users = []

#while unconfirmed_users:
#    current_user = unconfirmed_users.pop()

#    print("Verifying user: " + current_user.title())
#    confirmed_users.append(current_user)
#print ("\nThe following users have been confirmed:")
#for confirmed_user in confirmed_users:
#    print(confirmed_user.title())

    ## Removing All instances of spec values
#pets = ['dogs', 'cat', 'dog','goldfish', 'cat', 'rabbit', 'cat']
#print(pets)

#while 'cat' in pets:
#    pets.remove('cat')
#print (pets)

    ## Filling a Dictionary with User info
responses ={}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person resond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(name + "would like to climb " + response + ".") 