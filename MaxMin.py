#This program determines the MAX and MIN numbers between a set of numbers entered in by User.
#Enter "Done" to end inputing set of Numbers.

largest = None
smallest = None

while True:
    try:
        num = input("Enter a number: ")
        if num == "done": break

        num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
            smallest = num
    except ValueError:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)