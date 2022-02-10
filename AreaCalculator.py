"""
The program should do the following:

Prompt the user to select a shape.
Calculate the area of that shape.
Print the area of that shape to the user.
"""

print("Calculator is warmed up!")
option = input("Enter c for Circle or t for Triangle. \n")
if option.lower() == "c":
  radius = float(input("What is the radius of the circle? \n"))
  area = 3.14159 * radius ** 2
  print("The area is {}".format(round(area, 2)))
elif option.lower() == "t":
  base = float(input("What is the base of the triangle? \n"))
  height = float(input("What is the height of the triangle? \n"))
  area = base / 2 * height
  print("The area is {}".format(round(area, 2)))
else:
  "Invalid Input"
print("Program Finished.")