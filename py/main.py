# Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your height in kg: ")
# Don't change the code above
# Write my code below
bmi = int(weight) / float(height) ** 1.8
bmi_as_int = int(bmi)
print(bmi_as_int)