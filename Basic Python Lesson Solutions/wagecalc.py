hours = float(input("How many hours did you put in at work this week?"))
rate = float(input("How much is your hourly pay rate?"))
wage = rate * hours
round(wage, 2)
print("You will earn $", round(wage, 2), ".")