import json
import math

class Agent:
    
    def __init__(self, position, **agent_attributes):
        self.position = position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self, attr_name, attr_value)

class Position:
    def __init__(self, longitude_degrees, latitude_degrees):
        self.longitude_degrees = longitude_degrees
        self.latitude_degrees = latitude_degrees
        
    @property
    def longitude(self):
        return self.longitude_degrees * math.pi / 180







def main():
    for agent_attributes in json.load(open("agents-100k.json")):
        latitude = agent_attributes.pop("latitude")
        longitude = agent_attributes.pop("longitude")
        position = Position(longitude, latitude)

        agent = Agent(position, **agent_attributes)
        #print(agent.agreeableness)
        print(agent.position.longitude)

main()       
