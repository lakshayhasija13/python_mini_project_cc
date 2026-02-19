# TASK 1
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# TASK 2
prices = [2, 6, 1, 3, 2, 7, 2]

# TASK 3
num_two_dollar_prices = prices.count(2)

# TASK 4
num_pizzas = len(toppings)

# TASK 5
print(f'We sell {num_pizzas} different kinds of pizza!')

# TASK 6
pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]

# TASK 7
pizza_and_prices.sort()
print(pizza_and_prices)

# TASK 8
cheapest_pizza = pizza_and_prices[0]

# TASK 9
priciest_pizza = pizza_and_prices[-1]

# TASK 10
pizza_and_prices.pop()

# TASK 11
pizza_and_prices.append([2.5, "peppers"])

# TASK 12
pizza_and_prices.sort()
three_cheapest = pizza_and_prices[:3]

# TASK 13
print(three_cheapest)
