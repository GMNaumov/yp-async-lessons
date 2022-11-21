import time

from multiprocessing import Process, current_process

def custom_func():
    process_name = current_process().name
    process_pid = current_process().pid
    print(f'Process {process_name} [{process_pid}] has started.')
    time.sleep(2)

if __name__ == '__main__':
    p1 = Process(name='job1', target=custom_func)
    proc_pid = p1.pid
    proc_status = p1.is_alive()
    print(f'Process with pid[{proc_pid}] is working [{proc_status}]')

    p1.start()
    proc_status = p1.is_alive()
    proc_pid = p1.pid
    print(f'Process with pid[{proc_pid}] is working [{proc_status}]')
    p1.join()

    proc_status = p1.is_alive()
    print(f'Process with pid[{proc_pid}] is working [{proc_status}]')
