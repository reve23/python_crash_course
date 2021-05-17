#Question:

#Take User age as input and check if they are more than 18 or not. If they are more
#than 18 years old allow them to drive else stop them.
#Your answer should look like :
#You are 18 years old so you can drive,Have a good Journey
#or, You can't drive

#Answer:

age = int(input("Enter your age: "))

if age == 18:
    print("You are 18 years old so you can drive,Have a good Journey")
elif age > 18:
    print("You are more than 18 years old so you can drive,Have a good Journey")
else:
    print("You can't drive")
