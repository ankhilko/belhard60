import threading, time


def foo(i: int):
    for _ in range(10):
        time.sleep(1)
        print(i)


start_time = time.ctime()

threads = [threading.Thread(target=foo, args=(j, )) for j in range(10)]

for thread in threads:
    thread.start()

stop_time = time.ctime()

print(f'{stop_time - start_time}')

