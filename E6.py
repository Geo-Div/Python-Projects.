Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
create a function called computepay which takes two parameters (hours and rate).
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Answer:
hrs = float(input("Enter Hours: "))
rt = float(input("Enter Rate: "))
pay = computepay(hrs, rt)
print("Pay;" pay)

def computepay (hours, rate):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5
        pay = regular_pay + overtime_pay
    else:
    pay = hours * rate
return pay