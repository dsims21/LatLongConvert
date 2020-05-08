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

def country_county_zip(lat, long):
    coord = str(lat) + ', ' + str(long)
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    county = address.get('county', '')
    country = address.get('country', '')
    ZIP = address.get('postcode', '')

    return country, county, ZIP


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

df = pd.read_csv("ghcnd-stations-lat-long.csv",)

df["Country"] = ""
df["County"] = ""
df["ZIP"] = ""

for index, row in df.iterrows():

    lat = float(row['Latitude'])
    long = float(row['Longitude'])

    #Initially checking just WA state
    if 49.196064 > lat > 45.576501 and -125.375188 < long < -116.821468:
        data = country_county_zip(row['Latitude'],row['Longitude'])
        #Add data pieces to columns in the dataframe
        df.loc[df.index[index], 'Country'] = data[0]
        df.loc[df.index[index], 'County'] = data[1]
        df.loc[df.index[index], 'ZIP'] = data[2]
        #Just for debugging/interest, print line found.
        print('Row:'+ str(index))

df.to_csv("sample.csv", index=False)

print('hello')
