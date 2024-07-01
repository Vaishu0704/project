import time
def note_time_decorator(func):
    def wrapper():
        start_time=time.time()
        #print('Start_time:',start_time)
        func()
        end_time=time.time()
        #print('End_time:',end_time)
        print('Time taken  '+ str((end_time)-(start_time)))
    return wrapper()
@note_time_decorator
def log_function():
    time.sleep(5)
    print('Print the log of time taken')

@note_time_decorator
def report_function():
    time.sleep(2)
    print('Print the reporting time')