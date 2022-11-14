#Envelope Game
import random
import numpy as np

runs_Num = 100
env_Num = 1000
success = 0

def random_env(list_len):
    my_list = []
    for i in range(list_len):
        my_list.append(random.randint(0,500))

    return my_list


for drop_frac in range(10, 80, 2):
    drop_Rate = int(env_Num*drop_frac/100)

    for i in range(runs_Num):

        envelopes = random_env(env_Num)
        env_max = max(envelopes)

        drop_list = np.array(envelopes[0:drop_Rate])
        reject_max = drop_list.max()

        remain_list = np.array(envelopes[drop_Rate:])

        if reject_max == env_max:
            continue
        elif remain_list[remain_list > reject_max][0] == env_max:
            success += 1

    print("Successrate for ", drop_frac/100, success/runs_Num)



