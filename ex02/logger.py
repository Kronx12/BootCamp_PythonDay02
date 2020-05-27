import time
from random import randint


def log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        val = func(*args, **kwargs)
        exec_time = time.time() - start_time
        with open("machine.log", "a") as f:
            if exec_time < 1:
                if func.__name__ == "start_machine":
                    f.write("(gbaud)Running: %-20s" % ("Start Machine"))
                    f.write("[ exec-time = %.3f ms ]\n" % (exec_time * 1000))
                elif func.__name__ == "boil_water":
                    f.write("(gbaud)Running: %-20s" % ("Boil Water"))
                    f.write("[ exec-time = %.3f ms ]\n" % (exec_time * 1000))
                elif func.__name__ == "make_coffee":
                    f.write("(gbaud)Running: %-20s" % ("Make Coffee"))
                    f.write("[ exec-time = %.3f ms ]\n" % (exec_time * 1000))
                elif func.__name__ == "add_water":
                    f.write("(gbaud)Running: %-20s" % ("Add Water"))
                    f.write("[ exec-time = %.3f ms ]\n" % (exec_time * 1000))
            else:
                if func.__name__ == "start_machine":
                    f.write("(gbaud)Running: %-20s" % ("Start Machine"))
                    f.write("[ exec-time = %.3f s  ]\n" % (exec_time))
                elif func.__name__ == "boil_water":
                    f.write("(gbaud)Running: %-20s" % ("Boil Water"))
                    f.write("[ exec-time = %.3f s  ]\n" % (exec_time))
                elif func.__name__ == "make_coffee":
                    f.write("(gbaud)Running: %-20s" % ("Make Coffee"))
                    f.write("[ exec-time = %.3f s  ]\n" % (exec_time))
                elif func.__name__ == "add_water":
                    f.write("(gbaud)Running: %-20s" % ("Add Water"))
                    f.write("[ exec-time = %.3f s  ]\n" % (exec_time))
        return val
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
