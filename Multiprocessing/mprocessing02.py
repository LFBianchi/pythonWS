from multiprocessing import Process

def myFunc():
    print('Hello World!')

if __name__ == '__main__':
    proc = Process(target = myFunc)
    proc.start()
    proc.join()
