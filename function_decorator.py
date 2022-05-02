def print_func_name(func):
    def wrap():
        print("Now use function '{}'".format(func.__name__))
        func()
    return wrap

@print_func_name
def dog_bark():
    print("Bark !!!")

if __name__ == "__main__":
    dog_bark()
    # the same as print_func_name(dog_bark)()
    # > Now use function 'dog_bark'
    # > Bark !!!
