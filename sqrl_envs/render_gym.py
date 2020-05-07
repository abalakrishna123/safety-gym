import safety_gym_envs
import gym

env = gym.make('SafeExpPointEnv-v0')
env.reset()
for _ in range(10000):
    o,r,d,i = env.step(env.action_space.sample())
    if d:
        env.reset()
    env.render()
