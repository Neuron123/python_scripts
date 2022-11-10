#get current position of the ISS
import requests

# get current position of the ISS
def getISSPosition():
    # get the current position of the ISS
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
        # get the latitude and longitude
        lat = response['iss_position']['latitude']
        lon = response['iss_position']['longitude']
        return (lat, lon)
    else:
        return None

# get the current position of the ISS
lat, lon = getISSPosition()
print('The ISS is currently at latitude: %s and longitude: %s' % (lat, lon))