import time
def task_scheduler(fun,n):
    time.sleep(n)
    fun()

def print_function():
    print("Hi, we are implementing a scheduler.")

task_scheduler(print_function,1)
