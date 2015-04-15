from lxml import html
import requests, re, folium
from geopy.geocoders import Nominatim
from stuff import Stuff
import stuffify #this is a module
import webbrowser
import http.server
import time


#request
freestuff = requests.get('http://montreal.craigslist.com/search/zip')
#scraping, using xpath maybe I should I gone with bsoup
freetree = html.fromstring(freestuff.text)
stuffs = freetree.xpath('//a[@class="hdrlnk"]/text()')
urls = freetree.xpath('//a[@class="hdrlnk"]/@href')
locations = freetree.xpath('//span[@class="pnr"]/small/text()')

# this is a list combobulator. Python really is beautiful
freestuffs = [stuffify.gather_stuff(stuffs[x], urls[x], locations[x]) for x in range(0,10)]

#test geolocator, cool feature
geolocator = Nominatim()
findit = geolocator.geocode(freestuffs[0].location)
if findit is not None:    
    print(findit)

#Print recent stuff
output = str(freestuffs[0])
print(output)

myServer = BaseHTTPRequestHandler((localhost, 8000), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % ("localhost","8000"))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass


#Make sure http.server is running
stuffify.post_map(freestuffs)
webbrowser.open_new_tab("localhost:8000/findit.html")

