class Stuff(object):
    thing = ""
    url = ""
    location = ""
	image = "" #todo
		
    #constructor the de-structor!!  
    def __init__(self, thing, url, location):
        self.thing = thing
        self.url = 'http://montreal.craigslist.ca' + url
        place = str(location).strip(' ()')
        self.location = "montreal, " + place
    
    def __str__(self):
        return "what:%s \n where:%s \n link:%s" % (self.thing, self.location, self.url)
        
