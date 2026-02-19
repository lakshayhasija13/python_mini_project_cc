# TASK 1
# weight in pounds
weight = 8.4

# TASK 2
# GROUND SHIPPING:
if weight <= 2:
  cost = 1.5 + 20
elif weight > 2 and weight <= 6:
  cost = 3.0 + 20
elif weight > 6 and weight <= 10:
  cost = 4.0 + 20
elif weight > 10:
  cost = 4.75 + 20.0

# TASK 3
# PREMIUM GROUND SHIPPING
cost = 125

# TASK 4
#DRONE SHIPPING
if weight <= 2:
  cost = 4.5
elif weight > 2 and weight <= 6:
  cost = 9.0
elif weight > 6 and weight <= 10:
  cost = 12.00
elif weight > 10:
  cost = 14.25

