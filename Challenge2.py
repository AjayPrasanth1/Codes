import os
import json
f= open('/run/cloud-init/instance-data-sensitive.json')
data = json.load(f)
#print(type(data))
data_new=data.get("ds").get("meta-data")
print("Below are the EC2 metadata Details     :         ",data_new)

def get_all_values(jsondata,datakey):
    for key, value in jsondata.items():
        if type(value) is dict:
            get_all_values(value,datakey)
        else:
            if(datakey == key):

                print(key, ":", value)
                break


datakey=input("Enter Data key you want to get : ")
get_all_values(data_new,datakey)
