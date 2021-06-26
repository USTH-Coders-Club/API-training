#import the library to make http request
import requests

#URL of the API
URL = "https://ssd-api.jpl.nasa.gov/cad.api"

distmax = input("set the maximum distance: ")
vinfmax = input("set the maximum speed: ")


#Params 
param = {
    'dist-max': distmax,
    'v-inf-max': vinfmax
}

#Make an API request and store date to r
r = requests.get(url= URL, params = param)

#Json data
data = r.json()

#extract count from data
n = data['count']
print(f"The number of asteroids approaching earth within {distmax} at {vinfmax} is {n}")