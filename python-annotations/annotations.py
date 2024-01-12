# imporing types using typing
from typing import List, Tuple, Dict, Set, Union, Optional
#importy for a function
from typing import Callable, Iterator, Generator, Iterable, Sequence, Sized, Reversible, Container, Collection, MutableSet, MutableSequence, MutableMapping, Any, TypeVar, Generic

"""
#annoting the variables
age1: List[int] = [10, 20, 30]
age2: Tuple[int, str, float] = (10, "20", 30,10)
age3: Dict[str, int] = {'a': 10, 'b': 20, 'c': 30}
age4: Set[int] = {10, 20, 30, 30, 30, 30, 40}
print(age1, age2, age3, age4)

#annoting tuples with fixed size
age: Tuple[int, str, float] = (10, "Roseline", 30,10)
print(age)

#variable anotation diclaration

age: int = 10
print(age)

# annotation in conditinal 
child: bool
if age < 18:
    child = True
else:
    child = False
print(child)

#praying around these types
my_var: Union[int, str] = 10
my_var: Optional[int] = 10
print(my_var)

var1: list[Union[int, str]] = [10, "Rose"]
print(var1)
print(len(var1))

var2: Optional[list[Union[int, str]]] = [10, "Rosel"]
print(var2)
print(len(var2))

#annotating CONDITIONALS
var3: Optional[list[Union[int, str]]] = [10, "Roseliine"] if age > 18 else [10, "Rose"]
if var3 is not None:
    print(len(var3))
else:
    print("var3 is None")

# if the value cannot be none for a loggic use assert
    assert var3 is not None, "var3 is None"
    print(len(var3))
"""
    #FUNCTIONS 
def anotation_function(var: int) -> int:
    return var + 10
print(anotation_function(10))
    
    #specifying multiple args in annotation
def multi_args(var1: int, var2: str) -> int:
        return var1 + len(var2)
print(multi_args(10, "Rose"))

    #specifying default values
def default_value(var1: int, var2: str = "Rose") -> int:
        return var1 + len(var2)
print(default_value(10))

    #specifying return type
def return_type(var1: int, var2: str = "Rose") -> int:
        return var1 + len(var2)
print(return_type(10))

    # specifying functions with no return type
def no_return(var1: int, var2: str = "Rose") -> None:
        print(var1 + len(var2))
    
    #annotating functions with multiple return types
def multi_return(var1: int, var2: str = "Rose") -> Union[int, str]:
        return var1 + len(var2)
print(multi_return(20))
    
    # working withuntyped arguments
def untyped_args(var1, var2):
        var2.append(var1)
        print(var1 + var2)

    # working with Callable functions
x: Callable[[int, float], float] = float
def register(callback: Callable[[str], int], var1: int, var2: float) -> int:
        return callback(var1, var2)
print(register(lambda var1, var2: var1 + var2, 10, 20))

    # generator function is a fuction that return iterator
def gen(var1: int) -> Iterator[int]:
        i = 0
        while i < var1:
            yield i
            i += 1
            print(i)
print("end")

# spliting function over multiple lines
def send_email(address: Union[str, list[str]],
               sender: str,
               cc: Optional[list[str]],
               bcc: Optional[list[str]],
               subject: str = '',
               body: Optional[list[str]] = None
               ) -> bool:
    if isinstance(address, str):
        address = [address]
        if cc is None:
            cc = []
            if bcc is None:
                bcc = []
                if body is None:
                    body = []
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False   
    
