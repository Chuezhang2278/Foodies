# Jia Ming Ma
import re, polyline, googlemaps

# print functions are there for testing!

def get_formatted_address(geocode):
    # get formatted address from google
    print("formatted address: " + geocode[0]['formatted_address'])
    return geocode[0]['formatted_address']

def get_lat(geocode):
    # get latitude(x) location of delivery person
    print("latitude(x): " + str(geocode[0]['geometry']['location']['lat']))
    return geocode[0]['geometry']['location']['lat']

def get_long(geocode):
    # get longtitude(y) location of delivery person
    print("latitude(y): " + str(geocode[0]['geometry']['location']['lng']))
    return geocode[0]['geometry']['location']['lng']

def get_duration(direction):
    # get the duration it takes from delivery person to customer
    print("time to customer: " + direction[0]['legs'][0]['duration']['text'])
    return direction[0]['legs'][0]['duration']['text']

def get_distance(direction):
    # get the distance from delivery person to customer
    print("distance to customer: " + direction[0]['legs'][0]['distance']['text'])
    return direction[0]['legs'][0]['distance']['text']

def get_step_by_step_directions(direction):
    # get the set of step by step directions(driving) for the delivery guy with html tags removed
    TAG_RE = re.compile(r'<[^>]+>')
    list = []
    # print("\n\nstep by step directions for delivery guy (driving): ")
    for i in range(len(direction[0]['legs'][0]['steps'])):
        # print(TAG_RE.sub('', direction[0]['legs'][0]['steps'][i]['html_instructions']))
        list.append(TAG_RE.sub('', direction[0]['legs'][0]['steps'][i]['html_instructions']))
    return list


##### ended up not needing the polyline stuff because I was able to integrate a webview instead directly
def get_polyline(direction):
    # get step by step polylines
    list = []
    for i in range(len(direction[0]['legs'][0]['steps'])):
        list.append(direction[0]['legs'][0]['steps'][i]['polyline']['points'])
    return list

def decode_polyline(polylines):
    list = []
    for i in range(len(polylines)):
        list.append(polyline.decode(polylines[i]))
    return list
#########################################################################################################


gmaps = googlemaps.Client(key='AIzaSyC2OaGRo3fZsfzHjywnuNoiuoY3YBWGHeE')
