#to open and load the json file
import json
#to use the pi attribute
import math

###############################################################################

#I create a class Agent
class Agent:
    #it's initialised with a position and a dictionary of attributes
    def __init__(self, position, **agent_attributes):
        #set the position attribute
        self.position = position
        #creates an attribute for every entry of the dictionary
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)

###############################################################################

#I create a class Position
class Position:
    #it's initialised with a longitude and a latitude both in degrees
    def __init__(self, longitude_degrees, latitude_degrees):
        self.longitude_degrees = longitude_degrees
        self.latitude_degrees = latitude_degrees

    #i create a property that will make appear a method like an attribute
    @property
    def longitude(self):
        #it converts the degrees to radians
        return self.longitude_degrees * math.pi / 100

    #same here with the latitude
    @property
    def latitude(self):
        return self.latitude_degrees * math.pi /100

###############################################################################

#i create a class Zone that will contain a tab with all the zones of our
#fictional world
class Zone:

    ZONES = [] #empty list that will contain all the zones
    MIN_LONGITUDE_DEGREES = -180
    MAX_LONGITUDE_DEGREES = 180
    MIN_LATITUDE_DEGREES = -90
    MAX_LATITUDE_DEGREES = 90
    WIDTH_DEGREES = 1 #degree step
    HEIGHT_DEGREES = 1#idem

    #initialize 1 zone (zones are squares in the area) and 1 zone has
    def __init__(self, corner1, corner2):
        #one coordonate for its bottom left corner
        self.corner1 = corner1
        #one coordonate for its top right corner
        self.corner2 = corner2
        #a number of inhabitants
        self.inhabitants = []

    #this is a class method it can be run without having to instanciate
    @classmethod
    def initialize_zones(cls):
        #for every degree in the latitude from -90 to 90
        for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):
            #for every degree in the longitude from -180 to 180
            for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
                #coordonates of bottom_left_corner is (longitude , latitude)
                bottom_left_corner = Position(longitude, latitude)
                #coordonates of top_right_corner is (longitude + 1 , latitude + 1)
                top_right_corner = Position(longitude + cls.WIDTH_DEGREES, latitude + cls.HEIGHT_DEGREES)
                #instanciate a zone with the coordonates of (bottom_left_corner , top_right_corner)
                zone = Zone(bottom_left_corner, top_right_corner)
                #add the zone in the list class attribute ZONE
                cls.ZONES.append(zone)
        #debug print the lenght of the zone class attribute
        #i see 64800 that means 360 * 180, seems OK !
        print(len(cls.ZONES))

    def contains(self, position):
        return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
        position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
        position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
        position.latitude < max(self.corner1.latitude, self.corner2.latitude)

    @classmethod
    def find_zone_that_contains(cls, position):
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES) / cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES)
        zone_index = latitude_index * longitude_bins + longitude_index

        zone = cls.ZONES[zone_index]
        assert zone.contains(position)

        return zone

    def add_inhabitant(self, inhabitant):
        self.inhabitants.append(inhabitant)

    @property
    def population(self):
        return len(self.inhabitants)


###############################################################################

#beginning of the program
def main():
    Zone.initialize_zones()
    #i open the json file that contains 100k agents
    for agent_attributes in json.load(open("agents-100k.json")):
        # take the latitude from the attribute list and store it in a var
        #so i won't store two times the latitude when i'll initiate the agent
        latitude = agent_attributes.pop("latitude")
        #same here for longitude
        longitude = agent_attributes.pop("longitude")
        #i create an instance of position and store the latitude and longitude
        position =  Position(longitude, latitude)
        #i create an instance of agent dans give 2 args
        #the instance 'position' and the dict of 'agent_attributes'
        agent = Agent(position, **agent_attributes)
        #for evry agent i find the zone where he comes from
        #i instanciate this zone
        zone = Zone.find_zone_that_contains(position)
        #and i add the agent to the zone
        zone.add_inhabitant(agent)
        #i print the number of inhabitants of the zone
        print("Zone population:", zone.population)


main()
