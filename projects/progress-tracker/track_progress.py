"""
this is my main file for the progress tracker project
this project is about building using python
a web application/ app that will allow user to enter inpute data
 and display the data in a table
 and also the users will be able to track their progess on a particula task
"""
def input_values():
    name_of_task = input("enter the name of the task")    
    sub_task = input("enter the sub task")
    task_start_date = input("enter the date to start")
    task_finish_date = input("enter the date to finish")
    task_status = input("enter the status of the task")

    return name_of_task, sub_task, task_start_date, task_finish_date, task_status

print(input_values())