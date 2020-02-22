import requests 
  
# api-endpoint 
URL = "https://surgical-glass.herokuapp.com/api/v1/"

r = requests.get(url = URL) 
  
data = r.json()
#print(data['data'])

doctor = data['data'][0]['doctor']
print('the doctor is: ',doctor)
imp_pts = data['data'][0]['important_points']
meds = imp_pts = data['data'][0]['medications']
print('medications for this: ',meds)
print('The important points are: ',imp_pts)