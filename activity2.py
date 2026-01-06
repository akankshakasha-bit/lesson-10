print("select your menu: ")
print("1. indian")
print("2. chinese")
choice=int(input("enter your choice: "))
if (choice==1):
    print("what type of indian? ")
    print("1.idli\n")
    print("2.dosa\n")

    choice2=int(input("enter your choice2: "))
    if choice2==1: #inner if statement
        print("you have selected idli")
    else:
        print("you have selected dosa")

elif(choice==2):
    print("what type of chinese? ")
    print("1.dumpling")
    print("2.frog legs")
    choice3=int(input("enter your choice3: "))
    if choice3==1: 
        print("you have selected dumpling")
    else:
        print("you have selected frog legs")
else:
    print("wrong choice")