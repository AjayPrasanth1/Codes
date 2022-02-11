import os 
import requests
metadadata_url="http://169.254.169.254/latest/meta-data"
response=requests.get(metadadata_url)
print(response.content)

val = raw_input("Enter the details you want to know without / characters :")
URl=metadadata_url+"/"+val
response_user=requests.get(URl)
print(response_user.content)

while True:
    val = raw_input("Enter the Specific Sub details without / characters :")
    URl=URl+"/"+val
    response=requests.get(URl)
    

    if ("404" not in response.content):
        print(response.content)
        continue
    else:
        print("404 Error......End of results ..Please run the file once again to check other fields")
        break



    


