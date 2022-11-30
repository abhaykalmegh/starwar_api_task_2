import time
def time_calculate(function):
    def wrapper():
        start_time = time.time()
        function()
        end_time = time.time()
        total = end_time - start_time
        print(total)
    return wrapper
