# -*- coding: utf-8 -*-
import json
import requests
import time


#load 
XurBotURLCurl="https://www.reddit.com/user/DTG_Bot/.json"
response = requests.get(XurBotURLCurl)

#title formatting
today = str(datetime.date.today())
#today="2018-09-28"
string_post="[D2] Xûr Megathread ["+today+"]"

time.sleep(3)
parse=response.json()
time.sleep(3)
test_reddit= len(json.dumps(parse))

if test_reddit <1000:
   reprocess=1
   print("Bad DTG_Bot Load")
   time.sleep(5)
   for x in range(0,40):
      if reprocess==1:
         response = requests.get(XurBotURLCurl)
         time.sleep(3)
         parse=response.json()
         time.sleep(3)
         test_reddit= len(json.dumps(parse))
         if test_reddit >1000:
            print("Reddit attempt " +str(x) +" worked!")
            reprocess=0
         else:
            print("Reddit attempt " +str(x) +" did not work")
            time.sleep(7)

for y in range(0,20):
   if parse["data"]["children"][y]["kind"]=="t3":
      test=parse["data"]["children"][y]["data"]["title"]
      if test==string_post:
         xurtext=parse["data"]["children"][y]["data"]["selftext"]

length=len(xurtext)
length2=length-700
xurtext2=xurtext[1:length2]


headers = {'Content-type': 'application/json'}

payload = '{"text":" <!channel> Here is what Xur has in stock: \n \n' + xurtext2 + ' " }'

# webhook for Destiny_remastered
r = requests.post('YOUR WEBHOOK HERE', data=payload.encode('utf8'), headers=headers)


