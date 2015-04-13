from lxml import html
import requests, re, folium
from geopy.geocoders import Nominatim
from stuff import Stuff
import stuffify #this is a module


#request and scraping
freestuff = requests.get('http://montreal.craigslist.com/search/zip')
freetree = html.fromstring(freestuff.text)
stuffs = freetree.xpath('//a[@class="hdrlnk"]/text()')
urls = freetree.xpath('//a[@class="hdrlnk"]/@href')
locations = freetree.xpath('//span[@class="pnr"]/small/text()')

#the construction of free stuffs
freestuffs = [stuffify.gather_stuff(stuffs[x], urls[x], locations[x]) for x in range(0,10)]

#test coordinates
geolocator = Nominatim()
findit = geolocator.geocode(freestuffs[1].location)
if findit is not None:    
    print(findit, findit.latitude, findit.longitude)

#test the coord calculator
coordinates = stuffify.get_coordinates(freestuffs[1].location)
print(coordinates)
print(str(freestuffs[1]))
stuffify.post_map(freestuffs)