# string.find()
from gettext import find
# sending data to url
import requests
# delete file
import os
# Win32 commands
import ctypes  
# to get time
import datetime
#sleep
import time
#argc and argv
from sys import argv

LOGIN_URL = 'https://tds.ms/CentralizeSP/Student/Login/redmond911'
STATUS_SUCCESS = 200
NOT_FOUND = -1
TIMEOUT_LENGTH = 60

def main() -> int:
    if len(argv) != 3:
        print ("Please give the username and password")
        exit(-1)
    
    username = argv[1]
    password = argv[2]

    #data to be sent with request
    payload = {
        'hdnCompanyId': '457',
        'hdnCompanyIdentifier': 'redmond911',
        'username': username,
        'password': password
    }
    

    #creating session
    with requests.Session() as s:
        #POST Request to login url, sending data
        p = s.post(LOGIN_URL, data=payload)        

        # now that we logged in, ask to access schedule data
        r = s.get('https://tds.ms/CentralizeSP/BtwScheduling/Lessons?SchedulingTypeId=1')

        # check if everything is successful
        if (r.status_code == STATUS_SUCCESS):
            print ("Successfuly logged into 911 driving school")
        else:
            print ("Failed to login to 911 driving school")
            exit(-1)

        #check if a class has been found
        if (r.text.find("No Record Found") == NOT_FOUND):
            # we found an open class!
            print("class found! Check 911 school to schedule the class")
            ctypes.windll.user32.MessageBoxW(0, f"Class Found! Found at {datetime.datetime.now()}", "IMPORTANT", 1)
            return 0
        else:
            print ("Couldnt find a class")
            return 1


if __name__ == '__main__':
    
    val = 1
    while(val != 0):
        val = main()
        time.sleep(TIMEOUT_LENGTH)
