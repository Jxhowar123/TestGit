    ##diction
#alien_0 = {'color' : 'green', 'points' : 5}
#print(alien_0['color'])
#print(alien_0 ['points'])
    
    ## add values
#alien_0['x_position'] = 0 
#alien_0['y_postion'] = 25
#print (alien_0)
#print(alien_0['x_position'])
#alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
#print ("Oringial x-postiton: " + str(alien_0['x_position']))
#if alien_0 ['speed'] == 'slow' :
#    x_increment = 1
#elif alien_0 ['speed'] == 'medium' :
#    x_increment = 2
#else: 
#    x_increment = 3

#alien_0['x_position'] = alien_0 ['x_position'] + x_increment
#print("New position : " + str(alien_0['x_position']))
#alien_0['speed'] = 'fast'
#print("New postion : " + str (alien_0['speed']))
    
    ## removing values
    # deleting removes the value perm #
#del alien_0['points']
#print(alien_0)
 
 ##looping through all key-value pairs
#favorite_languages ={
#    'jen' : 'python',
#    'sarah' : 'c',
#    'edward' : 'ruby',
#    'phil' : 'python',
#     }
#print("Saras favorite landguage is " + favorite_languages['sarah'].title () + "." )

#user_0 ={
#    'username' : 'efermi',
#    'first' : 'enrico', 
#    'last' : 'fermi' , 
#    }
#for key, value in user_0.items():
#    print("\nKey: " + key)
#    print ("Value: " + value)
#for name, language in favorite_languages.items():
#    print(name.title() + "'s favorite language is " + language.title() + ".")
    
    ##Loop keys
#for name in favorite_languages.keys():
#    print(name.title())
#if 'erin' not in favorite_languages:
#    print ("Erin, please take our poll!")
#for name in sorted(favorite_languages):
#    print(name.title() + " thank you for taking the poll.")
    
    ## list of dictionaries *NESTING
#alien_0 = {'color' : 'green', 'points' : 5}
#alien_1 = {'color' : 'yellow', 'points' : 10}
#alien_2 = {'color' : 'red', 'points' : 15}
#aliens = [alien_0, alien_1, alien_2]
#for alien in aliens :
    #print(alien)
#aliens =[]
#for alien_number in range(30):
#    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
#    aliens.append(new_alien)
#    for alien in aliens [:5]  :
#        print(alien)
#    print("...")
#    print("Total number of aliens: " +str(len(aliens)))
#for alien in aliens[0:3]:
#    if alien['color'] == 'green':
#        alien['color'] = 'yellow'
#        alien['speed'] = 'medium'
#        alien['points'] = 10
#for alien in aliens [0:5]:
#    print(alien)

    ## A list in a Dictionary 
#pizza ={
#    'crust': 'thick' ,
#    'toppings' : ['mushrooms', 'extra cheese'],
#    }
#print("You ordered a " + pizza['crust'] + "-crust pizza "+
#      "with the following toppings: ")
#for toppings in pizza['toppings'] : 
#    print ("\t" + toppings) 
#favorite_languages = {
#      'jen' : ['python', 'ruby'],
#      'sarah' : ['c'], 
#      'edward' : ['rudy', 'go'],
#      'phil' : ['python', 'haskell'],
#      }
#for name , languages in favorite_languages.items():
#      print("\n" + name.title() + "'s favorite lanuages are:")
#      for languae in languages:
#            print("\t" + languae.title())
    ## A Dictionary in a Dictionary
