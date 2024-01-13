# print to the console
print("Hello World")

# spacing syntax
x = 10 + 20
print(x)

#specing with backslash
y = 2 +       1 \
 + 3
print(y)

# write an if statement if name has the value you are checking
# this checkes if the variable is equal to the value
# and it returns an output if it is true
name = 'Roseline'
if name == 'Roseline':
    print("Hello Roseline") 
    print("You are a great person")

 
 # variable declaration
    x = 10
    print(x)
# change the value of a variable
    x = 'ROSELINE'
    print(x)
    print(type(x))
#naming variables 
    # 1 camelcases
myName = 'Roseline'
    # snackcase
my_name = 'Roseline' 
    # kebabcase
my_name = 'Roseline'
    # multiple value assigning 
a = 1, 2, 3, 4, 5
print(a)
a, b, c, d, e = 1, 2, 3, 4, 5
print(e)

#to delete a variable 
del b

# COMPLEX NUMBER
m = 10 + 20j
print(m)

my_var = "[2, 4,]"
print(type(my_var))

# strings
my_var = "Hello World"\
        "I am Roseline"\
        "I am 25 years old"
print(my_var)
print(type(my_var))
print(len(my_var))
print(my_var[0])

#concatenate strings
var = "NAME IS " + " " + "ROSELINE"
print(var)
print(type(var))
print(len(var))
# access characters
print(var[0])

#creating a fuction 
def my_identity(name, surname, age):
    return name + " " + surname + " " + str(age)

# built in functions 
# input function
print("My name is input function")
location = input()
print("I am from " + location)

# len() function
my_vari = "ROSELINE DANGAZELA"
len(my_vari)

#str() function
print(str(123))

# int() function
print(int("345"))

# float() function
print(float("345.5"))

#how to use input and out put
email = input('please ender youremail')
name = input('please enter your name')
print(email + " " + name)
 #to check type of values
print(type(email))
print(type(name))
