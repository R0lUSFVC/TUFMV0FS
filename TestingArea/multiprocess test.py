from multiprocessing import Pool
from subprocess import check_call

commands = [
    'echo {time}; sleep {time}; echo {time}'.format(time=5),
    'echo {time}; sleep {time}; echo {time}'.format(time=10),
    'echo {time}; sleep {time}; echo {time}'.format(time=4),
]


def sample(command):
    check_call(command, shell=True)


if __name__ == '__main__':
    with Pool(len(commands)) as p:
        p.map(sample, commands)