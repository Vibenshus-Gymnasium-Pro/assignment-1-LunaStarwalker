class Runner:

    def __init__(self, list):
        self.name = list[0]
        self.run1 = float(list[1])
        self.run_leg = float(list[2])

    def get_info(self):
        return self.name + '\n'


def relay():
    n = int(input())
    runners = []

    min_time = 10000

    for i in range(n):
        info = list(map(str, input().split()))
        runners.append(Runner(info))

    for obj, obj2, obj3, obj4 in runners:
        time = obj.run1 + obj2.run_leg + obj3.run_leg + obj4.run_leg

        if time < min_time:
            min_time = time


    print(time)
    print(obj.get_info, obj2.get_info, obj3.get_info, obj4.get_info)


    for obj in runners:
        print(obj.name, obj.run1, obj.run_leg, sep=' ')


if __name__ == "__main__":
    relay()