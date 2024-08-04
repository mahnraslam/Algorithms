import requests
from randomuser import RandomUser
import pandas as pd
# This is one of several libraries including: httplib, urllib, that can work with the HTTP
# protocol.
# Requests is a python Library that allows you to send HTTP/1.1 requests easily. We can
# import the library as follows:
url = "https://www.ibm.com/"
r = requests.get(url)
# print(r.status_code)
# print(r.request.headers)


def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)
print(get_users())
df1 = pd.DataFrame(get_users())  