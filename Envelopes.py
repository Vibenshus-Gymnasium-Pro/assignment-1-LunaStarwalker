#Envelope game

import random

my_envelopes = []
my_envmaxdata = []
my_recordedmaxdata = []
my_data = []
maxEnvelope = 0


def random_env(my_range):
    my_list = []
    for i in range(my_range):
        value = random.randint(1, 500)
        my_list.append(value)

    return my_list


def pick_env(my_list):

    currentEnvelopes = []

    for i in range(50):
        value = random.choice(my_list)
        currentEnvelopes.append(value)
        my_list.remove(value)

    maxEnv = max(currentEnvelopes)

    return maxEnv


def find_max(my_list, maxEnv):

    for i in my_list:
        if i < maxEnv and i != my_list[-1]:
            my_list.remove(i)
        elif i > maxEnv or i == my_list[-1]:
            maxEnv = i

    return maxEnv


def find_probability(my_list):
    num = 0
    for i in range(len(my_list)):
        if my_list.keys == my_list.values:
            num += 1

    probability = i/len(my_list)*100

    return probability


for i in range(1000):
    my_envelopes = random_env(100)
    max_value = max(my_envelopes)
    maxEnvelope = pick_env(my_envelopes)
    env_max = find_max(my_envelopes, maxEnvelope)

    print(maxEnvelope)
    print(env_max)

    my_envmaxdata.append(max_value)
    my_recordedmaxdata.append(env_max)

my_data = dict(zip(my_envmaxdata, my_recordedmaxdata))

success = find_probability(my_data)
print(success)
