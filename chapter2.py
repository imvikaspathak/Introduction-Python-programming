# write your if statement here
points = 174  # use this input to make your submission

# write your if statement here
# points = int (input("enter any number :"))
# if points <= 50:
#     result = "Congratulations! You won a wooden rabbit"
# elif points <= 150:
#     result ="Oh dear, no prize this time."
# elif points <= 180:
#     result= "Congratulations! You won a wafer-thin mint"
# elif points <= 200:
#     result ="Congratulations! You won a penguin"

# print(result)


# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''


# state = "CA" #Either CA, MN, or NY
# purchase_amount = 100 #amount of purchase

# if state == CA: #provide conditional for checking state is CA
#     tax_amount = .075
#     total_cost = purchase_amount*(1+tax_amount)
#     result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

# elif #provide conditional for checking state is MN
#     tax_amount = .095
#     total_cost = purchase_amount*(1+tax_amount)
#     result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

# elif #provide conditional for checking state is NY
#     tax_amount = .089
#     total_cost = purchase_amount*(1+tax_amount)
#     result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

# print(result)
# is_raining = 5
# is_sunny =8
# if is_raining and is_sunny:
#     print("Is there a rainbow?")


# if (not unsubscribed) and (location == "USA" or location == "CAN"):
#     print("send email")

altitude = 10000
speed = 250
propulsion = "Propeller"
# print(altitude < 10000 and speed > 1000)

print(propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000

print(not (speed > 400 and propulsion == "Propeller"))

(altitude > 500 and speed > 100) or not propulsion == "Propeller"