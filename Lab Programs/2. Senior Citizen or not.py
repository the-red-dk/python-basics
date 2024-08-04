name = input("Enter your name: ")

current_age = int(input("Enter current year: "))
year_of_birth = int(input("Enter your year of birth: "))

real_age = current_age - year_of_birth

if real_age > 60:
  print(f"You are a senior citizen {name}!")
else:
  print(f"You are not a senior citizen {name}")
  
