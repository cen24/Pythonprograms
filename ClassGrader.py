#Class Grader Tool. Returns letter grade for scores.

try:
    score = input("Enter a number: ")
    x = float(score)
    if (x >= 100):
        print("Please enter number between 0 and 100")
        exit()

    elif (x >= 90):
        print("A")
    elif (x >= 80):
        print("B")
    elif (x >= 70):
        print("C")
    elif (x >= 60):
        print("D")
    else:
        print("F")
except:
    print("Please enter number")
    exit()