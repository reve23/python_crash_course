#Question:
#Make a hospital form where you have to fill few perameters. The perameters are
#name, age, address, phone_number, email..
#This should identify your information as :
# Your name is {name} and you are {age} years old. Your address is {address}
#We'll call you on {phone_number} and we've sent an email to {email}..


#Answer:
name = input("Enter your name: ") 
age = int(input("Enter your age: "))
address = input("Enter your Home address: ")
phone_number = int(input("Enter Phone Number: "))
email = input("Enter your E-mail address: ")

print("Your name is " , name , "and you are " , age , " years old. Your address is ", address , "We'll call you on " , phone_number , " and we've sent an email to " ,
      email)

