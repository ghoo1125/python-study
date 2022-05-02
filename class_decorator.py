# Example 1
class Dog:
    def __init__(self, func):
        self.talent = func

    def bark(self):
        print("Bark !!!")

@Dog
def dog_can_pee():
    print("I can pee very hard......")


@Dog
def dog_can_jump():
    print("I can jump uselessly QQQ")

if __name__ == "__main__":
    dog_1 = dog_can_pee
    dog_1.talent()
    # > I can pee very hard......

    dog_2 = dog_can_jump
    dog_2.talent()
    # > I can jump uselessly QQQ

    # create instance of Dog through decorator
    print(dog_can_pee)

# Example 2
class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@Counter
def foo():
    pass

for i in range(10):
    # foo is instance of Counter and foo() will call
    # foo.__call__ and increase the count
    foo()

print(foo.count) # 10
