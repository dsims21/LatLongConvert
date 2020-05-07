from geopy.geocoders import Nominatim
import pandas as pd

def city_state_country(coord):
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    county = address.get('county', '')
    state = address.get('state', '')
    country = address.get('country', '')
    ZIP = address.get('postcode', '')

    return city, county, state, country, ZIP

def get_county(lat, long):
    coord = str(lat)+', '+str(long)
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    county = address.get('county', '')

    return str(county)

def get_ZIP(lat, long):
    coord = str(lat)+', '+str(long)
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    ZIP = address.get('postcode', '')

    return str(ZIP)

def get_country(lat, long):
    coord = str(lat)+', '+str(long)
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    country = address.get('country', '')

    return str(country)

geolocator = Nominatim(user_agent="MyGeocoder")

location = geolocator.reverse("47.6144239, -122.19215913827682")
address = location.raw['address']
county = address.get('country', '')

print(location.raw)
print(city_state_country("47.6144239, -122.19215913827682"))


fields = ['ID', 'Latitude', 'Longitude']
df = pd.read_csv("ghcnd-stations-lat-long.csv",)

#df["Country"] = df.apply(lambda x: city_state_country("47.6144239, -122.19215913827682"), axis=1)
df["Country"] = ""
df["County"] = ""
df["ZIP"] = ""

for index, row in df.iterrows():
    #print(row['c1'], row['c2'])
    #country = get_country(row['Latitude'],row['Longitude'])

    df.loc[df.index[index], 'Country'] = get_country(row['Latitude'],row['Longitude'])
    df.loc[df.index[index], 'County'] = get_county(row['Latitude'], row['Longitude'])
    df.loc[df.index[index], 'ZIP'] = get_ZIP(row['Latitude'], row['Longitude'])

    print('Row:'+ str(index))
    #row['Country'] = get_country(row['Latitude'],row['Longitude'])
    #row['County'] = str(get_county(row['Latitude'], row['Longitude']))
    #row['ZIP'] = get_ZIP(row['Latitude'], row['Longitude'])

df.to_csv("sample.csv", index=False)

print('hello')
