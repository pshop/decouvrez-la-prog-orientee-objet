#to open and load the json file
import json
#to use the pi attribute
import math

###############################################################################

#I create a class Agent
class Agent:
    #it's initialised with a position and a dictionary of attributes
    def __init__(self, position, **agent_attributes):
        #set the pposition attribute
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

#beginning of the program
def main():
    #i open the json file that contains 100k agents
    for agent_attributes in json.load(open("agents-100k.json")):
        # take the latitude from the attribute list and store it in a var
        #so i won't store two times the latitude when i'll initiate the agent
        latitude = agent_attributes.pop("latitude")
        #same here for longitude
        longitude = agent_attributes.pop("longitude")
        #i create an instance of postion and store the latitude and longitude
        position =  Position(longitude, latitude)
        #i create an instance of agent dans give 2 args
        #the instance 'position' and the dict of 'agent_attributes'
        agent = Agent(position, **agent_attributes)
        #i print the latitude in RAD
        print(agent.position.latitude)

main()
