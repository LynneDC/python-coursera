# declare array variable 
num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]
num_list.sort()
count = 0
# create for loop that return the value in order
for idx, i  in enumerate(num_list):
    print(idx, i)
    count =+ 1
    # print numbers greater than 45
    if i > 45: 
        print("over 45")
        break
    elif i == 36:
        print(f"Number found at position {idx}")
        
    else:    
        print("Under 45")
print(count)




    