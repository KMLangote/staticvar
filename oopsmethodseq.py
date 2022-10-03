class Sequence:
    def __new__(cls, *args, **kwargs):
        print("Calling new function for creating object")
        return super(Sequence, cls).__new__(cls, *args, **kwargs)
    def __init__(self):
        print("Calling Constructor")
    def __call__(self, *args, **kwargs):
        print("Call method")

    def getName(self):
        print("My name is kanchan")
s = Sequence()
s()
s.getName()
