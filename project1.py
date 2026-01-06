age=int(input("enter the students age: "))
if age>=10:
    if age<=20:
        print("student is alloed to enroll in the class")
    else:
        print("student is NOT allowed to enroll in class. age is more than 20")
else:
    print("student is not allowed to enroll in class. age is less than 10")
