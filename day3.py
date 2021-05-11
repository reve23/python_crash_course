#conditions

#It checks the condition and return the answer in True or False

#==
#!=
#<=
#>=
#<
#>

print(2==2)
print(2<2)
print(4>8)
print(10<=5+4)
print(2+5-9>17)
print(True)
print(False==True)
print(12==3*4)
print(12+67-6+5*6/8 != 6+45+789-9)

#If-Else Statement

#case => 1:

if 2 < 10:
    print("yes")
else:
    print("no")

#case =>2 :
if 10 + 2 != 12:
    print("yes")
elif 10 - 3 != 7:
    print("9")
else:
    print("None of them are correct")
    print("if was ignored")
    print("elif was ignored")

#case => 3:
if 10 + 2 != 12:
    print("yes")
elif 10-3 ==7:
    print("9")
    if 10 + 20 != 30:
        print("elif wasn't ignored")
    elif 1 <= 1:
        print("I've not used else")
    else:
        print("if was ignored")


#case => 4:
if 1>0:
    print(0)
    if 2<9:
        print(0)
        if 3 == 9//3:
            print(3)







