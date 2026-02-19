# TASK 1
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# TASK 2
subjects = ["physics", "calculus", "poetry", "history"]

# TASK 3
grades = [98, 97, 85, 88]

# TASK 4
gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]

# TASK 5
gradebook.append(["computer science", 100])

# TASK 6
gradebook.append(["visual arts", 93])

# TASK 7
gradebook[-1][1] += 5

# TASK 8
gradebook[2].remove(85)

# TASK 9
gradebook[2].append("Pass")

# TASK 10
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
