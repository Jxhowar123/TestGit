while True:
    my_name = input("What is your name? \n")
    if my_name.lower() == 'quit':
        break
    elif my_name.lower()[0] in 'abcdefg' :
        print ('Please procced to table One')
    elif my_name.lower()[0] in 'hijklmnop':
        print ('Please procced to table Two')
    elif my_name.lower()[0] in 'qrustvwxyz':
        print('Plesase procced to table Three')
    
    