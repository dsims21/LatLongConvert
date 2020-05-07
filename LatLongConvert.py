from geopy.geocoders import Nominatim

def city_state_country(coord):
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    county = address.get('county', '')
    state = address.get('state', '')
    country = address.get('country', '')
    ZIP = address.get('postcode', '')

    return city, county, state, country, ZIP

geolocator = Nominatim(user_agent="MyGeocoder")

location = geolocator.reverse("47.6144239, -122.19215913827682")
address = location.raw['address']
county = address.get('county', '')

print(location.raw)
print(city_state_country("47.6144239, -122.19215913827682"))
