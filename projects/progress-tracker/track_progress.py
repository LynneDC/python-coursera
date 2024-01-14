"""
this is my main file for the progress tracker project
this project is about building using python
a web application/ app that will allow user to enter inpute data
 and display the data in a table
 and also the users will be able to track their progess on a particula task
"""
import datetime
import math
def input_values():
    print("Lets get organized whooop!")
    task_name = input("enter the name of the task")
    if task_name == "":
        task_name = input("enter the name of the task") 
    else:
        print(task_name)
        sub_task = input("enter the sub task")
        if sub_task == "":
            task_start_date = input("enter the date to start")
            # add condition to calcualte date based on number of days 
            task_start_date = datetime.datetime.strptime(task_start_date, "%Y-%m-%d")
            print(task_start_date)
            task_finish_date = input("enter the date to finish")
            task_finish_date = datetime.datetime.strptime(task_finish_date, "%Y-%m-%d") 
            print(task_finish_date)
            task_status = input("enter the status of the task")
            # add condition to calculate task status and write it in percentile
            if task_status == "in progress":
                task_status = 0.5
                # convert status to percentage
                print("Task done is {}".format(task_status)) 
                print("You are doing good, keep going")
                
            elif task_status == "done":
                task_status = 1
                print("Task done is {}".format(task_status))
                print("Congradulation you finished the task on {}".format(task_finish_date))
            
            else:
                task_status = 0
                print("Your due date for the task is {}".format(task_finish_date))
                print("You have to do the task")
                       

print(input_values())