medical_cause=input("did you have medical cause Y or N: ")
atten= int(input("enter attendence of the students: "))
if medical_cause=="Y":
    print("you are allowed")
else:
    if atten >=75:
        print("allowed")
    else:
        print("not allowed")
        