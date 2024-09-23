name = input("Enter your name: ")
Age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
bmi = weight/height**2
print(name+" you are "+str(Age)+" your BMI is ", str("%.2f" % bmi))