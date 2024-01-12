# VARIABLES
mypy infer type of variables from its value
# how to declare type of a variable
age: int = 1

to annote a variable you dont need to initilize it

 age: int

there will be no value at runtime, until assigned
# annotation in conditional branches
example

child: bool
if age < 18:
    child = True
else:
    child = False
## BUILT-IN TYPES
<!-- collecteion with item in brackets-->
age: list[int] = [1, 2, 3]
child: set[str] = {"child1", "child2"}

<!-- for mapping you need the type of both keys and values -->
age_dict: dict[int, str] = {1: "one", 2: "two"}

<!-- for tuples you need the types of all elements -->
age_tuple: tuple[int, str] = (1, "one")
   <!-- tuples can be of fixed position -->
   age_tuple: tuple[int, str, bool] = (1, "one", True)
 <!--tuples can be of various sizes -->
 age_tuple: tuple[int, ...] = (1, 2, 3)
 <!-- tuples can be of different types -->
 age_tuple: tuple[int, str, bool] = (1, "one", True)

<!-- the name of the collection can be capitalized and type is imported from typing module -->
from typing import List, Set, Dict, Tuple
age: List[int] = [1, 2, 3]
child: Set[str] = {"child1", "child2"}
age_dict: Dict[int, str] = {1: "one", 2: "two"}
age_tuple: Tuple[int, str] = (1, "one")

<!--- | can be used when a variable could be one of the types -->
age: list[int | str] = [1, 2, 3, "Roselien", "Name"]
<!-- union and optinal can be impoted and used -->
from typing import Union, Optional
age: Union[int, str] = 1
age: Optional[int] = None
age: List[Union[int, str]] = [1, 2, 3, "Roselien", "Name"]
age: Optional[List[Union[int, str]]] = None
# Optional[x] is the same as x | none or Union[x, none]
Optional is used when you dont know if a variable will be assigned a value or not
it is for a value that could be none

# Union[x, none] is the same as Optional[x]
Union is used when you know that a variable will be assigned a value
it is for a value that could be one of the types

### Example
 age: Optional[str] = "ROSELINE" if age < 18 else None
 if age is not None:
 ### mypy understand that age wont be none because it has a value
 print(age)
 print(len(age))
 print(age.lower())

 ### assert is used to assert a logic that you know its not none for a logic that is not known by mypy
 assert age is not None
 print(age.lower())

 ## FUNCTIONS
 you import the function you are to use
 from typing import Callable, Iterator, Union, Optional

 # HOW TO ANNOTE A FUNCTION DEFINATION
 def function_name(param1: int, param2: str) -> int:
 return param1 + int(param2)
 
 EXAMPLE
 def stringfy(num: int) -> str:
 return str(num)

 # How to specify multiple arguments
 def intergers(num: int, num2: int) -> str:
 return str(num + num2)

 # if a function does not return a value, use non as the return type
 def print_name(name: str) -> None:
 print(name)

 def show(value: str, excitement: int = 10) -> None:
 print(value + "!" * excitement) 

# arguments without a type are dynamical types
example
def no-type(x):
x.anything() + 1 + "string"

# annoting a collable function
X: Callable[[int, float], float] = f
def register(callback: Callable[[str], int]) -> None:...

# generator is a function that return an iterator
def generator(x; int) -> Iterator[int]:
i = 0;
while i < x:
yield i
i =+ 1

# splitting fucntionanotation over multiple lines
 def send_email(address: Union[str, List[str]]:
 sender: str,
 cc: Optional[List[str]],
 bcc: Optional[List[str]],
 subject: str = "",
 body: Optional[list[str]]
 ) -> bool:

  # CLASSES
  