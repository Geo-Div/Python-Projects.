Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0

Answer:
hours = (input("Enter Hours: 45 \n"))
rate = (input("Enter Rate: 10 \n"))

if "hours > 40":
   regular_pay = "40 * rate"
   overtime_pay = "(hours - 40) * rate * 1.5"
   pay = regular_pay + overtime_pay
else:
   pay = Hours * Rate

print("Pay:", 475.0)