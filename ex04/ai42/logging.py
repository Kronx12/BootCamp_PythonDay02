import time


def log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        val = func(*args, **kwargs)
        exec_time = time.time() - start_time
        with open("machine.log", "a") as f:
            if exec_time < 1:
                f.write("(gbaud)Running: %-20s" % (func.__name__))
                f.write("[ exec-time = %.3f ms ]\n" % (exec_time * 1000))
            else:
                f.write("(gbaud)Running: %-20s" % (func.__name__))
                f.write("[ exec-time = %.3f s  ]\n" % (exec_time))
        return val
    return wrapper
