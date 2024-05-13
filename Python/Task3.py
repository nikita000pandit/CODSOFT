import random
import string
print("==Welcome to Password generator application==")
alphabet_letters=string.ascii_letters
digits=string.digits
special_characters=string.punctuation
str=alphabet_letters+special_characters+digits
choice=1
while(choice):
    user_choice=int(input("Specify the length of the password: "))
    password=""
    if(user_choice<0):
        print("Please enter number greater than 0")
    else:
        for i in range(user_choice):
            password=password+random.choice(str)
        print(password)
        print("==Password generated successfully==")
    print("1. To continue generating password")
    print("2. Quit")
    choice=int(input('Choose either "1" or "0": '))
print("==Thanks for using Password generating application==")


































# user=int(input("Please Specify the desired length of the password:"))
# str="asdfghjklpoiuytrewqzxcvbnmAQSWZXCDERFVBGTYHNMJUIKOLP1234567890+-!@#$%^&*()"
# ran=""
# import random
# for i in range(0,user):
#     ran=ran+random.choice(str)
# print(ran)
#List example
# import random
# list=["nikita",'f',12,45.6,True]
# for i in list:
#     print(i)
#     ran=random.choice(list)
#     print(ran)
#String Example
#random.choice() is applicable for tuple,string, and list
#random.choice() selects one element from tuple,list and one character from a String
# import random
# str="nikita"
# for i in str:
#     # print(i)
#     ran=random.choice(str)
#     print(ran)
#randrange()-->Returns a random number within the range
#sample()-->Returns a particular length list of items chosen from the sequence