""" 
using awitch statement for more than one conditions to match

"""
htpps_status = input("enter code")
htpps_status = int(htpps_status)
match htpps_status:
    case 200 | 201:
        print('Sucess')
    case 400:
        print("Not Found")
        htpps_status
    case 500 | 501:
        print("Server error")
    case _:
        print('Unkwon')