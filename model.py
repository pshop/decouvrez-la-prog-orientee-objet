import json

###############################################################################

class Agent:

    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)

###############################################################################

class Position:

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

###############################################################################

def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position =  Position(longitude, latitude)
        agent = Agent(position, **agent_attributes)

main()
