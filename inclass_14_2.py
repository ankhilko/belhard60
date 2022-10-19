import multiprocessing

from time import sleep


def foo(i: int):
    for _ in range(10):
        sleep(1)
        with open(f'newfile_{str(i)}{str(i)}', 'a') as file:
            file.write(str(i))
            file.write('\n')


processes = [multiprocessing.Process(target=foo, args=(j,)) for j in range(10)]

for process in processes:
    process.start()

