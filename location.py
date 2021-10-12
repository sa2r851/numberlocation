import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium

key='0435017d25824903a1edae0624aaa114'
number = input("Drop number :")
sakrnumber=phonenumbers.parse(number+20)
yourlocation=geocoder.description_for_number(sakrnumber,'en')
print(yourlocation)
print(carrier.name_for_number(sakrnumber,'en'))
geo = OpenCageGeocode(key)
query = str(yourlocation)
result = geo.geocode(query)
#print(result)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)
mymap = folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=yourlocation).add_to((mymap))
mymap.save("myloctaion.html")