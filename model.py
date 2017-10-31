class Agent:

    def say_hello(self, first_name):
        return "bonjour " + first_name + "!"

agent1 = Agent()
print(agent1.say_hello("Jean Claude"))
