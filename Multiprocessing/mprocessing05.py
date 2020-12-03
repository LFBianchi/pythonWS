from multiprocessing import Pool
import time

tasks = (['A', 3], ['B', 54], ['F', 22], ['E', 43])

def  task_exec(tasks_data):
    print(f'Process {tasks_data[0]} waiting {tasks_data[1]} seconds')
    time.sleep(int(tasks_data[1]))
    print(f'Process {tasks_data[0]} finished!')

def pool_func():
    p = Pool(2)
    p.map(task_exec, tasks)

if __name__ == '__main__':
    pool_func()
