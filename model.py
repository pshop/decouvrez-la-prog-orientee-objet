class Agent:

    def say_hello(self, first_name):
        return "bonjour " + first_name + "!"

    def __init__(self, agreeableness):
        self.agreeableness = agreeableness

agent1 = Agent(1)
print(agent1.say_hello("Jean Claude"))
print(agent1.agreeableness)
