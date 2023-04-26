hours = float(input("Please enter the number of hours that you worked: "))
rate = float(input("Please enter your hourly rate: "))
my_sum = hours * rate
print(
    f"You earned ${my_sum:.2f} for {hours} hours of work at ${rate:.2f}/hour.")
