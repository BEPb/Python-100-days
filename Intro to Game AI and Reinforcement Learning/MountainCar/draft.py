import gym

env = gym.make("MountainCar-v0")
env.reset()

done = False
while not done:
    action = 2  # always go right!
    env.step(action)
    env.render()
