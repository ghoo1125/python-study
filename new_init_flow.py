class A():
    def __init__(self):
        print("init")
        print(self)
        super().__init__()

    def __new__(cls):
        print("new")
        print(cls)
        self = super().__new__(cls) # create instance of class A
        print(self)
        return self # return instance and pass to  __init__

    def __call__(self):
        return "calling __call__"

if __name__ == '__main__':
    a = A() # call __new__ -> __init__

    # if def __call__ then it is callable
    # print(callable(a))
    # print(a()) # use __call__

    print(isinstance(A, type))