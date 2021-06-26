#import the library to make http request
import requests

#URL of the API
URL = "http://127.0.0.1:5000"

dating_id = input("Id of the guy you want to flirt")

param ={
    'id':dating_id,
}

#Make an API request and store date to r
r = requests.get(url= URL, params=param)

#Json data
data = r.json()

#extract count from data
n = data['age']
name = data['name']
print(f"age of {name} is {n}")