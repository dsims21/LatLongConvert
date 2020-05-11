from geopy.geocoders import Nominatim
import pandas as pd

def country_state_county_zip(lat, long):
    coord = str(lat) + ', ' + str(long)
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    county = address.get('county', '')
    state = address.get('state', '')
    country = address.get('country', '')
    ZIP = address.get('postcode', '')

    return country, state, county, ZIP

geolocator = Nominatim(user_agent="MyGeocoder")

df = pd.read_csv("ghcnd-stations-lat-long.csv",)

df["Country"] = ""
df["State"] = ""
df["County"] = ""
df["ZIP"] = ""

for index, row in df.iterrows():

    lat = float(row['Latitude'])
    long = float(row['Longitude'])

    #Initially checking just WA state
    if 49.196064 > lat > 45.576501 and -125.375188 < long < -116.821468:
    #Entire US
    #if 22.824922 < lat < 49.774613  and -126.196032 < long < -64.103819:
        #Get data
        data = country_state_county_zip(row['Latitude'],row['Longitude'])

        #Add data pieces to columns in the dataframe
        df.loc[df.index[index], 'Country'] = data[0]
        df.loc[df.index[index], 'State'] = data[1]
        df.loc[df.index[index], 'County'] = data[2]
        df.loc[df.index[index], 'ZIP'] = data[3]

        #Just for debugging/interest, print line found.
        print('Row: '+ str(index))

df.to_csv("sample.csv", index=False)

print('Done')