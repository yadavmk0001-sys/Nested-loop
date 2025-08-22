marks = int(input("Enter the marks "))

if marks>=40:
    print("You have passed the exam")
    if marks>=90:
        print("Grade A")
    if marks>=75:
        print("Grade B")
    if marks>=60:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("You are failed")