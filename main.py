import subprocess
import multiprocessing as mp
import os
import time
import ast
numtasks = 3

from conf import *

def save_conf(dict, filename):
    with open(filename, 'w+') as f:
        for key in dict:
            f.write(key + '$' + str(dict[key]) + '\n')

def async_tasks(task):
    match task:
        case 0: #video computing 1
            compute_vid(0)
        case 1: #video computing 2
            compute_vid(1)
        case 2: #send to esp
            upd_client()


def compute_vid(worknum):
    command = ['python', ('predict' + str(worknum) + '.py')]  
    os.chdir("./YOLOv8_deepsort_count/ultralytics/yolo/v8/detect/")
    subprocess.call(command)

def upd_client():
    command = ['python', 'sender.py']  
    os.chdir("./YOLOv8_deepsort_count/ultralytics/yolo/v8/detect/")
    subprocess.call(command)



if __name__ == '__main__':
    save_conf(cfgdict, confpath)
    pool = mp.Pool(numtasks)
    for y in range(numtasks):
        pool.apply_async(async_tasks, args=(y,))
        time.sleep(0.5)
    pool.close()
    pool.join()

