# TASK 1
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# TASK 2
def f_to_c(f_temp):
  c_temp = (5/9) * f_temp - 32
  return c_temp

# TASK 3
f100_in_celcius = f_to_c(100)

# TASK 4
def c_to_f(c_temp):
  f_temp = (9 / 5) * c_temp + 32
  return f_temp

# TASK 5
c0_in_fahrenheit = c_to_f(0)

# TASK 6
def get_force(mass, acceleration):
  return mass * acceleration
  
# TASK 7
train_force = get_force(train_mass, train_acceleration)
print("Train Force:")


# TASK 8
print(f'The GE train supplies {train_force} Newtons of force.')

# TASK 9
def get_energy(mass, c = 3*(10**8)):
  return mass * c 

# TASK 10
bomb_energy = get_energy(bomb_mass)
print("Bomb Energy:")
print(f'A 1kg bomb supplies {bomb_energy} Joules.')

# TASK 11
def get_work(mass, acceleration, distance):
  work = get_force(mass, acceleration) * distance
  return work

# TASK 12
train_work = get_work(train_mass, train_acceleration, train_distance)

# TASK 13
print("Train Work:")
print(f'The GE train does {train_work} Joules of work over {train_distance} meters.')
