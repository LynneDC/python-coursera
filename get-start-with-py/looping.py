# using for loop
import time
stat_time = time.time()

#time module to check time stamp
x = "Roseline"
for idx, i in  enumerate(x):
    #print each later of a string
    if i == "R":
        print(idx, i)
        break
        
        print("Initial")
  

y = ["lavish", "Blessed"]
for idx, item in enumerate(y):
    print(idx, item)

# while loop
# declare counter
x = 0
while x < len(y):
    print(y[x])
    x += 1

#nested loops


# outer loop
for i in range(100):
    print(0, end= " ")
     # inner loop
    for j in range(100):
         print(0, end= " ")
    print()  
print(round((time.time() - stat_time), 2))  
