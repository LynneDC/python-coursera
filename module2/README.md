## FUNCTIONS
Are created to be reused
they are decaled using def key word
<pre>
def calculate(bill, tax_rate):
    return(bill * tax_rate) / 100.00

    # call the function
print(calculate(122, 10))
</pre>
### SCOPE
there are local scope, enclosing scope, global scope and builtin scope <br>
Variables in builtin and global scope are accessible from anaywhere in the code <br>
scope protect the variable so it wont be changed <br>
the inner most function has access to all outer variables <br>
builtin scope can be accessed anywhere<br>

## DATA STRUCTURES
Is used to organize and arrange data to perform operations on them 
# builtin data structures 
<ol>
    <li> SET</li>
    <li> LIST</li>
    <li>TUPLES </li>
    <li>DICTIONARIY</li>
</ol>
they are all called non-primitive meaning they are classed as objects.

# user defined data structures
<ol>
    <li> STACKS
    <LI>QUEUES
    <LI>TREE
    <LI>LINKED LISTS
    <LI>GRAPH
    <LI>HASHMAP
    </LI>
</ol>
they can be designed to solve a particular problem


# multability and immutability
mutability ----> refers to the data inside the structure that can be  modified(changed, updated, delete) example list<br>
immutable -----> data that cannot be changed or modified example tuple <br>

## LISTS
Sequence of one or more similar or different data types <br>
they are a dynamicarray that can hold any data type <br>
Example
<pre> #declare a list
    x = [1, 2, 3, 10, 5, 'Rose', 12,4, 'line', 'q'] 
    #print out list iterm at number 6
    print(x[5])   
</pre>
list are bassed on indexes<br>
lists can be nested

## TUPLES
DECLARATION
<pre>
my_tuple = ('ROSE', True, 1, 12.5)
# access tuple data
print(my_tuple[1])
# detemine type of tuple 
print(type(my_tuple))
</pre>
the  main difference between tuple and li
st is tuple are immutable and list are

## SET
set they store unique values only
<pre> # declaration 
set1 = {1, 3, 4, 5}
</pre>
sets are unordered and cannot be indexed.

## DICTIONARY
used to retrieve values, they access values based on keys <br>
a key is assigned to a specific value and this is called a key value pair<br>
values can be changed or updated <br>
you can access keys by their name

## args and kwargs









