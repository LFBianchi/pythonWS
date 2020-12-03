import multiprocessing as mp
import time

def sqr():
#    while True:
#        print('Please insert a number!: ')
#        a = input()
#        print(a ** a)
    pass

def sleeper():
    while True:
        print('I will go to sleep for 15 seconds')
        time.sleep(15)

if __name__ == '__main__':
    p1 = mp.Process(target = sqr)
    p2 = mp.Process(target = sleeper)
    p1.start()
    p2.start()
