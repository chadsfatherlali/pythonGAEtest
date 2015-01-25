import webapp2
import urllib2
import json


class MainPage(webapp2.RequestHandler):
    def get(self):
        #path = os.path.dirname(os.path.abspath(__file__))
        #r = requests.post("https://api.cloudconvert.com/convert?apikey=15UY8HvuA1ivPAj7pp125N0rzhgqIAVwEm_1Po-MuYGvp8w5Wtwj5xRzkY4KB3B9tdy3XOkAWuulnSR0SCZ7XQ&input=upload&download=inline", files = {"file": open(path + "/bootstrap/MAD-C8116-S2.svg", "r")})
        #data = urllib.urlencode({"file": path + "/bootstrap/MAD-C8116-S2.svg"})
        #r = urllib2.urlopen("https://api.cloudconvert.com/convert?apikey=15UY8HvuA1ivPAj7pp125N0rzhgqIAVwEm_1Po-MuYGvp8w5Wtwj5xRzkY4KB3B9tdy3XOkAWuulnSR0SCZ7XQ&input=upload&download=inline", data)
        
        
        
        #with open("output.undefined", "wb") as fd:
            #for chunk in r.iter_content(1024):
                #fd.write(chunk)
        
        #linestring = open(path + "/bootstrap/MAD-C8116-S2.svg", "r").read()
        #linestring = base64.b64encode(linestring)
        
        #self.response.write(linestring)
        
        r = urllib2.Request("https://api.cloudconvert.com/convert?apikey=81EYtYLUndjNqQ6zE0srviQtPRvVUZjswVEqKLpaDW7wnE69YSiL0bI-NyMB1CQdsUO_9YivKjgxbqzKFtbSYw&input=download&output=googledrive&download=false&inputformat=svg&outputformat=jpg&file=http%3A%2F%2Ftheta-yen-836.appspot.com%2Fbootstrap%2FMAD-C8116-S25.svg")
        response = urllib2.urlopen(r)
        self.response.headers["Content-Type"] = "application/json"
        self.response.write(response.read())
        #self.response.write(response)
        #with open("MAD-C8116-S252.svg.jpg", "wb") as fd:
            #for chunk in response.iter_content(1024):
                #fd.write(chunk)

application = webapp2.WSGIApplication([
    ("/", MainPage)
], debug=True)
