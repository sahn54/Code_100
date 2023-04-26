# unlimited Positional Argument
def add(t_sum=0, *args):  # args -> tuple
    for n in args:
        t_sum += n
    return t_sum


print(add(3, 5, 6))


def calculate(n, **kwargs):  # kwargs -> dictionary
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]  # required
        self.model = kw.get("model")  # default as None
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Honda", model="Accord")
print(my_car.model)
