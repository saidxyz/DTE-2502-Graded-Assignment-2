from game_environment import Snake
import numpy as np

env = Snake(board_size=10, frames=2)
s = env.reset()
env.print_game()

done = False
step_count = 0


while(not done):
    action = np.random.choice([-1, 0, 1], 1)[0]
    # instead of random action, take input from user
    #action = int(input('Enter action [-1, 0, 1] : '))
    # print(action)
    s, r, done, info, extra = env.step(action)
    print(f"Reward: {r}, Done: {done}, Info: {info}")
    # print(env._snake_direction)
    # for i, x in enumerate(env._snake):
        # print(i, x.row, x.col)
    env.print_game()
    step_count += 1

