def check_pass_fail():
    sub1 = float(input("Enter marks for first subject: "))
    sub2 = float(input("Enter marks for second subject: "))
    sub3 = float(input("Enter marks for third subject: "))

    # Calculate percentage for each subject (assuming max marks is 100)
    per1 = (sub1/100) * 100
    per2 = (sub2/100) * 100
    per3 = (sub3/100) * 100

    # Calculate total percentage
    total_per = (sub1 + sub2 + sub3)/300 * 100

    # Check pass/fail conditions
    if per1 >= 33 and per2 >= 33 and per3 >= 33 and total_per >= 40:
        print("Congratulations! You have passed")
        print(f"Your total percentage is: {total_per}%")
    else:
        print("Sorry, you have failed")
        print(f"Your total percentage is: {total_per}%")

check_pass_fail()
