#number = 3 
#while number <5 :
#    print(number)

#age = input("What is your age? ")
#while age > 10:
#    age -= 1 
#    print(age,end= " ")

#while False:
#   print("My", end=" ")
#    print("Name", end=" ")
#    print("is", end=" ")
#    continue
#    print("chika-chicka", end=" ")
#    break
#    print("Slim Shady", end=" ")
#age = 1
#while age < 10:
#    if age % 2 ==1:
#        if age == 3:
#            print("ding", end=" ")
#        elif age ==4:
#            print("dong", end=" ")
#        elif age ==5: 
#            print("the", end=" ")
#        print("whicn", end=" ")
 #   age += 1
#print("is dead", end=" ")

#num =1 
#new_num = 0
#while num < 10 :
#    for i in range(3):
#        new_num += 1
#    num += 2
#print(new_num)

#x = 10 
#my_list = ["Yaba", "Daba", "doo"]
#while x < 13:
#    for remark in my_list:
#        print(remark, end=" ")
#        x += 1

i = 6 
while i <= 10:
    for j in range(3):
        i*=j+2
        print(j, end=" ")
        break