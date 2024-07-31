name = input("Enter Student Name: ")
usn = input("Enter Student USN: ")

print("Enter marks of three subjects: ")
m1 = int(input())
m2 = int(input())
m3 = int(input())

total = m1+m2+m3
percentage = total/3

print("Student Details".center(30, "-"))
print(f"Student Name: {name.upper()}")
print(f"Student USN: {usn.upper()}")
print(f"Total marks: {total}")
print(f"Percentage: {percentage}")

if percentage > 90:
  print("Grade: A")
elif percentage > 80:
  print("Grade: B")
elif percentage > 70: 
  print("Grade: C")
elif percentage > 60:
  print("Grade: D")
elif percentage > 35: 
  print("Grade E")
elif percentage < 36: 
  print("Fail")
