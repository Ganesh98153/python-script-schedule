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

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': 'OpenIddict.Client.State.SOXoJA40ps0juYgoPDIQb-D01UKp1UAdnMVIlmph-bU=AQAAACtaaVBqdzA2amVPc3FldEFXYWdDYTlhRHBmUFVwcGVDVlJHTUVuTUh1RXE0; canary=never; .RigoHR.SharedCookie=CfDJ8Cx-cLqiER5NtW0nQuVCfk0kA20Xwn5vc2jkSSVAMv68m0acY62nYByB8FLGiw2KI00dQ82nQPOxUmecB0ehTnUxV6ioXIojd3Y5VAObpezr1fyEn2mdSqBFg3Bk599WThE27WWL7iy5m0dSD9l2a-OXAuxsmV_nv2A0PNjvcLYRUtKKTerzlBhdzXU4NNOkcPS8ncwjKawCjNw0BDvV9uBO0_yAD6qBL4rcYkTTwp82NCJmieBnqsEJsFbYAUxzgDhLUdObp7sD6x5_V_LrzEsOTFkozRb5hQ01rPXQh-Dl9kfs3pE2jJWXEA1HjpQrB-pGdZz_23Lz9C8pfN0RNnPrJhrznsZrGrvDWuCK2QyJIyN2tMgOvW7_2F9VlysrJk301SEpXhyyQ3x2vMHBwpRimc_p8coGwqgcZrw2DkfGcKs0W6n1DAglgemwo3N1x87YnRFCDgZ5NUamtuEglllAtFHF4ebvAn7AG48wsJW9utmz4w0NkSgBXYAeUtkzLbExKTJD-cKd0rqqJ6uFkfvhPyItVDPgb17QWqwQCXYPY-OtEsakuLAnBeLwc9pOxLUxqQNOxbkYb3Zn7yQp7fTm5uMNZdSqCqh12ns5RFJCz5dWnQ4WLaMWcHl3vwoJuzuEH2m8GE7wwTX2pVqy3ApXGzydCNJ6rCa11ZwwOX2wZ-sbxmRs-w4ykJbmq1u59rqsMxYpw-nrpQXs5Hjxwfum1P7n1FKQsU8LVL4W2MtiEOeRedyc12w7Yq2QkUU7SQQFEQe895XwLfzs34cDPL8PnGULPWH42VZwC-CxB-Liv1wYINMiHyrLw_u9kr1bSNaoXJQQFxuKkjTRQBRiPnv0WnzezoWCIhWpF-aZNlP3n4A6toR2uEKrJzagmHUbMuOjntFpWXh8DiSCZvWgw_DxOkayYGwpmpxUdJQxCsAGKtSh9JtcQOWkvrdQCe8YaHDQnk32lMOBQqkIv256zCGSHCpf2D9P8mwJ2XaljhHZt661C4CA2HOnMWYlrPsgyjvgo98p_duAaQJvQQ4GV_iHXCkVor9-wqWKdv_i4FCJqAFWAy-foX9s4R1Mzjkx_w',
    'origin': 'https://app.rigohr.com',
    'priority': 'u=1, i',
    'referer': 'https://app.rigohr.com/hr/clock/in',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'tenantid': '5764af9a-5073-44db-9af1-9c6a6d29a15a',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
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
    'https://api.app.rigohr.com/v1/leave-time/attendance/manual',
    #cookies=cokies_dict,
    params=params,
    headers=headers,
    json=json_data,
)

print(response.content)
        
    
