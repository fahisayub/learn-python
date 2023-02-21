
def announce(f):
    def wrapper():
        print('programe is about to run...')
        f()
        print('process finsihed')
    return wrapper


@announce
def hello():
    print('hello world!')

hello()