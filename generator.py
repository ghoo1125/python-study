def generator_func(x=0):
    for i in range(5):
        if x is None:
            x = yield i
        else:
            x = yield i + x

if __name__ == '__main__':
    # selectively add input to a sequence from 0 to 4
    g = generator_func()
    print(next(g))
    print(next(g))
    # pass in as input, value of yield, no matter what the yield value is
    print(g.send(5))
    print(next(g))
    print(next(g))
    print(next(g)) # end of sequence, get StopIteration

