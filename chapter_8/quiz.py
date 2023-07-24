def do_something(a_list):
    my_string=""
    for element in a_list:
        my_string += element[0]
    return my_string
aladdin_characters = ["Jasmine", "Aladdin","Flaja", "Abu"]
print(do_something(aladdin_characters))