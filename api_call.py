import requests 
  
# api-endpoint 
URL = "https://surgical-glass.herokuapp.com/api/v1/"

r = requests.get(url = URL) 
  
data = r.json()
#print(data['data'])

doctor = data['data'][0]['doctor']
print('\nThe doctor is: ',doctor)
imp_pts = data['data'][0]['important_points']
meds = data['data'][0]['medications']
log = data['data'][0]['log']
print('\nLOG: ',log)
print('\nmedications for this: ',meds)
print('\nThe important points are: ',imp_pts)
