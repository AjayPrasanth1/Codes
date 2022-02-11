import os
#object = {"a":{"b":{"c":"d"}}}
#key = "a/b/c"
def output(object,key):
    try:
        keysplit=key.split("/")
        object_new=object
        
        for i in range(len(keysplit)):
            object_new=object_new[keysplit[i]]
        print("Value=",object_new)
    except:
        print("ERROR")
object=input("Enter object :  ")

key=input("Enter Key :  ")
object1=eval(object)
output(object1,key)