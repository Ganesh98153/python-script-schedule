import os
import requests
import time

from datetime import datetime
import random

random_number = random.randint(0, 60)
time.sleep(random_number)

# Get the current date and time
now = datetime.now()

current_hour_24hr = now.hour

if(current_hour_24hr < 8):
    isCheckIn = 'true'
else:
    isCheckIn='false'

# Format the datetime object to the desired format
formatted_time = now.strftime("%I:%M:%S %p")

print(formatted_time)

json_data = {
    'userName': 'ganesh.tiwari@Bitskraft.com',
    'password': 'Bits@98153', #Enter your password here
    'strategy': 'password',
}


response = requests.post('https://bitskraft.rigohr.com/v1/auth/signin', json=json_data)

if response.status_code == 200:
    json_response = response.json()
    token = json_response.get('Token')

    cokies_dict = response.cookies.get_dict()
    #print("Cokies : ", cokies_dict)
    print()
    
    #print(token)

else :
    print(f"Request failed with status code : {response.status_code}")

headers = {
    'authority': 'bitskraft.rigohr.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'authorization': f'bearer {str(token)}',
    'content-type': 'application/json',
    #'cookie': '.AspNetCore.Identity.Application=CfDJ8MfsdsRL3gtLhbygVOOENYrx9BsWKZgQDsKCFZTefPIRfZbcUEZzX3ajhzIGHGeo9tojbmvT77-QLPnb2Lj7kkwbA7t7fRTOQmYx9rNU44lSsHFhzoskQa-roB4mbWAVTzXGaNzQVgDo9IctB_W9L0Igc5mWa4ZsjZULCdOChykh0dfOtG1BpW8ZB5iyBwl7bQGZ1Da7ynAMXrPrqMXHpIo7FQ264U8BRBrnt8uyek2ukxxwSh0eOVds3SKOlBlpbkL2kUDZqKWbj2orPc0aqoHaFqC1f4-cWg0or1ZAVfniYDlstDsYO4pEshiBRNAAXqSSQiwZm7k9H1NR30k3u8Dn9dm75zeoJy1ufZHioXjtvhSKLZlhc51GoUONX59ElliyqKXNTT4wAJb3JxwQM-bw6db1IfGx9sGvWLXH8wrzwmA1ClTuy24qMdgmg1--tUrIoRzZfJ8kg5aR_zegJi0uExf_0zP_F8K7c18pYmAnYlP90CqQPVeKPCHDrEFIOibnQ8HVIg3tYjjLpFaoUZzlwhOT3nRjeIkBNHx5WFnkmMQyaxVOMc1niUmht7-Zn5baZP4GfBlhrLpAvx1ev0BFeo7gMzRNFbwO2xwGXT5WkijWnIE1JtsW_PiX2Cklzc1X8VP6pyMwwgo7-DuR8SDgzdgeO8XlOUOtrR9YCFz37_tR121Gd42sWTEZMAGUxBabCRfDUBY-4nshGCUvRXk; .AspNet.SharedCookie=CfDJ8MfsdsRL3gtLhbygVOOENYp52Gyo63vYiGj-jn8wZZo6nw0pLZ8_C-gkQZsb15mubDCyKaMczeVH-bUhyDJJnV2czdxuju-KfZRUDTM5B0QD4U3JAE0I-vkb6Ltqasu3QA6ITUjbdxRZ25pfkDwvvaVb7495NJ-Og63SvT059or_dXcbF5ClHic24JL2vznQRjgH-q6Fu5AhOjrEJ7sIAf3RJt-xzST0WHSgkXypffXnR3ygkIiBtqRkBxNWUmKiaCarM7X1jWviw4E8yfxpxNjgqKIRVO8pwoNEUtylhX0b4B6qoL9TdcwCTw4aGVJ2Qo3BObTnhGQlZFkgmpAXnBFzyCTUD_SNraSd99ITLj93jvvptRkXihWluh41wNF2A_LuoNyzFdnR6YQeqmziQNIclVcACIhYhg2Zsq-jCPOCLdbDYab5PSyvRtP3m9syPXE0MmDV69tzHn_4mT-Y4fMTFA5yeJLX3O5Utf_1Ktgy4tDYXnbjwXdKuCTmPPJye8g9WW92jc6fV7Ep39M2MZb1mxDi3MGUml01EFh19l4I9j7UdtjJ7QywLcDnHT9PotW618irLeFvdzYdoUicolf0O_U5-LLK_redLzhHqOnEOZ44mfm9s1X5QrFlg7DnLL3bXEbxvh3J3PJeeQjLivgLcDELMDHStrv38Km8jCW6',
    'loading': 'false',
    'origin': 'https://bitskraft.rigohr.com',
    'referer': 'https://bitskraft.rigohr.com/employee/personal-information',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
#isBreakIn
params = {
    'isCheckIn': isCheckIn,
}

json_data = {
    'ManualVisibleTime': formatted_time,
    'remarks': '',
}

response = requests.post(
    'https://bitskraft.rigohr.com/v1/leave-time/attendance/manual',
    cookies=cokies_dict,
    params=params,
    headers=headers,
    json=json_data,
)

print(response.content)
        
    