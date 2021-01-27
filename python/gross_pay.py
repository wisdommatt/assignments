# Python assignment.
# 
# Instruction: Calculate the gross pay of an employee given
# the hours worked and the rate of pay.
# 
# Lecturer: Mr. Chizzy
# Course: CMS 112

# Calculation:
#       gross pay = hours worked * rate of pay
def gross_profit_calculator():
    hours_worked = input("What is the hours worked: ")
    while hours_worked.isdigit() == False:
        hours_worked = input("Hours worked should be a number, please retry: ")

    pay_rate = input("What is the rate of pay: ")
    while pay_rate.isdigit() == False:
        pay_rate = input("Rate of pay should be a number, please retry: ")

    gross_pay = int(hours_worked) * int(pay_rate)
    print ("The employee's gross pay is: " + str(gross_pay))

# running the gross profit calculation function.
gross_profit_calculator()