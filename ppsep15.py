'''
Input Formatting: Accept input from user
Integer,Float,String,coma seperated values,space seperated values

#input from user --> input()

name = input('Enter the name:')
print(name)
print(type(name))
print(len(name))


#split()
#by default it will be space seperated
names = input('Enter the names:').split()
print(names)
print(type(names))
print(len(names))

#split(',') --> coma seperates values

names = input('Enter the names:').split(',')
print(names)
print(type(names))
print(len(names))

#Accept single integer,multiple integer values,group of integers

num1 = int(input("Enter the number:"))
print(num1)
print(type(num1))

#Every  built-in data-type is a built-in function.--> Functions = Objects

#Usage of map() --> group of integers

numbers = list(map(int,input('Enter the values=').split(',')))
print(numbers)

#for float
numbers = (map(float,input('Enter the values=').split(',')))
print(numbers)


#accept multiple values--> Integers,float,names(str)...

temperature,pressure = map(float,input('Enter the values:').split(','))
print('Temperature is',temperature)
print('Pressure is:',pressure)
'''
text = input('Enter 















