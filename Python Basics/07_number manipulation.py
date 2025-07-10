# Rounding function in Python is used to round a number to a specified number of decimal places.
bmi = 84.2 / 1.8**2 
print(bmi)
print(int(bmi))
print(round(bmi))
# Rounding to 2 decimal places :
print(round(bmi, 2))  

# Assingment operators :
score = 1
score += 5 # This is equivalent to score = score + 5
score -= 2 # This is equivalent to score = score - 2
score *= 3 # This is equivalent to score = score * 3
score /= 2 # This is equivalent to score = score / 2
score //= 2 # This is equivalent to score = score // 2
print(score)

scores = 0
height = 1.8
is_winning = True
# Multiple assignment in Python :
# Use of multiple assignment in Python allows you to assign multiple variables in a single line is know as f-string .
print(f"Your score is {scores}, your height is {height}, and you are winning: {is_winning}")
# f-string is a way to format strings in Python.
# It allows you to embed expressions inside string literals, using curly braces {}.
