'''
input()---> Input formatting

print()--> Output formatting(fstring)

a,b = 13,4.5

print(a,b) #by default sep =' '
print(a,b,sep='')
print(9,15,sep=':')
print('codegnan','python','vizag',sep='---->')
#end by default throws new line, we can modify it..
a,b = 13,4.5
print(a,b,end=' ')
print('codegnan is in vizag',end='\t')
print('PFS6 and DA6')
print()
print('------------>Welcome to the Game----->')


a,b = map(int,input("Enter the values").split(','))
addition = a+b
subtraction = a-b
multiplication = a*b
division = a/b


a = int(input('Enter your first number:'))
b = int(input('Enter your second number:'))
print(f'Addition of {a} and {b} is {a+b}')
print(f'Subtraction of {a} and {b} is {a-b}')
print(f'Multiplication of {a} and {b} is {a*b}')
print(f'division of {a} and {b} is {a/b}')

#Usage of %d,%f,%s
#print('Usage of %'%(args))
price = 45.3;grade='A';stock= 15
print('price is %d'%price)
print('price is %f'%price)
print('price is %.1f'%price)
print('Grade is %s'%grade)

#Area of circle when radius is 3.5cm, round off the area to 2 decimal value:

radius = 3.5
pi = 3.1416
area = pi*(radius**2)
print(f'area of circle is %.2f'%area)



#New style formatting --> fstring
name = 'codegnan';batch='PFS6'
print(f'{batch} is in {name}')
print(f'Lahar is in {name}')

#Control Block statements



#BMI Converter (Body Mass Index -->weight,height) (weight kgs,height, cms,metres

#bmi = weight / ((height)**2)


weight = int(input('Enter the weight in kgs:'))
height = float(input('Enter the height in centimetres:'))
name = input('Enter the name')
height = height / 100
bmi = weight / ((height)**2)
#print(bmi)
#now lets divide into categories

<18.5--> Underweight
>=18.5-24.9 --> Healthy
>=25 - 29.9--> Over weight
>30--> Obesity


if bmi<18.5:
    print(f'BMI of {name} is {bmi} and character is underweight --> Eat well')
elif bmi>=18.5 and bmi <=24.9:
    print(f'BMI of {name} is {bmi} and you are  Healthy --> Keep consistent')
elif bmi >=25 and bmi <=29.9:
    print(f'BMI of {name} is {bmi} and you are Overweight --> Start exercising')
elif bmi>30:
    print(f'{name} is in obese Category and bmi is {bmi}')

name = input("Enter your name: ")

weight = float(input("Enter your weight in kg: "))

unit = input("Enter height unit (feet/cm/inches/meters): ").lower()

height = float(input("Enter your height: "))
'''
name = input("Enter your name: ")

weight = float(input("Enter your weight in kg: "))

unit = input("Enter height unit (feet/cm/inches/meters): ").lower()

height = float(input("Enter your height: "))

if unit == "feet":
    height_ = height * 0.3048

elif unit == "cm":
    height_ = height / 100

elif unit == "inches":
    height_ = height * 0.0254

elif unit == "meters":
    height_ = height

else:
    print("Invalid height unit")
    exit()

bmi = weight / (height_ ** 2)

print("Name:", name)
print("BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Underweight")

elif bmi < 25:
    print("Normal weight")

elif bmi < 30:
    print("Overweight")

else:
    print("Obesity")
