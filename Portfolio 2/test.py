import agentframework

agent_1 = agentframework.Agent(5,10)

print('the x coordinate of agent_1 is ' + str(agent_1.x))

agent_1.move(5)

print(agent_1.x)
print(help(agentframework.Agent.move))