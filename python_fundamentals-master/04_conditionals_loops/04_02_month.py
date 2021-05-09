'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
user_input = int(input("Enter a number between 1 and 12 and I will return a month: "))
month_list = ["January", "February", "March", "April", "May", "June", "Juy", "August", "September", "October", "November", "December"]
if user_input == 1:
    print(month_list[0])
elif user_input == 2:
    print(month_list[1])
elif user_input == 3:
    print(month_list[2])
elif user_input == 4:
    print(month_list[3])
elif user_input == 5:
    print(month_list[4])
elif user_input == 6:
    print(month_list[5])
elif user_input == 7:
    print(month_list[6])
elif user_input == 8:
    print(month_list[7])
elif user_input == 9:
    print(month_list[8])
elif user_input == 10:
    print(month_list9)
elif user_input == 11:
    print(month_list[10])
elif user_input == 12:
    print(month_list[11])
else:
    print("Your number is out of range")