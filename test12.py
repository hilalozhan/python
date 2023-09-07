from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Locater")
location =geolocator.geocode("Denizli")

print("Address: ",location.address)
print("Latitude: ",location.latitude)
print("Longitude: " ,location.longitude)

'''''
output is :
    Address:  Denizli, Ege Bölgesi, Türkiye
    Latitude:  37.8275892
    Longitude:  29.2389539

'''''
