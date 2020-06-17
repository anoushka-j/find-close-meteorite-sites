import requests
import math 
meteor_response = requests.get("https://data.nasa.gov/resource/gh4g-9sfh.json")
meteor_data = meteor_response.json()

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

print("Loading...")
user_lat = input("What is your latitude?")
user_long = input("What is your longitude?")

distances = []


for meteor in meteor_data: 
  if 'reclat' and 'reclong' in meteor : 
    meteor['distance'] = calc_dist(float(user_lat), float(user_long), float(meteor['reclat']), float(meteor['reclong']))
    distances.append(meteor['distance'])
    if meteor['distance'] < 1000 : 
      print(meteor['name'], meteor['year'], meteor['distance'])


  
