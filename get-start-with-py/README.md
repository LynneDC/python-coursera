Welcome to intoduction to Py

# Syntax and spacing 
print is used to print to the console
syntax eeror happen when you have the wrong syntax (broken programming gramma)

# variable declaration
x = 2 + 3;
can be printend through using print(x);
the output of this will be 3

# spacing 
to effectively space your code use \
example:
x = 2 +     1 \   
3;
this will return the total of 2 and 1 and 3

# commenting 
single line comments are done using 1 #
multi line comments are done using """ """
comments should explain in brief the code
 
 # variable types
 allow you to work and manipilate data 
 their values can be changed and manipulated
  # declaration
   x = 10;
# to change the value of a variable 
    X = 20;

# variable naming
give variables explanatory names
variable give referance to a value
you cane name using camel cases 
be consistant in your naming 
varriable reasignement does not overwrite its content

# DATA TIYPES
A data type is an atribute of a variable that defines the type of data that can be stored in the variable and tell the intepreter how to interpret its value
# NUMERIC 
has (integers, float, complex number)
### INTEGER 
any non fractional number 
can be  + or -
example 10 or -10
### FLOATS
 has decimal numbers 
 explamples 
 10,45 
 10,000000009
 
 ### COMPLEX 
 complex numbers made up of real and imaginary number 
 example 
 10 + 10j

# SEQUENCES
has (string, list, tuples)
### STRING
is a sequence of characters enclosed in quotes
represented with str
example
### to declare 
 my_string = "hello world"
  ### for multi lines 
  my_string = "hello world \
  this is a multi line string\
  this is the end of the string"
 
  ## TO REASINE 
  name = "john"
  name = "jane"

  ### USES INDEXIG 
  to check length use len
### LIST
is a sequence of values
are array 
can be accessed by indexes
represpented by list() 
values are in []
### TUPLE
is a sequence of values
they are not modifiable or changed
can be accessed by indexes
represented by tuple()
values are in ()
# DICTIONARY
key value objexts 
stored in {}
store any data type
represented by dict()
to print value access the key
can be done in indexing
# SET
unorderd and non indexed set of values
represented by set()
# BOOLEAN
has only 2 values (true, false)
represented by bool()

### DATA TYPES AND FUNCTIONS CHEATSHEET

<table>
<tr>
  <td>DATA TYPE</td>  
  <td>MEANING</td>
  <td>EXAMPLE</td>
</tr>
<tr>
   <td>STRING</td>
   <td>text</td>
   <td>"hello world 1am 24"</td>
  </tr>
  <tr>
   <td>INTEGER</td> 
   <td>whole numbers</td>
   <td>12, -5, 201, 1</td>
  </tr> 
  <tr>
   <td>FLOAT</td>
   <td>numbers with decimal points</td>
   <td>1.2, 4.67, -2,45</td>
  </tr>
</table>

## FLOW CONTROL
COMPARISON OPERATORS
<table>
<tr>
  <td>OPERATOR</td>
  <td>MEANING</td>
  <td>EXAMPLE</td>
</tr>
<tr>
  <td> == </td>
  <td>equal to</td>
  <td>x == y</td>
</tr>
<tr>
  <td>!= </td>
  <td>not equal to</td>
  <td>x!= y</td>
</tr>
<tr>
  <td> > </td>
  <td>greater than</td>
  <td>x > y</td>
</tr>
<tr>
  <td> < </td>
  <td>less than</td>
  <td>x < y</td>
</tr>
<tr>
  <td> >= </td>
  <td>greater than or equal to</td>
  <td>x >= y</td>
</tr>
<tr>
  <td> <= </td>
  <td>less than oe equal to</td>
  <td>x <= y</td>
</tr>
</table>


### COMMENTING 
YOU CAN COMMENT YOUR CODE IN 2 WAYS
1. SINGLE LINE COMMENTS
here you place # before the line you want to comment
you can do this for multi line but each line starting with #

2. MULTI LINE COMMENTS
You use """ """ to comment your code
this can beused to coment 2+ lines of code

### CREATING FUNCTIONS
  you use keyword: def to creat a function 
  the body of a function contains the code to run when it is called
  the function name is the name of the function
  the parameters are the variables that are passed to the function
  the function can have a return value
  the return value is the value that is returned by the function
  EXAPLE:
    def my_function(x, y):
        return x + m;
## type casting
    you can convert a value to a different data type using it
    example:
    x = str(x) 

### CONDITIONAL STATEMENTS
Operator tells python how to operate a statement
### OPERATORS
<table>
  <tr>
    <td>OPERATOR</td>
    <td>MEANING</td>
    <td>EXAMPLE</td>
  </tr>
  <tr>
    <td>+ </td>
    <td>addition</td>
    <td>x + y</td>
  </tr>
  <tr>
   <td> - </d>
   <td>subtraction</td>
   <td>x - y</td>
   </tr>
  <tr>
    <td> * </d>
    <td>multiplication</td>
    <td>x * y</td>
  </tr>
  <tr>
    <td> / </td>
    <td>division</td>
    <td>x / y</td>
   </tr>
   <tr>
    <td> % </td>
    <td>modulus</td>
    <td>x % y</td>
  </tr>
<table>

### LOGICAL OPERATORS
<table>
  <tr>
    <td> Operator </td>
    <td> Meaning </td>
    <td> Example </td>
    </tr>
    <tr>
    <td> and </td>
    <td> checks for both condition to be true  </td>
    <td> x > 2 && y < 5 </td>
  </tr>
  <tr>
    <td> OR </td>
    <td> check for one condition to be true </td>
    <td> x > 2 OR y < 5 </td>
   </tr>
  <tr>
  <td> NOT </td>
  <td> return false if value is true </td>
  <td> NOT(x > 2) </td>
  </tr>
</table>

### control flow
1. conditional
  if statement:
    if x > 2:
    print("x is greater than 2")
    elif x < 2:
    print("x is less than 2")
    else:
     print("x is not greater than 2")

2. looping
    while loop
    while x < 5:
     for x in range(5):
     print(x)
     break;

### SWITCHES
IT is a match statement
When you have large number of conditions
You can combine different srarements using or
default is what to be returnedb if no value match
case is equivalent to if
default is equal to else

### looping 
looping is used to iterate through the variable and access each character in the variable

### Nested loops
the outer loop runs first into the inner,and the inner loop will run until its complited then the outer loop will run




# #### BUILT IN FUNCTIONS

1. type(value)<br>
  tells you the data type of a value 

2. len(value)<br>
  tells you the length of a value

3. print(value)<br>
  prints the value to the console

4. input(value) <br>
  takes input from the user
  And print it out to the console
  it captures the input value
  then the value can be assigned or used
5. int()<br>
  return an integer of the value it has received
6. str()<br>
  convert a value it has received to strings
7. float() <br>
  convert input value to float
8. range(vaue) <br>
  is used to specify the number of items

9. enumarate() <br>
  used in the for loop when you dont have access to the index

