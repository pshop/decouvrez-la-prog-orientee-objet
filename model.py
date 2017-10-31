class Agent:

    def say_hello(self, first_name):
        return "bonjour " + first_name + "!"

    def __init__(self):
        self.agreeableness = 0

agent1 = Agent()
print(agent1.say_hello("Jean Claude"))
print(agent1.agreeableness)
